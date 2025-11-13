from datetime import date, timedelta
from .decorator import input_error


def _days_word(n: int) -> str:
    """
    Повертає правильну форму слова 'день' для вказаної кількості:
    1 день, 2–4 дні, 5+ днів (з урахуванням 11–19).
    """
    n = abs(n)
    last_two = n % 100
    last = n % 10

    if 11 <= last_two <= 19:
        return "днів"
    if last == 1:
        return "день"
    if 2 <= last <= 4:
        return "дні"
    return "днів"


@input_error
def birthdays_in(args, book):
    """
    Команда: birthdays-in <кількість_днів>

    Повертає список контактів, у яких день народження
    через задану кількість днів від сьогодні.
    """
    if len(args) != 1:
        return (
            "Помилка: команда 'birthdays-in' очікує рівно 1 аргумент:\n"
            "birthdays-in <кількість_днів>"
        )

    days_str = args[0]

    # Перевірка, що аргумент — ціле число
    try:
        days = int(days_str)
    except ValueError:
        return "Помилка: кількість днів має бути цілим числом."

    if days < 0:
        return "Помилка: кількість днів не може бути від'ємною."

    today = date.today()
    target_date = today + timedelta(days=days)

    matches = []

    # book — це AddressBook (UserDict), як і в інших командах
    for record in book.data.values():
        birthday_field = getattr(record, "birthday", None)
        if not birthday_field:
            continue

        # Дата народження (без року)
        bday = birthday_field.value  # datetime.date

        # Наступний день народження для цього контакту
        next_bday = bday.replace(year=today.year)
        if next_bday < today:
            next_bday = next_bday.replace(year=today.year + 1)

        if next_bday == target_date:
            matches.append(f"{record.name.value} → {next_bday.strftime('%d.%m.%Y')}")

    if not matches:
        return (
            f"Немає контактів з днем народження через {days} {_days_word(days)}."
        )

    return "\n".join(matches)
