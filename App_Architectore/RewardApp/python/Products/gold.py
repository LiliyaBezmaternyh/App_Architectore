from Products.i_game_item import GameItem


class Gold(GameItem):
    def open(Self):
        print("\033[3;33m Gold!\033[0m")
