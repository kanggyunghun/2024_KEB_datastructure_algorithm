## 함수 선언 부분 ##
def quick_sort(ary):
    n = len(ary)
    if n <= 1:  # 정렬할 리스트의 개수가 1개 이하면
        return ary

    pivot = ary[n // 2]  # 기준값을 중간값으로 지정
    print(pivot)
    left_ary, right_ary = [], []

    for num in ary:
        if num < pivot:
            left_ary.append(num)
        elif num > pivot:
            right_ary.append(num)

    return quick_sort(left_ary) + [pivot] + quick_sort(right_ary)


## 전역 변수 선언 부분 ##
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

## 메인 코드 부분 ##
print('정렬 전 -->', dataAry)
dataAry = quick_sort(dataAry)
print('정렬 후 -->', dataAry)
