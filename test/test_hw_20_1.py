import pytest

# 1. Программа получает на вход число. Реализовать
# функцию, которая определяет, является ли это число простым
# (делится только на единицу и на само себя).
# Написать модульное автотестирование с учетом граничных значений и классов эквивалентности 5 тестов


def is_prime(n):
    """Проверяем, является ли число простым"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Проверяем делители от 3 до корня из n
    for i in range(3, int(n**0.5) + 1, 2):  # - начинается с 3 и заканчивается корнем из n
        if n % i == 0:  # n % i == 0 проверяет, делится ли n на i без остатка
            return False  # Если нашли делитель - число не простое
    return True  # Если не нашли делитель - число простое


@pytest.mark.parametrize("n", [-3, 0, 1])
def test_not_prime_for_n_le_1(n):
    assert not is_prime(n)


def test_two_is_prime():
    # n = 2 → True
    assert is_prime(2)


@pytest.mark.parametrize("n", [4, 10])
def test_even_gt_two_is_not_prime(n):
    # ожидаю False
    assert not is_prime(n)


@pytest.mark.parametrize("n", [3, 5, 11])
def test_odd_primes_are_prime(n):
    # ожидаю True
    assert is_prime(n)


@pytest.mark.parametrize("n", [9, 15, 21])
def test_odd_composites_are_not_prime(n):
    # ожидаю False
    assert not is_prime(n)
