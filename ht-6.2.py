def count_char(STR_VAL):
    char_count = {}
    for char in STR_VAL:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
STR_VAL = 'python is the fastest-growing major programming language'
result = count_char(STR_VAL)
for char, count in result.items():
    print(f"'{char}': {count}")