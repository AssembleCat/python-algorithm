"""
1. 오전/오후 일을 나누는 조합을 생성 -> Back Traking
2. 조합에 따라 점수차이를 연산, 기존보다 차이가 적을 경우 갱신

"""
N = int(input())
work_matrix = [list(map(int, input().split())) for _ in range(N)]

work_nums = [x for x in range(1, N+1)]
visited = [False] * N
work_combo = set()
target_size = len(work_matrix)

def get_combinations(start, elements):
    if len(elements) == N // 2:
        work_am = tuple(sorted(elements))
        work_pm = tuple(sorted([x for x in work_nums if x not in elements]))
        work_combo.add(tuple(sorted([work_am, work_pm])))
        return 

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            get_combinations(i+1, elements + [work_nums[i]])
            visited[i] = False

def calculate_synergy(elements):
    synergy_point = 0
    for i in range(len(elements) - 1):
        for j in range(i+1, len(elements)):
            synergy_point += work_matrix[elements[i] - 1][elements[j] - 1] + work_matrix[elements[j] - 1][elements[i] - 1]
    return synergy_point    

get_combinations(0, [])
minimum_diff = 10000000
for am, pm in work_combo:
    am_point = calculate_synergy(am)
    pm_point = calculate_synergy(pm)
    if abs(am_point - pm_point) < minimum_diff:
        minimum_diff = abs(am_point - pm_point)
print(minimum_diff)