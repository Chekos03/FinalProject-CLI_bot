HELP_TEXT = """\
Команди:
  hello
      Результат: How can I help you?

  add <name> <phone>
      Приклад: add John 1234567890
      Результат: Контакт було додано/оновлено.

  change <name> name|phone|address|birthday|email [old] <new>
      Приклади:
          change John name Johnny
          change John phone 1234567890 0987654321
          change John address Kyiv Lesi Ukrainky 12
          change John birthday 01.01.1990
          change John email old@example.com new@example.com
      Результат: Оновлення вибраного поля контакту (для phone/email потрібно вказати старе значення).

  phone <phone>
      Приклад: phone 1234567890
      Результат: Показує контакт, який містить цей номер телефону.

  all
      Результат: Усі контакти у форматі: <name>: <phones>, birthday: <DD.MM.YYYY|-> 
                 Або: Адресна книга порожня.

  add-birthday <name> <DD.MM.YYYY>
      Приклад: add-birthday John 17.08.1980
      Результат: День народження було додано/оновлено.

  add-address <name> <address>
      Приклад: add-address John Kyiv, Lesi Ukrainky 12
      Результат: Адресу додано. 

  add-email <name> <email>
      Приклад: add-email John john@example.com
      Результат: Email додано.

  email <email>
      Приклад: email john@example.com
      Результат: Показує контакт, що відповідає email

  delete <name>
      Приклад: delete John
      Результат: Видаляє контакт з адресної книги.

  show-birthday <name>
      Приклад: show-birthday John
      Результат: <DD.MM.YYYY> Або: День народження не збережено.

  birthdays
      Результат: Список привітань на наступні 7 днів (дні народження у вихідні перенесено на понеділок),
                 Або: Немає днів народження впродовж наступних 7 днів.

  add-note <title> <text>
      Приклад: add-note Shopping Buy milk and bread
      Результат: Нотатку додано.

  find-note <title>
      Приклад: find-note Shopping
      Результат: Текст нотатки Або: Нотатку не знайдено.

  edit-note <title> <new_text>
      Приклад: edit-note Shopping Buy milk, bread and cheese
      Результат: Нотатку оновлено.

  delete-note <title>
      Приклад: delete-note Shopping
      Результат: Нотатку видалено.

  show-notes
      Результат: Усі збережені нотатки Або: Жодної нотатки не збережено.

  help
      Показати цей текст.

  close | exit
      Результат: Goodbye! та завершення роботи.
"""


def help_text():
    return HELP_TEXT
