import re
import decimal


def generator_numbers(text: str):
    # Задаємо регулярний вираз для пошуку чисел
    pattern = r"\b\d+\.\d+\b"
    # Знаходимо всі збіги
    matches = re.findall(pattern, text)
    # Проходимося по знайденим числам
    for match in matches:
        # Конвертуємо знайдене число у формат Decimal і повертаємо його як генератор
        yield decimal.Decimal(match)

def sum_profit(text: str, func: callable):
    sum = 0
    # Проходимося по кожному числу, яке повертає функція-генератор
    for number in func(text):
        sum += number
    return sum



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")