
import arcade
from arcade.key import ESCAPE
from tilegamelib import load_tiles
from tilegamelib import Vector
from tilegamelib import TiledMap
from tilegamelib import config
from tilegamelib.vector import UP, DOWN, LEFT, RIGHT
import json


config.BASE_PATH = './'
SIZEX, SIZEY = (850, 950)
TIMER = 10

SYNONYMS = [
    ('player', 'b.pac_right'),
]


FLOOR = {'.', 'x', 'a', 'b', 'c', 'd', 'e', 'f', 'g'}


class Level(TiledMap):
    """
    Loads a 2D grid from a JSON file
    """
    def __init__(self, filename, tiles, player, offset):
        self.tiles = tiles
        self.player = player
        j = json.load(open(filename))
        dungeon = '\n'.join(j['map'])
        self.exit = j['exit']
        super().__init__(tiles, dungeon, offset)

    def is_exit(self, position):
        c = self.level.at(position)
        if c !='.':
            print(c)
        return self.level.at(position) == 'stairs'

    def update(self):
        ...

    def can_enter(self, pos):
        if self.at(pos) in FLOOR:
            return True


class Player:
    """
    Manages a player position and possible moves.
    """
    def __init__(self, tiles, pos):
        self.tiles = tiles
        self.pos = pos
        self.level = None

    def adjacent_positions(self, position):
        for move in [UP, DOWN, LEFT, RIGHT]:
            new_pos = position + move
            if self.level.at(new_pos) != '#':
                yield new_pos, move

    def draw(self):
        px = self.level.pos_in_pixels(self.pos)
        self.tiles['player'].draw(px.x, px.y, 32, 32)

    def move(self, vec):
        dest = self.pos + vec
        if self.level.can_enter(dest):
            self.pos = dest



class DungeonCrawl(arcade.Window):
    """
    Manages graphics
    """
    def __init__(self, pclass):
        super().__init__(SIZEX, SIZEY, "Dungeon Crawl")
        arcade.set_background_color(arcade.color.BLACK)
        self.tiles = load_tiles('fruit.csv')
        self.add_tile_synonyms()
        self.player = pclass(self.tiles, None)
        self.level = None
        self.level_cache = {}
        self.enter_level('level.json', Vector(2, 6))

    def enter_level(self, filename, pos):
        if filename not in self.level_cache:
            self.level = Level(filename, self.tiles, self.player, offset=Vector(50, 170))
            self.level_cache[filename] = self.level
        else:
            self.level = self.level_cache[filename]
        self.player.level = self.level
        self.player.pos = pos
        self.timer = TIMER

    def add_tile_synonyms(self):
        for s, t in SYNONYMS:
            self.tiles[s] = self.tiles[t]

    def on_draw(self):
        arcade.start_render()
        self.level.draw()
        self.player.draw()
        arcade.draw_text("Graph Traversal", 50, 840, "lightblue", 32)
        arcade.draw_text("Kristian Rother – www.academis.eu", 50, 800, "lightblue", 24)

    def update(self, time_delta):
        self.level.update()
        if self.timer > 0:
            self.timer -= 1
        if self.timer == 0:
            self.timer = TIMER
            self.player.move()
            if self.player.pos == self.level.exit:
                arcade.window_commands.close_window()
            

    def on_key_press(self, symbol, mod):
        """Handle player movement"""
        if symbol == ESCAPE:
            arcade.window_commands.close_window()
