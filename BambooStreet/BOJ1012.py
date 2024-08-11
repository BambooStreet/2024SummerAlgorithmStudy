import sys
sys.setrecursionlimit(10000)

# 1. 배추흰지렁이는 인접한 다른 배추로 이동할 수 있어 상하좌우에 위치한 배추들은 서로 보호받을 수 있다.
# 2. 배추들이 몇 군데에 퍼져있는지만 조사하면 몇 마리의 지렁이가 필요한지 알 수 있다.

# dfs
def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N: #경계 검사
        return False
        
    if array[y][x] == 1:
        array[y][x] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False


T = int(input())

for _ in range(T):
    #각 가로, 세로, 위치 개수
    M, N, K = map(int, input().split()) 

    # NXM 보드 크기 설정
    array = [[0] * M for _ in range(N)]

    #배추 위치 입력
    for i in range(K):
        x,y = map(int,input().split()) #배추의 위치는 x, y
        array[y][x] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(j,i): #배추 그룹을 탐색!
                count += 1

    print(count)
