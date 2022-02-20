def capital_indexes(letter):
    result = []
    for item in letter:
        if item.isupper() is True:
            result.append(letter.index(item))
    return result
print(capital_indexes("HeLlO"))
