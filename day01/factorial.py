import mymath as mm
import time


if __name__ == '__main__': # 매직매서드
    n = int(input("Input n: "))
    r = int(input("Input r: "))
    # start = time.time()
    print(f'{n}C{r} = {mm.nCr(n,r)}')
    end = time.time()
    # print(f'소요시간: {end - start}')
    # f = int(input())
    # print(factorial(f))