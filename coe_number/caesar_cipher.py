import string


def caesarCipher(s, k):
    if type(s) != str or type(k) != int:
        return "Invalid Input"
    elif len(s) < 1 or len(s) > 100 or k < 0 or k > 100:
        return "Out of Range"
    else:
        al_lower = string.ascii_lowercase
        al_upper = string.ascii_uppercase
        new_s = ""
        for i in range(len(s)):
            if s[i].islower():
                new_s += al_lower[(al_lower.index(s[i]) + k) % len(al_lower)]
            elif s[i].isupper():
                new_s += al_upper[(al_upper.index(s[i]) + k) % len(al_upper)]
            else:
                new_s += s[i]
        return new_s
