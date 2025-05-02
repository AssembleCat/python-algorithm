"""
rank 배열내에 new_score보다 더 큰 요소의 갯수를 확보
만약 큰 요소가 p이상이라면 더이상 ranking에 진입할 수 없으므로 -1 출력
p보다 작다면 ranking에 높은 요소들 다음으로 진입가능하지 +1하여 출력

TODO(문제가 어렵지않지만 제공되는 요소가 0개일때 입력을 제어해줘야했음. 0개일때의 조건을 엄밀히 따지자)
"""
n, new_score, p = map(int, input().split())
rank = []
if n != 0:
    rank = list(map(int, input().split()))
greater_num_count = sum(1 if num >= new_score else 0 for num in rank)

if greater_num_count >= p:
    print("-1")
else:
    eq_num_count = sum(1 if num == new_score else 0 for num in rank)
    print(greater_num_count - eq_num_count + 1)
