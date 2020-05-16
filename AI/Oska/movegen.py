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

# Prints board out for debugging purposes
def print_board(board):
    count = 0
    for row in board:
        print(row)

# Returns true if specific piece can move down left
def can_move_down_left(board, row, col):
    if (board[row + 1][col - 1] == '-'):
        return True
    else:
        return False

# Moves piece down left and updates board accoridingly
def move_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 1][col - 1] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

# Returns true if a jump down left if possible
def can_jump_down_left(board, row, col):
    curr_piece = board[row][col]
    # if not on second to last row and down left is blocked by enemy, and enemy can be jumped and col - 2 > 0
    if (row < len(board) - 2 and board[row + 1][col - 1] != curr_piece and (col - 2) >= 0 and board[row + 2][col - 2] == '-' ):
        return True
    else:
        return False

# Jumps down left and updates board accordingly
def jump_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 2][col - 2] = curr_piece
    copy_board[row + 1][col - 1] = '-'
    copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move down right
def can_move_down_right(board, row, col):
    if(board[row + 1][col] == '-'):
        return True
    else:
        return False

# moves piece down right and updates board accordinly 
def move_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 1][col] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

# returns true if jump can be made down right
def can_jump_down_right(board, row, col):
    curr_piece = board[row][col]
    # if not on second to last row and down right is blocked by enemy, and enemy can be jumped and col > length of two rows down
    if (row < len(board) - 2 and board[row + 1][col] != curr_piece and (col) < len(board[row + 2]) and board[row + 2][col] == '-' ):
        return True
    else:
        return False

# jumps down right and updates board accordinly 
def jump_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row + 2][col] = curr_piece
    copy_board[row + 1][col] = '-'
    copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move up right
def can_move_up_right(board, row, col):
    # space is open
    if (board[row - 1][col] == '-'):
        return True
    else:
        return False

# moves piece up right and updates board accordingly
def move_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 1][col] = curr_piece
    copy_board[row][col] = '-'
    return copy_board

# returns true if piece can jump up right
def can_jump_up_right(board, row, col):
    curr_piece = board[row][col]
    # If not on second row and the blocking piece is an enemy, a space is open to jump and the col is not out of range
    if (row > 1 and board[row - 1][col] != curr_piece and col < len(board[row - 2]) and board[row - 2][col] == '-'):
        return True
    else:
        return False

# jumps up right and updates board accordingly 
def jump_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 2][col] = curr_piece
    copy_board[row - 1][col] = '-'
    copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move up left
def can_move_up_left(board, row, col):
    # dealing with bottom half of the board
    if (len(board[row - 1]) < len(board[row])):
        # space is open
        if (board[row - 1][col - 1] == '-'):
            return True
        else:
            return False
    # dealing with top half of board
    else:
        # space is open
        if (board[row - 1][col] == '-'):
            return True
        else:
            return False


# moves up left and updates board accordingly 
def move_up_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with bottom half of board
    if (len(board[row - 1]) < len(board[row])):
        copy_board[row - 1][col - 1] = curr_piece
        copy_board[row][col] = '-'
    else:
        copy_board[row - 1][col] = curr_piece
        copy_board[row][col] = '-'

    return copy_board

# reutrns true if piece can jump up left
def can_jump_up_left(board, row, col):
    curr_piece = board[row][col]
    # if not on second row and up left is blocked by enemy, and enemy can be jumped and col - 2 > 0
    if (row > 1 and board[row - 1][col - 1] != curr_piece and (col - 2) >= 0 and board[row - 2][col - 2] == '-' ):
        return True
    else: 
        return False

# jumps up left and updates board accordingly 
def jump_up_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    copy_board[row - 2][col - 2] = curr_piece
    copy_board[row - 1][col - 1] = '-'
    copy_board[row][col] = '-'
    return copy_board

# performs all possible moves with curr_board, returns as a list of possible moves
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
                            moves.append(jump_down_right(curr_board, row, col))

                    # if the piece is in the top right corner of the board
                    elif (row == 0 and col == len(curr_board[0]) - 1):
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append(move_down_left(curr_board, row, col)) 

                        # Move down left is blocked, so checking if can jump
                        elif (can_jump_down_left(curr_board, row, col)):
                            moves.append(jump_down_left(curr_board, row, col))

                    # try all possible moves: down left, and down right for white piece
                    else:
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append(move_down_left(curr_board, row, col))
                        elif (can_jump_down_left(curr_board, row, col)):
                            moves.append(jump_down_left(curr_board, row, col))
                        
                        # make sure row below this is not out of range
                        # if piece is on far right side and row below is shorter skip this iteration
                        if (col == len(curr_board[row]) - 1 and len(curr_board[row + 1]) < len(curr_board[row])):
                            continue
                        else:
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
                        
                        # for up right, need to make sure col above is not out of range
                        # if piece is on far right side and above row is not smaller skip this iteration
                        if (col == len(curr_board[row]) - 1 and len(curr_board[row - 1]) < len(curr_board[row])):
                            continue
                        else:
                            if (can_move_up_right(curr_board, row, col)):
                                moves.append(move_up_right(curr_board, row, col))

                            elif (can_jump_up_right(curr_board, row, col)):
                                moves.append(jump_up_right(curr_board, row, col))

    # convert all moves back to format given
    for board in moves:
        final_moves.append(convert_back(board))


    return final_moves


x = movegen( [ "-----", 
                "----",
                 "---",
                 "--" ,
                 "--b", 
                "----", 
                "-----"], 'b')
for i in x:
    print_board(i)
    print()
