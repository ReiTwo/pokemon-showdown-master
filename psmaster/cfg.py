import queue


# Global Variables
game_state = {"room_id": "lobby", "timer": "off"}
request_queue = queue.Queue(10)
battle_message_queue = queue.Queue(10)

main_to_login = queue.Queue(1)
login_to_main = queue.Queue(1)
main_to_battle = queue.Queue(1)
battle_to_main = queue.Queue(1)


# Global Variables (load and save files)
pokedex = None
states = None
sapairs = None
actions_js = None
actions_np = None
