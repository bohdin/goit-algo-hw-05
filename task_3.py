import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    components = dict()
    data, time, level, message = line.split(maxsplit=3)

    # Зберігаємо компоненти логу у словнику
    components['data'] = data
    components['time'] = time
    components['level'] = level
    components['message'] = message.strip() # Позбавляємося від \n

    return components
        

def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Проходимося по кожному рядку логу та розбираємо його за допомогою функції parse_log_line
            for line in lines:
                logs.append(parse_log_line(line))
    
    # Обробка помилок, які можуть виникнути під час читання файлу
    except FileNotFoundError as f:
        print(f"Файл {file_path} не знайдено")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    
    return logs
    
    
def filter_logs_by_level(logs: list, level: str) -> list:
     # Фільтрує логи за рівнем логування та повертає список відфільтрованих логів.
    return list(filter(lambda x: x['level'] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    # Обчислює кількість логів для кожного рівня логування та повертає словник.
    count_logs = defaultdict(int)
    for log in logs:
        count_logs[log['level']] += 1
    return dict(count_logs)

def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-'*17 + '|' + '-'*10)
    for k, v in counts.items():
        print(f"{k:<17}| {v:<10}")
    



if __name__ == "__main__":
    # Завантажуємо логи та обчислюємо кількість логів за кожним рівнем логування
    log = load_logs(sys.argv[1])
    count = count_logs_by_level(log)

    # Виводимо кількість логів за кожним рівнем логування
    display_log_counts(count)
    
    # Якщо вказано другий аргумент командного рядка
    if len(sys.argv) > 2:
        
        requested_level = sys.argv[2].upper()
        print(f"Деталі логів для рівня '{requested_level}':")
        
        for i in filter_logs_by_level(log, sys.argv[2]):
            # Виводимо інформацію про кожний лог
            print(" ".join(f"{v}" if v != requested_level else '-' for v in i.values()))

