from collections import defaultdict

s, p = map(int, input().split())
dna = input().strip()  # .strip()으로 개행 문자 제거
min_req = list(map(int, input().split()))

# 각 문자에 대한 최소 요구 개수와 현재 윈도우의 문자 개수를 저장
req_map = {'A': min_req[0], 'C': min_req[1], 'G': min_req[2], 'T': min_req[3]}
my_count = defaultdict(int)

count = 0


# 유효성 검사 함수
def is_passwordable():
    # req_map의 모든 키(A, C, G, T)에 대해 조건을 만족하는지 확인
    for char, req_num in req_map.items():
        if my_count[char] < req_num:
            return False
    return True


# 1. 초기 윈도우 설정 (0부터 p-1까지)
for i in range(p):
    my_count[dna[i]] += 1

# 2. 초기 윈도우에 대한 유효성 검사
if is_passwordable():
    count += 1

# 3. 슬라이딩 윈도우 시작 (한 칸씩 이동하며 검사)
for i in range(p, s):
    # 맨 앞 문자 제거 (윈도우에서 빠져나가는 문자)
    my_count[dna[i - p]] -= 1

    # 맨 뒤 문자 추가 (윈도우에 새로 들어오는 문자)
    my_count[dna[i]] += 1

    # 새로 만들어진 윈도우에 대한 유효성 검사
    if is_passwordable():
        count += 1

print(count)