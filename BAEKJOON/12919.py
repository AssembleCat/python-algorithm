from collections import deque

S = input()
T = input()

q = deque([T])
result = 0
visited = {T}

while q:
    curr = q.popleft()

    if len(curr) == len(S):
        if curr == S:
            result = 1
        continue

    # 1. BXX B를 제거하고 뒤집기
    if curr[0] == 'B':
        new = ''.join(reversed(curr[1:]))
        if new not in visited:
            visited.add(new)
            q.append(new)
    # 2. XXA A를 제거
    if curr[-1] == 'A':
        new = curr[:-1]
        if new not in visited:
            visited.add(new)
            q.append(new)

print(result)
