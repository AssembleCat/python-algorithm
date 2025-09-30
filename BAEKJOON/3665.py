"""
위상정렬 규칙을 찾는것까지는 괜찮았음. 근데 'a b' 가 주어졌을때 이 데이터의 의미가 '상대적 위치 변환'의미를
a가 b를 역전했다라는 의미로 받아들여서 문제가 생겼었음. 알고리즘이해는 문제없는데, 또 문제이해에 약했음.
Input의 조건을 명확하게 파악하자.
"""
from collections import defaultdict, deque

T = int(input())

for _ in range(T):
    N = int(input())
    last_year_rank = list(map(int, input().split()))

    # 작년 순위를 표현하는 in, out 차원포현
    indegree, outgraph = defaultdict(int), defaultdict(set)
    for i in range(len(last_year_rank)):
        from_node = last_year_rank[i]
        for j in range(i + 1, len(last_year_rank)):
            to_node = last_year_rank[j]
            indegree[to_node] += 1
            outgraph[from_node].add(to_node)

    # 바뀐 등수에 대해서 삽입/삭제
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if a in outgraph[b]:  # a가 b를 역전
            outgraph[b].remove(a)
            indegree[a] -= 1
            outgraph[a].add(b)
            indegree[b] += 1
        elif b in outgraph[a]:  # b가 a를 역전
            outgraph[a].remove(b)
            indegree[b] -= 1
            outgraph[b].add(a)
            indegree[a] += 1

    # 위상정렬 순서 실행!
    q = deque([])
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    is_undefined_rank = False
    while q:
        if len(q) > 1:  # 진입차수가 0인 Node가 2개 이상이면 순위가 명확하지않음.
            is_undefined_rank = True
            break
        else:  # 1개만 담겨있으면 순위가 확실함. 결과에 포함
            num = q.popleft()
            result.append(num)

            for next_num in outgraph[num]:
                indegree[next_num] -= 1
                if indegree[next_num] == 0:
                    q.append(next_num)

    if is_undefined_rank:
        print('?')
    elif len(result) != N:
        print('IMPOSSIBLE')
    else:
        print(*result)
