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
    # dealing with top half of board
    if (row < len(board) - 1 and len(board[row + 1]) < len(board[row])):
        # if piece is on far left
        if (col == 0):
            return False
        elif (board[row + 1][col - 1] == '-'):
            return True
        else:
            return False
    # dealing with bottom half of board
    else:
        if (row == len(board) - 1):
            return False
        # space is open 
        if (board[row + 1][col] == '-'):
            return True
        else:
            return False

# Moves piece down left and updates board accoridingly
def move_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with top half of board
    if (len(board[row + 1]) < len(board[row])):
        copy_board[row + 1][col - 1] = curr_piece
        copy_board[row][col] = '-'
    # dealing with bottom half
    else:
        copy_board[row + 1][col] = curr_piece
        copy_board[row][col] = '-'
    return copy_board

# Returns true if a jump down left if possible
def can_jump_down_left(board, row, col):
    curr_piece = board[row][col]
    # dealing with top half of board
    if (row < len(board) - 2 and len(board[row + 1]) < len(board[row])):
 
        # jump is going to cross the middle section
        if (len(board[row + 2]) == len(board[row])):
            # if on left side
            if (col == 0):
                return False
            # if down left blocked and can be jumped
            elif (board[row + 1][col - 1] != curr_piece and board[row + 2][col - 1] == '-'):
                return True
            else:
                return False
        # if piece would go out of bounds checking
        elif (col - 2 < 0):
            return False
        # if not on second to last row and down left is blocked by enemy, and enemy can be jumped and col - 2 > 0
        elif (board[row + 1][col - 1] != curr_piece and board[row + 2][col - 2] == '-' ):
            return True
        else:
            return False
    # dealing with the bottom half of the board
    else:
        if (row < len(board) - 2 and board[row + 1][col] != curr_piece and board[row + 2][col] == '-'):
            return True
        else:
            return False
        

# Jumps down left and updates board accordingly
def jump_down_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with jump accross middle of board
    if (len(board[row + 2]) == len(board[row])):
        copy_board[row + 2][col - 1] = curr_piece
        copy_board[row + 1][col - 1] = '-'
        copy_board[row][col] = '-'
    # dealing with top of board
    elif(len(board[row + 1]) < len(board[row])):
        copy_board[row + 2][col - 2] = curr_piece
        copy_board[row + 1][col - 1] = '-'
        copy_board[row][col] = '-'
    # dealing with bottom half
    else:
        copy_board[row + 2][col] = curr_piece
        copy_board[row + 1][col] = '-'
        copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move down right
def can_move_down_right(board, row, col):
    # dealing with top half of board
    if (row < len(board) - 1 and len(board[row + 1]) < len(board[row])):
        # if piece is on far right
        if (col == len(board[row]) - 1):
            return False
        # if the space is open
        elif(board[row + 1][col] == '-'):
            return True
        else:
            return False
    # dealing with the bottom half of the board
    else:
        if (row == len(board) - 1):
            return False
        # if space is open
        if(board[row + 1][col + 1] == '-'):
            return True
        else:
            return False

# moves piece down right and updates board accordinly 
def move_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with top half of boared
    if (len(board[row + 1]) < len(board[row])): 
        copy_board[row + 1][col] = curr_piece
        copy_board[row][col] = '-'
    # dealing with bottom half of board
    else:
        copy_board[row + 1][col + 1] = curr_piece
        copy_board[row][col] = '-'
    return copy_board

# returns true if jump can be made down right
def can_jump_down_right(board, row, col):
    curr_piece = board[row][col]
    # dealing with top half of board
    if (row < len(board) - 2 and len(board[row + 1]) < len(board[row])):
        # jump is going to cross the middle section
        if (len(board[row + 2]) == len(board[row])):
            # if on right side
            if (col == len(board[row]) - 1):
                return False
            # if down right blocked by enemy and enemy can be jumped
            elif (board[row + 1][col] != curr_piece and board[row + 2][col + 1] == '-'):
                return True
            else:
                return False
        # piece will be out of bounds
        elif (col > len(board[row + 2]) - 1):
            return False
        # if down right is blocked by enemy, and enemy can be jumped 
        elif (board[row + 1][col] != curr_piece and board[row + 2][col] == '-' ):
            return True
        else:
            return False
    # dealing with bottom half of board
    else:
        # if row is not second to last and down right is blocked and can be jumped
        if (row < len(board) - 2 and board[row + 1][col + 1] != curr_piece and board[row + 2][col + 2] == '-'):
            return True
        else:
            return False

