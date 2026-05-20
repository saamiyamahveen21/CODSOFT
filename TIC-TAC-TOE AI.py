import math
import random

HUMAN = "X"
AI = "O"
EMPTY = " "

# ---------------- BOARD ----------------
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()

# ---------------- GAME CHECKS ----------------
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)

# ---------------- MINIMAX ----------------
def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best_score = min(best_score, score)

        return best_score

# ---------------- AI MOVE (DIFFICULTY SYSTEM) ----------------
def best_move(board, difficulty):
    moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

    # 🟢 EASY: random move
    if difficulty == "easy":
        return random.choice(moves)

    # 🟡 MEDIUM: 50% random, 50% smart
    if difficulty == "medium":
        if random.random() < 0.5:
            return random.choice(moves)

    # 🔴 HARD: Minimax optimal move
    best_score = -math.inf
    move = None

    for i, j in moves:
        board[i][j] = AI
        score = minimax(board, False)
        board[i][j] = EMPTY

        if score > best_score:
            best_score = score
            move = (i, j)

    return move

# ---------------- SAFE INPUT ----------------
def get_human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("❌ Enter values between 0 and 2!")
                continue

            if board[row][col] != EMPTY:
                print("❌ Cell already taken!")
                continue

            return row, col

        except ValueError:
            print("❌ Please enter numbers only!")

# ---------------- GAME LOOP ----------------
def play():
    while True:
        board = create_board()

        print("\n🎮 TIC-TAC-TOE AI (Minimax)")
        print("You are X | AI is O\n")

        # Difficulty selection
        print("Choose Difficulty Level:")
        print("1 - Easy 🟢")
        print("2 - Medium 🟡")
        print("3 - Hard 🔴")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            difficulty = "easy"
        elif choice == "2":
            difficulty = "medium"
        else:
            difficulty = "hard"

        print(f"\nYou selected: {difficulty.upper()}\n")

        # GAME LOOP
        while True:
            print_board(board)

            # HUMAN TURN
            row, col = get_human_move(board)
            board[row][col] = HUMAN

            if check_winner(board):
                print_board(board)
                print("🎉 You Win!")
                break

            if is_draw(board):
                print_board(board)
                print("😐 Draw!")
                break

            # AI TURN
            print("🤖 AI is thinking...")
            move = best_move(board, difficulty)

            if move:
                board[move[0]][move[1]] = AI

            if check_winner(board):
                print_board(board)
                print("🤖 AI Wins!")
                break

            if is_draw(board):
                print_board(board)
                print("😐 Draw!")
                break

        # 🔁 PLAY AGAIN OPTION
        again = input("\n🔁 Do you want to play again? (y/n): ").lower()

        if again != "y":
            print("\n👋 Thanks for playing!")
            break

# ---------------- START GAME ----------------
if __name__ == "__main__":
    play()