from .decorator import input_error
from .address_book import Record

@input_error
def add_contact(args, book):
    if len(args) < 2:
        return "Помилка: команда 'add' очікує 2 аргументи: add <ім'я> <телефон>."
    
    name, phone = args[0], args[1]
    record = book.find(name)
    existing_owner = book.find_record_by_phone(phone)
    if existing_owner and (record is None or existing_owner.name.value != record.name.value):
        return f"Номер {phone} вже використовується контактом '{existing_owner.name.value}'."
    
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

    if subcommand == "name":
        if not params:
            return "Формат: change <ім'я> name <нове_ім'я>."
        return record.change_name(book, params[0])

    if subcommand == "phone":
        if len(params) < 2:
            return "Формат: change <ім'я> phone <старий_номер> <новий_номер>."
        old_phone, new_phone = params[0], params[1]
        owner = book.find_record_by_phone(new_phone)
        if owner and owner.name.value != record.name.value:
            return f"Номер {new_phone} вже використовується контактом '{owner.name.value}'."
        return record.edit_phone(old_phone, new_phone)

    if subcommand == "email":
        if len(params) < 2:
            return "Формат: change <ім'я> email <старий_email> <новий_email>."
        old_email, new_email = params[0], params[1]
        owner = book.find_record_by_email(new_email)
        if owner and owner.name.value != record.name.value:
            return f"Email {new_email} вже використовується контактом '{owner.name.value}'."
        return record.edit_email(old_email, new_email)

    if subcommand == "address":
        if not params:
            return "Будь ласка, введіть нову адресу."
        return record.change_address(" ".join(params))

    if subcommand == "birthday":
        if not params:
            return "Формат: change <ім'я> birthday <DD.MM.YYYY>."
        return record.change_birthday(params[0])

    else:
        return "Невідома підкоманда. Доступні: name, phone, address, birthday, email."

@input_error
def show_phone(args, book):
    if len(args) < 1:
        return "Помилка: команда 'phone' очікує 1 аргумент: phone <номер>."
    phone = args[0]
    record = book.find_record_by_phone(phone)
    if not record:
        return f"Контакт з номером {phone} не знайдено."
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
    owner = book.find_record_by_email(email)
    if owner and owner.name.value != record.name.value:
        return f"Email {email} вже використовується контактом '{owner.name.value}'."
    return record.add_email(email)


@input_error
def delete_contact(args, book):
    if len(args) < 1:
        return "Помилка: команда 'delete' очікує 1 аргумент: delete <ім'я>."
    name = args[0]
    return book.delete(name)


@input_error
def find_by_email(args, book):
    if len(args) < 1:
        return "Помилка: команда 'email' очікує 1 аргумент: email <адреса>."
    email = args[0]
    record = book.find_record_by_email(email)
    if not record:
        return f"Контакт з email {email} не знайдено."
    return f'Контакт знайдено {record}.'


@input_error
def find_by_name(args, book):
    if len(args) < 1:
        return "Помилка: команда 'name' очікує 1 аргумент: name <ім'я>."
    name = args[0]
    record = book.find(name)
    if not record:
        return f"Контакт з ім'ям {name} не знайдено."
    return f'Контакт знайдено {record}.'

@input_error
def birthdays(book):
    upcoming = book.get_upcomming_birthdays()
    if not upcoming:
        return "На цьому тижні немає днів народження."
    return "\n".join(f"{b['name']} → {b['birthday']}" for b in upcoming)
