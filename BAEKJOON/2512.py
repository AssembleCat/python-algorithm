N = int(input())
requests = list(map(int, input().split()))
M = int(input())

if sum(requests) <= M:  # 모든 예산이 지급가능하면 전체예산 출력
    print(max(requests))
else:
    left = 0
    right = max(requests)

    while left <= right:
        curr_amount = 0  # 지급액
        mid = (left + right) // 2
        for request in requests:
            if request <= mid:
                curr_amount += request
            else:
                curr_amount += mid

        if curr_amount > M:
            right = mid - 1
        else:
            left = mid + 1

    print(right)
