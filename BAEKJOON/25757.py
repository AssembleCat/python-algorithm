"""
TODO(문제의 시뮬레이션을 그대로 따라가지않고 규칙을 찾아서 해결한게 핵심이었음. 플레이어 중복을 제거하고 몫을 확보)
"""

play_record = set()
n, game = input().split()

for _ in range(int(n)):
    play_record.add(input())

mans = 0
if game == 'Y':
    mans = 1
elif game == 'F':
    mans = 2
elif game == 'O':
    mans = 3
print((int(len(play_record) / mans)))
