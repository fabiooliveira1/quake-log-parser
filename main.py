from src.controller.controller import Controller

def main ():
    controller_instance = Controller()

    controller_instance.populate_history()

    controller_instance.get_game_report()
    controller_instance.get_player_ranking()
    controller_instance.get_all_kills_by_means()

main()