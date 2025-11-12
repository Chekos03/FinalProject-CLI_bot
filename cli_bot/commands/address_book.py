from collections import UserDict 
from datetime import datetime,timedelta,date

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)


class Address(Field):
    def __init__(self, address):
        super().__init__(address)


class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        new_value = new_value.strip()
        if not new_value.isdigit() or len(new_value) != 10:
            raise ValueError("Номер телефону має бути до 10 символів.")
        self._value = new_value

    def __str__(self):
        return self._value


class Record:
    def __init__(self, name : str):
        self.name = Name(name)
        self.phones : list[Phone] = []
        self.birthday : Birthday = None
        self.address : Address = None
        
    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
            return "Телефон додано."
        except ValueError as e:
            return f"Невірний номер: {e}"
    
    def remove(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Телефон {phone} видалено."
        return f"Телефон {phone} не знайдено."
    
    def edit_phone(self,old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return f'Старий номер : {old_phone} був змінений на {new_phone}.'
        return 'Телефон не знайдено.'
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None
    
    def add_birthday(self,birthday:str):
        if self.birthday is not None:
            return f"У контакту '{self.name.value}' вже вказано день народження: {self.birthday}"
        try:
            self.birthday = Birthday(birthday)
            return "Дату народження додано."
        except ValueError as er:
            return f"Не вірний формат дати {er}"
    
    def add_address(self, address: str):
        self.address = Address(address)
        return "Адресу додано."
    
    def __str__(self):
        phones = '; '.join(phone.value for phone in self.phones) if self.phones else "Телефонів ще немає."
        birthday = f', день народження: {self.birthday}' if self.birthday else ""
        address = f', адреса: {self.address}' if self.address else ""
        return f"Контакт: {self.name.value}, телефон: {phones}{birthday}{address}"
    
    
class Birthday(Field):
    def __init__(self, value:str):
        try:
            birthday_date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте DD.MM.YYYY")
    def __str__(self):
        return self.value.strftime("%d.%m.%Y")

class AddressBook(UserDict): 
    def add_record(self, record):
        self.data[record.name.value] = record
        return
    
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Запис {name} видалено."
        return f"{name} не знайдено."
    
    def get_upcomming_birthdays(self):
        today = date.today()
        next_week = today + timedelta(days=7)
        upcoming = []

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year = today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                if today <= birthday_this_year <= next_week:
                    upcoming.append({
                        "name": record.name.value,
                        "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })
        return upcoming
