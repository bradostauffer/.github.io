# Convert initial list of strings to 2d list of chars
def convert_to_2d(board):
    return ([list(row) for row in board])

# Convert 2d list of chars back to list of strings
def convert_back(board):
    tmp_str = ""
    converted_board = []
    for row in board:
        tmp_str.join(row)
        converted_board.append(tmp_str[:].join(row))
    return converted_board

def print_board(board):
    count = 0
    for row in board:
        if (count == 0 or count == len(board) - 1):
            print(row)
            count = count + 1
        else:
            print("  ", row)
            count = count + 1


def can_move_down_left(board, row, col):
    if (board[row + 1][col - 1] == '-'):
        return True
    else:
        return False

def move_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 1][col - 1] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

def can_jump_down_left(board, row, col):
    curr_piece = board[row][col]
    # if down left is blocked by enemy, and enemy can be jumped and col - 2 > 0
    if (board[row + 1][col - 1] != curr_piece and (col - 2) >= 0 and board[row + 2][col - 2] == '-' ):
        return True
    else:
        return False

def jump_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 2][col - 2] = curr_piece
    copy_board[row + 1][col - 1] = '-'
    copy_board[row][col] = '-'
    return copy_board


def can_move_down_right(board, row, col):
    if(board[row + 1][col] == '-'):
        return True
    else:
        return False

def move_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 1][col] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

def can_jump_down_right(board, row, col):
    curr_piece = board[row][col]
    # if down right is blocked by enemy, and enemy can be jumped and col > length of two rows down
    if (board[row + 1][col] != curr_piece and (col) < len(board[row + 2]) and board[row + 2][col] == '-' ):
        return True
    else:
        return False

def jump_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 2][col] = curr_piece
    copy_board[row + 1][col] = '-'
    copy_board[row][col] = '-'
    return copy_board

def can_move_up_right(board, row, col):
    # space is open
    if (board[row - 1][col] == '-'):
        return True
    else:
        return False
def move_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 1][col] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

def can_jump_up_right(board, row, col):
    curr_piece = board[row][col]
    # If the blocking piece is an enemy, a space is open to jump and the col is not out of range
    if (board[row - 1][col] != curr_piece and col < len(board[row - 2]) and board[row - 2][col] == '-'):
        return True
    else:
        return False

def jump_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 2][col] = curr_piece
    copy_board[row - 1][col] = '-'
    copy_board[row][col] = '-'
    return copy_board

def can_move_up_left(board, row, col):
    # space is open
    if (board[row - 1][col - 1] == '-'):
        return True
    else:
        return False

def move_up_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 1][col - 1] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

def can_jump_up_left(board, row, col):
    curr_piece = board[row][col]
    # if up left is blocked by enemy, and enemy can be jumped and col - 2 > 0
    if (board[row - 1][col - 1] != curr_piece and (col - 2) >= 0 and board[row - 2][col - 2] == '-' ):
        return True
    else: 
        return False

def jump_up_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 2][col - 2] = curr_piece
    copy_board[row - 1][col - 1] = '-'
    copy_board[row][col] = '-'
    return copy_board


# def main():
#     f = convert_to_2d( ["wwww", 
#                         "bbb", 
#                          "--", 
#                         "b-w", 
#                         "bbbb"])
#     print_board(f)
#     print()
#     if(can_move_up_left(f, 4, 3)):
#         g = move_up_left(f, 4, 3)
#         print_board(g)
#     else:
#         if(can_jump_up_left(f, 4, 3)):
#             g = jump_up_left(f, 4, 3)
#             print_board(g)
#     # elif (can_jump_down_left(f, 0, 3)):
#     #     g = jump_down_left(f, 0, 3)
#     #     print_board(g)
     
# main()

def movegen(curr_board, player):
    curr_board = convert_to_2d(curr_board)
    moves = []
    final_moves = []

    for row in range(len(curr_board)):
        for col in range(len(curr_board[row])):
            curr_piece = curr_board[row][col]

            # the piece we found is going
            if (curr_piece == player):
                # Check the possible white moves 
                if (curr_piece == 'w'):

                    # if the piece is in the top left corner of the board
                    if (row == 0 and col == 0):
                        if (can_move_down_right(curr_board, row, col)):
                            moves.append(move_down_right(curr_board, row, col))

                        # Move down right is blocked, so checking if can jump
                        elif (can_jump_down_right(curr_board, row, col)):
                            print()

                    # if the piece is in the top right corner of the board
                    elif (row == 0 and col == len(curr_board[0]) - 1):
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append(move_down_left(curr_board, row, col)) 

                        # Move down left is blocked, so checking if can jump
                        elif (can_jump_down_left(curr_board, row, col)):
                            print()

                    # try all possible moves: down left, and down right for white piece
                    else:
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append(move_down_left(curr_board, row, col))
                        elif (can_jump_down_left(curr_board, row, col)):
                            moves.append(jump_down_left(curr_board, row, col))
                        if (can_move_down_right(curr_board, row, col)):
                            moves.append(move_down_right(curr_board, row, col))
                        elif (can_jump_down_right(curr_board, row, col)):
                            moves.append(jump_down_right(curr_board, row, col))

                # Check the possible black moves
                elif (curr_piece == 'b'):
                    
                    # If the piece is at the bottom left corner of the board
                    if (row == len(curr_board) - 1 and col == 0):

                        # If the piece can move up and right
                        if (can_move_up_right(curr_board, row, col)):
                            moves.append(move_up_right(curr_board, row, col))

                        # Else if you can jump the blocking piece
                        elif (can_jump_up_right(curr_board, row, col)):
                            moves.append(jump_up_right(curr_board, row, col))

                    # If the piece is at the bottom right corner of the board
                    elif (row == len(curr_board) - 1 and col == len(curr_board[0]) - 1): 

                        if (can_move_up_left(curr_board, row, col)):
                            moves.append(move_up_left(curr_board, row, col))

                        # Else if you can jump the blocking piece
                        elif (can_jump_up_left(curr_board, row, col)):
                            moves.append(jump_up_left(curr_board, row, col))
                    
                    # try all possible moves: up left, up right, for black piece 
                    else:
                        if (can_move_up_left(curr_board, row, col)):
                            moves.append(move_up_left(curr_board, row, col))

                        elif (can_jump_up_left(curr_board, row, col)):
                            moves.append(jump_up_left(curr_board, row, col))

                        if (can_move_up_right(curr_board, row, col)):
                            moves.append(move_up_right(curr_board, row, col))

                        elif (can_jump_up_right(curr_board, row, col)):
                            moves.append(jump_up_right(curr_board, row, col))

    # convert all moves back to format given
    for board in moves:
        final_moves.append(convert_back(board))


    return final_moves

# return 3-tuple with (board, num_white, num_black)
def player_counter(board):

# Return percent of players pieces in last row
def percent_in_last_row(board, player_color):


# Return static board score
def static_eval(board, player_color, curr_player, num_white, num_black):

# returns tuple of (board, score) for the next best move for 
def minimax(curr_state, player_color, curr_player, depth, depth_counter):
x = movegen( ["wwww", 
                "bbb", 
                "--", 
                "www", 
                "bbbb"], 'b')
for i in x:
    print_board(i)
    print()
    print()

