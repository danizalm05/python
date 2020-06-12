"""
 https://www.pygame.org/ 
 https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/pygame-tutorial-movement/
 https://techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/jumping/
"""
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))  # window  500 X 500
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(10)  # delay amount of 0.1 milliseconds.
    for event in pygame.event.get():  # loop through a list keyboard or mouse events.
        if event.type == pygame.QUIT:  # The red button in the corner of the window is clicked
            run = False  # Ends the game loop
    keys = pygame.key.get_pressed()  # This will give us a dictonary .
                                     # 1 - key pressed       0 - key not pressed.

    if keys[pygame.K_LEFT]  and x > vel:  # Don't move over screen left side .
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:  # Don't move over screen left side
        x += vel
    if keys[pygame.K_UP]    and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    win.fill((0, 0, 0))  # Fills the screen with black
                  # window/surface, color, rect
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()  # This updates the screen so we can see our rectangle
pygame.quit()  # close our game
