"""
N개 숫자카드
M개 정수

특정 숫자카드를 몇개 가지고 있는지 반환
"""
from collections import defaultdict

N = int(input())
number_cards = list(map(int, input().split()))

M = int(input())
requests = list(map(int, input().split()))


card_dict = defaultdict(int)
for n_card in number_cards:
    card_dict[n_card] += 1
for request in requests:
    print(card_dict[request], end=' ')
