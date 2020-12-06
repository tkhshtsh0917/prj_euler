from typing import Generator, List


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


if __name__ == "__main__":
    num: int = 20
    answer: int = 1

    for prime in prime_generator(num):
        i = 1
        while prime**i <= num:
            answer *= prime
            i += 1

    print(answer)
