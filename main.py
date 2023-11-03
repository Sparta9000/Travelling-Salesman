import pygame
from math import sqrt

pygame.init()

displayWidth = 800
displayHeight = 600
circleRadius = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Travelling Salesman')

running = True
start = False

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
                #print(event)
                start = True

        #print(event)

    gameDisplay.fill(BLACK)

    if start:
        if points:
            point = points[0]
            while point.done:
                point = point.next

            i = points.index(point)

            for j, point2 in enumerate(points):
                if j != i:
                    if not point2.done:
                        if point2 not in point.values:
                            point.next = point2
                            point.values[point2] = point.distance(point2)
                            break
            else:
                if point.values:
                    point.next = min(point.values, key=lambda x: point.values[x])
                    point.done = True

    for point in points:
        if point.next:
            pygame.draw.line(gameDisplay, WHITE, point.getTuple(), point.next.getTuple())

    for point in points:
        pygame.draw.circle(gameDisplay, GREEN, point.getTuple(), circleRadius)

    pygame.display.update()

pygame.quit()
quit()