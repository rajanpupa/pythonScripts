import pyautogui                    # pip install pyautogui
from PIL import Image, ImageGrab    # pip install pillow
import time
# from numpy import asarray

def takeScreenshot():
    image = ImageGrab.grab().convert('L')
    # image.show()
    return image

def hit(key):
    pyautogui.keyDown(key)

def draw():
    pass

def _is_collide(x1, x2, y1, y2, data):
    for i in range(x1, x2):
        for j in range(y1, y2):
            if data[i,j] < 100:
                return True
    return False

def is_bird(data):
    return _is_collide(315, 400, 570, 590, data)
    
def is_cactus(data):
    return _is_collide(340, 425, 600, 650, data)

# automatically play chrome://dino game
if __name__ == "__main__":
    print('...Loading game play')
    time.sleep(3)
    hit('up')
    while True:
        image = takeScreenshot()
        data = image.load()
        if is_cactus(data):
            hit("up")
            print("hitting up")
            #time.sleep(.4)
        elif is_bird(data):
            hit("down")
            print("hitting down")
            #time.sleep(.4)
            

        #print(asarray(image))

        # # is_cactus
        # for i in range(315, 415):
        #     for j in range(650, 690):
        #         data[i,j] = 0
        # # is_bird
        # for i in range(315, 415):
        #     for j in range(570, 590):
        #         data[i,j] = 0
        # break
    
    image.show()