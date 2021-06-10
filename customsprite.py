from quest.sprite import QuestSprite, Background
import time
class EndMixIn:
        def on_collision(self, sprite, game):
            super().on_collision(sprite,game)

            if game.game_over == False:
                game.game_over = True
                print("Finished")
                end = time.time()
                print(end - game.start)
class End(EndMixIn, Background):
    description = "end"
