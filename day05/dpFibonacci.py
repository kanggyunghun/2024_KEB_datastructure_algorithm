memo = [0 if i == 0 else 1 if i ==1 else None for i in range(100)]
# memo = [0, 1] + [None] * (100-1)

def fibo_repetition(number: int) -> int:
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    global count

    a = 0
    b = 1
    for _ in range(number):
        count += 1
        a, b = b, a + b
    return a


def fibo_memoization(number: int, memo: list) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global count

    if memo[number] is not None:
        return memo[number]


    result = fibo_memoization(number-1, memo) + fibo_memoization(number-2, memo)
    count += 1
    memo[number] = result

    return result

if __name__ == "__main__":
    count = 0
    n = int(input("Input number : "))

    for i in range(0, n):
        # print(i)
        print(fibo_memoization(i, memo))
    print(count)

    count = 0
    n = int(input("Input number : "))
    print(fibo_repetition(n))
    print(count)