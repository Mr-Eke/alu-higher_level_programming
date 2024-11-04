#!/usr/bin/python3

def divide_elements(a, b):
    try:
        return a / b
    except (ZeroDivisionError):
        print('division by zero')
        return 0
    except (TypeError):
        print('wrong type')
        return 0

def list_division(my_list_1, my_list_2, list_length):
    return [
        divide_elements(a, b)
        for a, b in zip(my_list_1[:list_length], my_list_2[:list_length])
    ]

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)
