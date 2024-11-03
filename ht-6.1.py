def yes_or_no():
    numbers = input('Введите целые числа, разделенные запятыми: ').split(',')
    seen = set()
    for number in numbers:
        num = int(number)
        if num in seen:
            print("Yes")
        else:
            print("No")
            seen.add(num)
yes_or_no()