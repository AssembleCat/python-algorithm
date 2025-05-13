"""
4개의 톱니바퀴가 입력됨.
오른쪽 - 3번째, 왼쪽 - 7번째 극성이 다른 톱니바퀴에 영향을 줌.
각 배열(톱니바퀴)를 회전시키는 동작 함수를 구성(배열, 방향)
매 회전마다 주변 극성을 확인해서 회전시킬 톱니바퀴 번호와 방향을 선정함.
큐를 생성해서 해당 큐에 회전시킬 이벤트를 입력함.
최종 점수는 1번째 극성여부에 따름.
0 = N극, 1 = S극
방향 1 - 시계, -1 - 반시계
"""
from collections import deque

wheel = [input() for _ in range(4)]
N = int(input())
rotation_event = deque()


def do_rotation(effect_by, direction, ):


for _ in range(N):
    wheel_num, rotation = map(int, input().split())

