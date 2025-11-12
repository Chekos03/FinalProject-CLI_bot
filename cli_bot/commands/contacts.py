from .decorator import input_error
from .address_book import Record

@input_error
def add_contact(args, book):
    if len(args) < 2:
        return "Помилка: команда 'add' очікує 2 аргументи: add <ім'я> <телефон>."
    
    name, phone = args[0], args[1]
    record = book.find(name)

    if not record:
        record = Record(name)
        book.add_record(record)
        msg = "Контакт додано."
    else:
        msg = "Контакт оновлено."
    
    phone_result = record.add_phone(phone)
    if "Невірний номер" in phone_result:
        return phone_result
    return f"{msg} {phone_result}"

@input_error
def change_contact(args, book):
    if len(args) < 2:
        return "Помилка: команда 'change' очікує 2 аргументи: change <ім'я> <старий_номер>. <новий_телефон>."
    name, old_phone, new_phone = args[0], args[1], args[2]
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдено.'
    record_result = record.edit_phone(old_phone, new_phone)
    return f"Контакт змінено {record_result}."

@input_error
def show_phone(args, book):
    if len(args) < 1:
        return "Помилка: команда 'phone' очікує 1 аргумент: phone <ім'я>."
    name = args[0]
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдено.'
    return f'Контакт знайдено {record}.'

@input_error
def show_all(book):
    if not book.data:
        return "Немає збережених контактів."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args, book):
    if len(args) < 2:
        return "Помилка: команда 'add-birthday' очікує 2 аргументи: add_birthday <ім'я> <дата_народження>."
    name, birth_date = args[0], args[1]
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдно.'
    return record.add_birthday(birth_date)

@input_error
def show_birthday(args,book):
    if len(args) < 1:
        return "Помилка: команда 'show-birthday' очікує 1 аргумент: show <ім'я>" 
    name = args[0]
    record = book.find(name)
    if not record:
        return 'Контакту не існує.'
    if not record.birthday:
        return 'Не контакті не вказано день народження.'
    return f"{name}: {record.birthday}"

@input_error
def add_address(args, book):
    if len(args) < 2:
        return "Помилка: команда 'add-address' очікує 2 аргументи: add-address <ім'я> <адреса>."
    name = args[0]
    address = " ".join(args[1:])
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдно.'
    return record.add_address(address)

@input_error
def add_email(args, book):
    if len(args) < 2:
        return "Помилка: команда 'add-email' очікує 2 аргументи: add-email <ім'я> <email>."
    name, email = args[0], args[1]
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдно.'
    return record.add_email(email)

@input_error
def birthdays(book):
    upcoming = book.get_upcomming_birthdays()
    if not upcoming:
        return "На цьому тижні немає днів народження."
    return "\n".join(f"{b['name']} → {b['birthday']}" for b in upcoming)
