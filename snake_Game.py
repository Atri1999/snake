#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 10:47:08 2020

@author: atri
"""

import pygame 

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
        pass
    
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
        for event in pygame.event.get():     
            if event.type==pygame.QUIT:
                pygame.quit()
                
            keys=pygame.key.get_pressed()
               
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
                if i==len[self.body]-1:
                    self.turn.pop(p)
            else:
                if c.dirx==-1 and c.pos[0]<=0:
                    c.pos=(c.rows-1,c.pos[1])
                elif c.dirx==1 and c.pos[0]>=c.rows-1:
                    c.pos=(0,c.pos[1])
                elif c.diry==1 and c.pos[1]>=c.rows-1:
                    c.pos=(c.pos[0],0)
                elif c.diry==-1 and c.pos[0]<=0:
                    c.pos=(c.pos[0],c.rows-1)
                else:
                    c.move(c.dirx,c.diry)
                    
                    
                
           
           
           
           
        
    
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
        

def redraw_window(win):
    global s
    win.fill((0,0,0))
    draw_grid(win)
    s.draw(win)
    
    pygame.display.update()
    pass
    
    
def mainloop():
    global side,row,s
    side=500
    row=20
    win=pygame.display.set_mode((side,side))
    pygame.display.set_caption("Snake Game")
    clock=pygame.time.Clock()
    s=snake((255,0,0),(10,10))
    
    run=True
    while run:
        pygame.time.delay(50)
        clock.tick(10)
        
        for event in pygame.event.get():     
            if event.type==pygame.QUIT:
                run=False
                
        redraw_window(win)
    pygame.quit()
    
mainloop()        
        
    
        