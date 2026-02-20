def alternatingCharacters(s):
    if type(s) != str:
        return "Not String"
    elif len(s) < 1 or len(s) > 100000:
        return "Out of Range"
    else:
        char = "AB"
        deleteion_count = 0
        for i in range(len(s) - 1):
            if s[i] not in char or s[i + 1] not in char:
                return "Invalid Input"
            elif s[i] == s[i + 1]:
                deleteion_count += 1
        return deleteion_count
