def test(n):
    if n > 0:
        test(n-1)
        print(n*n)

"""
def test(3):
    if n > 0:
        test(n-1) 스택에 호출. 위치가 저장
        print(n*n)
"""

"""
def test(2):
    if n > 0:
        test(n-1)
        print(n*n)
"""

"""
def test(1):
    if n > 0:
        test(n-1)
        print(n*n)
"""

"""
def test(0):
    if n > 0:
        test(n-1)
        print(n*n)
"""
test(3)