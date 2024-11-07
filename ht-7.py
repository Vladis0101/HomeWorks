class Phone:
    brand:str
    model:str
    issue_year:int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    @staticmethod
    def receive_call(name) -> str:
        return f"Звонит {name}"

    def get_info(self) -> tuple:
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return f"{{\n Бренд: “{self.brand}”\n Модель: “{self.model}”\n Год выпуска: “{self.issue_year}”\n}}"

my_phone = Phone('Samsung', 'Galaxy S24+','2024')

print(Phone.receive_call('Влад'))
print(my_phone.get_info())
print(my_phone)
