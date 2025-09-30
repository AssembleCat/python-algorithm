"""
- N개의 문제를 모두풀어
- 먼저 푸는 것이 좋은 규칙이 있음. 1 -> 2
- 쉬운 문제부터 풀어 -> 숫자가 클수록 더 어려움.

매번 indgree가 0인것들을 추출하여 가장 쉬운 문제만 q에 다시 put
"""
import heapq as hq
from collections import defaultdict, deque

N, M = map(int, input().split())
indgree, outgraph = defaultdict(int), defaultdict(set)

for _ in range(M):
    before, after = map(int, input().split())
    outgraph[before].add(after)
    indgree[after] += 1

available_quest, processed_quest = [], set()
for i in range(1, N + 1):
    if indgree[i] == 0:
        hq.heappush(available_quest, i)
        processed_quest.add(i)

result = []
while available_quest:
    quest = hq.heappop(available_quest)
    result.append(quest)

    for next_quest in outgraph[quest]:
        indgree[next_quest] -= 1
        if indgree[next_quest] == 0 and next_quest not in processed_quest:
            hq.heappush(available_quest, next_quest)
            processed_quest.add(next_quest)

print(*result)
