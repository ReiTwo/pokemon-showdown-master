import random
import tkinter as tk
import webbrowser
from tkinter import filedialog

import cfg
import teamf


# Graphical User Interface (GUI) for Login Window

class LoginWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.flag = False
        self.information = [0, "", "", 0]   # login_type, username, password, avatar_index

        self.parent.title("Pokemon Showdown Master")
        self.avatar_lst = list(range(0, 294))

        self.avatar_index = tk.IntVar()
        self.avatar_index.set(0)
        self.login_type = tk.IntVar()
        self.login_type.set(0)
        self.message = tk.StringVar()
        self.message.set("")

        def close_window():
            self.parent.destroy()

        def disable_entry():
            self.username_entry.config(state="disabled")
            self.password_entry.config(state="disabled")

        def enable_entry():
            self.username_entry.config(state="normal")
            self.password_entry.config(state="normal")

        def log_in_click():
            self.information[0] = self.login_type.get()
            self.information[1] = self.username_entry.get()
            self.information[2] = self.password_entry.get()

            if self.avatar_index.get() == 0:
                self.information[3] = random.randint(1, 293)
            else:
                self.information[3] = self.avatar_index.get()

            if self.information[0] == 1:
                if (not self.information[1]) or (not self.information[2]):
                    self.message.set("Incomplete login information !")
                    return

            self.log_in_button.config(state="disabled")
            self.flag = True
            self.message.set("Connecting . . .")

        self.login_label = tk.Label(self, text="Log in as :")
        self.radio_button_0 = tk.Radiobutton(self, text="Guest", variable=self.login_type,
                                             value=0, command=disable_entry)
        self.radio_button_1 = tk.Radiobutton(self, text="Registered User", variable=self.login_type,
                                             value=1, command=enable_entry)
        self.username_label = tk.Label(self, text="User Name :")
        self.username_entry = tk.Entry(self)
        self.username_entry.config(state="disabled")   # Config after initialization
        self.password_label = tk.Label(self, text="Password :")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.config(state="disabled")   # Config after initialization
        self.avatar_label = tk.Label(self, text="Avatar Number :\n( select 0 for random avatar )")
        self.avatar_option_menu = tk.OptionMenu(self, self.avatar_index, *self.avatar_lst)
        self.message_label = tk.Label(self, text="--------------------")
        self.message_content = tk.Message(self, width=150, textvariable=self.message)
        self.log_in_button = tk.Button(self, text="Log in", width=15, command=log_in_click)
        self.close_button = tk.Button(self, text="Close", width=10, command=close_window)

        self.login_label.pack(pady=(10, 0))
        self.radio_button_0.pack()
        self.radio_button_1.pack()
        self.username_label.pack(pady=(10, 0))
        self.username_entry.pack()
        self.password_label.pack(pady=(10, 0))
        self.password_entry.pack()
        self.avatar_label.pack(pady=(20, 0))
        self.avatar_option_menu.pack()
        self.message_label.pack(padx=(100, 100), pady=(10, 0))
        self.message_content.pack()
        self.log_in_button.pack(pady=(10, 0))
        self.close_button.pack(pady=(10, 20))

    def login_send(self):
        if not self.flag:
            self.parent.after(500, self.login_send)
        else:
            cfg.login_to_main.put(self.information)
            self.flag = False

            self.parent.after(10, self.login_send)

    def login_receive(self):
        if cfg.main_to_login.empty():
            self.parent.after(500, self.login_receive)
        else:
            result = cfg.main_to_login.get()

            if result == "Success":
                self.parent.destroy()
            elif result == "Fail":
                self.message.set("Incorrect login information ,\nplease try again !")
                self.log_in_button.config(state="normal")

                self.parent.after(10, self.login_receive)
            else:
                self.message.set("Connection timeout ,\napplication closing !")
                self.parent.destroy()


# Graphical User Interface (GUI) for Battle Window

class BattleWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.flag = False
        self.information = [0, "", "", 1, ""]   # battle_type, format_type, rival_username, num_of_rounds, team
        self.team = ""
        self.url = "https://play.pokemonshowdown.com/"

        self.parent.title("Pokemon Showdown Master")
        self.formats = ["gen7ou", "gen7ubers", "gen7uu", "gen7oublitz"]
        self.rounds = [1, 2, 3, 4, 5, 10, 15, 20, 25, 50, 75, 100, 125, 250, 375, 500]

        self.battle_type = tk.IntVar()
        self.battle_type.set(0)
        self.format_type = tk.StringVar()
        self.format_type.set("gen7ou")
        self.message = tk.StringVar()
        self.message.set("")
        self.num_of_rounds = tk.IntVar()
        self.num_of_rounds.set(1)

        def close_window():
            self.parent.destroy()

        def radio_button_0_click():
            self.rival_entry.config(state="normal")
            self.battle_rounds.config(state="disabled")

        def radio_button_1_click():
            self.rival_entry.config(state="disabled")
            self.battle_rounds.config(state="normal")

        def battle_click():
            self.information[0] = self.battle_type.get()
            self.information[1] = self.format_type.get()
            self.information[2] = self.rival_entry.get()
            self.information[3] = self.num_of_rounds.get()
            self.information[4] = self.team

            if self.information[0] == 0:
                if not self.information[2]:
                    self.message.set("Opponent's user name cannot be blank !")
                    return

            if not self.information[4]:
                self.message.set("No valid team imported !")
                return

            self.battle_button.config(state="disabled")
            self.import_button.config(state="disabled")
            self.flag = True
            self.message.set("Searching . . .")

        def import_team():
            filename = filedialog.askopenfilename()

            if not filename:
                self.message.set("No file selected !")
                return

            if filename[-4:] != ".txt":
                self.message.set("Team file must be in '.txt' format !")
                return

            pokemon_data = []
            team_data = []

            with open(filename) as team:
                for line in team:
                    if line == "\n":
                        team_data.append(pokemon_data)
                        pokemon_data = []
                    else:
                        pokemon_data.append(line.rstrip())

            if pokemon_data:
                team_data.append(pokemon_data)

            try:
                team_conversion = teamf.team_converter(team_data)
                self.team = team_conversion

                self.message.set("Team successfully imported !")
                return
            except Exception:
                self.message.set("Invalid team !")
                return

        def open_browser():
            webbrowser.open_new(self.url)

        self.format_label = tk.Label(self, text="Battle Formats :")
        self.format_option_menu = tk.OptionMenu(self, self.format_type, *self.formats)
        self.import_button = tk.Button(self, text="Import Team", width=15, command=import_team)
        self.split_label = tk.Label(self, text="--------------------")
        self.challenge_label = tk.Label(self, text="Select a challenge type :")
        self.radio_button_0 = tk.Radiobutton(self, text="Challenge an Opponent", variable=self.battle_type,
                                             value=0, command=radio_button_0_click)
        self.rival_label = tk.Label(self, text="Opponent's User Name :")
        self.rival_entry = tk.Entry(self)
        self.radio_button_1 = tk.Radiobutton(self, text="[Ladder] Challenge Random Players", variable=self.battle_type,
                                             value=1, command=radio_button_1_click)
        self.rounds_label = tk.Label(self, text="Number of Rounds :")
        self.battle_rounds = tk.OptionMenu(self, self.num_of_rounds, *self.rounds)
        self.battle_rounds.config(state="disabled")   # Config after initialization
        self.message_label = tk.Label(self, text="--------------------")
        self.message_content = tk.Message(self, textvariable=self.message, width=150)
        self.battle_button = tk.Button(self, text="Battle !", width=15, command=battle_click)
        self.spectate_button = tk.Button(self, text="Spectate", width=15, command=open_browser)
        self.spectate_button.config(state="disabled")   # Config after initialization
        self.close_button = tk.Button(self, text="Close", width=10, command=close_window)

        self.format_label.pack(pady=(10, 0))
        self.format_option_menu.pack()
        self.import_button.pack(pady=(10, 0))
        self.split_label.pack(padx=(100, 100), pady=(10, 0))
        self.challenge_label.pack()
        self.radio_button_0.pack(pady=(10, 0))
        self.rival_label.pack(pady=(5, 0))
        self.rival_entry.pack()
        self.radio_button_1.pack(pady=(20, 0))
        self.rounds_label.pack(pady=(5, 0))
        self.battle_rounds.pack()
        self.message_label.pack(pady=(10, 0))
        self.message_content.pack()
        self.battle_button.pack(pady=(10, 0))
        self.spectate_button.pack(pady=(10, 0))
        self.close_button.pack(pady=(10, 20))

    def set_message(self, m):
        self.message.set(m)

    def battle_send(self):
        if not self.flag:
            self.parent.after(1000, self.battle_send)
        else:
            cfg.battle_to_main.put(self.information)
            self.flag = False

            self.parent.after(10, self.battle_send)

    def battle_receive(self):
        if cfg.main_to_battle.empty():
            self.parent.after(1000, self.battle_receive)
        else:
            result = cfg.main_to_battle.get()

            if result == "Fail":
                self.message.set("Timeout . . .\nPlease make sure you have a valid team and try again.")
                self.battle_button.config(state="normal")
                self.import_button.config(state="normal")

                self.parent.after(10, self.battle_receive)
            elif result == "End":
                self.spectate_button.config(state="disabled")

                self.message.set("All battles have ended.")
                self.battle_button.config(state="normal")
                self.import_button.config(state="normal")

                self.parent.after(10, self.battle_receive)
            else:
                self.message.set(result)

                self.parent.after(10, self.battle_receive)

    def battle_spectate(self):
        if cfg.game_state["room_id"] != "lobby":
            self.url = ("https://play.pokemonshowdown.com/" + cfg.game_state["room_id"]).strip()

            if str(self.spectate_button["state"]) == "disabled":
                self.spectate_button.config(state="normal")

            self.parent.after(5000, self.battle_spectate)
        else:
            self.parent.after(5000, self.battle_spectate)
