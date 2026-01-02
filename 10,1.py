from typing import Generator, Callable, Union

Number = Union[int, float]


def sequence_generator(start: Number, n: int, func: Callable[[Number], Number]) -> Generator[Number, None, None]:
    """
    Генерує n членів числової послідовності.

    :param start: Початкове значення.
    :param n: Кількість членів послідовності.
    :param func: Функція, що приймає поточне значення і повертає наступне.
    """
    current_value = start
    for _ in range(n):
        yield current_value
        current_value = func(current_value)



if __name__ == "__main__":

    print("Арифметична прогресія (start=0, n=5, step=+2):")
    gen_arithmetic = sequence_generator(start=0, n=5, func=lambda x: x + 2)
    print(list(gen_arithmetic))

    print("-" * 20)

    print("Геометрична прогресія (start=1, n=4, factor=*3):")
    gen_geometric = sequence_generator(start=1, n=4, func=lambda x: x * 3)
    for num in gen_geometric:
        print(num)

    print("-" * 20)

    print("Ступенева послідовність (start=2, n=4, rule=x^2):")
    gen_power = sequence_generator(start=2, n=4, func=lambda x: x ** 2)
    print(list(gen_power))