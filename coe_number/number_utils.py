def is_prime_list(numbers):
    try:
        if not numbers:
            return False
        for num in numbers:
            if num < 0:
                return False
            else:
                for n in range(2, num):
                    if num % n == 0:
                        return False
        return True
    except TypeError:
        return False
