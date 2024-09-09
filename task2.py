#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:12:41 2024

@author: ruslan
"""


class Fibonachi:
    
    def __init__(self):
        self._fibonachiNumbers = [0, 1]
        self._currentPosition = -1
        
    def calculateNext(self):
        _fibonachiNumbersLength = len(self._fibonachiNumbers)
        self._currentPosition+=1
        if self._currentPosition >= _fibonachiNumbersLength:
            self._AddUncalculatedElement()
        return self._fibonachiNumbers[self._currentPosition]
    
    def _calculateNextUncalculatedElement(self):
        _fibonachiNumbersLength = len(self._fibonachiNumbers)
        lastElement = self._fibonachiNumbers[_fibonachiNumbersLength - 1]
        prevElement = self._fibonachiNumbers[_fibonachiNumbersLength - 2]
        nextElement = lastElement + prevElement
        return nextElement
    
    def _AddUncalculatedElement(self):
        nextElement = self._calculateNextUncalculatedElement()
        self._fibonachiNumbers.append(nextElement)
        

    
def task0_1():
    fibonachi = Fibonachi()
    for _ in range(10):
        print(fibonachi.calculateNext())

if __name__ == '__main__':
    task0_1()