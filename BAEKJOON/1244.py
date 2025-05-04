"""
todo(구현 문제였는데 기본기가 많이 부족했음. 할당과, 인덱스 접근을 엄밀히 정의하자, 출력형식도 따로 존재했었음!)
"""
n = int(input())
switches = list(map(int, input().split()))
student_num = int(input())


def toggleSwitchTerm(start, end):
    for i in range(start, end + 1):
        switches[i] = 1 - switches[i]


def findTerms(pivot):
    start = end = pivot
    while True:
        if start - 1 < 0 or end + 1 >= len(switches):
            break
        if switches[start - 1] != switches[end + 1]:
            break
        start -= 1
        end += 1
    return start, end


def toggleSwitchMulti(request_num):
    for i in range(len(switches)):
        if (i + 1) % request_num == 0:
            switches[i] = 1 - switches[i]


for _ in range(student_num):
    sex, num = map(int, input().split())
    if sex == 1:
        toggleSwitchMulti(num)
    else:
        pivot = num - 1  # 인덱스 보정
        start, end = findTerms(pivot)
        toggleSwitchTerm(start, end)

# 출력 형식 맞추기
for i in range(len(switches)):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
