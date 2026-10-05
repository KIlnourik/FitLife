# Проект FitLife - MVP версия 1.0
from helpers import get_imt_interpretation, get_plural_noun

WATER_PER_KILO = 30
MILLILITERS_IN_LITER = 1000
# Минимальные и максимальные значения
MIN_AGE = 18
MAX_AGE = 65
# Минимальный рост взрослого человека (взято по женщинам)
MIN_HEIGHT_IN_METERS = 1.2
# Максимальный рост человека в истории человека
MAX_HEIGHT_IN_METERS = 2.72
# Минимальный вес взрослого человека с ростом 1.2 м
MIN_WEIGHT = 26.6
# Максимальный вес взрослого человека в истории
MAX_WEIGHT = 635
# Вопросы пользователю, используемые в input
AGE_QUESTION = f"Каков твой возраст? (от {MIN_AGE} до {MAX_AGE})"
HEIGHT_QUESTION = "Какой у тебя рост в МЕТРАХ?"
WEIGHT_QUESTION = "Сколько ты весишь в КИЛОГРАММАХ?"


def get_user_data(
        raw_data: str,
        question: str,
        min_value: int | float,
        max_value: int | float,
        return_type: str
) -> int | float:
    """
    Функция получения данных пользователя
    :param raw_data: str - Первичные полученные данные от пользователя
    Добавлены для успешного прохождения тестов
    :param question: str - вопрос пользователю для получения данных
    :param min_value: int - минимальное значение
    :param max_value: int - максимальное значение
    :param return_type: str - возвращаемый тип данных - int или float
    :rtype: float | None
    """
    value = None

    while value is None:
        raw_data = input(question) if raw_data is None else raw_data

        try:
            if return_type == 'int':
                value = int(raw_data)
            else:
                raw_data = raw_data.replace(',', '.')
                value = float(raw_data)

            if value < min_value:
                print(f"Число не должно быть ниже {min_value}")
                value = None
                raise ValueError

            if value >= max_value:
                print(f"Число не должно превышать {max_value}")
                value = None
                raise ValueError

            return value

        except ValueError:
            print("Перепроверь правильность введенного числа")

        raw_data = None


def get_user_age(raw_data: str) -> int:
    """
    Функция  получения возраста пользователя
    :rtype: int
    """
    return get_user_data(
        raw_data,
        AGE_QUESTION,
        MIN_AGE,
        MAX_AGE,
        'int')


def get_user_height(raw_data: str) -> float:
    """
    Функция, по получению роста пользователя
    :rtype: float
    """
    return get_user_data(
        raw_data,
        HEIGHT_QUESTION,
        MIN_HEIGHT_IN_METERS,
        MAX_HEIGHT_IN_METERS,
        'float'
    )


def get_user_weight(raw_data: str) -> float:
    """
    Функция, по получению веса пользователя
    :rtype: float
    """
    return get_user_data(
        raw_data,
        WEIGHT_QUESTION,
        MIN_WEIGHT,
        MAX_WEIGHT,
        'float')


# Приветствие
print("Привет! Это консольный бот FitLife.")
print("Могу подсчитать твой индекс массы тела и норму воды в день.")
print("Для проведения расчетов нужные твои данные.")
# 1. Знакомство
# Запрашиваем имя
user_name = input("Как твое имя?")

# Запрашиваем возраст, пробуем перевести в int,
# перезапрашиваем данные пока не получим валидные
raw_age = input(AGE_QUESTION)
user_age = get_user_age(raw_age)
user_age_form = get_plural_noun(user_age)

# 2. Сбор данных
# Запрашиваем вес и пробуем перевести во float,
# перезапрашиваем данные пока не получим валидные
raw_weight = input(WEIGHT_QUESTION)
user_weight = get_user_weight(raw_weight)

# Запрашиваем рост и пробуем перевести во float,
# перезапрашиваем данные пока не получим валидные
raw_height = input(HEIGHT_QUESTION)
user_height = get_user_height(raw_height)

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# Считаем ИМТ
bmi = round(user_weight / (user_height ** 2), 1)
# Получаем интерпретацию данных ИМТ
interpretations = get_imt_interpretation(bmi)

# Подсчет воды: вес * WATER_PER_KILO мл
water = (user_weight * WATER_PER_KILO) / MILLILITERS_IN_LITER

# 4. Вывод красивого результата
print(f"{user_name}, я создал тут отчет для тебя. Смотри ниже")
print(f"""
Твои данные:
    тебе - {user_age} {user_age_form},
    рост - {user_height} метров,
    вес - {user_weight} кг
""")
print(f"Твой Индекс Массы Тела (ИМТ): {bmi}")
print(f"Согласно рассчитанному ИМТ у тебя {interpretations}")

print(f"Рекомендуемая норма воды: {water} л. в день")
print("Расчет окончен. Будь здоров!")
