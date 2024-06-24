"""
Домашнее задание №17: Лямбда-функции
Задание №2
Написать игру крестики-нолики
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Проверка всех строк, столбцов и диагоналей на выигрыш
    for row in board:
        if all(s == player for s in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(all(cell in ["X", "O"] for cell in row) for row in board)

def make_move(board, player, move):
    moves = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    row, col = moves[move]
    if board[row][col] not in ["X", "O"]:
        board[row][col] = player
        return True
    else:
        return False

def main():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ходит игрок {current_player}")
        
        try:
            move = int(input("Введите номер ячейки (от 1 до 9): "))
        except ValueError:
            print("Пожалуйста, введите число от 1 до 9.")
            continue

        if move not in range(1, 10):
            print("Пожалуйста, введите допустимое значение от 1 до 9.")
            continue

        if not make_move(board, current_player, move):
            print("Эта клетка уже занята. Попробуйте еще раз.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} выиграл!")
            break

        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
