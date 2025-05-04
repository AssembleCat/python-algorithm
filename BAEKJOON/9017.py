"""
1. Map을 생성함. Key는 팀 번호, Value는 등수를 담은 List를 저장 이때 등수는 Index + 1을 지정해야함.
2. 모든 Key에 대해서 길이가 6인 자료만 필터링
3. 상위 4개 등수를 합산
4. 점수가 같은 팀이 있다면 5번째 값이 더 작은 팀 번호를 출력

TODO(또또 조건을 허투로 읽었음. 유효하지않은 참가자에 대해서는 랭킹점수를 집계하지 않는 조건을 무시함. 문제 정확히 읽자!!)
TODO(dict에 추가되지않은)
"""
T = int(input())
for _ in range(T):
    N = int(input())
    players_count, score = {}, {}
    ranking = list(map(int, input().split()))

    # 1. 팀별 참가자 수 카운팅
    for idx, team_id in enumerate(ranking):
        players_count[team_id] = players_count.get(team_id, 0) + 1

    # 2. 참가자가 6명 미만인 참가자는 랭킹 집계에서 제거
    for team_id, count in players_count.items():
        if count < 6:
            ranking = [x for x in ranking if team_id != x]

    # 3. 팀별로 점수를 매기고 분리
    for idx, team_id in enumerate(ranking):
        if team_id not in score:
            score[team_id] = []
        score[team_id].append(idx + 1)

    result = [0, 10000]
    for team_id, score_list in score.items():
        if sum(score_list[:4]) < result[1]:
            result = [team_id, sum(score_list[:4])]
        elif sum(score_list[:4]) == result[1] and score[team_id][4] < score[result[0]][4]:
            result = [team_id, sum(score_list[:4])]

    print(result[0])