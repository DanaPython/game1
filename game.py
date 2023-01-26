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