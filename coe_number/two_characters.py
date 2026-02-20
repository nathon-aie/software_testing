def alternate(s):
    if type(s) != str:
        return "Invalid Input"
    elif len(s) < 1 or len(s) > 1000:
        return "Out of Range"
    max_len = 0
    unique_chars = list(set(s))
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1 = unique_chars[i]
            char2 = unique_chars[j]
            filtered_s = [c for c in s if c == char1 or c == char2]
            is_alternating = True
            for k in range(len(filtered_s) - 1):
                if filtered_s[k] == filtered_s[k + 1]:
                    is_alternating = False
                    break
            if is_alternating:
                max_len = max(max_len, len(filtered_s))
    return max_len
