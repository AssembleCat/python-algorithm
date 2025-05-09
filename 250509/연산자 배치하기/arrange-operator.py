n = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi = map(int, input().split())
operations = ['+'] * plus + ['-'] * minus + ['*'] * multi
minimum, maximum = 1000000000, -1000000000

def calculate(op_combo):
    global minimum, maximum
    result = numbers[0]
    for i in range(len(op_combo)):
        if op_combo[i] == '+':
            result += numbers[i+1]
        elif op_combo[i] == '-':
            result -= numbers[i+1]
        elif op_combo[i] == '*':
            result *= numbers[i+1]
    minimum = min(minimum, result)
    maximum = max(maximum, result)


def get_combinations():
    result = set()
    visited = [False for _ in range(len(operations))]
    
    def back_track(combo):
        if len(combo) == len(operations):
            result.add(tuple(combo))
            return
        
        for i in range(len(operations)):
            if not visited[i]:
                visited[i] = True
                back_track(combo + [operations[i]])
                visited[i] = False
    
    back_track([])
    
    return result

operations_combos = get_combinations()
for operations_combo in operations_combos:
    calculate(operations_combo)

print(minimum, maximum)