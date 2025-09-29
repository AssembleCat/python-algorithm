N = int(input())
result = []
towers = list(map(int, input().split()))

stack = []
for i, tower in enumerate(towers):
    if not stack:  # Stack이 비어있으면 수신받아줄 타워가 없음.
        stack.append((i, tower))
        result.append(0)
        continue

    while True:  # Stack의 가장 위가 나보다 높으면 수신받아줄 수 있음. Stack 상위 (index+1)을 result에 추가
        if not stack:
            stack.append((i, tower))
            result.append(0)
            break

        l_i, l_tower = stack[-1]

        if l_tower < tower:
            stack.pop(-1)
            continue
        elif l_tower > tower:
            stack.append((i, tower))
            result.append((l_i + 1))
            break

print(*result)
