def get_plural_noun(value: int | float) -> str:
    """
    Функция получения корректных форм возраста (лет, год, года)
    в зависимости от переданного значения
    :param value:
    :rtype: str
    """
    dec = value % 10

    if dec == 1:
        return 'год'
    elif 2 <= dec <= 4:
        return 'года'
    else:
        return 'лет'


def get_imt_interpretation(value: float) -> str | None:
    """
    Функция получения интепретации результатов
    расчета ИМТ
    :param value:
    :rtype: str
    """
    imt_interpretation = {
        (float('-inf'), 16): "выраженный дефицит массы тела",
        (16, 18.5): "недостаточная (дефицит) масса тела",
        (25, 30): "избыточная масса тела (предожирение)",
        (30, 35): "ожирение 1 степени",
        (35, 40): "ожирение 2 степени",
        (40, float('inf')): "ожирение 3 степени"
    }

    for (min_value, max_value), description in imt_interpretation.items():
        if min_value <= value < max_value:
            return description

    print("Ошибка данных")
