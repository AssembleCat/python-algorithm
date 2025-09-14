n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi = map(int, input().split())

minimum = 1_000_000_000
maximum = -1_000_000_000

def dfs(index, current, plus, minus, multi):
    global minimum, maximum
    if index == len(numbers):
        minimum = min(minimum, current)
        maximum = max(maximum, current)
        return 
    
    next_number = numbers[index]

    if plus > 0:
        dfs(index + 1, current + next_number, plus - 1, minus, multi)
    if minus > 0:
        dfs(index + 1, current - next_number, plus, minus - 1, multi)
    if multi > 0:
        dfs(index + 1, current * next_number, plus, minus, multi - 1)

dfs(1, numbers[0], plus, minus, multi)

print(minimum, maximum)
