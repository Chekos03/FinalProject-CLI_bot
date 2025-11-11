from .decorator import input_error
from .note_book import Note


from .decorator import input_error
from .note_book import Note


@input_error
def add_note(args, notes):
    if len(args) < 2:
        return "Помилка: команда 'add-note' очікує 2 аргументи: add-note <Назва> <нотатка>"
    title = args[0]
    text = " ".join(args[1:]) 
    note = Note(title, text)
    return notes.add(note)


@input_error
def find_note(args, notes):
    if len(args) < 1:
        return "Помилка: команда 'find-note' очікує 1 аргумент: find-note <ключове слово>"
    query = args[0]
    results = notes.find(query)
    return "\n\n".join(str(r) for r in results) if results else "Нотаток не знайдено."


@input_error
def edit_note(args, notes):
    if len(args) < 2:
        return "Помилка: команда 'edit-note' очікує 2 аргументи: edit-note <Назва> <новий текст>"
    title = args[0]
    new_text = " ".join(args[1:])
    return notes.edit(title, new_text)


@input_error
def delete_note(args, notes):
    if len(args) < 1:
        return "Помилка: команда 'delete-note' очікує 1 аргумент: delete-note <Назва>"
    title = args[0]
    return notes.delete(title)


@input_error
def show_notes(notes):
    if not notes.data:
        return "Немає збережених нотаток."
    return "\n\n".join(str(n) for n in notes.data.values())
