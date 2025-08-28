from aoc import DIAG_DIRS, read_input

lines = read_input()
wins = {1: 0, 2: 0, 3: 0}


def check_winner(board, player):
    for start_y, row in enumerate(board):
        for start_x, p in enumerate(row):
            if p != player:
                continue
            for dx, dy in DIAG_DIRS:
                x, y = start_x, start_y
                count = 0
                while 0 <= x < 7 and 0 <= y < 7 and board[y][x] == player:
                    x, y = x + dx, y + dy
                    count += 1

                if count >= 4:
                    return True

    return False


for line in lines:
    moves = [int(n) - 1 for n in line]
    board = [[0] * 7 for _ in range(7)]

    player = 1
    for move in moves:
        row = 0
        while row < 7 and board[row][move] == 0:
            row += 1
        row -= 1
        board[row][move] = player

        if check_winner(board, player):
            wins[player] += 1
            break

        player = (player % 3) + 1

product = 1
for v in wins.values():
    product *= v
print(product)
