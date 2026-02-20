def funnyString(s):
    if type(s) != str:
        return "Not String"
    elif len(s) < 2 or len(s) > 10000:
        return "Out of Range"
    else:
        r = s[::-1]
        for i in range(len(s) - 1):
            if abs(ord(r[i]) - ord(r[i + 1])) != abs(ord(s[i]) - ord(s[i + 1])):
                return "Not Funny"
    return "Funny"
