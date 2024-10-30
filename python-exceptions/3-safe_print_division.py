#!/usr/bin/python3
def safe_print_division(a, b):
    div_result = 0
    try:
        div_result = a / b
    except ZeroDivisionError:
        pass
    else:
        return div_result
    finally:
        print("Inside result: {}".format(div_result))
        return None
