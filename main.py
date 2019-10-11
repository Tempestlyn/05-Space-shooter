import sys, logging, os, random, math, arcade
import threading
import random
import time
#check to make sure we are running the right version of Python

version = (3,7)

assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])



#turn on logging, in case we have to leave ourselves debugging messages

logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)



SCREEN_WIDTH = 800

SCREEN_HEIGHT = 600

SCREEN_TITLE = ""

PLAYER_MOVEMENT_SPEED = 4

STARTING_LOCATION = (400,100)
class Player(arcade.Sprite):


    def __init__(self, position):
        super().__init__("assets/SpaceShipUp.png", 0.5)
        (self.center_x, self.center_y) = position
        
        self.dx = 0
        self.dy = 0
        self.ey = 0
        self.ex = 0
    def update(self):

        self.center_x += self.dx
        self.center_y += self.dy

class Bullet(arcade.Sprite):
    def __init__(self, position, velocity, damage):
 
        super().__init__("assets/bullet.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):

        self.center_x += self.dx
        self.center_y += self.dy


class Enemy(arcade.Sprite):
    def __init__(self, position, velocity, damage):

        super().__init__("assets/SpaceShipDown.png", 0.5)
        (self.center_x, self.center_y) = position
        (self.dx, self.dy) = velocity
        self.damage = damage

    def update(self):
        self.center_x += self.dx
        self.center_y += self.dy

    

class Window(arcade.Window):



    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        
        self.set_mouse_visible(True)
        arcade.set_background_color((34,61,81))
        self.player_sprite = None
        self.player_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        # Make the mouse disappear when it is over the window.

        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)



        
    

    def on_draw(self):
        
        arcade.start_render()
        #self.player.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()
        #self.enemy.draw()





    def setup(self):
        
        self.enemy = Enemy((50,500), (1,0), 0)
        self.player = Player(STARTING_LOCATION)
        self.player_sprite = arcade.Sprite("assets/SpaceShipUp.png", 0.5)
        self.player_list.append(self.player)
        self.enemy_list.append(self.enemy)
        

    def update(self, delta_time):
        self.player_list.update()
        self.bullet_list.update()
        self.enemy_list.update()
        self.player.center_y += self.player.dy
        self.player.center_x += self.player.dx
        self.player.center_y += self.player.ey
        self.player.center_x += self.player.ex
        for e in self.bullet_list:
            e.center_y += e.dy
        for enemy in self.enemy_list:
            collisions = enemy.collides_with_list(self.bullet_list)
            for c in collisions:
                self.enemy_list.remove(enemy)
                self.bullet_list.remove(c)
                c.kill()
                enemy.kill()

            hit_trigger = arcade.check_for_collision(self.player, enemy)
            if hit_trigger:
                self.player.kill()
                exit()
                hit_trigger = False
        self.enemy.center_x += self.enemy.dx
        for p in self.enemy_list:
            if p.center_x < -50 or p.center_x > SCREEN_WIDTH + 50 or p.center_y < -50 or p.center_y > SCREEN_HEIGHT + 50:
                    p.dx = -p.dx
                    p.center_y = p.center_y - 50
                    self.NewEnemy = Enemy((random.randint(25,75),500), (random.randint(1,5),0), 0)
                    self.enemy_list.append(self.NewEnemy)
            

        if len(self.enemy_list) == 0:
             self.NewEnemy = Enemy((random.randint(25,260),500), (random.randint(1,5),0), 0)
             self.enemy_list.append(self.NewEnemy)
    def on_mouse_press(self, x, y, button, modifiers):
        pass




    def on_mouse_release(self, x, y, button, modifiers):



        pass



    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.dy = 5
            
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.dx = -5
            
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.ex = 5

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.ey = -5

        elif key == arcade.key.SPACE:
            
            bullet = Bullet((self.player.center_x, self.player.center_y), (0,5), 10)
            self.bullet_list.append(bullet)
            
    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player.dy = 0
            
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player.dx = 0
            
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player.ex = 0

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player.ey = 0

    def spawn(self):
        time.sleep(5)

        while True:
            print("e")
            time.sleep(1)





def main():

    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()




    

if __name__ == "__main__":

    main()