from collections import deque

wheels = [input() for _ in range(4)]
K = int(input())


def print_wheels():
    print('-' * 20)
    for wheel in wheels:
        print(*wheel)


def rotate_wheel(num, direction):
    global wheels
    if direction == 1:  # 시계방향
        wheels[num] = wheels[num][-1] + wheels[num][:-1]
    else:  # 반시계
        wheels[num] = wheels[num][1:] + wheels[num][0]


def get_score():
    score = 0
    for i, wheel in enumerate(wheels):
        if wheel[0] == '1':  # 12시가 s극임.
            score += (1 << i)

    return score


for _ in range(K):
    num, direction = map(int, input().split())
    num = num - 1

    # 회전한 번호, 적용할 번호, 방향(움직일 조건이 된다면)
    q = deque([[num, num - 1, -direction], [num, num + 1, -direction]])
    rotation_log = [(num, direction)]
    while q:
        from_num, cur_num, cur_direction = q.popleft()

        if cur_num < 0 or cur_num > 3:
            continue

        if from_num > cur_num:  # 검사할 바퀴가 왼쪽에 있음.
            if wheels[from_num][6] != wheels[cur_num][2]:
                rotation_log.append((cur_num, cur_direction))
                q.append([cur_num, cur_num - 1, -cur_direction])
        elif from_num < cur_num:  # 검사할 바퀴가 오른쪽에 있음.
            if wheels[from_num][2] != wheels[cur_num][6]:
                rotation_log.append((cur_num, cur_direction))
                q.append([cur_num, cur_num + 1, -cur_direction])

    for target_num, direction in rotation_log:
        rotate_wheel(target_num, direction)

print(get_score())
