#!/usr/bin/python3
def fizbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print('Fizz', end=' ')
        elif 1 % 15 == 0:
            print('FizzBuzz', end='')
        else:
            print(i, end=' ')
fizbuzz()
