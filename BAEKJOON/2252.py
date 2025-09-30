"""
N명을 키순서대로 줄세우기
학생끼지 비교한 정보 M개

N개의 Node, M개의 Edge
작은쪽에서 큰쪽으로 방향그래프 작성

in_dict
out_dict
1. 진입차수가 0인 node를 선택 q에 집어넣어
2. q에서 pop해
3. pop한 node의 out_dict에 있는 node의 in_dict를 제거
"""
from collections import defaultdict, deque

in_dict, out_dict = defaultdict(int), defaultdict(list)
N, M = map(int, input().split())

for _ in range(M):
    small, big = map(int, input().split())
    out_dict[small].append(big)
    in_dict[big] += 1

q = deque([])
for i in range(1, N + 1):
    if in_dict[i] == 0:
        q.append(i)

result = []
while q:
    curr_node = q.popleft()
    result.append(curr_node)

    for out_edge in out_dict[curr_node]:
        in_dict[out_edge] -= 1
        if in_dict[out_edge] == 0:
            q.append(out_edge)

print(*result)