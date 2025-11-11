from collections import UserDict
from datetime import datetime,time



class Note:
    def __init__(self,title, text):
        self.title = title
        self.text = text
        self.created_at = datetime.now()

    def __str__(self):
        return (
            f"{self.title}\n"
            f"{self.text}\n"
            f"Створено: {self.created_at.strftime('%d.%m.%Y %H:%M')}"
        )
    

class NoteBook(UserDict):
    def add(self, note : Note):
        self.data[note.title.lower()] = note
        return f"Нотатку '{note.title}' додано "
    
    def edit(self,title,new_text):
        note = self.data.get(title.lower())
        if not note:
            return f"Нотатку '{title}' не знайдено"
        note.text = new_text
        return f"Нотатку '{title}' оновлено"
    
    def find(self, query: str):
        results = [
            i for i in self.data.values()
            if query.lower() in i.title.lower()
        ]
        return results
    
    def delete(self,title):
        if title.lower() in self.data:
            del self.data[title.lower()]
            return f"Нотатка {title} видалено"
        return f"{title} не знайдено"



