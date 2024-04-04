#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        return res

    except ZeroDivisionError:
        pass

    finally:
        print('Inside result: {:.1f}'.format(res))

    return None
