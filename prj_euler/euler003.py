import math
from typing import Generator, List, Set


def prime_generator(num: int) -> Generator:
    """
    2 ~ numまでの範囲の素数を昇順で返却する。
    素数の生成には、Sieve of Eratosthenesアルゴリズムを使用する。

    Args:
        num (int): 素数列挙の上限値

    Yields:
        Generator: 素数
    """

    numbers: List = list(i for i in range(2, num+1))

    while len(numbers) > 0:
        prime = numbers[0]
        yield prime

        numbers = list(n for n in numbers if n%prime != 0)


def generate_prime_factor(num: int) -> Generator:
    """
    numの素因数を昇順で返却する。

    Args:
        num (int): 素因数分解の対象値

    Yields:
        Generator: 素因数
    """

    generator: Generator = prime_generator(math.ceil(math.sqrt(num)))

    for prime in generator:
        if prime**2 > num:
            break

        while num%prime == 0:
            num /= prime
            yield prime

    if num != 1:
        yield int(num)


if __name__ == "__main__":
    num: int = 600_851_475_143
    answer: Set = set(p for p in generate_prime_factor(num))

    print(max(answer))
