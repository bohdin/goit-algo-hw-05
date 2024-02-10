import re
import decimal


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    matches = re.findall(pattern, text)
    for match in matches:
        yield decimal.Decimal(match)

def sum_profit(text: str, func: callable):
    sum = 0
    for number in func(text):
        sum += number
    return sum



text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")