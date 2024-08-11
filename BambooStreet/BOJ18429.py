from collections import deque

# 변수, 처음에 오른쪽 이동 dir = 1
n, k, l, y, x, t, ret, idx, dir = 0, 0, 0, 0, 0, 0, 0, 0, 1

# NXN 보드 크기 설정
a = [[0] * 104 for _ in range(104)]
# 방문한 보드 표시
visited = [[0] * 104 for _ in range(104)]

_time = []

# 보드의 크기 N (2<=N<=100), 사과의 개수 K (0<= K <= 100)
n = int(input())
k = int(input())

# 사과의 위치, 첫번째 줄은 정수 행, 두번째 정수는 열 위치 의미, 
# 위치는 모두 다르며 맨위 맨 좌측(1행 1열)에는 사과가 없다.
for _ in range(k):
    y, x = map(int, input().split())
    a[y-1][x-1] = 1

# 뱀의 방향 전환 횟수 L이 주어진다. (1<= L <= 100)
# 뱀의 방향 변환 정보가 주어지는데, 
# 정수 X와 문자 C로 이루어져 있으며, 게임 시작 시간으로 X초가 끝난 뒤에 90도 방향 회전
l = int(input())
for _ in range(l):
    t, c = input().split()
    t = int(t)
    if c == 'D':
        _time.append((t, 1))
    else:
        _time.append((t, 3))

time = 0
# dq (0,0)
dq = deque()
dq.append((0, 0))

# x, y방향으로 이동 벡터
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while dq:
    time += 1 # 시간을 1 증가
    y, x = dq[0] # 현재 뱀의 머리 위치
    ny = y + dy[dir] # 다음 머리 위치
    nx = x + dx[dir] # 다음 머리 위치

    # 벽과 충돌 여부 
    if ny >= n or ny < 0 or nx >= n or nx < 0 or visited[ny][nx]:
        break

    # 사과가 없으면, 앞으로 이동만
    if not a[ny][nx]:
        visited[dq[-1][0]][dq[-1][1]] = 0 # 꼬리가 있던 위치의 값 0으로
        dq.pop() # dq에서 마지막 요소제거

    # 사과가 있으면, 길이 늘리면서 전진
    else:
        a[ny][nx] = 0
    
    
    visited[ny][nx] = 1 # 방문한 곳 기록
    dq.appendleft((ny, nx)) # dq에 추가
    if idx < len(_time) and time == _time[idx][0]: # 방향전환 명령 확인 시간대 확인
        dir = (dir + _time[idx][1]) % 4 # 방향 확인 후 1은 오른쪽 90도 회전, 3은 왼쪽 90도 회전
        idx += 1

print(time)