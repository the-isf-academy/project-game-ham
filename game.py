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
    player_initial_x = 10*32
    player_initial_y = 25*32
    player_speed = 15
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
        for i in range(20):
            npc_data.append([Monster, "Assets/Characters/monster.png", 3, 1088, 1792])
        self.npc_list = self.get_current_map().get_layer_by_name("end").sprite_list
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(image, scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)
        for i in range(20):
            monster = self.npc_list[-1-i]
            walk = RandomWalk(0.05)
            monster.strategy = walk

def repel(self, sprite):
    "Backs the sprite away from self"
    away = (self.center_x - sprite.center_x, self.center_y - sprite.center_y)
    away_x, away_y = scale(away, self.repel_distance)
    sprite.center_x = sprite.center_x - away_x
    sprite.center_y = sprite.center_y - away_y
    sprite.stop()



class Monster(NPC):
    def on_collision(self, sprite, game):
        if isinstance(sprite, Player):
            print("test")
            game.player_x = 10*32
            game.player_y = 25*32
            game.player.center_x = 10*32
            game.player.center_y = 25*32


if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
