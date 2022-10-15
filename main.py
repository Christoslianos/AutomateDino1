from PIL import ImageGrab, ImageOps
from pynput import *
import pyautogui
import np
import time


# get coordinates of the mouse
#def get_coords(x, y):
    #print("Now is:{}".format((x, y)))

#with mouse.Listener(on_move=get_coords) as listen:
    #listen.join()



def press(key):
    pyautogui.keyDown(key)
    return


def detect_collision(data):
    for i in range(1230, 1340):
        for j in range(800, 850):
            if data[i, j] > 100:
               press("up")
            return
    return




if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    press('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        detect_collision(data)

        # draw the rectangle for bush
        #for i in range(1230, 1340):
                #for j in range(800, 850):
                    #data[i, j] = 0
        #image.show()

        #break
