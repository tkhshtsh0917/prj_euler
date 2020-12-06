from typing import Generator


def generate_fibonacci(max_num: int) -> Generator:
    """
    1 ~ max_numまでの間のfibonacci数を昇順で返却する。

    Args:
        max_num (int): 上限値

    Yields:
        Generator: fibonacci数
    """

    last = 1
    result = 1

    while result < max_num:
        yield result

        result, last = result+last, result


if __name__ == "__main__":
    max_num: int = 4_000_000
    answer: int = sum(f for f in generate_fibonacci(max_num) if f%2 == 0)

    print(answer)
