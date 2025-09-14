"""
좌표가 (1, 1) 부터 시작됨 입력값 스케일링 필요
연쇄적인 움직임이 있음! Queue에 움직임을 순차적으로 넣어서 구현

특정 동작으로 인해 조건에 따라 다른 오브젝트들도 연쇄적으로 이동해야한다면 Queue를 가장 먼저 떠올리자
일일히 구현하지않고 조건과 행동만 해당 단계에서 정의하면 구현이 어렵지않다!
"""
import copy
from collections import deque

L, N, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(L)]
knights = [list(map(int, input().split())) for _ in range(N)]
original_knights = copy.deepcopy(knights)
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L

def simulate_move(knight_idx, direction):
    if knights[knight_idx][4] < 1: # 기사 체력이 없으면 명령 실행하지않음.
        return False

    q = deque()
    q.append((knight_idx, direction))
    while q:
        k_idx, dir = q.popleft()
        r, c, h, w, k = knights[k_idx]
        if k < 1:
            continue
        # r, c가 direction 방향으로 움직였을때, 범위 밖으로 나가는지(1), 움직인 곳에 벽이 존재하는지(2) 검사
        nr, nc = r + dr[dir], c + dc[dir]
        for i in range(nr, nr + h): 
            for j in range(nc, nc + w):
                if not in_range(i, j):
                    return False
                if grid[i][j] == 2:
                    return False
        # 다른 기사들이 움직인 칸에 존재하는지 확인, 있다면 해당 기사를 움직여야함.
        another_knights = [knight for knight in knights if knight != knights[k_idx]]
        for a_knight in another_knights:
            ar, ac, ah, aw, ak = a_knight # 1, 0, 2, 1, 1
            if ak < 1:
                continue
            for ai in range(ar, ar+ah): # 1~2 
                for aj in range(ac, ac+aw): # 0
                    if nr <= ai < nr + h and nc <= aj < nc + w:
                        if (knights.index(a_knight), direction) not in q:
                            q.append((knights.index(a_knight), direction))
    return True

def count_trap(x, y, h, w):
    count = 0
    for i in range(x, x+h):
        for j in range(y, y+w):
            if grid[i][j] == 1:
                count += 1
    return count

def move(knight_idx, direction):
    # 시뮬레이션으로 경로상의 모든 기사를 밀 수 있음이 보장된 상태임
    # 기사를 이동하고, 체력을 조정하는 기능
    # 첫 대상 기사는 체력이 0 이상임이 보장됨.
    global knights
   
    q = deque()
    q.append((knight_idx, direction))
    while q:
        k_idx, dir = q.popleft()
        cr, cc, ch, cw, ck = knights[k_idx]
        if ck < 1: # 이동할 대상 기사체력이 없다면 작동 x
            continue
        nr, nc = cr + dr[dir], cc + dc[dir]
        # 이동을 실행한 기사는 데미지를 입지않음.
        if k_idx != knight_idx:
            ck = max(0, ck - count_trap(nr, nc, ch, cw))
        knights[k_idx] = (nr, nc, ch, cw, ck)
        
        another_knights = [knight for knight in knights if knight != knights[k_idx]]
        for a_knight in another_knights:
            ar, ac, ah, aw, ak = a_knight 
            if ak < 1:
                continue
            for ai in range(ar, ar+ah): 
                for aj in range(ac, ac+aw):
                    if nr <= ai < nr + ch and nc <= aj < nc + cw:
                        if (knights.index(a_knight), direction) not in q:
                            q.append((knights.index(a_knight), direction))

def total_damage():
    damage = 0
    for start, end in zip(original_knights, knights):
        if end[4] < 1:
            continue
        damage += start[4] - end[4]
    
    return damage

for idx, knight in enumerate(knights):
    r, c, h, w, k = knight
    knights[idx] = [r-1, c-1, h, w, k]

for _ in range(Q):
    num, dir = map(int, input().split())
    if simulate_move(num - 1, dir): # 기사번호가 1부터 주어지므로 index에 맞게 1을 빼서 전달함.
        move(num-1, dir)

print(total_damage())