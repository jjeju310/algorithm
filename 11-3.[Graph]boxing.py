def solution(n, results):
    answer = 0
    board = [[0]*n for _ in range(n)]

    for b, c in results:
        board[b-1][c-1] = 1  # 이긴 것 세팅
        board[c-1][b-1] = -1  # 진 것 세팅
    '''
    board = 
    [
    [0, 1, 0, 0, 0], 
    [-1, 0,-1,-1, 1], 
    [0, 1, 0, -1, 0], 
    [0, 1, 1, 0, 0], 
    [0,-1, 0, 0, 0]
    ]
    '''
    for a in range(n):  # k = a
        for b in range(n):  # i = b
            for c in range(n):  # j = c
                if b == c or board[b][c] == 1:  # 자기끼리 or 이긴 경우
                    continue

                #  중간에 낀 애들
                if board[b][a] == board[a][c] == 1:  # ex. b > a, a > c 이면 (b,c) 말고 나머지 (c,b) 및 (a,b) (c,a) 는 -1
                    board[b][c] = 1
                    board[c][b] = board[a][b] = board[c][a] = -1

    print(f'updated board: {board}')
    '''
    updated board:
    [
    [0, 1,  0,  0, 1], 
    [-1, 0, -1, -1, 1], 
    [0,  1,  0,  -1, 1], 
    [0,  1,  1,  0,  1], 
    [-1, -1, -1, -1, 0]
    ]
    '''
    # 순위 확실한 애들 판단
    for row in board:
        if row.count(0) == 1:  # 이기고 진게 확실한 애들(지고 이긴 여부가 모든 애들하고 확실하게 있는 애)만 더해줌
            answer += 1

    return answer


def main():
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    solution(n, results)


if __name__ == "__main__":
    main()