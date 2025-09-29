"""
밑바닥 배열부터 1차원 배열을 만들어 검사
"""

H, W = map(int, input().split())
height = list(map(int, input().split()))
lowest = min(height) + 1  # 검사를 시작할 높이

total_rain = 0
for h in range(lowest, H + 1):  # 높이 별로 검사
    walls = [True if height[i] >= h else False for i in range(W)]
    for i in range(W-1):
        if walls[i] and not walls[i+1]:
            count = 0
            is_complete = False
            for j in range(i+1, W):
                if not walls[j]:
                    count += 1
                elif walls[j]:
                    is_complete = True
                    break

            if is_complete:
                total_rain += count

print(total_rain)