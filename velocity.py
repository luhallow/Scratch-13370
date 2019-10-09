#!/usr/local/env python3
import sys, logging, os, random, open_color, arcade
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0], version[1])

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 50
SCREEN_TITLE = "Space Shooter Example"

#create a little function for returning the sign of an expression
sign = lambda x: x and (1, -1)[x < 0]

class Player(arcade.Sprite):
    def __init__(self, image, scale, x, y):
        super().__init__(image, scale)
        self.center_x = x
        self.center_y = y
        self.dx = 1
        self.dy = 1
        self.ddx = 1.001
        self.ddy = 1.001
    
    def update(self):
        self.center_y = self.center_y + self.dy
        self.center_x = self.center_x + self.dx
        self.dx = self.dx * self.ddx
        self.dy = self.dy * self.ddy

        if self.center_x < 0:
            self.center_x = 0
            self.dx = abs(self.dx)
        if self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.dx = abs(self.dx) * -1
        if self.center_y < 0:
            self.center_y = 0
            self.dy = abs(self.dy)
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = SCREEN_HEIGHT
            self.dy = abs(self.dy) * -1
            


class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        self.set_mouse_visible(True)

        arcade.set_background_color(open_color.blue_4)

        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_bullet_list = arcade.SpriteList()

    def setup(self):
        self.player = Player("assets/player.png",0.5, 0, 0)
        self.player_list.append(self.player)
        self.player_2 = Player("assets/enemy_09.png",0.5, 400, 300)
        self.player_2.dx = -1
        self.player_list.append(self.player_2)


    def update(self, delta_time):
        self.player_list.update()
        colliding = arcade.check_for_collision_with_list(self.player, self.player_list)
        for c in colliding:
            if c != self.player:
                tx = self.player.dx
                ty = self.player.dy
                self.player.dx = c.dx
                self.player.dy = c.dy
                c.dx = tx
                c.dy = ty

    def on_draw(self):
        arcade.start_render()        
        self.player_list.draw()
    
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass



def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()