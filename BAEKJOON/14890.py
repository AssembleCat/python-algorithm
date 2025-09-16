N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]


def get_after_flat(roads, x):
    # 현재 칸에서 이후 칸에 -1만큼 높이가 얼마나 연속적으로 존재하는지 확인
    if x == len(roads) - 1:
        return 0

    target_high = roads[x]
    after_roads = roads[x:]

    count = 0
    for road in after_roads:
        if target_high == road:
            count += 1
        else:
            break

    return count


def simulate(roads):
    global L
    # 1. ramp_placed(lamp_set)를 1차원 배열로 수정
    ramp_placed = [False] * len(roads)

    for i in range(1, len(roads)):
        last_high, curr_high = roads[i - 1], roads[i]

        # 높이 차이가 1보다 크면 불가능
        if abs(last_high - curr_high) > 1:
            return False

        # 오르막길
        if last_high < curr_high:
            # 경사로를 놓을 이전 L개의 칸을 확인
            for j in range(i - L, i):
                # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면 실패
                if j < 0 or roads[j] != last_high or ramp_placed[j]:
                    return False

            # 경사로 설치
            for j in range(i - L, i):
                ramp_placed[j] = True

        # 내리막길
        elif last_high > curr_high:
            # 경사로를 놓을 이후 L개의 칸을 확인
            for j in range(i, i + L):
                # 범위를 벗어나거나, 높이가 다르거나, 이미 경사로가 있다면 실패
                if j >= len(roads) or roads[j] != curr_high or ramp_placed[j]:
                    return False

            # 경사로 설치
            for j in range(i, i + L):
                ramp_placed[j] = True

    return True


success_count = 0
for row in grid:
    if simulate(row):
        # print(f"성공: {row}")
        success_count += 1

for i in range(N):
    col = []
    for row in grid:
        col.append(row[i])

    if simulate(col):
        # print(f"성공: {col}")
        success_count += 1

print(success_count)
