from collections import UserDict
from datetime import datetime



class Note:
    
    def __init__(self, title, text, tags=None): 
        self.title = title
        self.text = text
        self.created_at = datetime.now()
        # КРИТИЧНО ВАЖЛИВА ЗМІНА: Ініціалізуємо теги як множину
        self.tags = set(tag.lower() for tag in tags) if tags else set() 

    #  КРИТИЧНО ВАЖЛИВА ЗМІНА: Додаємо метод для додавання тегів
    def add_tags(self, new_tags):
        """Додає один або кілька тегів до нотатки."""
        for tag in new_tags:
            self.tags.add(tag.lower())

    # Змінюємо __str__ для відображення тегів
    def __str__(self):
        tags_display = f"Теги: #{' #'.join(self.tags)}" if self.tags else "Теги: немає"
        return (
            f"{self.title}\n"
            f"{self.text}\n"
            f"Створено: {self.created_at.strftime('%d.%m.%Y %H:%M')}\n"
            f"{tags_display}" # Додаємо відображення тегів
        )

class NoteBook(UserDict):
    def add(self, note : Note):
        self.data[note.title.lower()] = note
        return f"Нотатку '{note.title}' додано."
    
    def edit(self,title,new_text):
        note = self.data.get(title.lower())
        if not note:
            return f"Нотатку '{title}' не знайдено."
        note.text = new_text
        return f"Нотатку '{title}' оновлено."
    
    def add_tags(self, title, tags):
        """Знаходить нотатку за назвою та додає до неї теги."""
        note = self.data.get(title)
        if note:
            note.add_tags(tags)
            return f"До нотатки '{title}' додано теги: {', '.join(tags)}"
        return f"Помилка: Нотатка з назвою '{title}' не знайдена."


    def find_by_tags(self, tags_query):
        """Шукає нотатки за ключовими словами (тегами)."""
        # Перетворюємо рядок запиту в множину тегів для пошуку
        search_tags = {tag.strip().lower() for tag in tags_query.replace(',', ' ').split()}
        
        found_notes = []
        for note in self.data.values():
            # Використовуємо .intersection() для пошуку спільних елементів
            if note.tags.intersection(search_tags):
                found_notes.append(note)
                
        return found_notes

    def sort_by_tags(self):
        """Сортує нотатки, використовуючи перший тег в алфавітному порядку як ключ сортування."""
        
        def sort_key(note):
            # Якщо теги є, повертаємо перший тег у алфавітному порядку
            if note.tags:
                return sorted(list(note.tags))[0] 
            # Якщо тегів немає, повертаємо великий рядок, щоб вони йшли в кінці
            else:
                return 'zzzzz' 

        # Сортуємо список об'єктів Note і повертаємо його
        sorted_notes = sorted(self.data.values(), key=sort_key)
        return sorted_notes

    def find(self, query: str):
        results = [
            i for i in self.data.values()
            if query.lower() in i.title.lower()
        ]
        return results
    
    def delete(self,title):
        if title.lower() in self.data:
            del self.data[title.lower()]
            return f"Нотатка {title} видалено."
        return f"{title} не знайдено."



