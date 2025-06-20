import sys
from collections import defaultdict

# 입력이 많이 호출된다면 sys.stdin.readline를 사용하자, import 문도 까먹지 말고!
input = sys.stdin.readline

n, m = map(int, input().split())

count_dict = defaultdict(int)
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    count_dict[word] += 1

result = sorted(count_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in result:
    print(word)
