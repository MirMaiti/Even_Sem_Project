#Snake Tutorial Python
import numpy as np
import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

num_rows    = 20
num_columns = 20
vec = pygame.math.Vector2

class cube(object):
    rows = num_rows
    w = 500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

        
    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)

class Snake(object):
    
    def __init__(self, color, pos):
        self.win = pygame.display.set_mode((500, 500))
        self.reset((10,10))
        self.color = color
        self.clock = pygame.time.Clock()


    def move(self,action):
        reward = 0
        self.frame+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if action == [1, 0, 0]:  # Move forward
            pass

        elif action == [0, 1, 0]:  # Turn right
            if self.dirnx == 0:
                self.dirnx = -self.dirny
                self.dirny = 0
            else:
                self.dirny = self.dirnx
                self.dirnx = 0

        elif action == [0, 0, 1]:  # Turn left
            if self.dirnx == 0:
                self.dirnx = self.dirny
                self.dirny = 0
            else:
                self.dirny = -self.dirnx
                self.dirnx = 0


        self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
        
        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx,c.dirny)
        
        #Display the game:
        
        self.redrawWindow(self.win)

        #Adjusting Reward
        if self.check_collision() or (self.frame>100*len(self.body)):
            reward = -10
            return (reward,True,len(self.body))
        
        if self.body[0].pos == self.snack.pos:
            reward = 10
            self.addCube()
            self.snack = cube(self.randomSnack(num_rows, self), color=(0,255,0))

        

        return (reward,self.check_collision(),len(self.body))
    
    def danger(self):
        point_l = (self.head.pos[0] - 1, self.head.pos[1])
        point_r = (self.head.pos[0] + 1, self.head.pos[1])
        point_u = (self.head.pos[0], self.head.pos[1] - 1)
        point_d = (self.head.pos[0], self.head.pos[1] + 1)

        danger_forward,danger_left,danger_right=False,False,False

        if [self.dirnx,self.dirny] == [1,0]:
            if (point_r in self.body) or (point_r[0] < 0 or point_r[0] >= num_rows or point_r[1] < 0 or point_r[1] >= num_columns):
                danger_forward = True
            if (point_u in self.body) or (point_u[0] < 0 or point_u[0] >= num_rows or point_u[1] < 0 or point_u[1] >= num_columns):
                danger_left = True
            if (point_d in self.body) or (point_d[0] < 0 or point_d[0] >= num_rows or point_d[1] < 0 or point_d[1] >= num_columns):
                danger_right = True
        
        if [self.dirnx,self.dirny] == [-1,0]:
            if (point_l in self.body) or (point_l[0] < 0 or point_l[0] >= num_rows or point_l[1] < 0 or point_l[1] >= num_columns):
                danger_forward = True
            if (point_d in self.body) or (point_d[0] < 0 or point_d[0] >= num_rows or point_d[1] < 0 or point_d[1] >= num_columns):
                danger_left = True
            if (point_u in self.body) or (point_u[0] < 0 or point_u[0] >= num_rows or point_u[1] < 0 or point_u[1] >= num_columns):
                danger_right = True

        if [self.dirnx,self.dirny] == [0,1]:
            if (point_d in self.body) or (point_d[0] < 0 or point_d[0] >= num_rows or point_d[1] < 0 or point_d[1] >= num_columns):
                danger_forward = True
            if (point_r in self.body) or (point_r[0] < 0 or point_r[0] >= num_rows or point_r[1] < 0 or point_r[1] >= num_columns):
                danger_left = True
            if (point_l in self.body) or (point_l[0] < 0 or point_l[0] >= num_rows or point_l[1] < 0 or point_l[1] >= num_columns):
                danger_right = True

        if [self.dirnx,self.dirny] == [0,-1]:
            if (point_u in self.body) or (point_u[0] < 0 or point_u[0] >= num_rows or point_u[1] < 0 or point_u[1] >= num_columns):
                danger_forward = True
            if (point_l in self.body) or (point_l[0] < 0 or point_l[0] >= num_rows or point_l[1] < 0 or point_l[1] >= num_columns):
                danger_left = True
            if (point_r in self.body) or (point_r[0] < 0 or point_r[0] >= num_rows or point_r[1] < 0 or point_r[1] >= num_columns):
                danger_right = True       
        
        return [danger_forward,danger_right,danger_left]


    def check_collision(self):
        head_pos = self.body[0].pos

        # Check collision with walls
        if head_pos[0] < 0 or head_pos[0] >= num_rows or head_pos[1] < 0 or head_pos[1] >= num_columns:
            return True  # Collision with wall

        # Check self-collision
        for x in range(len(self.body)):
            if self.body[x].pos in list(map(lambda z: z.pos, self.body[x+1:])):
                return True  # Self-collision

        return False  # No collision   

    def reset(self, pos):
        self.body = []
        self.frame = 0
        self.head = cube(pos)
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.snack = cube(self.randomSnack(num_rows, self),dirnx=1,dirny=0,color=(0,255,0))


    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
        

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)

    def drawGrid(self,w, rows, surface):
        sizeBtwn = w // rows

        x = 0
        y = 0
        for l in range(rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(surface, (255,255,255), (x,0),(x,w))
            pygame.draw.line(surface, (255,255,255), (0,y),(w,y))
            

    def redrawWindow(self,surface):
        surface.fill((0,0,0))
        self.draw(surface)
        self.snack.draw(surface)
        self.drawGrid(500,20, surface)
        pygame.display.update()


    def randomSnack(self,rows, item):

        positions = item.body

        while True:
            x = random.randrange(rows)
            y = random.randrange(rows)
            if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                continue
            else:
                break
            
        return (x,y)


    def message_box(self,subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass


