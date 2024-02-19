## 함수 선언 부분 ##
def grow_rich() :
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = goldMaze[0][0]

    row_sum = memo[0][0]
    for i in range(1, ROW) :
        row_sum += goldMaze[0][i]
        memo[0][i] = row_sum

    col_sum = memo[0][0]
    for i in range(1, COL) :
        col_sum += goldMaze[i][0]
        memo[i][0] = col_sum
    # ------------------------------------------------------

    for row in range(1, ROW) :
        for col in range(1, COL):
            if memo[row][col-1] < memo[row-1][col]:
                memo[row][col] = memo[row][col-1] + goldMaze[row][col]
            else:
                memo[row][col] = memo[row-1][col] + goldMaze[row][col]

    return memo[ROW-1][COL-1]

## 전역 변수 선언 부분 ##
ROW, COL = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
          [1, 3, 3, 0, 5],
          [1, 2, 4, 3, 0],
          [3, 3, 0, 4, 2],
          [1, 3, 4, 5, 3]]

## 메인 코드 부분 ##
macolGold = grow_rich()
print('황금 미로에서 얻은 최대 황금 개수 -->', macolGold)
