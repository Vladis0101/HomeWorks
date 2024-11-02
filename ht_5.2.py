#Я мог копейки сделать как рубли и было бы короче, но я решил двумя способами сделать
rubles = int(input('рубли:'))
kopecks = int(input('копейки:'))
if  rubles % 10 == 1 and rubles % 100 != 11 and rubles < 1000 :
    print(rubles,'рубль')
elif rubles == 11:
    print(rubles, 'рублей')
elif rubles == 111:
    print(rubles, 'рублей')
elif rubles == 211:
    print(rubles, 'рублей')
elif rubles == 311:
    print(rubles, 'рублей')
elif rubles == 411:
    print(rubles, 'рублей')
elif rubles == 511:
    print(rubles, 'рублей')
elif rubles == 611:
    print(rubles, 'рублей')
elif rubles == 711:
    print(rubles, 'рублей')
elif rubles == 811:
    print(rubles, 'рублей')
elif rubles == 911:
    print(rubles, 'рублей')
elif rubles % 10 == 2 and rubles < 1000:
    print(rubles,'рубля')
elif rubles % 10 == 3 and rubles < 1000:
    print(rubles,'рубля')
elif rubles % 10 == 4 and rubles < 1000:
    print(rubles,'рубля')
elif rubles % 10 == 6 and rubles < 1000:
    print(rubles,'рублей')
elif rubles % 10 == 7 and rubles < 1000:
    print(rubles,'рублей')
elif rubles % 10 == 8 and rubles < 1000:
    print(rubles,'рублей')
elif rubles % 10 == 9 and rubles < 1000:
    print(rubles,'рублей')
elif rubles % 5 == 0 and rubles <= 1000:
    print(rubles,'рублей')
elif rubles > 1000:
    print('Введите до 1000')

if kopecks == 1:
    print(kopecks,'копейка')
elif 1 < kopecks <=4:
    print(kopecks,'копейки')
elif 5 <= kopecks <= 20:
    print(kopecks,'копеек')
elif kopecks == 21:
    print(kopecks,'копейка')
elif 21 < kopecks <=24:
    print(kopecks,'копейки')
elif 25 <= kopecks <= 30:
    print(kopecks,'копеек')
elif kopecks == 31:
    print(kopecks,'копейка')
elif 31 < kopecks <=34:
    print(kopecks,'копейки')
elif 35 <= kopecks <= 40:
    print(kopecks, 'копеек')
elif kopecks == 41:
    print(kopecks,'копейка')
elif 41 < kopecks <=44:
    print(kopecks,'копейки')
elif 45 <= kopecks <= 50:
    print(kopecks, 'копеек')
elif kopecks == 51:
    print(kopecks, 'копейка')
elif 51 < kopecks <=54:
    print(kopecks,'копейки')
elif 55 <= kopecks <= 60:
    print(kopecks, 'копеек')
elif kopecks == 61:
    print(kopecks, 'копейка')
elif 61 < kopecks <=64:
    print(kopecks,'копейки')
elif 65 <= kopecks <= 70:
    print(kopecks, 'копеек')
elif kopecks == 71:
    print(kopecks, 'копейка')
elif 71 < kopecks <= 74:
    print(kopecks, 'копейки')
elif 75 <= kopecks <= 80:
    print(kopecks, 'копеек')
elif kopecks == 81:
    print(kopecks, 'копейка')
elif 81 < kopecks <=84:
    print(kopecks,'копейки')
elif 85 <= kopecks <= 90:
    print(kopecks, 'копеек')
elif kopecks == 91:
    print(kopecks, 'копейка')
elif 91 < kopecks <=94:
    print(kopecks,'копейки')
elif 95 <= kopecks <= 100:
    print(kopecks, 'копеек')
elif kopecks > 100:
    print('Введите не более 100 копеек')