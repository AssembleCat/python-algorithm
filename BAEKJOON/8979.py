"""
TODO(Map을 사용한건 좋았는데 문제의 동점 기준을 명확히 이해하지 못했음. 금은동이 모두 숫자가 같아야 동점인데 점수로 환산했을때 엣지케이스를 고려하지 못함.)
"""
n, k = map(int, input().split())

country = []
for _ in range(n):
    temp = list(map(int, input().split()))
    country.append([temp[0], 1000000*temp[1] + 1000*temp[2] + 1*temp[3]])

sorted_country = sorted(country, key=lambda x: x[1], reverse=True)

rank_board = {}
last_score = -1
rank = 0
for idx, item in enumerate(sorted_country):
    if item[1] != last_score:
        rank = idx + 1
        last_score = item[1]
        rank_board[item[0]] = rank
    elif item[1] == last_score:
        rank_board[item[0]] = rank
print(rank_board[k])