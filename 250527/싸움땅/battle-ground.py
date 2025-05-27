"""
1. 플레이어 이동 -> 방향대로 한칸씩, 범위를 벗어날경우 반대로 회전 
2. 이동 이후 벌어지는 일
    - 다른 플레이어 없음 -> 총이 있는지 확인하고, 더 강한 총으로 교체
    - 플레이어가 있음 -> 초기능력치 + 총 공격력 싸움 
        - 루저 -> 총 내려놓고, 한칸 이동 -> 이동못할경우 90도 회전하여 갈 수 있는 칸을 찾음.
        - 위너 -> 현재칸에서 유지하고 가장 강한 총을 획득

"""
n, m, k = map(int, input().split())

guns = [
    [0] * n
    for _ in range(n)
]
for i in range(n):
    line = list(map(int, input().split()))
    for j, gun in enumerate(line):
        guns[i][j] = [gun]

players = []
for _ in range(m):
    x, y, d, s = list(map(int, input().split()))
    players.append([x-1, y-1, d, s])

player_gun = [0] * m
score = [0] * m
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(player_idx):
    x, y, d, s = players[player_idx]
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny): # 격자를 벗어나면 반대로 전환
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d] 
    players[player_idx] = [nx, ny, d, s]

def change_gun(player_idx):
    player = players[player_idx]
    x, y, d, s = player
    #print(f"플레이어({player_idx + 1}) {x, y}에서 총 교체 ")
    
    target_guns = guns[x][y]
    if player_gun[player_idx] != 0:
        target_guns.append(player_gun[player_idx])
    
    #print(f"획득가능 대상 총: {target_guns}")
    selected = max(target_guns)
    target_guns.remove(selected)

    player_gun[player_idx] = selected
    if len(target_guns) == 0:
        target_guns.append(0)
    guns[x][y] = target_guns

    #print(f"최종 획득 총: {selected}")
    #print(f"바닥에 놓인 총: {target_guns}")
    
def move_loser(loser_idx):
    x, y, d, s = players[loser_idx]
    # 패배자 이외의 정보를 가져옴.
    other_player = [(p[0], p[1]) for p in players if players.index(p) != loser_idx] 
    # 총 내려놓기
    if player_gun[loser_idx] != 0:
        guns[x][y].append(player_gun[loser_idx])
        player_gun[loser_idx] = 0
    
    # 도달가능한 방향으로 이동
    for i in range(4):
        direction = (d + i) % 4
        nx, ny = x + dx[direction], y + dy[direction]
        if in_range(nx, ny) and (nx, ny) not in other_player:
            players[loser_idx] = [nx, ny, direction, s]
            break
    
    #print(f"패자 움직임 상태: {players[loser_idx]}")
    # 주울 수 있는 총 줍기 
    change_gun(loser_idx)


def move_winner(winner_idx):
    #print(f"승자({winner_idx}) 움직임")
    change_gun(winner_idx)

def fight(player_idx, other_idx):
    player, other = players[player_idx], players[other_idx]
    p_power, other_power = player_gun[player_idx] + player[3], player_gun[other_idx] + other[3]
    #print(f"결투 발생 {player_idx}번 player({p_power}), {other_idx}번 other({other_power})") 
    
    # 승자 패자 결정 
    winner, loser = None, None    
    if p_power > other_power:
        winner, loser = player_idx, other_idx
    elif p_power < other_power:
        winner, loser = other_idx, player_idx
    else:
        if player[3] > other[3]:
            winner, loser = player_idx, other_idx
        else:
            winner, loser = other_idx, player_idx

    gap = abs(p_power - other_power)
    score[winner] += gap

    move_loser(loser)
    move_winner(winner)

def check_collision(player_idx):
    is_fight = False
    x, y, _, _ = players[player_idx]
    for other in players:
        ox, oy, _, _ = other
        if (x, y) == (ox, oy) and players.index(other) != player_idx :
            is_fight = True
            fight(player_idx, players.index(other))

    if not is_fight:
        change_gun(player_idx)    

for _ in range(k):
    for i in range(m):
        move(i)

        check_collision(i)

for s in score:
    print(s, end=" ")