import pygame
import sys
import random as r
#easter egg
a = r.randint(0,255)
b = r.randint(0,255)
c = r.randint(0,255)
if [a,b,c] == [223, 163, 49]:
    apple_color = [100, 255, 0]
else:
    apple_color = [255, 50, 0]



class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((Screen_Width/2),(Screen_Height/2))]
        self.direction = r.choice([up, down, left, right])
        self.color = (a,b,c)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point
    
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*Grid_Size)) % Screen_Width),((cur[1] + (y*Grid_Size)) % Screen_Height))
        if len(self.positions) > 4 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        self.length = 1
        self.positions = [((Screen_Width/2),(Screen_Height/2))]
        self.direction = r.choice([up, down, left, right])
        self.color = (a,b,c)
    
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0]),(p[1]),(Grid_Size,Grid_Size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.turn(down)
                if event.key == pygame.K_UP:
                    self.turn(up)
                if event.key == pygame.K_LEFT:
                    self.turn(left)
                if event.key == pygame.K_RIGHT:
                    self.turn(right)


class food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = apple_color
        self.randomise_position()

    def randomise_position(self):
        self.position = (r.randint(0, Grid_Width - 1), r.randint(0, Grid_Height - 1))

    def draw(self, surface):
        r = pygame.Rect((self.position[0]),(self.position[1]),(Grid_Size,Grid_Size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
        

def drawGrid(surface):
    for y in range(0, int(Grid_Height)):
        for x in range(0, int(Grid_Width)):
            if ((x + y) % 2 == 1):
                r = pygame.Rect((x*Grid_Size),(y*Grid_Size), (Grid_Size,Grid_Size))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*Grid_Size),(y*Grid_Size), (Grid_Size,Grid_Size))
                pygame.draw.rect(surface, (84, 194, 205), rr)


Screen_Width = 12
Screen_Height = 12

Grid_Size = 1
Grid_Width = Screen_Width/Grid_Size
Grid_Height = Screen_Height/Grid_Size

up = (1,0)
down = (-1,0)
left = (0,-1)
right = (0,1)

def main():
    pygame.init()

    clock = pyhame.time.Clock()
    screen = pygame.display.set_mode((Screen_Width, Screen_Height), 0, 32)
    
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = snake()
    food = food()

    score = 0
    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food_randomise_position()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0,0))
        pygame.display.update()


        
        