"""
heapq, defaultdict를 사용해서 효율적으로 다익스트라를 구현한 방향은 맞았음.
그러나 heapq가 비대해졌을때 push, pop 비용도 비싼것을 간과함.
아예 heapq에 안넣는 방향으로 진행하는것이 베스트!
"""
import heapq as hq
from collections import defaultdict

INF = 2 ** 31 - 1

V, E = map(int, input().split())
entry_vertex = int(input())
graph = defaultdict(list)
cost = [INF for _ in range(V + 1)]

for _ in range(E):
    start, end, edge_cost = map(int, input().split())
    graph[start].append((end, edge_cost))

cost[entry_vertex] = 0  # 시작점 0으로 초기화
q = [(0, entry_vertex)]  # (비용, 위치)

while q:
    curr_cost, vertex = hq.heappop(q)

    if cost[vertex] < curr_cost:
        continue

    for next_node, extra_cost in graph[vertex]:
        new_cost = curr_cost + extra_cost
        if new_cost < cost[next_node]:
            cost[next_node] = new_cost
            hq.heappush(q, (curr_cost + extra_cost, next_node))

for i in range(1, V + 1):
    print(cost[i] if cost[i] != INF else 'INF')
