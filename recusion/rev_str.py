def reverse_string(s):
    if len(s) == 0:
        return s

    return reverse_string(s[1:]) + s[0]

text = "Python"

print(reverse_string(text))