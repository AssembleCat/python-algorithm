arr = [1, 2, 3]


def permutations(target_len, arr):
    result = []
    visited = [False for _ in range(len(arr))]

    def generate(temp_list):
        if len(temp_list) == target_len:
            result.append(temp_list[:])
            return

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                temp_list.append(arr[i])
                generate(temp_list[:])
                temp_list.pop()
                visited[i] = False

    generate([])
    return result


def combinations(target_len, arr):
    result = []

    def generate(temp_list, start):
        if len(temp_list) == target_len:
            result.append(temp_list[:])
            return

        for i in range(start, len(arr)):
            temp_list.append(arr[i])
            generate(temp_list[:], i + 1)
            temp_list.pop()

    generate([], 0)
    return result


permute = permutations(len(arr), arr)
print(permute)
combo = combinations(2, arr)
print(combo)
