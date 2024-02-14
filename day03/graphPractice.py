# graph = [
#     [0, 0, 1, 1, 0],
#     [0, 0, 1, 0, 0],
#     [1, 1, 0, 1, 1],
#     [1, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0]
# ]
'''
nameAry = ["문별","솔라","휘인","쯔위","선미","화사"]
mb, sl, hi, zz, sm, hs = 0,1,2,3,4,5
'''

graph = [
    [0, 1, 1, 0, 0, 0], #문별
    [1, 0, 0, 1, 0, 0], #솔라
    [1, 0, 0, 1, 0, 0], #휘인
    [0, 1, 1, 0, 1, 0], #쯔위
    [0, 0, 0, 1, 0, 0], #선미
    [0, 0, 0, 0, 0, 0], #화사 고립시키기

]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)


visited = [0] * len(graph)
dfs(graph, 0, visited)