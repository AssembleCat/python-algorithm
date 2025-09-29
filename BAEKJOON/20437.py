from collections import defaultdict

T = int(input())

for _ in range(T):
    al_dict = defaultdict(list)
    W = input()
    K = int(input())

    for i, w in enumerate(W):
        al_dict[w].append(i)

    # 문자열을 K개 이상 포함하고 있는지 확인
    is_valid = False
    for _, pos_list in al_dict.items():
        if len(pos_list) >= K:
            is_valid = True
            break

    if not is_valid:
        print(-1)
        continue

    # k개 포함하는 가장 짧은 문자열
    # k개 포함하는 가장 긴 문자열
    shortest, longest = 2 ** 31 - 1, 0
    for a, pos_list in al_dict.items():
        if len(pos_list) < K:
            continue
        for i in range(len(pos_list) - K + 1):
            length = pos_list[i + K - 1] - pos_list[i]
            if length < shortest:
                shortest = length
            if length > longest:
                longest = length

    print(shortest + 1, longest + 1)
