from typing import List


def is_palindromic(num: int) -> bool:
    """
    引数で受け取った整数値が回文になっているかを判定する。

    Args:
        num (int): 対象の整数値

    Returns:
        bool: 判定結果
    """

    num_str: str = str(num)
    reverse_num: int = 0

    for s in range(len(num_str)-1, -1, -1):
        reverse_num *= 10
        reverse_num += int(num_str[s])

    return num == reverse_num


if __name__ == "__main__":
    palindromic_numbers: List = list(
        i*j for i in range(999, 99, -1) for j in range(i, 99, -1) if is_palindromic(i*j)

    )
    print(max(palindromic_numbers))
