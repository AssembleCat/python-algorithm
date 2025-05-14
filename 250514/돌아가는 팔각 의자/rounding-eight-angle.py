"""
의자번호, 회전방향을 입력받아 회전을 실행시키는 함수
    1. 요청 의자번호의 좌우에 맞닿은 사람의 조건을 확인
    2. 회전조건이 맞을때 회전을 실행시킨 의자의 반대방향으로 회전됨.
    3. 아! 그러면 각 단계별로 1회만 돌아가니 해당 단계를 위한 회전을 기억하는 배열을 생성하고 거기에 기록하자


핵심을 알았다. 이거 제공된 번호랑 방향은 Trigger일 뿐임. 
일단 의자간에 붙어있는 N/S를 검사하는 것이 핵심
"""
def can_go(n):
    return 0 <= n < 4

def check_rotation(n, rotate_from, rotation_type):
    global wheel
    # n이 rotate_from보다 클때, n-1과 n이 접촉한 사람 출신지역이 다르고(1), n-1이 회전하는 조건이어야함(2).
    # n이 torate_from보다 작을때, n과 n+1이 접촉한 사람 출신지역이 다르고(1), n+1이 회전하는 조건이어야함(2).
    if n > rotate_from:
        if wheel[n][6] != wheel[n-1][2] and rotation_type[n-1] != 0:
            rotation_type[n] = rotation_type[n-1] * -1
    elif n < rotate_from:
        if wheel[n][2] != wheel[n+1][6] and rotation_type[n+1] != 0:
            rotation_type[n] = rotation_type[n+1] * -1

def do_rotate(n, d):
    global wheel
    if d == 1:
        wheel[n] = wheel[n][-1] + wheel[n][:7]
    elif d == -1:
        wheel[n] = wheel[n][1:] + wheel[n][0]

def simulation(n, d):
    global wheel

    # 각 의자번호별로 어떤 방향으로 회전할지 기억, 시계(1), 반시계(-1), 회전없음(0)
    rotation_type = [0 for _ in range(4)]
    rotation_type[n] = d

    # n의 양옆으로 전진하면서 회전가능한지 확인
    for i in range(1, 4):
        if can_go(n+i):
            check_rotation(n+i, n, rotation_type)
        if can_go(n-i):
            check_rotation(n-i, n, rotation_type)
    
    for idx, r_type in enumerate(rotation_type):
        do_rotate(idx, r_type)

def calculate():
    global wheel
    result = 0
    for i in range(4):
        if wheel[i][0] == '1':
            result += 2 ** i
    
    return result

wheel = [input() for _ in range(4)]

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())
    simulation(n-1, d)

print(calculate())
