# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 14:36:11 2022

@author: iscca
"""

import random

def create_lista():
    numbers = []
    for i in range(1, 365+1):
        numbers.append([i," "])
    return numbers

def randy():
    a = random.randint(1,365)
    return a

def random_num(file):
    control = 1
    while control == 1:
        a = randy()
        with open(file, 'r') as f:
            if str(a) in f.read():
                f.close()
                return True
                
            else:
                with open(file, 'a') as f:
                    f.write(str(a)+"\n")
                    print(a)
                    f.close()
                    control = 2 

    

file = "ahorro.txt"
num_lista = create_lista()
numero = random_num(file)


