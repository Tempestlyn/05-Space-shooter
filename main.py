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

STARTING_LOCATION = (400,100)
class Player(arcade.Sprite):
    def __init__(self):
        super().__init__("assets/SpaceShipUp.png", 0.5)
        (self.center_x, self.center_y) = 300,300



class Window(arcade.Window):



    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.set_mouse_visible(True)
        arcade.set_background_color((34,61,81))
        self.player = Player()
        


        # Make the mouse disappear when it is over the window.

        # So we just see our object, not the pointer.

        self.set_mouse_visible(False)

    def on_mouse_motion(self, x, y, dx, dy):
        '''
        The player moves left and right with the mouse
        '''
        
    

    def on_draw(self):
        
        arcade.start_render()
        self.player.draw()







    def setup(self):

        pass 



    def update(self, delta_time):

        pass

















    def on_mouse_press(self, x, y, button, modifiers):

        """

        Called when the user presses a mouse button.

        """

        pass



    def on_mouse_release(self, x, y, button, modifiers):

        """

        Called when a user releases a mouse button.

        """

        pass



    def on_key_press(self, key, modifiers):

        """ Called whenever the user presses a key. """

        if key == arcade.key.LEFT:

            print("Left")

        elif key == arcade.key.RIGHT:

            print("Right")

        elif key == arcade.key.UP:

            print("Up")

        elif key == arcade.key.DOWN:

            print("Down")



    def on_key_release(self, key, modifiers):

        """ Called whenever a user releases a key. """

        pass





def main():

    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()





if __name__ == "__main__":

    main()