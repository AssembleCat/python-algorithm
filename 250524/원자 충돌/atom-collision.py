"""
1. 원자의 초기위치가 1~n으로 표현됨. 스케일링 필요함.
- 1초 마다 원자 이동 함수
- 원자 합성 함수
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
        #print(f"move({idx}) to {d}, speed({s}): {x, y}")
        for _ in range(s):
            nx, ny = x + dx[d], y + dy[d]
            if not in_range(nx, ny):
                x, y = (nx + n) % n, (ny + n) % n
            else:
                x, y = nx, ny
        atoms[idx] = [x, y, m, s, d]
        #print(f"new({idx}): {x, y}")

def is_same_direction(targets):
    # 방향 인덱스가 짝수면 상하좌우, 홀수면 대각선 
    directions = sum([
        0 if atom[4] % 2 == 0 else 1 
        for atom in targets 
        ])
    
    # 전부 짝수인덱스라서 0이거나, 홀수인덱스라서 target의 길이오 같거나 
    return directions == len(targets) or directions == 0  

def create_new_atoms(collied_atoms):
    #print(f"collied: {collied_atoms}")
    # 무게
    total_weight, total_speed = 0, 0
    for atom in collied_atoms:
        total_weight += atom[2]
        total_speed += atom[3]
    
    avg_weight = total_weight // 5
    avg_speed = total_speed // len(collied_atoms)
    
    if avg_weight < 1:
        #print(f"무게가 0임 원자 소멸")
        return []
    
    # 방향
    new_atoms = []
    x, y, _, _, _ = collied_atoms[0]
    if is_same_direction(collied_atoms):
        #print(f"모두 같은 방향임! 상하좌우로 분할")
        for new_direction in range(0, 8, 2):
            new_atoms.append([x, y, avg_weight, avg_speed, new_direction])
    else:
        #print(f"다른 방향이 존재함! 대각선으로 분할")
        for new_direction in range(1, 8, 2):
            new_atoms.append([x, y, avg_weight, avg_speed, new_direction])
    #print(f"새롭게 생성된 원자: {new_atoms}")
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
    #print(f"{i+1} 번째 실험 시작")
    #print(f"현재 원자: {atoms}")
    move()
    #print(f"이동 후 원자: {atoms}")
    collision()

print(get_total_weight())