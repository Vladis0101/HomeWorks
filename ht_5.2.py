rubles = int(input('рубли:'))
kopecks = int(input('копейки:'))
if rubles % 10 == 1 and rubles % 100 != 11 and rubles <= 1000:
    print(rubles,'рубль')
elif 2 <= rubles % 10 <= 4 and not (12 <= rubles % 100 <= 14) and rubles <= 1000:
    print(rubles,'рубля')
elif rubles > 1000:
    print('Введите до 1000')
else:
    print(rubles,'рублей')

if kopecks % 10 == 1 and kopecks % 100 != 11 and kopecks <= 100:
    print(kopecks,'копейка')
elif 2 <= kopecks % 10 <= 4 and not (12 <= kopecks % 100 <= 14) and kopecks <= 100:
    print(kopecks,'копейки')
elif kopecks > 100:
    print('Введите не более 100 копеек')
else:
    print(kopecks,'копеек')