def mid(string):
    if len(string) % 2 == 0:
        return ""
    else:
        middle_letter = int(len(string) / 2)
        return string[middle_letter : middle_letter + 1]

print(mid("abc"))
print(mid("aaaa"))
