"""
1에서 N까지 도달
도달하기 까지 Edge의 비용이 최소한

- 각 노드들이 연결된 비용을 담은 Graph Dict
- 1에서 각 Node의 비용을 infinite로 초기화한 Dict
- 1에서 연결된 Node들에 대해서 q에 (Node, 비용, visited 배열)을 추가
- 현재 Node에 도달하는 비용이 최소값이면, visited하지않은 경로를 q에 자신과 연결된 Node를 다시 q에 추가
"""
from collections import defaultdict, deque
import heapq as hq

inf = 2 ** 31 - 1
N, M = map(int, input().split())
cost_dict = defaultdict(lambda: inf)
graph = defaultdict(list)  # (시작 Node): (Node, 비용)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

q = []  # (비용, Node)
hq.heapify(q)
for end, cost in graph[1]:
    hq.heappush(q, (cost, end))

while q:
    cost, curr_node = hq.heappop(q)
    if curr_node == N:
        if cost_dict[N] > cost:
            cost_dict[N] = cost
        continue

    if cost_dict[curr_node] < cost:  # 비용이 더 많이든 경로는 탐색할 필요없음.
        continue
    elif cost_dict[curr_node] > cost:  # 더 적은 비용으로 도달하는 비용을 찾으면 업데이트
        cost_dict[curr_node] = cost

        for next_node, next_cost in graph[curr_node]:
            hq.heappush(q, (cost + next_cost, next_node))

print(cost_dict[N])
