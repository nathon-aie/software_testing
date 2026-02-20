import random


def guess_int(start, stop):
    if type(start) != int or type(stop) != int:
        return "Invalid Input"
    elif start >= stop:
        return "Out of Range"
    return random.randint(start, stop)


def guess_float(start, stop):
    if type(start) != float or type(stop) != float:
        return "Invalid Input"
    elif start >= stop:
        return "Out of Range"
    return random.uniform(start, stop)
