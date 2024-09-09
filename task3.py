#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:17:22 2024

@author: ruslan
"""
import random

def task1():
    aq=random.uniform(11, 19)
    print('aq=', aq)
    random.seed(22)
    print(random.random())

def generatePassword():
    password = ''
    for _ in range(10):
        password = password + random.choice(list('RuslanMAKHNEV123456789'))
    return password


if __name__ == '__main__':
    task1();
    print(generatePassword())