firstname ='Влад'
lastname = 'Лось'
age = '20'
some_text = f'Привет,меня зовут {firstname} {lastname}, мне {age} лет'
print(some_text)
some_text_1 = some_text[3]
some_text_1x = some_text[2]
print(some_text_1)
print(some_text_1x)
#тут я не понял ,мне нужен 3 символ из текста или по нумерации пайтона(0,1,2,3) и сделал и так и так
some_text_2 = some_text[-2]
print(some_text_2)
some_text_3 = some_text[:6]
print(some_text_3)
some_text_4 = some_text[0:len(some_text)-2]
print(some_text_4)
some_str = 'Hello, World!'
print(some_str)
print(some_str.replace('World', "Влад"))
# Я заменил просто на свое имя, так как поставить переменную firstname туда нельзя,но вроде в задании и написанно,что просто заменить на имя, а не на переменную с именем
