from commands import (
    add_contact, change_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays,
    add_note, show_notes, find_note, edit_note, delete_note,
    parse_input, save_data, load_data, NoteBook, help_text
)
from difflib import get_close_matches

ERROR_MSG = "Команда не існує. Введіть 'help' для ознайомлення."

COMMANDS = (
    "hello",
    "add",
    "change",
    "phone",
    "all",
    "add-birthday",
    "show-birthday",
    "birthdays",
    "add-note",
    "find-note",
    "edit-note",
    "delete-note",
    "show-notes",
    "help",
    "close",
    "exit",
)


def suggest_command(user_cmd: str):
    """Повертає найбільш схожу команду або None."""
    matches = get_close_matches(user_cmd, COMMANDS, n=1, cutoff=0.6)
    return matches[0] if matches else None

def execute_command(command: str, args: list[str], book, notes):
    """Виконує команду і повертає текст для виводу, або None, якщо команда невідома."""
    if command == "hello":
        return "How can I help you?"
    elif command == "add":
        return add_contact(args, book)
    elif command == "change":
        return change_contact(args, book)
    elif command == "phone":
        return show_phone(args, book)
    elif command == "all":
        return show_all(book)
    elif command == "add-birthday":
        return add_birthday(args, book)
    elif command == "show-birthday":
        return show_birthday(args, book)
    elif command == "birthdays":
        return birthdays(book)
    elif command == "add-note":
        return add_note(args, notes)
    elif command == "find-note":
        return find_note(args, notes)
    elif command == "edit-note":
        return edit_note(args, notes)
    elif command == "delete-note":
        return delete_note(args, notes)
    elif command == "show-notes":
        return show_notes(notes)
    elif command == "help":
        return help_text()
    else:
        return None

def main():
    book = load_data()
    notes = NoteBook()
    print("Ласкаво просимо до асистента!")

    try:
        while True:
            user_input = input("Введіть команду: ")
            command, args = parse_input(user_input)

            if not command:
                continue

            # завершення роботи
            if command in ("close", "exit"):
                print("До побачення!")
                save_data(book)
                break

            # спроба виконати введену команду
            result = execute_command(command, args, book, notes)

            if result is not None:
                print(result)
                continue

            # якщо команда невірна – пробуємо підказати
            suggestion = suggest_command(command)
            if suggestion:
                answer = input(f"Ви мали на увазі '{suggestion}'? (y/n): ").strip().lower()
                if answer in ("y", "yes", "т", "так"):
                    result = execute_command(suggestion, args, book, notes)
                    if result is not None:
                        print(result)
                else:
                    print(ERROR_MSG)
            else:
                print(ERROR_MSG)
    except KeyboardInterrupt:
        save_data(book)
        


if __name__ == "__main__":
    main()
