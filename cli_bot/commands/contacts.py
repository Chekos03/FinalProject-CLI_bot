from .decorator import input_error
from .address_book import Record, Birthday, Name

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
    if len(args) < 3:
        return ("Помилка: команда 'change' очікує формат "
                "change <ім'я> name|phone|address|birthday|email [старе_значення] <нове_значення>.")
    name = args[0]
    subcommand = args[1].lower()
    params = args[2:]
    record = book.find(name)
    if not record:
        return 'Контакту не було знайдено.'

    handlers = {
        "name": _change_name,
        "phone": _change_phone,
        "email": _change_email,
        "address": _change_address,
        "birthday": _change_birthday,
    }

    handler = handlers.get(subcommand)
    if not handler:
        return "Невідома підкоманда. Доступні: name, phone, address, birthday, email."

    return handler(book, record, params, name)


def _change_name(book, record, params, original_name):
    if not params:
        return "Формат: change <ім'я> name <нове_ім'я>."
    new_name = params[0]
    current_name = record.name.value
    if new_name == current_name:
        return "Нове ім'я збігається з поточним."
    if book.find(new_name):
        return f"Контакт з ім'ям '{new_name}' вже існує."
    del book.data[current_name]
    record.name = Name(new_name)
    book.add_record(record)
    return f"Ім'я контакту змінено на {new_name}."


def _change_phone(_book, record, params, _original_name):
    if len(params) < 2:
        return "Формат: change <ім'я> phone <старий_номер> <новий_номер>."
    old_phone, new_phone = params[0], params[1]
    return record.edit_phone(old_phone, new_phone)


def _change_email(_book, record, params, _original_name):
    if len(params) < 2:
        return "Формат: change <ім'я> email <старий_email> <новий_email>."
    old_email, new_email = params[0], params[1]
    return record.edit_email(old_email, new_email)


def _change_address(_book, record, params, _original_name):
    new_address = " ".join(params).strip()
    if not new_address:
        return "Будь ласка, введіть нову адресу."
    return record.add_address(new_address)


def _change_birthday(_book, record, params, _original_name):
    if not params:
        return "Формат: change <ім'я> birthday <DD.MM.YYYY>."
    new_birthday = params[0]
    try:
        record.birthday = Birthday(new_birthday)
        return "Дату народження оновлено."
    except ValueError as er:
        return f"Не вірний формат дати {er}"

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
