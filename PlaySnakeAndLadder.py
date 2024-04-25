from Dice import *
from Entities import *


def check_for_greater_than_100(end_pos):
    return end_pos <= 100


class PlaySnakeAndLadder:
    player_history = dict()
    player_latest_position = dict()
    dice = Dice()
    entities = Entities()

    def play_game(self):
        self.initialize_game()
        i = -1
        while not self.is_player_won(self.entities.get_players()[i]):
            i += 1
            if i >= len(self.entities.get_players()):
                i = 0

            player_name = self.entities.get_players()[i]
            dice_number = self.dice.roll()
            player_end_pos = self.player_latest_position[player_name] + dice_number
            result_string = player_name + " rolled a " + str(dice_number) + " and moved from " + str(self.player_latest_position[player_name] )+" to "
            s1 = ""
            if check_for_greater_than_100(player_end_pos):
                if self.entities.get_snake().get(player_end_pos) is not None:
                    s1 = " after Snake dinner"
                    self.player_latest_position[player_name] = self.entities.get_snake()[player_end_pos]
                elif self.entities.get_ladder().get(player_end_pos) is not None:
                    s1 = " after Ladder ride"
                    self.player_latest_position[player_name] = self.entities.get_ladder()[player_end_pos]
                else:
                    self.player_latest_position[player_name] = player_end_pos
            result_string = result_string + str(self.player_latest_position[player_name]) + s1
            print(result_string)

        return self.entities.get_players()[i]

    def initialize_game(self):
        for i in range(len(self.entities.get_players())):
            x = self.entities.get_players()
            self.player_latest_position[x[i]] = 0

    def is_player_won(self, player):
        return self.player_latest_position[player] == 100
