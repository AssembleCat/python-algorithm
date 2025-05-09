"""
1. 오전/오후 일을 나누는 조합을 생성 -> Back Traking
2. 조합에 따라 점수차이를 연산, 기존보다 차이가 적을 경우 갱신

TIL: 큰 수에서 조합을 저장해두는 것을 큰 비용이 발생함. 조합이 기억되어야하지않다면 조합 생성 즉시 연산하는것을 추천
TIL: 요소들에서 n개의 조합을 생성하는 것을 잘 기억하자! 
"""

N = int(input())
work_matrix = [list(map(int, input().split())) for _ in range(N)]

work_nums = [x for x in range(1, N+1)]
visited = [False] * N
minimum_diff = 10000000

def calculate_synergy(elements):
    synergy_point = 0
    for i in range(len(elements) - 1):
        for j in range(i+1, len(elements)):
            synergy_point += work_matrix[elements[i] - 1][elements[j] - 1] + work_matrix[elements[j] - 1][elements[i] - 1]
    return synergy_point   

def get_combinations(start, elements):
    global minimum_diff
    if len(elements) == N // 2:
        work_am = tuple(sorted(elements))
        work_pm = tuple(sorted([x for x in work_nums if x not in elements]))
        point_am = calculate_synergy(work_am)
        point_pm = calculate_synergy(work_pm)
        if abs(point_am - point_pm) < minimum_diff:
            minimum_diff = abs(point_am - point_pm)
        return 

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            get_combinations(i+1, elements + [work_nums[i]])
            visited[i] = False 

get_combinations(0, [])
print(minimum_diff)