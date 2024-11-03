def bread(func):
    def wrapper(*args,**kwargs):
        print("</------------\\>")
        func(*args,**kwargs)
        print("<\\____________/>")
    return wrapper

def tomato(func):
    def wrapper(*args,**kwargs):
        print("*** помидоры ****")
        func(*args,**kwargs)
    return wrapper

def salad(func):
    def wrapper(*args,**kwargs):
        print("~~~~ салат ~~~~~")
        func(*args,**kwargs)
    return wrapper

def cheese(func):
    def wrapper(*args,**kwargs):
        print("^^^^^ сыр ^^^^^^")
        func(*args,**kwargs)
    return wrapper

def onion(func):
    def wrapper(*args,**kwargs):
        print("----- лук ------")
        func(*args,**kwargs)
    return wrapper


def beef():
    print("### говядина ###")

def chicken():
    print("|||| курица ||||")

@ bread
@ onion
@ tomato
def make_hamburger():
    beef()

@ bread
@ cheese
@ salad
def make_chikenburger():
    chicken()

# Это уже чисто для интереса все в одно смешал
@ bread
@ cheese
@ onion
@ salad
@ tomato
def make_combo_burger():
    beef()
    chicken()


print('Гамбургер:')
make_hamburger()

print('\nЧикенбургер:')
make_chikenburger()

print('\nКомбо Бургер:')
make_combo_burger()


