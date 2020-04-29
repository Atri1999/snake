#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:47:08 2020

@author: atri
"""

import pygame
import random 
import tkinter as tk
from tkinter import messagebox

pygame.init()

class cube(object):
    
    def __init__(self,pos,dirx=1,diry=0,color=(250,0,0)):
        self.pos=pos
        self.dirx=dirx
        self.diry=diry
        self.color=color
        
    def move(self,dirx,diry):
        self.dirx=dirx
        self.diry=diry
        self.pos=(self.pos[0]+self.dirx,self.pos[1]+self.diry)
        
    def draw(self,win,eyes=False):
        dis=side//row
        
        i=self.pos[0]
        j=self.pos[1]
        
        pygame.draw.rect(win,self.color,(i*dis+1,j*dis+1,dis-1,dis-1))
        
        if eyes:
            center=dis//2
            radius=3
            circleMiddle=(i*dis+center-radius,j*dis+8)
            circleMiddle2=(i*dis+dis-radius*2,j*dis+8)
            pygame.draw.circle(win,(0,0,0),circleMiddle,radius)
            pygame.draw.circle(win,(0,0,0),circleMiddle2 ,radius)
    
class snake(object):
    body=[]
    turns={}
    def __init__(self,color,pos):
        self.color=color
        self.head=cube(pos)
        self.body.append(self.head)
        self.dirx=0
        self.diry=1
        
        
    def move(self):
        global row,side
        for event in pygame.event.get():     
            if event.type==pygame.QUIT:
                pygame.quit()
                
        keys=pygame.key.get_pressed()
            
        for key in keys:
            if keys[pygame.K_LEFT]:
                self.dirx=-1
                self.diry=0
                self.turns[self.head.pos[:]]=[self.dirx,self.diry]  
            elif keys[pygame.K_RIGHT]:
                self.dirx=1
                self.diry=0
                self.turns[self.head.pos[:]]=[self.dirx,self.diry] 
            elif keys[pygame.K_UP]:
                self.dirx=0
                self.diry=-1
                self.turns[self.head.pos[:]]=[self.dirx,self.diry] 
            elif keys[pygame.K_DOWN]:
                self.dirx=0
                self.diry=1
                self.turns[self.head.pos[:]]=[self.dirx,self.diry] 
                
                
        for i,c in enumerate(self.body):
            p=c.pos[:]
            if p in self.turns:
                turn=self.turns[p]
                c.move(turn[0],turn[1])
                if i==len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirx==-1 and c.pos[0]<=0:
                    c.pos=(row-1,c.pos[1])
                elif c.dirx==1 and c.pos[0]>=row-1:
                    c.pos=(0,c.pos[1])
                elif c.diry==1 and c.pos[1]>=row-1:
                    c.pos=(c.pos[0],0)
                elif c.diry==-1 and c.pos[0]<=0:
                    c.pos=(c.pos[0],row-1)
                else:
                    c.move(c.dirx,c.diry)
       
    def add_cube(self):
        tail=self.body[-1]
        dx,dy=tail.dirx,tail.diry
        
        if dx==1 and dy==0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx==-1 and dy==0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx==0 and dy==-1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1))) 
        elif dx==0 and dy==1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        
        self.body[-1].dirx=dx
        self.body[-1].diry=dy   

    def reset(self,pos):
        self.head=cube(pos)
        self.body=[]
        self.turns={}
        self.body.append(self.head)
        self.dirx=0
        self.diry=1         
                    
                
    
    def draw(self,win):
         for i,c in enumerate(self.body):
             if i==0:
                 c.draw(win,True)
             else:
                 c.draw(win)
        
    
def draw_grid(win):    
    set_width=side//row
    x,y=0,0
    for i in range(row):
        x+=set_width
        y+=set_width
        pygame.draw.line(win,(100,100,100),(x,0),(x,side))
        pygame.draw.line(win,(100,100,100),(0,y),(side,y))
        
def random_snack(item):
    positions=item.body
    
    while True:
        x=random.randrange(row)
        y=random.randrange(row)
        if len(list(filter(lambda z:z.pos==(x,y),positions)))>0:
            continue
        else:
            break
        
    return (x,y)


def message_box(subject,content):
    root=tk.Tk()
    root.attributes("-topmost",True)
    root.withdraw()
    messagebox.showinfo(subject,content)
    try:
        root.destroy()
    except:
        pass
        

def redraw_window(win):
    global s,side,row,snack
    win.fill((0,0,0))
    draw_grid(win)
    s.draw(win)
    snack.draw(win)
    
    pygame.display.update()
    pass
    
    
def mainloop():
    global side,row,s,snack
    side=500
    row=20
    win=pygame.display.set_mode((side,side))
    pygame.display.set_caption("Snake Game")
    clock=pygame.time.Clock()
    s=snake((255,0,0),(10,10))
    snack=cube(random_snack(s),color=(0,250,0))
    run=True
    while run:
        pygame.time.delay(70)
        clock.tick(5)
        
        for event in pygame.event.get():     
            if event.type==pygame.QUIT:
                run=False
        s.move()
        if s.body[0].pos == snack.pos:
            s.add_cube()
            snack=cube(random_snack(s),color=(0,250,0))
            
        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print("Score:",len(s.body))
                message_box("You Lost!","Play Again")
                s.reset((10,10))
                break
            
            
        redraw_window(win)
    pygame.quit()
    
mainloop()        
        
    
        