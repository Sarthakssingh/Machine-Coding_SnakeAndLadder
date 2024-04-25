from Entities import *
from PlaySnakeAndLadder import *


class Main:

    entities = Entities()

    number_of_snakes = int(input())
    for i in range(number_of_snakes):
        inputSnake = input()
        head, tail = inputSnake.split()
        entities.set_snake(int(head), int(tail))

    number_of_ladders = int(input())
    for i in range(number_of_ladders):
        inputLadder = input()
        top, bot = inputLadder.split()
        entities.set_ladder(int(top), int(bot))

    number_of_players = int(input())
    for i in range(number_of_players):
        entities.set_players(input())

    play_the_game = PlaySnakeAndLadder()
    print(play_the_game.play_game() + " wins the game")
