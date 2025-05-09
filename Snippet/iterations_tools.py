target = [1, 1, 2, 3]
print(f"사용된 리스트: {target}")


def get_permutations(p):
    """
    대상 배열 특정 길이의 모든 순열을 확보
    순열: 순서가 존재함. [1, 2] <-> [2, 1] 을 서로 다른것으로 취급
    """

    result = set()
    visited = [False for _ in range(len(p))]
    target_len = len(p) // 2

    def back_track(curr):
        if len(curr) == target_len:  # 원하는 길이를 여기 조건에서 제어가능 ex) 전체길이의 절반일때 len(p) // 2
            result.add(tuple(curr))
            return

        for i in range(len(p)):
            if not visited[i]:
                visited[i] = True
                back_track(curr + [p[i]])
                visited[i] = False

    back_track([])

    return list(result)


print(f"순열 확보 결과: {get_permutations(target)}")


def get_combinations(p):
    """
    대상 배열의 특정 길이의 모든 조합을 확보
    조합: 순서가 존재하지않고 구성요소의 종류를 고려함.
    """
    result = set()
    target_len = len(p) // 2

    def dfs(start, combo):
        if len(combo) == target_len and tuple(combo) not in result:
            result.add(tuple(combo))
            return

        for i in range(start, len(p)):
            dfs(i + 1, combo + [p[i]])

    dfs(0, [])

    return result


print(f"조합 확보 결과: {get_combinations(target)}")
