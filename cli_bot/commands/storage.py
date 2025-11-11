import pickle
import os
from .address_book import AddressBook


DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_CONTACT_FILE = os.path.join(DATA_DIR, "addressbook.pkl")


def save_data(book, filename=DATA_CONTACT_FILE):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print(f"[INFO] Дані збережено у файлі: {filename}")


def load_data(filename=DATA_CONTACT_FILE):
    if not os.path.exists(filename):
        print("[INFO] Файл не знайдено, створено нову адресну книгу.")
        return AddressBook()
    with open(filename, "rb") as f:
        book = pickle.load(f)
    print(f"[INFO] Дані завантажено з файлу: {filename}")
    return book