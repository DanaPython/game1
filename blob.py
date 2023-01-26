import pygame
import sys
from blob import RedBlob, BlueBlob

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255) # (RED, GREEN, BLUE)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def twins(blue):
    for id, blue_blob in blue.copy().items():
        for _id, _blue_blob in blue.copy().items():
            if id!=_id:
                if blue_blob.is_touching(_blue_blob):
                    blue_blob +_blue_blob

def colissionsHandle(red, blue):
    for blue_id, blue_blob in blue.items():
        for red_id, other_blob in red.items():
            if blue_blob.is_touching(other_blob):
                blue_blob+other_blob
    twins(blue)
    twins(red)

def draw_env(*blobs):
    # Draw one Frame
    game_display.fill(WHITE)
    red, blue = {}, {}
    if len(blobs)==2:
        red, blue = blobs
    colissionsHandle(red, blue)
    for blob in {**red, **blue}.values():
        blob.move()
        #print("Size is:",  blob.size)
        if blob.size > 0:
            pygame.draw.circle(game_display, blob.color,
                            (blob.x, blob.y), blob.size)

def main():
    red_blobs = { i:RedBlob() for i in range(100)} 
    blue_blobs = { i:BlueBlob() for i in range(100,200)} 
    """red_blobs ={1: RedBlob()}
    blue_blobs = {2: RedBlob()}
    red_blobs[1].x = 100
    red_blobs[1].y = 101
    red_blobs[1].size = 13
    blue_blobs[2].x = 110
    blue_blobs[2].y = 100
    blue_blobs[2].size = 15
    print({**red_blobs, **blue_blobs})"""


    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        draw_env(red_blobs, blue_blobs)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

if __name__=="__main__":
    main()

Наташа Дочь, [26.01.2023 18:40]
import random

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255) # (RED, GREEN, BLUE)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Blob():
    def __init__(self, color):
        self.size = random.randint(4, 8)
        self.color = color
        self.x, self.y = random.randint(10, WIDTH-10), random.randint(10, HEIGHT-10)
    def move(self):
        self.x += random.randrange(-1, 2)
        self.y += random.randrange(-1, 2)
        if self.x<10:
            self.x = 10
        elif self.x>WIDTH-10:
            self.x=WIDTH-10
        if self.y<10:
            self.y = 10
        elif self.y>HEIGHT-10:
            self.y=HEIGHT-10
    def isReal(self):
        if self.size<=0:
            del self
    def is_touching(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dd = pow( pow(dx, 2) + pow(dy, 2) , 0.5)
        if self.size+other.size >= dd:
            return True
        else:
            return False

class RedBlob(Blob):
    def __init__(self):
        super().__init__(RED)
    def __add__(self, other_blob):
        if isinstance(other_blob, RedBlob):
            self.size += other_blob.size
            other_blob.size = 0

class BlueBlob(Blob):
    def __init__(self):
        super().__init__(BLUE)
    def __add__(self, other_blob):
        """
            blue+red --> minus size
            blue+blue --> plus size
        """
        if isinstance(other_blob, RedBlob):
            new_blue_size = self.size - other_blob.size
            if new_blue_size<=0:
                #print("Red with Blue colision +=SIZE")
                other_blob.size -= self.size
                self.size=0
            else:
                self.size -= other_blob.size
                other_blob.size=0
            #print("Red with Blue colision")
            #self.isReal()
            #other_blob.isReal()
        else:
            #print("Blue with Blue colision")
            self.size += other_blob.size
            other_blob.size = 0
            #del other_blob
"""
obj1 = RedBlob()
obj2 = BlueBlob()

obj1 + obj2
"""