def staircase(n, pattern):
    try:
        if n < 0 or n >= 30:
            return "Out of Range"
        if len(pattern) > 1 or len(pattern) == 0:
            return "Invalid Input"
        result = ""
        for i in range(1, n + 1):
            result += (" " * (n - i)) + (pattern * i) + "\n"
        return result[:-1]
    except TypeError:
        return "Invalid Input"
