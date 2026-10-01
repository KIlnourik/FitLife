# Проект FitLife - MVP версия 1.0

WATER_PER_KILO = 30
MILLILITERS_IN_LITER = 1000
EXPONENT = 2
MAX_AGE = 150
MAX_HEIGHT_IN_METERS = 3
MAX_WEIGHT = 200


# Функция, по получению возраста пользователя
def get_user_age() -> int|None:
    raw_user_age = input("Каков твой возраст?")

    try:
        age = int(raw_user_age)
        if age <= 0:
            print("0 и менее лет?")
            raise ValueError
        elif age >= MAX_AGE:
            print("Ты из клана Дункан Маклауд из клана Маклаудов? 0_o")
            raise ValueError
        else:
            return age

    except ValueError:
        print("Перепроверь правильность введенного числа. Должно быть целое число.")


# Функция, по получению роста пользователя
def get_user_height() -> float|None:
    raw_user_data = input(f"Какой у тебя рост в МЕТРАХ? (дробные данные разделяй точкой, а не запятой)")

    try:
        height = float(raw_user_data)
        if height <= 0:
            print("Ты что МИКРОБ? 0_о")
            raise ValueError
        elif height >= MAX_HEIGHT_IN_METERS:
            print("Выше 2 метров?")
            raise ValueError
        else:
            return height

    except ValueError:
        print("Перепроверь правильность введенного числа")


# Функция, по получению веса пользователя
def get_user_weight() -> float|None:
    raw_user_weight = input(f"Сколько ты весишь в КИЛОГРАММАХ? (дробные данные разделяй точкой, а не запятой)")

    try:
        weight = float(raw_user_weight)
        if weight <= 0:
            print("Совсем ничего не весишь?")
            raise ValueError
        elif weight >= MAX_WEIGHT:
            print("Больше ДВУХСОТ КИЛО?")
            raise ValueError
        else:
            return weight

    except ValueError:
        print("Перепроверь правильность введенного числа")


# 1. Знакомство
# Запрашиваем имя
user_name = input("Как твое имя?")
# Запрашиваем возраст, пробуем перевести в int, перезапрашиваем данные пока не получим валидные
user_age = get_user_age()
while user_age is None:
    user_age = get_user_age()
    if user_age:
        break

# 2. Сбор данных
# Запрашиваем вес и пробуем перевести во float, перезапрашиваем данные пока не получим валидные
user_weight = get_user_weight()
while user_weight is None:
    user_weight = get_user_weight()
    if user_weight:
        break

# Запрашиваем рост и пробуем перевести во float, перезапрашиваем данные пока не получим валидные
user_height = get_user_height()
while user_height is None:
    user_height = get_user_height()
    if user_height:
        break

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# Считаем ИМТ
bmi = round(user_weight / (user_height ** EXPONENT), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water = (user_weight * WATER_PER_KILO) / MILLILITERS_IN_LITER

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
print(f"Привет, {user_name}!")
print("Создал тут отчет для тебя. Давай посмотрим?")

# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Твои данные: тебе - {user_age} лет, рост - {user_height} метров, вес - {user_weight} кг")
print(f"Твой Индекс Массы Тела (ИМТ): {bmi}")
print(f"Рекомендуемая норма воды: {water} л. в день")
print("Расчет окончен. Будьте здоровы!")