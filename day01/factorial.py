def factorial(n) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def nCr(n, r) -> int:
    """
    조합 함수
    :param n:
    :param r:
    :return:
    """
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)

    return numerator / denominator

if __name__ == '__main__': # 매직매서드
    n = int(input("Input n: "))
    r = int(int("Input r: "))
    print(f'{n}C{r} = {nCr(n,r)}')