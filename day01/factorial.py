import mymath as mm

if __name__ == '__main__': # 매직매서드
    n = int(input("Input n: "))
    r = int(input("Input r: "))
    print(f'{n}C{r} = {mm.nCr(n,r)}')
    # f = int(input())
    # print(factorial(f))