"""
문제
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우

단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다.
예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

TODO(각 Row별로 나누어서 리스트로 저장하고 싶을때는 sys.stdin으로 각 라인을 받아서 리스트에 append할 수 있음. 단, 탈출 조건을 명시해주어야함.)
"""
import sys

lengths = []

for line in sys.stdin:
    nums = list(map(int, line.split()))
    if nums == [0, 0, 0]:
        break
    lengths.append(nums)

for length in lengths:
    l1, l2, l3 = length
    if max(length) >= sum(length) - max(length):
        print("Invalid")
    elif l1 == l2 and l1 == l3 and l2 == l3:
        print("Equilateral")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isosceles")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Scalene")
