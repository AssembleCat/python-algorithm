"""
시간초과버전 ㅠㅜ 열심히 했는데 ㅠㅜ

N = int(input())

powers = []
for _ in range(N):
    powers.append(list(map(int, input().split())))


def divide_teams(members, target_size):
    n = len(members)
    result = set()

    def back_track(start, team_a):
        if len(team_a) == target_size:
            team_a = tuple(sorted(team_a))
            team_b = tuple(sorted([m for m in members if m not in team_a]))
            result.add(tuple(sorted([team_a, team_b])))
            return

        for i in range(start, n):
            back_track(i + 1, team_a + [members[i]])

    back_track(0, [])
    return list(result)


def get_combination(elements):
    # 완성된 팀에서 시너지 접근을 위한 2명의 조합을 추출
    result = set()
    for i in range(len(elements)):
        for j in range(i + 1, len(elements)):
            if tuple(sorted([elements[i], elements[j]])) not in result:
                result.add(tuple(sorted([elements[i], elements[j]])))
    return list(result)


member_num = [x for x in range(1, N + 1)]
team_comb = divide_teams(member_num, len(member_num) // 2)
minimum_diff = 1000000
for teams in team_comb:
    team_a, team_b = teams
    score_a, score_b = 0, 0
    comb_a = get_combination(team_a)
    comb_b = get_combination(team_b)
    for i in range(len(comb_a)):
        # 중첩된 자료에 접근하다보니 인덱스 실수가 발생했었음. 꼼꼼히 접근하자
        score_a += powers[comb_a[i][0] - 1][comb_a[i][1] - 1] + powers[comb_a[i][1] - 1][comb_a[i][0] - 1]
        score_b += powers[comb_b[i][0] - 1][comb_b[i][1] - 1] + powers[comb_b[i][1] - 1][comb_b[i][0] - 1]
    diff = abs(score_a - score_b)
    if diff < minimum_diff:
        minimum_diff = diff

print(minimum_diff)

"""
N = int(input())

powers = []
for _ in range(N):
    powers.append(list(map(int, input().split())))

visited = [False] * N
minimum_diff = float('inf')


def calc_synergy(team):
    total = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            a, b = team[i], team[j]
            total += powers[a][b] + powers[b][a]
    return total


def back_track(idx, depth):
    global minimum_diff
    if depth == N // 2:
        team_a = [i for i in range(N) if visited[i]]
        team_b = [i for i in range(N) if not visited[i]]

        score_a = calc_synergy(team_a)
        score_b = calc_synergy(team_b)

        diff = abs(score_a - score_b)
        minimum_diff = min(minimum_diff, diff)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            back_track(i + 1, depth + 1)
            visited[i] = False


back_track(0, 0)
print(minimum_diff)
