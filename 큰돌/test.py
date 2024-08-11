from copy import deepcopy
from itertools import permutations

def rotate_operation(A, r, c, s):
    #회전 연산을 수행할 배열의 복사본 생성
    B = deepcopy(A)

    #(r-s, c-s)부터 (r+s, c+s)의 정사각형을 시계방향으로 회전
    for layer in range(s):
        #시작점과 끝점 설정
        sy, sx = r-s+layer, c-s+layer
        ey, ex = r+s-layer, c+s-layer

        #현재 레이어의 첫 번쨰 요소를 저장한다.
        temp = B[sy][sx]

        #왼쪽 변 이동
        for i in range(sy,ey):
            B[i][sx] = B[i+1][sx]

        #아래쪽 변 이동
        for j in range(sx, ex):
            B[ey][j] = B[ey][j+1]

        #오른쪽 변 이동
        for i in range(ey,sy,-1): #ey부터 sy까지 1씩 감소시킨다.
            B[i][ex] = B[i-1][ex]
        
        #위쪽 변 이동
        for j in range(ex,sx,-1): 
            B[sy][j] = B[sy][j-1]

        B[sy][sx+1] = temp

    return B


#배열 정보
N, M, K = map(int, input().split())
array = [list(map(int,input().split())) for _ in range(N)]

#회전 연산 정보
operations = []
for _ in range(K):
    r,c,s = map(int,input().split())
    operations.append((r-1, c-1, s))

#모든 가능한 회전 순서에 대해 최소값 계산
min_value = float('inf')
for perm in permutations(range(K)):
    temp_array = deepcopy(array)
    for idx in perm:
        r,c,s = operations[idx]
        temp_array = rotate_operation(temp_array, r,c,s)


    #각 행의 값 중 최소값 계산하기
    min_value = min(min_value, min(sum(row) for row in temp_array))


#최소값 출력
print(min_value)
