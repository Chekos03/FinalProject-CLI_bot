from commands import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from commands import add_note, show_notes,find_note,edit_note,delete_note
from commands import parse_input
from commands import save_data,load_data
from commands import NoteBook


    

def main():
    book, note = load_data()
    print("Welcome to the assistant bot!")

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
