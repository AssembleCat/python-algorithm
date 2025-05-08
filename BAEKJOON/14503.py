"""
1 - 벽, 0 - 청소필요, 2 - 청소 완료
TODO(배열의 인덱스 접근을 마이너스로 하는 것을 좋지않은 습관임. 배열의 크기로 나머지 연산(%)을 해주어 양수로 접근하도록 습관을 들이자.)
"""
N, M = map(int, input().split())
X, Y, cur_direction = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cleaning_count = 0
pos = [X, Y]


def check_direction():
    for i in range(4):
        nx = pos[0] + dx[(cur_direction + 3 - i) % 4]
        ny = pos[1] + dy[(cur_direction + 3 - i) % 4]
        if field[nx][ny] == 0:
            return (cur_direction + 3 - i) % 4
    return -1


while True:
    if field[pos[0]][pos[1]] == 0:
        cleaning_count += 1
        field[pos[0]][pos[1]] = 2
    new_direction = check_direction()
    if new_direction == -1:
        nx = pos[0] + dx[(cur_direction + 2) % 4]
        ny = pos[1] + dy[(cur_direction + 2) % 4]
        if field[nx][ny] == 1:
            break  # 후진해야하는데 벽이거나 밖으로 나가면 청소 종료
        pos = [nx, ny]
    else:
        nx = pos[0] + dx[new_direction]
        ny = pos[1] + dy[new_direction]
        cur_direction = new_direction
        pos = [nx, ny]

print(cleaning_count)
