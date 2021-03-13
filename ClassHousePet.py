class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def get_name(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_age(self):
        return self.age

    def print_cat(self):
        print('Имя', self.name)
        print('Пол', self.sex)
        print('Возраст', self.age)

class Client:

    def __init__(self, name, balans):
        self.name = name
        self.balans = balans

    def get_name(self):
        return self.name

    def get_balans(self):
        return self.balans
    # Здесь можно было бы обойтись одной процедурой
    # но мне кажется если разделить то будет проще в дальнейшем
    def add_coming(self, money):
        self.balans += money

    def add_consumption(self, money):
        self.balans -= money

    # Для вывода можно переопределить __str__, но ведь не всегда при печати
    # нужно будет выводить баланс, поэтому вынес в отдельную процедуру
    def print_balans(self):
        print(f'Клиент "{self.name}". Баланс: {self.balans} руб.')

class Guest(Client):
    def __init__(self, name, adress, status):
        self.name = name
        self.adress = adress
        self.status = status

    def get_adress(self):
        return self.adress

    def get_status(self):
        return self.status

    def __str__(self):
        return f'{self.name}, {self.adress}, статус "{self.status}"'