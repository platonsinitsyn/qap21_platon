import random

import pytest

# 2.Написать модульное автотестирование с учетом граничных значений и классов эквивалентности 5 тестов
# Для тестирования создать фикстуру которая подготовит тестовые данные для функции -
# [(случайные данные от 20-120, случайные данные от 20-220),
# (случайные данные от 20-120, случайные данные от 20-220),
# (случайные данные от 20-120, случайные данные от 20-220),
# (случайные данные от 20-120, случайные данные от 20-220),
# (случайные данные от 20-120, случайные данные от 20-220)]
# + параметризация


@pytest.fixture(scope="module")
def random_bmi_data():
    pairs = [(random.randint(20, 120), random.randint(20, 220)) for _ in range(5)]  # 5 случайных пар (в+р)
    return pairs


def imt(w, h):
    try:
        if w <= 0 or h <= 0:
            raise ValueError("Значения должны быть положительными")
        h = h / 100
        index = w / (h**2)

        if index < 16:
            return "выраженный дефицит"
        elif 16 <= index < 18.5:
            return "дефицит"
        elif 18.5 <= index < 25:
            return "норма"
        elif 25 <= index < 30:
            return "избыточность"
        elif 30 <= index < 35:
            return "1 степени"
        elif 35 <= index < 40:
            return "2 степени"
        elif index >= 40:
            return "3 степени"

    except ValueError:
        return "Error"


@pytest.mark.parametrize("index", range(5))
def test_imt_random(random_bmi_data, index):
    w, h = random_bmi_data[index]
    result = imt(w, h)
    assert result in [
        "выраженный дефицит",
        "дефицит",
        "норма",
        "избыточность",
        "1 степени",
        "2 степени",
        "3 степени",
        "Error",
    ]
    print(f"Результат пары: {index} [вес: {w}, рост: {h}] - {result})")
