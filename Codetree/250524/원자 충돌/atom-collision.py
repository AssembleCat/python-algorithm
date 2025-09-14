"""

defaultdict 사용법은 외운것 같음. 기본값이 존재하는 map이 필요하면 사용하자
move에서 speed에 따라 반복하면서 위치를 변경+보정 하는 방식이 단순해서 좋은것 같음. 한번에 위치를 지정하지말고 점차 증가시켜나가자
지역변수를 헷갈리게 사용하는 습관이 있음. 새롭게 생성된 변수와 지역변수를 명확히 구분해서 사용해야됨
append/extend를 알맞게 잘 사용했음. 잊지말고 정확히 사용하자.
입력 좌표가 1~n이라서 인덱스 접근할때 까다로운 경우가 있음. 미리 스케일링하는 습관을 들이면 좋다!

"""
from collections import defaultdict

n, m, k = map(int, input().split())
atoms = [list(map(int, input().split())) for _ in range(m)]
dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move():
    global atoms
    # x, y, s, d
    for idx, atom in enumerate(atoms):
        x, y, m, s, d = atom
        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny):
                x, y = (nx + n) % n, (ny + n) % n
            else:
                x, y = nx, ny
        atoms[idx] = [x, y, m, s, d]

def is_same_direction(targets):
    # 방향 인덱스가 짝수면 상하좌우, 홀수면 대각선 
    directions = sum([
        0 if atom[4] % 2 == 0 else 1 
        for atom in targets 
        ])
    
    # 전부 짝수인덱스라서 0이거나, 홀수인덱스라서 target의 길이오 같거나 
    return directions == len(targets) or directions == 0  

def create_new_atoms(collied_atoms):
    # 무게
    total_weight, total_speed = 0, 0
    for atom in collied_atoms:
        total_weight += atom[2]
        total_speed += atom[3]
    
    avg_weight = total_weight // 5
    avg_speed = total_speed // len(collied_atoms)
    
    if avg_weight < 1:
        return []
    
    # 방향
    new_atoms = []
    x, y, _, _, _ = collied_atoms[0]
    if is_same_direction(collied_atoms):
        for new_direction in range(0, 8, 2):
            new_atoms.append([x, y, avg_weight, avg_speed, new_direction])
    else:
        for new_direction in range(1, 8, 2):
            new_atoms.append([x, y, avg_weight, avg_speed, new_direction])

    return new_atoms

def collision():
    global atoms
    atom_map = defaultdict(list)
    for atom in atoms:
        x, y, _, _, _ = atom
        atom_map[(x, y)].append(atom)

    new_atoms = []
    for moved_atom in atom_map.values():
        if len(moved_atom) == 0:
            continue
        if len(moved_atom) == 1: # 원자가 하나만 있으면 그대로 추가 
            new_atoms.extend(moved_atom)
            continue

        created_atoms = create_new_atoms(moved_atom)
        if len(created_atoms) > 0:
            new_atoms.extend(created_atoms)
    
    atoms = new_atoms

def get_total_weight():
    return sum([atom[2] for atom in atoms])

for idx, atom in enumerate(atoms):
    x, y, m, s, d = atom
    atoms[idx] = [x-1, y-1, m, s, d]

for i in range(k):
    move()
    collision()

print(get_total_weight())