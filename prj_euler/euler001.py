def euler001(max_num: int) -> int:
    """
    1 ~ max_numの連続値のうち、3または5で割り切れる数を合算した値を返却する。

    Args:
        max_num (int): 評価対象範囲とする最大の値

    Returns:
        int: 条件を満たす値の合算値
    """

    return sum(i for i in range(1, max_num+1) if i%3 == 0 or i%5 == 0)


if __name__ == "__main__":
    max_num: int = 1_000
    print(euler001(max_num))
