#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:35:29 2024

@author: ruslan
"""
import time
import task2
import matplotlib.pyplot as plt

def runTests(func, numberOfTests):
    numbers = []
    times = []
    for i in range(numberOfTests):
        times.append(measureTime(func, i))
        numbers.append(i)
    return numbers, times
        
def measureTime(func, numberOfFibonachiNumber):
    startTime = time.time()
    func(numberOfFibonachiNumber)
    endTime = time.time()    
    return endTime - startTime

def getFibonachiNumberByFor(numberOfFibonachiNumber):
    fibonachi = task2.Fibonachi()
    for _ in range(numberOfFibonachiNumber):
        fibonachi.calculateNext()
    return fibonachi.calculateNext()

def getFibonachiNumberByRecursion(numberOfFibonachiNumber):
    return calculateFibonachi(numberOfFibonachiNumber)
    
def calculateFibonachi(numberOfFibonachiNumber):
    if numberOfFibonachiNumber == 0:
        return 0
    elif numberOfFibonachiNumber == 1:
        return 1
    return calculateFibonachi(numberOfFibonachiNumber-1) + calculateFibonachi(numberOfFibonachiNumber-2)

if __name__ == '__main__':
    numberOfFibonachiNumber = 32
    print('numberOfFibonachiNumber', numberOfFibonachiNumber)
    print('fibanachiNumber', getFibonachiNumberByFor(numberOfFibonachiNumber))
    numbersByFor, timesByFor = runTests(getFibonachiNumberByFor, numberOfFibonachiNumber)
    numbersByRecursion, timesByRecursion = runTests(getFibonachiNumberByRecursion, numberOfFibonachiNumber)
    plt.plot(numbersByFor, timesByFor, label='cycle time')
    plt.plot(numbersByRecursion, timesByRecursion, label='funct time')
    plt.legend()
    plt.show()
