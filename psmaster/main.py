import _thread
import hashlib
import json
import os
import queue
import time
import tkinter as tk

import numpy as np
import requests
import websocket

import cfg
import gui
import helper


_battle_flag = False
_login_flag = False
_q = queue.Queue(1)

_actions_info = {"hash": "", "loaded": False}
_server_login_info = ["", ""]   # guest_username, challstr_value

_script_dir = os.path.dirname(__file__)


def on_message(ws, message):
    print(message)

    global _battle_flag
    global _login_flag
    global _q

    global _actions_info
    global _server_login_info

    global _script_dir

    if _battle_flag and ">battle" == message[:7]:

        message_lst = []
        temp_message_lst = message.split("\n")
        for entry in temp_message_lst:
            temp_message = entry.strip()
            if temp_message:
                message_lst.append(temp_message)

        if cfg.game_state["room_id"] == "lobby":
            cfg.game_state["room_id"] = message_lst[0][1:]

        if cfg.game_state["timer"] == "off":
            ws.send(cfg.game_state["room_id"] + "|" + "/timer on")
            cfg.game_state["timer"] = "on"

        if "|deinit" in message:
            for entry in message_lst:
                if "|deinit" in entry:
                    if "|deinit" == entry[:7]:

                        _q.put("item")
                        actions_js_path = "states/" + _actions_info["hash"] + ".json"
                        actions_js_path_abs = os.path.join(_script_dir, actions_js_path)
                        with open(actions_js_path_abs, "w", encoding="utf-8") as output:
                            json.dump(cfg.actions_js, output, ensure_ascii=False)

                        weights_np_path = "states/" + _actions_info["hash"] + ".npy"
                        weights_np_path_abs = os.path.join(_script_dir, weights_np_path)
                        np.save(weights_np_path_abs, cfg.weights_np)
                        temp_item = _q.get()

                        cfg.game_state = {"room_id": "lobby", "timer": "off"}
                        _battle_flag = False

                        return

        if ("|win|" in message) or ("|tie" in message):
            for entry in message_lst:
                if ("|win|" in entry) or ("|tie" in entry):
                    if ("|win|" == entry[:5]) or ("|tie" == entry[:4]):
                        cfg.battle_message_queue.put(message_lst)

                        time.sleep(1)
                        ws.send(cfg.game_state["room_id"] + "|" + "/leave")

                        return

        if "|error|[Invalid choice]" in message:
            for entry in message_lst:
                if "|error|[Invalid choice]" in entry:
                    if "|error|[Invalid choice]" == entry[:23]:

                        if "|error|[Invalid choice] There's nothing to choose" not in entry:
                            ws.send(cfg.game_state["room_id"] + "|" + "/choose default")

                        return

        if "|request|" in message:
            for entry in message_lst:
                if "|request|" in entry:
                    if "|request|" == entry[:9] and "{" in entry and "}" in entry:
                        cfg.request_queue.put(entry)

                        return

        if ("|teampreview" in message) or ("|turn" in message) or ("|upkeep" in message):
            for entry in message_lst:
                if ("|teampreview" in entry) or ("|turn" in entry) or ("|upkeep" in entry):
                    if ("|teampreview" == entry[:12]) or ("|turn" == entry[:5]) or ("|upkeep" == entry[:7]):
                        cfg.battle_message_queue.put(message_lst)

                        return

    if not _login_flag:

        if not _server_login_info[0]:

            if "|updateuser|" in message:
                end_index = message.find("|0|")
                guest_username = message[12:end_index].strip()
                _server_login_info[0] = guest_username

        if not _server_login_info[1]:

            if "|challstr|" in message:
                challstr_value = message[10:].strip()
                _server_login_info[1] = challstr_value


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):

    def run(*args):
        global _battle_flag
        global _login_flag
        global _q

        global _actions_info
        global _server_login_info

        global _script_dir

        pokedex_path = "data/pokedex.json"
        pokedex_path_abs = os.path.join(_script_dir, pokedex_path)
        with open(pokedex_path_abs) as data:
            cfg.pokedex = json.load(data)

        while not _login_flag:

            while cfg.login_to_main.empty():
                time.sleep(1)

            if (not _server_login_info[0]) or (not _server_login_info[1]):
                cfg.main_to_login.put("Timeout")

                return

            login_lst = cfg.login_to_main.get()

            if login_lst[0] == 0:
                ws.send("|/avatar {}".format(str(login_lst[3])))

                _login_flag = True
                cfg.main_to_login.put("Success")
                break
            else:
                login_data = {"act": "login",
                              "name": login_lst[1],
                              "pass": login_lst[2],
                              "challstr": _server_login_info[1]}

                r = requests.post("http://play.pokemonshowdown.com/action.php", data=login_data)
                request_result = r.text[1:].strip()

                if '"actionsuccess":false' in request_result:
                    cfg.main_to_login.put("Fail")
                    continue

                _server_login_info[0] = login_lst[1]
                assertion_data = json.loads(request_result)["assertion"]
                ws.send("|/trn {},0,{}".format(_server_login_info[0], assertion_data))
                ws.send("|/avatar {}".format(str(login_lst[3])))

                _login_flag = True
                cfg.main_to_login.put("Success")
                break

        while _login_flag:

            while cfg.battle_to_main.empty():
                time.sleep(1)

            battle_lst = cfg.battle_to_main.get()
            battle_format = battle_lst[1]
            battle_team = battle_lst[4]

            hash_team = hashlib.sha1(battle_team.encode("utf-8")).hexdigest()
            if _actions_info["hash"] != hash_team:
                _q.put("item")
                cfg.actions_js = None
                cfg.weights_np = None
                _actions_info["hash"] = hash_team
                _actions_info["loaded"] = False
                temp_item = _q.get()

            if battle_lst[0] == 0:
                battle_rival = battle_lst[2]

                _battle_flag = True
                ws.send("|/utm {}".format(battle_team))
                ws.send("|/challenge {}, {}".format(battle_rival, battle_format))

                for i in range(16):
                    time.sleep(1)

                    if cfg.game_state["room_id"] == "lobby":
                        if i == 15:
                            _battle_flag = False
                            ws.send("|/cancelchallenge {}".format(battle_rival))

                            _actions_info["hash"] = ""
                            cfg.main_to_battle.put("Fail")
                    else:
                        break

                if _battle_flag:
                    cfg.main_to_battle.put("Battle with {} is in progress . . .".format(battle_rival))
                else:
                    continue

                if not _actions_info["loaded"]:
                    _q.put("item")

                    try:
                        actions_js_path = "states/" + _actions_info["hash"] + ".json"
                        actions_js_path_abs = os.path.join(_script_dir, actions_js_path)
                        with open(actions_js_path_abs) as data:
                            cfg.actions_js = json.load(data)

                        weights_np_path = "states/" + _actions_info["hash"] + ".npy"
                        weights_np_path_abs = os.path.join(_script_dir, weights_np_path)
                        cfg.weights_np = np.load(weights_np_path_abs)
                    except Exception:
                        cfg.actions_js = {"total": 0, "win": 0}
                        cfg.weights_np = np.zeros(1000)

                    temp_item = _q.get()

                    _actions_info["loaded"] = True

                while _battle_flag:
                    time.sleep(10)

                cfg.main_to_battle.put("End")
            else:
                battle_rounds = battle_lst[3] - 1

                _battle_flag = True
                ws.send("|/utm {}".format(battle_team))
                ws.send("|/search {}".format(battle_format))

                for i in range(16):
                    time.sleep(1)

                    if cfg.game_state["room_id"] == "lobby":
                        if i == 15:
                            _battle_flag = False
                            ws.send("|/cancelsearch")

                            _actions_info["hash"] = ""
                            cfg.main_to_battle.put("Fail")
                    else:
                        break

                if _battle_flag:
                    cfg.main_to_battle.put("Round 1 battle is in progress . . .")
                else:
                    continue

                if not _actions_info["loaded"]:
                    _q.put("item")

                    try:
                        actions_js_path = "states/" + _actions_info["hash"] + ".json"
                        actions_js_path_abs = os.path.join(_script_dir, actions_js_path)
                        with open(actions_js_path_abs) as data:
                            cfg.actions_js = json.load(data)

                        weights_np_path = "states/" + _actions_info["hash"] + ".npy"
                        weights_np_path_abs = os.path.join(_script_dir, weights_np_path)
                        cfg.weights_np = np.load(weights_np_path_abs)
                    except Exception:
                        cfg.actions_js = {"total": 0, "win": 0}
                        cfg.weights_np = np.zeros(1000)

                    temp_item = _q.get()

                    _actions_info["loaded"] = True

                while _battle_flag:
                    time.sleep(10)

                for i in range(battle_rounds):
                    _battle_flag = True
                    ws.send("|/search {}".format(battle_format))

                    cfg.main_to_battle.put("Round {} battle is in progress . . .".format(str(i + 2)))

                    while _battle_flag:
                        time.sleep(10)

                cfg.main_to_battle.put("End")

        time.sleep(1)
        ws.close()

    def run_gui(*args):
        global _login_flag
        global _q

        root = tk.Tk()
        login_class = gui.LoginWindow(root)
        login_class.pack(expand=1, fill="both")

        login_class.login_send()
        login_class.login_receive()
        login_class.mainloop()

        if not _login_flag:
            ws.close()
            return

        root = tk.Tk()
        battle_class = gui.BattleWindow(root)
        battle_class.pack(expand=1, fill="both")
        battle_class.set_message("Login Successful !\nUser Name : {}".format(_server_login_info[0]))

        battle_class.battle_send()
        battle_class.battle_receive()
        battle_class.battle_spectate()
        battle_class.mainloop()

        _q.put("item")

        time.sleep(1)
        ws.close()

    def run_ai(*args):
        global _login_flag

        while not _login_flag:
            time.sleep(5)

        while _login_flag:

            while cfg.request_queue.empty():
                time.sleep(1)

            new_req = cfg.request_queue.get()
            valid_choice = helper.process_request(new_req)
            if not valid_choice[0]:
                continue

            time.sleep(1)

            while not cfg.battle_message_queue.empty():
                new_msg = cfg.battle_message_queue.get()

            result = np.random.choice(valid_choice[0])
            ws.send(cfg.game_state["room_id"] + "|/" + result + valid_choice[1])

        time.sleep(1)
        ws.close()

    _thread.start_new_thread(run, ())
    _thread.start_new_thread(run_gui, ())
    _thread.start_new_thread(run_ai, ())


if __name__ == "__main__":
    websocket.enableTrace(True)   # default : True
    ws = websocket.WebSocketApp("ws://sim.smogon.com:8000/showdown/websocket",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