# jumps down right and updates board accordinly 
def jump_down_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with jump across middle of board
    if (len(board[row + 2]) == len(board[row])):
        copy_board[row + 2][col + 1] = curr_piece
        copy_board[row + 1][col] = '-'
        copy_board[row][col] = '-'

    # delaing with top half 
    elif (len(board[row + 1]) < len(board[row])):
        copy_board[row + 2][col] = curr_piece
        copy_board[row + 1][col] = '-'
        copy_board[row][col] = '-'
    
    # dealing with bottom half
    else:
        copy_board[row + 2][col + 2] = curr_piece
        copy_board[row + 1][col + 1] = '-'
        copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move up right
def can_move_up_right(board, row, col):
    # dealing with bottom half of board
    if (row > 0 and len(board[row - 1]) < len(board[row])):
        # if piece is on far right
        if (col == len(board[row]) - 1):
            return False
        # space is open
        elif (board[row - 1][col] == '-'):
            return True
        else:
            return False

    # dealing with top half of board
    else:
        if (row == 0):
            return False
        # space is open
        if (board[row - 1][col + 1] == '-'):
            return True
        else:
            return False

# moves piece up right and updates board accordingly
def move_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with bottom half of board
    if (row > 0 and len(board[row - 1]) < len(board[row])):
        copy_board[row - 1][col] = curr_piece
        copy_board[row][col] = '-'
    else:
        copy_board[row - 1][col + 1] = curr_piece
        copy_board[row][col] = '-'
    return copy_board

# returns true if piece can jump up right
def can_jump_up_right(board, row, col):
    curr_piece = board[row][col]
    # if dealing with bottom half of board
    if (row > 1 and len(board[row - 1]) < len(board[row])):
        # if jump is going to cross the middle section
        if (len(board[row - 2]) == len(board[row])):
            # if on the right side
            if (col == len(board[row]) - 1):
                return False
            # if up right blocked and space can be jumped 
            if (board[row - 1][col] != curr_piece and board[row - 2][col + 1] == '-'):
                return True
            else:
                return False
        # piece will be out of bounds
        elif (col > len(board[row - 2]) - 1):
            return False
        # If not on second row and the blocking piece is an enemy, a space is open to jump
        elif (row > 1 and board[row - 1][col] != curr_piece and board[row - 2][col] == '-'):
            return True 
        else:
            return False

    # dealing with top half of board
    else:
        # if up right is blocked by enemy and can be jumped
        if (row > 1 and board[row - 1][col + 1] != curr_piece and board[row - 2][col + 2] == '-'):
            return True
        else:
            return False

# jumps up right and updates board accordingly 
def jump_up_right(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col]
    # dealing with jump across middle of board
    if (len(board[row - 2]) == len(board[row])):
        copy_board[row - 2][col + 1] = curr_piece
        copy_board[row - 1][col] = '-'
        copy_board[row][col] = '-'
    # dealing with bottom half of board
    elif (len(board[row - 1]) < len(board[row])):
        copy_board[row - 2][col] = curr_piece
        copy_board[row - 1][col] = '-'
        copy_board[row][col] = '-'
    # dealing with top half
    else:
        copy_board[row - 2][col + 2] = curr_piece
        copy_board[row - 1][col + 1] = '-'
        copy_board[row][col] = '-'
    return copy_board

# returns true if piece can move up left
def can_move_up_left(board, row, col):
    # dealing with bottom half of the board
    if (row > 0 and len(board[row - 1]) < len(board[row])):
        # if piece is on far left
        if (col == 0):
            return False
        # space is open
        if (board[row - 1][col - 1] == '-'):
            return True
        else:
            return False
    # dealing with top half of board
    else:
        if(row == 0):
            return False
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
    if (row > 0 and len(board[row - 1]) < len(board[row])):
        copy_board[row - 1][col - 1] = curr_piece
        copy_board[row][col] = '-'
    else:
        copy_board[row - 1][col] = curr_piece
        copy_board[row][col] = '-'

    return copy_board

