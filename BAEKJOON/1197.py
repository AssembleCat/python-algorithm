"""
hq (cost, start, end)
pop 이후 parent 검사
- 추가(parent가 다르면)
- 스킵
"""
import heapq as hq

V, E = map(int, input().split())
q = []
for _ in range(E):
    start, end, cost = map(int, input().split())
    hq.heappush(q, (cost, start, end))

parent = {i: i for i in range(1, V + 1)}


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_a] = root_b
    else:
        parent[root_b] = root_a


total_cost = 0
while q:
    cost, start, end = hq.heappop(q)
    if find(start) != find(end):
        union(start, end)
        total_cost += cost

print(total_cost)
