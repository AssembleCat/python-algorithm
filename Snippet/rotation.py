arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"초기 정사각형 배열:")
for row in arr:
    print(row)


def rotation_90():
    n = len(arr)
    new_90 = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            new_90[j][n - i - 1] = arr[i][j]
    print("90도 회전:")
    for row in new_90:
        print(row)


def rotation_180():
    n = len(arr)
    new_180 = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            new_180[n - i - 1][n - j - 1] = arr[i][j]
    print("180도 회전")
    for row in new_180:
        print(row)


def rotation_270():
    n = len(arr)
    new_270 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_270[n - j - 1][i] = arr[i][j]
    print("270도 회전")
    for row in new_270:
        print(row)


rotation_90()
rotation_180()
rotation_270()

l_arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print("초기 직사각형 배열:")
for row in l_arr:
    print(row)


def l_rotation_90():
    n = len(l_arr)
    m = len(l_arr[0])
    new_90 = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_90[j][n - i - 1] = l_arr[i][j]
    print("90도 회전")
    for row in new_90:
        print(row)


def l_rotation_180():
    n = len(l_arr)  # 원본 x 길기
    m = len(l_arr[0])  # 원본 y 길이
    new_180 = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_180[n - i - 1][m - j - 1] = l_arr[i][j]
    print("180도 회전")
    for row in new_180:
        print(row)


def l_rotation_270():
    n = len(l_arr)  # 원본 x길이
    m = len(l_arr[0])  # 원본 y 길이
    new_270 = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_270[m - j - 1][i] = l_arr[i][j]
    print("270도 회전")
    for row in new_270:
        print(row)


l_rotation_90()
l_rotation_180()
l_rotation_270()
