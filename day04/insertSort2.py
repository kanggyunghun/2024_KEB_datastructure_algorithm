## 함수 선언 부분 ##
def insertion_sort(ary) :
    n = len(ary)
    for end in range(1, n) :
        for cur in range(end, 0, -1) :
            if ( ary[cur-1] > ary[cur] ) :
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
    return ary

## 전역 변수 선언 부분 ##
data_ary = [188, 162, 168, 120, 50, 150, 177, 105]

## 메인 코드 부분 ##
print('정렬 전 -->', data_ary)
data_ary = insertion_sort(data_ary)
print('정렬 후 -->', data_ary)
