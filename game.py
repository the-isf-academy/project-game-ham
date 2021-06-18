# game.py
# Authors: Anderson, James
#
# This file should run your game.
#
# You can (and should) create other files and modules to import them
# here as needed.

from quest.game import QuestGame
from quest.map import TiledMap
from quest.sprite import Background, Wall
from quest.helpers import resolve_resource_path
import arcade
import os
from pathlib import Path
from customsprite import End
import time
from quest.sprite import QuestSprite, Player, Wall, NPC
from quest.strategy import RandomWalk
class IslandAdventure(QuestGame):
    """A very simple subclass of :py:class:`QuestGame`.

    To run this example::

        $ python -m quest.examples.island

    :py:class:`IslandAdventure` shows off the basic features of the Quest
    framework, loading a map and letting the player explore it.
    After you play it, check out the sorce code by clicking on "source" in the
    blue bar just above.
    """

    player_sprite_image = ("Assets/Characters/girlsimple.png")
    screen_width = 500
    screen_height = 500
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    teleportx = 10*32
    teleporty = 25*32
    player_initial_x = 4*32
    player_initial_y = 145.5*32
    player_speed = 10
    game_over = False
    start = time.time()


    def setup_maps(self):
        """Sets up the map.

        Uses a :py:class:`TiledMap` to load the map from a ``.tmx`` file,
        created using :doc:`Tiled <tiled:manual/introduction>`.
        """
        super().setup_maps()
        sprite_classes = {
            "bg": Wall,
            "outline": Background,
            "decoration": Background,
            "end": End,
            "start": Background,
            "tp": TP,
        }
        island_map = TiledMap("Assets/Map/map.tmx", sprite_classes)
        self.add_map(island_map)

    def setup_walls(self):
        """Assigns sprites to `self.wall_list`. These sprites will function as walls, blocking
        the player from passing through them.
        """
        self.wall_list = self.get_current_map().get_layer_by_name("bg").sprite_list


    def setup_npcs(self):
        npc_data = []
        for i in range(8):
            npc_data.append([Monster, "Assets/Characters/monster.png", 4, 1088, 1792])
            npc_data.append([Eviel, "Assets/Characters/girlsimple.png", 3, 1920, 384])
            npc_data.append([BM, "Assets/Characters/bm.png", 3, 1792, 1376])
        self.npc_list = self.get_current_map().get_layer_by_name("end").sprite_list
        self.npc_list.extend(self.get_current_map().get_layer_by_name("tp").sprite_list)
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(image, scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)
        for i in range(8):
            monster = self.npc_list[-1-i]
            walk = RandomWalk(0.05)
            monster.strategy = walk

class TP(NPC):
    description = "tp"

    def on_collision(self, sprite, game):
        print("Start")
        if isinstance(sprite, Player):
            game.player_x = 10*32
            game.player_y = 25*32
            game.player.center_x = 10*32
            game.player.center_y = 25*32
            game.right_viewport_margin = 96
            game.bottom_viewport_margin = 96

class BM(NPC):
    def on_collision(self, sprite, game):
        if isinstance(sprite, Player):
            print("Ded")
            game.player_x = 10*32
            game.player_y = 25*32
            game.player.center_x = 10*32
            game.player.center_y = 25*32
            game.right_viewport_margin = 96
            game.bottom_viewport_margin = 96
            game.top_viewport_margin = 96
class Eviel(NPC):
    def on_collision(self, sprite, game):
        if isinstance(sprite, Player):
            print("Ded")
            game.player_x = 10*32
            game.player_y = 25*32
            game.player.center_x = 10*32
            game.player.center_y = 25*32
            game.right_viewport_margin = 96
            game.bottom_viewport_margin = 96
            game.top_viewport_margin = 96

class Monster(NPC):
    def on_collision(self, sprite, game):
        if isinstance(sprite, Player):
            print("Ded")
            game.player_x = 10*32
            game.player_y = 25*32
            game.player.center_x = 10*32
            game.player.center_y = 25*32
            game.right_viewport_margin = 96
            game.bottom_viewport_margin = 96
            game.top_viewport_margin = 96

if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
