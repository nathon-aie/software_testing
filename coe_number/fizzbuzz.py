def fizzbuzz(n):
    try:
        if n % 3 == 0 and n % 5 == 0:
            return "FizzBuzz"
        elif n % 3 == 0:
            return "Fizz"
        elif n % 5 == 0:
            return "Buzz"
        else:
            return n
    except TypeError:
        return "Invalid Input"
    except ValueError:
        return "Invalid Input"
