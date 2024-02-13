def caching_fibonacci(num):
    #Створюємо пустий словник для кешу
    cache = dict()

    def fibonacci(n):
        # Базовий випадок для 0 і 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Перевіряємо, чи вже маємо обчислений результат для n
        elif n in cache.keys():
            return cache[n]
        else:
            # Рекурсивно обчислюємо результат та зберігаємо його в кеші
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
    # Викликаємо внутрішню функцію для обчислення числа Фібоначчі
    return fibonacci(num)

# Отримуємо функцію fibonacci
fib = caching_fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
