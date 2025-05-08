"""
1. 사용가능한 연산자들을 담은 배열 생성
2. 배열을 통해 가능한 모든 연산 조합 생성
3. 숫자와 연산자 조합을 하나의 배열로 합침
4. 모든 경우의 수 연산, 최소/최대 생성
"""
N = int(input())
numbers = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))
op = ['+'] * plus + ['-'] * minus + ['*'] * mul + ['//'] * div
max_result, min_result = -1000000000, 1000000000


def get_op_combination(operations):
    comb = set()
    n = len(operations)
    visited = [False] * n

    def back_trank(elements):
        if len(elements) == n:
            comb.add(tuple(elements))
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                back_trank(elements + [operations[i]])
                visited[i] = False

    back_trank([])
    return list(comb)


def calculate(operations):
    global max_result, min_result
    result = numbers[0]
    for idx, operation in enumerate(operations):
        if operation == '+':
            result += numbers[idx + 1]
        elif operation == '-':
            result -= numbers[idx + 1]
        elif operation == '*':
            result *= numbers[idx + 1]
        elif operation == '//':
            if result < 0:
                result = -(-result // numbers[idx + 1])
            else:
                result //= numbers[idx + 1]
    if result > max_result:
        max_result = result
    if result < min_result:
        min_result = result


op_combs = get_op_combination(op)
for op_comb in op_combs:
    calculate(op_comb)

print(max_result)
print(min_result)
