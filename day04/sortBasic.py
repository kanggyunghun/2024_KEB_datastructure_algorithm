## 함수 선언 부분 ##
def selection_sort(ary) :
    n = len(ary)
    for i in range(0, n-1) : # 맨 마지막은 볼 필요 없기 때문에 n - 1
        minIdx = i
        for k in range(i+1, n) :
            if (ary[minIdx] > ary[k]) :
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

## 전역 변수 선언 부분 ##
data_ary = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', data_ary)
data_ary = selection_sort(data_ary)
print('정렬 후 -->', data_ary)
