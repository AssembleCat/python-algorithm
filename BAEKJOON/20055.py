"""
1. 컨베이어벨트 회전 / 로봇 큐도 함께 회전
2. 각 위치마다 로봇 전진 -> 가장 뒷 인덱스부터
"""
from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([False] * N)

turn = 0
while True:
    turn += 1

    # 1. 벨트 회전
    belt.rotate()

    # 1-1. 로봇 회전
    robot.pop()
    robot.appendleft(False)

    # 2. 로봇 이동
    for i in range(N - 1, -1, -1):
        if i == N - 1:
            robot[i] = False
            continue

        # 이동하려는 칸에 로봇이 없으며, 내구도가 1이상
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1

    # 3. 올리는 위치에 칸의 내구도가 0이 아니면 로봇을 올림.
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료
    zero_cell = 0
    for cell in belt:
        if cell == 0:
            zero_cell += 1

    if zero_cell >= K:
        break

print(turn)
