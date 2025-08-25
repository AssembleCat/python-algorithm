bucket, score = [], 0
def insert_doll(doll):
    global bucket, score
    if not bucket:
        bucket.append(doll)
    elif bucket[-1] == doll:
        score += 2
        bucket = bucket[:-1]
    else:
        bucket.append(doll)


def pick_doll(line, board):
    for row, b in enumerate(board):
        if b[line] != 0:
            doll = b[line]
            board[row][line] = 0
            return doll
    return None


def solution(board, moves):
    # moves의 각 요소마다 가장 높은 "행"의 값을 뽑아서 별도의 리스트에 삽입해야함.
    ## 리스트에 삽입전에 리스트의 가장 상위 값이 지금 넣으려는 값과 같으면 넣지않고 score를 상승시킴. -> 리스트에 어떻게 삽입하지?
    ### 점수는 사라진 인형의 갯수이니 무조건 짝수로 올라가야함.
    for move in moves:
        line = move - 1  # 실제 접근 index
        doll = pick_doll(line, board)
        #print(f"선택된 인형: {doll}")
        if doll is None:
            continue
        insert_doll(doll)
        #print(f"현재 버킷: {bucket}")

    #print(score)
    return score


if __name__ == '__main__':
    _board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    _moves = [1, 5, 3, 5, 1, 2, 1, 4]
    solution(_board, _moves)
