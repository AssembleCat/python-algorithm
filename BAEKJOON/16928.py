from collections import deque, defaultdict

inf = 2 ** 31 - 1

N, M = map(int, input().split())
ladder, snake = defaultdict(int), defaultdict(int)

for _ in range(N):
    s, e = map(int, input().split())
    ladder[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    snake[s] = e

q = deque([(1, 0)])  # 번호, 횟수
cost = [inf] * 101
visited = [False] * 101

while q:
    num, count = q.popleft()

    # 도달한적이 있지만 더 오래걸렸으면 탐색할 이유가 없음.
    if cost[num] > count:
        cost[num] = count
    else:
        continue

    # 현재 위치에 사다리 or 뱀이 있으면 해당 위치로 이동
    if ladder[num]:
        q.append((ladder[num], count))
        continue
    if snake[num]:
        q.append((snake[num], count))
        continue

    # 현재 위치에서 주사위 이동
    for i in range(1, 7):
        new_num = num + i
        if new_num > 100:
            continue
        q.append((new_num, count + 1))

print(cost[100])