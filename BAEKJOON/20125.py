"""
심장의 위치를 어떻게 찾을것인가? -> 상하좌우 모두 '*' 쿠기가 존재하는 칸이 심장!

TODO(특정 행, 열에 존재하는 요소를 카운팅하는 테크닉을 기억하자)
행 검사 left_arm = matrix[heart_idx[0]][:heart_idx[1]].count("*")
열 검사 right_leg = sum(1 for row in matrix if row[heart_idx[1]+1] == "*") - 1
"""
n = int(input())
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
matrix = [list(input()) for _ in range(n)]


def isHeart(x, y):
    for mat_i in range(len(dx)):
        nx = x + dx[mat_i]
        ny = y + dy[mat_i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return False
        if matrix[nx][ny] != '*':
            return False
    return True


heart_idx = (-1, -1)
for i in range(n):
    for j in range(n):
        if isHeart(i, j):
            heart_idx = (i, j)

left_arm = matrix[heart_idx[0]][:heart_idx[1]].count("*")
right_arm = matrix[heart_idx[0]][heart_idx[1]+1:].count("*")
body = sum(1 for row in matrix if row[heart_idx[1]] == "*") - 2
left_leg = sum(1 for row in matrix if row[heart_idx[1]-1] == "*") - 1
right_leg = sum(1 for row in matrix if row[heart_idx[1]+1] == "*") - 1

print(heart_idx[0]+1, heart_idx[1]+1)
print(left_arm, right_arm, body, left_leg, right_leg)
