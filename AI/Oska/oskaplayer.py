import copy
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


def movegen(curr_state, player):
    curr_board = convert_to_2d(curr_state[0])
    num_white = curr_state[1]
    num_black = curr_state[2]
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
                            moves.append((move_down_right(curr_board, row, col), num_white, num_black))

                        # Move down right is blocked, so checking if can jump
                        elif (can_jump_down_right(curr_board, row, col)):
                            moves.append((jump_down_right(curr_board, row, col), num_white, num_black - 1))

                    # if the piece is in the top right corner of the board
                    elif (row == 0 and col == len(curr_board[0]) - 1):
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append((move_down_left(curr_board, row, col), num_white, num_black)) 

                        # Move down left is blocked, so checking if can jump
                        elif (can_jump_down_left(curr_board, row, col)):
                            moves.append((jump_down_left(curr_board, row, col), num_white, num_black - 1))

                    # try all possible moves: down left, and down right for white piece
                    else:
                        if (can_move_down_left(curr_board, row, col)):
                            moves.append((move_down_left(curr_board, row, col), num_white, num_black))
                        elif (can_jump_down_left(curr_board, row, col)):
                            moves.append((jump_down_left(curr_board, row, col), num_white, num_black - 1))
                        if (can_move_down_right(curr_board, row, col)):
                            moves.append((move_down_right(curr_board, row, col), num_white, num_black))
                        elif (can_jump_down_right(curr_board, row, col)):
                            moves.append((jump_down_right(curr_board, row, col), num_white, num_black - 1))

                # Check the possible black moves
                elif (curr_piece == 'b'):
                    
                    # If the piece is at the bottom left corner of the board
                    if (row == len(curr_board) - 1 and col == 0):

                        # If the piece can move up and right
                        if (can_move_up_right(curr_board, row, col)):
                            moves.append((move_up_right(curr_board, row, col), num_white, num_black))

                        # Else if you can jump the blocking piece
                        elif (can_jump_up_right(curr_board, row, col)):
                            moves.append((jump_up_right(curr_board, row, col), num_white - 1, num_black))

                    # If the piece is at the bottom right corner of the board
                    elif (row == len(curr_board) - 1 and col == len(curr_board[0]) - 1): 

                        if (can_move_up_left(curr_board, row, col)):
                            moves.append((move_up_left(curr_board, row, col), num_white, num_black))

                        # Else if you can jump the blocking piece
                        elif (can_jump_up_left(curr_board, row, col)):
                            moves.append((jump_up_left(curr_board, row, col), num_white - 1, num_black))
                    
                    # try all possible moves: up left, up right, for black piece 
                    else:
                        if (can_move_up_left(curr_board, row, col)):
                            moves.append((move_up_left(curr_board, row, col), num_white, num_black))

                        elif (can_jump_up_left(curr_board, row, col)):
                            moves.append((jump_up_left(curr_board, row, col), num_white - 1, num_black))

                        if (can_move_up_right(curr_board, row, col)):
                            moves.append((move_up_right(curr_board, row, col), num_white, num_black))

                        elif (can_jump_up_right(curr_board, row, col)):
                            moves.append((jump_up_right(curr_board, row, col), num_white - 1, num_black))

    # convert all moves back to format given
    for board in moves:
        final_moves.append((convert_back(board[0]), board[1], board[2]))

    if (len(final_moves) != 0):
        return final_moves
    else:
        final_moves.append((convert_back(curr_board), num_white, num_black))
        return final_moves

# return 3-tuple with (board, num_white, num_black)
def player_counter(board):
    white_count = 0
    black_count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            # piece is white
            if (board[row][col] == 'w'):
                white_count = white_count + 1
            # piece is black
            elif (board[row][col] == 'b'):
                black_count = black_count + 1

    return(board, white_count, black_count)


# Return percent of players pieces in last row
def percent_in_last_row(board, player_color, number_of_pieces):
    pieces_in_row = 0
    last_row = board[len(board) - 1]
    # if player if white, check the bottom row
    if (player_color == 'w'):
        for piece in last_row:
            if (piece == 'w'):
                pieces_in_row = pieces_in_row + 1

    # if player is black, check the top row
    elif (player_color == 'b'):
        for piece in board[0]:
            if (piece == 'b'):
                pieces_in_row = pieces_in_row + 1
    return (pieces_in_row/number_of_pieces)
