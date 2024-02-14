# 8진수로 변환하는 재귀함수

def decimal_to_octal(number: int) -> int:
    """
    decimal_to_octal number (by recursion)
    :param number:integer (base dec)
    :return: string (base octal)
    """
    if number < 8:
        return str(number)
    else:
        return decimal_to_octal(number//8) + str(number % 8)


n = int(input("Input decimal number: "))
print(decimal_to_octal(n))
