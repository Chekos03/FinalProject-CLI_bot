import pickle
import os
from .address_book import AddressBook
from .note_book import NoteBook


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_CONTACT_FILE = os.path.join(DATA_DIR, "addressbook.pkl")
DATA_NOTE_FILE = os.path.join(DATA_DIR, "notes.pkl")


def save_data(book, notes, contact_filename=DATA_CONTACT_FILE, note_filename=DATA_NOTE_FILE):
    try:
        os.makedirs(os.path.dirname(contact_filename), exist_ok=True)
        with open(contact_filename, "wb") as f:
            pickle.dump(book, f)
        with open(note_filename, "wb") as f:
            pickle.dump(notes, f)
        print(f"[INFO] Дані збережено у файлах: {contact_filename}, {note_filename}")
    except Exception as e:
        print(f"[ERROR] Помилка збереження даних: {e}")


def load_data(contact_filename=DATA_CONTACT_FILE, note_filename=DATA_NOTE_FILE):
    try:
        if not os.path.exists(contact_filename):
            print("[INFO] Файл адресної книги не знайдено, створено нову.")
            book = AddressBook ()
        else:
            with open (contact_filename, "rb") as f:
                book = pickle.load(f)
        if not os.path.exists(note_filename):
            print("[INFO] Файл нотаток не знайдено, створено новий.")
            notes = NoteBook ()
        else:
            with open (note_filename, "rb") as f:
                notes = pickle.load(f)
        print(f"[INFO] Дані завантажено з файлів: {contact_filename}, {note_filename}")
        return book, notes
    except Exception as e:
        print (f"[ERROR] Помилка завантаження даних: {e}")
        return AddressBook(), NoteBook()