# reutrns true if piece can jump up left
def can_jump_up_left(board, row, col):
    curr_piece = board[row][col]
    # if dealing with the bottom half of the board
    if (row > 0 and len(board[row - 1]) < len(board[row])):
        # if row is not the first or second and jump is going to cross the middle section
        # if on far left
        if (col == 0):
            return False
        elif (row > 1 and len(board[row - 2]) == len(board[row])):
            # if up left is blocked by enemy and enemy can be jumped
            if (board[row - 1][col - 1] != curr_piece and board[row - 2][col - 1] == '-'):
                return True
            else:
                return False
        # if piece will be out of bounds
        if (col - 2 < 0):
            return False
        # if up left is blocked by enemy, and enemy can be jumped and not jumping out of bounds
        elif (board[row - 1][col - 1] != curr_piece and (col - 2) >= 0 and board[row - 2][col - 2] == '-' ):
            return True
        else: 
            return False
    # dealing with the top half of the board
    else:
        # if row is not second and up left is blocked by enemy, and can be jumped 
        if (row > 1 and board[row - 1][col] != curr_piece and board[row - 2][col] == '-'):
            return True
        else:
            return False 

# jumps up left and updates board accordingly 
def jump_up_left(board, row, col):
    copy_board = [row[:] for row in board]
    curr_piece = copy_board[row][col] 
    # dealing with a jump across the board
    if (len(board[row - 2]) == len(board[row])):
        copy_board[row - 2][col - 1] = curr_piece
        copy_board[row - 1][col - 1] = '-'
        copy_board[row][col] = '-'
    # if dealing with bottom half of board
    elif (len(board[row - 1]) < len(board[row])):
        copy_board[row - 2][col - 2] = curr_piece
        copy_board[row - 1][col - 1] = '-'
        copy_board[row][col] = '-'
    # dealing with the top half of board
    else:
        copy_board[row - 2][col] = curr_piece
        copy_board[row - 1][col] = '-'
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
                    
                    # check up left move and jump
                    if (can_move_up_left(curr_board, row, col)):
                        moves.append(move_up_left(curr_board, row, col))

                    elif (can_jump_up_left(curr_board, row, col)):
                        moves.append(jump_up_left(curr_board, row, col))
                    
                    # check up right move and jump
                    if (can_move_up_right(curr_board, row, col)):
                        moves.append(move_up_right(curr_board, row, col))

                    elif (can_jump_up_right(curr_board, row, col)):
                        moves.append(jump_up_right(curr_board, row, col))

    # convert all moves back to format given
    for board in moves:
        final_moves.append(convert_back(board))

    if (len(final_moves) != 0):
        return final_moves
    else:
        return curr_board

# x = movegen( [ "bbbbb", 
#                 "----",
#                  "---",
#                  "--" ,
#                  "---", 
#                 "----", 
#                 "-----"], 'b')
# x = movegen( [ "-----", 
#                 "----",
#                  "---",
#                  "--" ,
#                  "---", 
#                 "wwww", 
#                 "bbbbb"], 'w')

# x = movegen( [ "-----", 
#                 "----",
#                  "www",
#                  "bb" ,
#                  "---", 
#                 "----", 
#                 "-----"], 'w')
# x = movegen( [ "-----", 
#                 "----",
#                  "---",
#                  "ww" ,
#                  "bbb", 
#                 "----", 
#                 "-----"], 'b')
x = movegen( [ "-----", 
                "wwww",
                 "bbb",
                 "--" ,
                 "---", 
                "----", 
                "-----"], 'b')
# x = movegen( [ "-----", 
#                 "----",
#                  "---",
#                  "--" ,
#                  "www", 
#                 "bbbb", 
#                 "-----"], 'w')

# x = movegen( [ "wwwww", 
#                 "----",
#                  "---",
#                  "--" ,
#                  "---", 
#                 "----", 
#                 "bbbbb"], 'b')

# x = movegen( [ "wwwww", 
#                 "----",
#                  "---",
#                  "--" ,
#                  "---", 
#                 "----", 
#                 "bbbbb"], 'w')


for i in x:
    print_board(i)
    print()
