#!/usr/bin/env python
# coding: utf-8

# In[2]:


## python simple game project
import random
win = random.randint(10,20)
num = int(input('enter a number between 1 to 100:'))
game_over = False
while not game_over:
    if win == num:
        game_over = True
    else:
        if num>win:
           print('ading mmala')
           num = int(input('enter a number between 1 to 100:'))
        else:
            if num<win:
                print('enter max')
                num = int(input('enter a num:'))
            

