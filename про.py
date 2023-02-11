import pygame


size=[500,500]
pygame.init()
screen=pygame.display.set_mode(size)

# Colours
LIME = (0,255,0)
RED = (255, 0, 0)
BLACK = (0,0,0)
PINK = (255,102,178)
SALMON = (255,192,203)
WHITE = (255,255,255)
LIGHT_PINK = (255, 181, 197)
SKY_BLUE = (176, 226, 255)
screen.fill(BLACK)

# Width and Height of game box
width=50
height=50

# Margin between each cell
margin = 5

# Create a 2 dimensional array. A two dimesional
# array is simply a list of lists.
grid=[]
for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)
grid[1][5] = 1

# Set title of screen
pygame.display.set_caption("Spatial Recall")
done=False
clock=pygame.time.Clock()

# -------- Main Program Loop -----------
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT:
            done=True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
            column=pos[0] // (width+margin)
            row=pos[1] // (height+margin)
            grid[row][column]=1
            print("Click ",pos,"Grid coordinates: ",row,column)


# Draw the grid
for row in range(10):
    for column in range(10):
        color = LIGHT_PINK
        if grid[row][column] == 1:
            color = RED
        pygame.draw.rect(screen,color,[(margin+width)*column+margin,(margin+height)*row+margin,width,height])

# Limit to 20 frames per second
clock.tick(20)

# Go ahead and update the screen with what we've drawn.
pygame.display.flip()

pygame.quit ()