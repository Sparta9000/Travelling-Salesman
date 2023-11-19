import pygame
from math import sqrt

pygame.init()

displayWidth = 800
displayHeight = 600
circleRadius = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Travelling Salesman')

font = pygame.font.Font('freesansbold.ttf', 15)

running = True
start = False
cost = 0
last = None

points = []

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None
        self.done = False
        self.values = {}

    def __sub__(self, other):
        return Point(abs(self.x - other.x), abs(self.y - other.y))
    
    def __lt__(self, other: int):
        return self.x < other and self.y < other
    
    def getTuple(self):
        return (self.x, self.y)
    
    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def add_point(point):
    point = Point(*point)
    for i in points:
        if point - i < circleRadius:
            return

    points.append(point)

def remove_point(point):
    point = Point(*point)
    for count, i in enumerate(points):
        if point - i < circleRadius:
            points.pop(count)
            break

def all_done():
    for point in points:
        if not point.done:
            return False
        
    return True

def set_points(score):
    text = font.render(f"Cost: {int(score)}", True, WHITE)
    textRect = text.get_rect()
    textRect.center = displayWidth//12, displayHeight//12
    gameDisplay.blit(text, textRect)

while running:
    #start = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                add_point(event.pos)
            elif event.button == 3:
                remove_point(event.pos)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cost = 0
                #print(event)
                start = True
                last = None
                for point in points:
                    point.done = False
            elif event.key == pygame.K_BACKSPACE:
                cost = 0
                points = []
                start = False
                last = None
            elif event.key == pygame.K_RIGHT:
                start = True

        #print(event)

    gameDisplay.fill(BLACK)

    if start:
        if points:
            point = points[0]
            while point and point.done:
                point = point.next

            if point:
                i = points.index(point)

                for j, point2 in enumerate(points):
                    if j != i:
                        if not point2.done:
                            if point2 not in point.values:
                                point.next = point2
                                point.values[point2] = point.distance(point2)
                                break
                else:
                    point.next = None
                    last = point
                    if point.values:
                        point.next = min(point.values, key=lambda x: point.values[x])
                        cost += point.values[point.next]
                    point.done = True
                    point.values.clear()

            else:
                if last:
                    cost += last.distance(points[0])
                start = False
                

    for point in points:
        if point.next:
            pygame.draw.line(gameDisplay, WHITE, point.getTuple(), point.next.getTuple())
    if points and last:
        pygame.draw.line(gameDisplay, WHITE, points[0].getTuple(), last.getTuple())

    for point in points:
        pygame.draw.circle(gameDisplay, GREEN if point.done else RED, point.getTuple(), circleRadius)

    set_points(cost)

    pygame.display.update()

pygame.quit()
quit()