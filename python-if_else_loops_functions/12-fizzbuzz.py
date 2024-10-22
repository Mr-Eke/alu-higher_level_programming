#!/usr/bin/python3
# def fizbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0:
#             print('Fizz', end=' ')
#         elif i % 5 == 0:
#             print('Buzz', end=' ')
#         elif i % 15 == 0:
#             print('FizzBuzz', end='')
#         else:
#             print(i, end=' ')
def fizzbuzz():
    for i in range(1, 101):
        fizzBuzz = "Fizz" * (not i % 3) + "Buzz" * (not i % 5)
        if not fizzBuzz:
            fizzBuzz = i
        print('{}'.format(fizzBuzz), end=' ')
