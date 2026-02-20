def cat_and_mouse(x, y, z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
        if x <= 0 or y <= 0 or z <= 0 or x >= 100 or y >= 100 or z >= 100:
            return "Out of Range"
        else:
            if abs(x - z) < abs(y - z):
                return "Cat A"
            elif abs(x - z) > abs(y - z):
                return "Cat B"
            else:
                return "Mouse C"
    except ValueError:
        return "Invalid Input"
    except TypeError:
        return "Invalid Input"
