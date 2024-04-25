def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance


@singleton
class Entities:
    snake_head_tail = dict()
    ladder_top_bot = dict()
    players = []

    # def __init__(self, snakeHeadTail, ladderTopBot, players):
    #     self.snakeHeadTail = snakeHeadTail
    #     self.ladderTopBot = ladderTopBot
    #     self.players = players

    def set_snake(self, head, tail):
        self.snake_head_tail[head] = tail

    def get_snake(self):
        return self.snake_head_tail

    def set_ladder(self, top, bottom):
        self.ladder_top_bot[top] = bottom

    def get_ladder(self):
        return self.ladder_top_bot

    def set_players(self, players):
        self.players.append(players)

    def get_players(self):
        return self.players