# Returns true if the player has won
def has_won(board, player_color, number_of_white, number_of_black):
    # If the player is White
    if (player_color == 'w'):
    # if all opposing pieces are gone
        if(number_of_black == 0):
            return True        
        elif (number_of_white == 0):
            return False
        # if all of their pieces are in the bottom row
        elif (percent_in_last_row(board, player_color, number_of_white) == 1.0):
            return True
       
        else:
            return False
    # If the player is black
    elif (player_color == 'b'):
        # if all opposing pieces are gone
        if(number_of_white == 0):
            return True
        elif(number_of_black == 0):
            return False
        #if all of their pieces are in the top row
        elif (percent_in_last_row(board, player_color, number_of_black) == 1.0):
            return True
        
        else:
            return False

# Return static board score
# if either players win, the score is the total number of pieces (both black and white) that were on the board originally
# That way when the board gets larger my other heuristics do not falsely score higher
# Otherwise if there is no win, the board score:
# number of player pieces - number of opponent pieces + (percent player in opponents last row * win score) + (percent opponent in player last row * -win score)
# This way it addresses the posibiliy of winning by having all pieces of one color in the opposite players row. 
def static_eval(board, total_num_pieces, curr_player, num_white, num_black, user_color):
    
    # Rare case of a tie
    if(has_won(board, 'b', num_white, num_black) and has_won(board, 'w', num_white, num_black)):
        return 0
    # if user is white
    if (user_color == 'w'):
        # player is max and wins return positve 10 if won
        if (has_won(board, user_color, num_white, num_black)):
            return total_num_pieces
        # player is min and wins return - 10
        elif(has_won(board, 'b', num_white, num_black)):
            return -(total_num_pieces)
        # else, return num players pieces - num opponents pieces + percentage of players pieces in last row 
        else:
            return ((num_white - num_black) + (percent_in_last_row(board, 'w', num_white) * total_num_pieces ) + 
            (percent_in_last_row(board, 'b', num_black) * (-(total_num_pieces))))


    # user color is black
    else:
        # player is max and wins return positve 10
        if(has_won(board, user_color, num_white, num_black)):
            return total_num_pieces
        elif (has_won(board, 'w', num_white, num_black)):
            return -(total_num_pieces)
        # else, return num players pieces - num opponents pieces + percentage of players pieces in last row 
        else:
            return ((num_black - num_white) + (percent_in_last_row(board, 'b', num_black) * total_num_pieces ) + 
            (percent_in_last_row(board, 'w', num_white) * (-(total_num_pieces))))

             
# returns tuple of (board, score) for the next best move for
# function takes in the current state(board and number of each piece on that board), current players color, the current player (max or min), 
# the maximum depth, the current depth, and the user's color (the original user's color) 
def minimax(curr_state, player_color, curr_player, depth, depth_counter, user_color, total_num_pieces):
    # desired depth reached
    if (depth_counter == depth):
        return ((curr_state[0], static_eval(curr_state[0], total_num_pieces, curr_player, curr_state[1], curr_state[2], user_color)))

    # if current player is a max
    if (curr_player == "max"):
        moves = movegen(curr_state, player_color)
        best_score = ([], float("-inf"))
        score = ([], 0)
        for move in moves:
            # call minimax with opposite of player color
            # player is white, so call with min on black
            if (player_color == 'w'):
                score = minimax(move, 'b', 'min', depth, depth_counter + 1, user_color, total_num_pieces)
            # player is black so call with min on white
            else:
                score = minimax(move, 'w', 'min', depth, depth_counter + 1, user_color, total_num_pieces)
            # set best_score == to max between score and best_score
            if(score[1] > best_score[1]):
                tmp_board = move[0]
                tmp_score = score[1]
                best_score = (tmp_board[:], tmp_score)
        return best_score
    # if current player is min
    else:
        moves = movegen(curr_state, player_color)
        best_score = ([], float("inf"))
        score = ([], 0)
        for move in moves:
            #if player is white call max on black 
            if (player_color == 'w'):
                score = minimax(move, 'b', 'max', depth, depth_counter + 1, user_color, total_num_pieces)
            # if player is black call max on white
            else:
                score = minimax(move, 'w', 'max', depth, depth_counter + 1, user_color, total_num_pieces)
            
            # set best_score = min between best_score and score
            if (score[1] < best_score[1]):
                tmp_board = move[0]
                tmp_score = score[1]
                best_score = (tmp_board[:], tmp_score)
        return best_score

                
def oskaplayer(board, player_color, depth):
    curr_state = player_counter(board)
    next_state = minimax(curr_state, player_color, 'max', depth, 0, player_color, len(board[0]) * 2)
    return(next_state[0])

    


#print(oskaplayer(['--b----','------','-----','----','---','--','---','----','--w--','---b--','w------'],'w',4))
# print(oskaplayer(['-----', '----', '---', '--', '--w', 'w--b', '-----'], 'w', 8))
# print(has_won(["wbbw", "-w-", "--", "---", "----"], 'b', 3, 2))