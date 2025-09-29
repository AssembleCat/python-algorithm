N = int(input())
start = [int(digit) for digit in input()]
end = [int(digit) for digit in input()]


def do_flip(idx):
    if idx == 0:
        flip(idx)
        flip(idx + 1)
    elif idx == N - 1:
        flip(idx)
        flip(idx - 1)
    else:
        flip(idx)
        flip(idx - 1)
        flip(idx + 1)


def flip(idx):
    if start[idx] == 0:
        start[idx] = 1
    else:
        start[idx] = 0


result = 2 ** 31 - 1
temp_start = start[:]

# 첫번째를 뒤집은 경우
do_flip(0)
flip_count = 1
for i in range(1, N):
    if start[i - 1] != end[i - 1]:
        do_flip(i)
        flip_count += 1
# print(f"flip_case: {flip_count}번 {start} -> {end}")
if start == end:
    result = flip_count

# 첫번째를 뒤집지않은 경우
start = temp_start  # 시작 문자열 복구
flip_count = 0
for i in range(1, N):
    if start[i - 1] != end[i - 1]:
        do_flip(i)
        flip_count += 1
# print(f"non_flip_case: {flip_count}번 {start} -> {end}")
if start == end and flip_count < result:
    result = flip_count

if result == 2 ** 31 - 1:
    print(-1)
else:
    print(result)
