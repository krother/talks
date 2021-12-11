
from dungeon import DungeonCrawl, Player, UP, DOWN, LEFT, RIGHT
import random
import arcade


class RandomPlayer(Player):

    def move(self):
        direction = random.choice([UP, DOWN, LEFT, RIGHT])
        super().move(direction)


if __name__ == '__main__':
    dc = DungeonCrawl(RandomPlayer)
    arcade.run()
