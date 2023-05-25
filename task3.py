def initialize_board():
   
    board = [['1','  ', '2', '  ','3'],
             ['4','  ', '5', '  ','6'],
             ['7','  ', '8', '  ','9']]

    return board

def display_board(board):
    print("------------     TIC TAC TOE    -------------")
    for row in board:
        print(' '.join(row))
    print("---------------------------------------------")

def get_player_symbols():
    player1_symbol='X'
    player2_symbol='Y'
   
    return player1_symbol, player2_symbol
   
   

def get_player_move(player_symbol, board):
    valid_move = False
    while not valid_move:
        move = input(f"{player_symbol}, Enter the index : ")
        if not move.isnumeric() or int(move) not in range(1, 10):
            print("Invalid move. Please Enter the other index (1-9):")
        else:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3 * 2
            if board[row][col] != 'X' and board[row][col] != 'O':
                valid_move = True
            else:
                print("Position already taken. Please Enter the other index:")
    board[row][col] = player_symbol
    return board

def check_win(board):
    # Check rows
    for row in board:
        if row[0] == row[2] == row[4]:
            return row[0]
    # Check columns
    for i in range(3):
        if board[0][i*2] == board[1][i*2] == board[2][i*2]:
            return board[0][i*2]
    # Check diagonals
    if board[0][0] == board[1][2] == board[2][4]:
        return board[0][0]
    if board[0][4] == board[1][2] == board[2][0]:
        return board[0][4]
    # Check for tie
    for row in board:
        if any(c.isdigit() for c in row):
            return None
    return 'Tie'

def play_game():

    board = initialize_board()
  
    player1_symbol, player2_symbol = get_player_symbols()
    current_player = 1
    winner = None
    while not winner:
        display_board(board)
       
        print('Player1_symbol : ', player1_symbol)
        print('Player2_symbol : ', player2_symbol)
        if current_player == 1:
            board = get_player_move(player1_symbol, board)
            current_player = 2
        else:
            board = get_player_move(player2_symbol, board)
            current_player = 1
        winner = check_win(board)
    display_board(board)
    if winner == 'Tie':
        print("Game is a tie!")
    else:
        if current_player==1:
            print("Player Y Won!!!")
        else:
            print("Player X Won!!!")
play_game()