from commands import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from commands import add_note, show_notes,find_note,edit_note,delete_note
from commands import parse_input
from commands import save_data,load_data
from commands import NoteBook


    

def main():
    book = load_data()
    note = NoteBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ("close", "exit"):
            save_data(book)
            print("Data saved.Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args,book))
        elif command =="show-birthday":
            print(show_birthday(args,book))
        elif command =="birthdays":
            print(birthdays(book))
        elif command == "add-note":
            print(add_note(args, note))
        elif command == "find-note":
            print(find_note(args, note))
        elif command == "edit-note":
            print(edit_note(args, note))
        elif command == "delete-note":
            print(delete_note(args, note))
        elif command == "show-notes":
            print(show_notes(note))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
