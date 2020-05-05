import ast
import heapq

# Prints each board in proper format
def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("\n")



# Prints traceback of states used once goal is reached
def trace_back(trace_dict, finalboard):
    output = []
    output.append(finalboard)
    trace_element = trace_dict[str(finalboard)]
    while (not(trace_element is None)):
        output.append(ast.literal_eval(trace_element))
        trace_element = trace_dict[trace_element]
            
    for i in range(len(output)-1,-1,-1):
        print_board(output[i])
        print()
    print("Total moves: ", len(output)-1)



# converts array of strings to 2d array of chars
def convert(initial_board):
    new_list = [list(row) for row in initial_board]
    return new_list



# returns whether a specific char belongs to vertical car or not
def is_vertical(row, col, curr_state):
    # if last row check above
    if(row == len(curr_state[0])-1):
        if (curr_state[row-1][col] == curr_state[row][col]):
            return True
        else:
            return False
    # if row is first one check below
    elif(row == 0):
        if (curr_state[row+1][col] == curr_state[row][col]):
            return True
        else:
            return False
    # otherwise if above or below then it's vertical
    else:
        if (curr_state[row+1][col] == curr_state[row][col] or 
            curr_state[row-1][col] == curr_state[row][col]):
            return True
        else:
            return False



# returns whether a specific char belongs to horizontal car or not
def is_horizontal(row, col, curr_state):
     # if last col check left
    if(col == len(curr_state)-1):
        if (curr_state[row][col-1] == curr_state[row][col]):
            return True
        else:
            return False
    # if col is first one check right
    elif(col == 0):
        if (curr_state[row][col+1] == curr_state[row][col]):
            return True
        else:
            return False
    # otherwise if left or right then it's horizontal
    else:
        if (curr_state[row][col+1] == curr_state[row][col] or 
            curr_state[row][col-1] == curr_state[row][col]):
            return True
        else:
            return False   



# Finds positions of horizontal car
# Returns horizonal positions in list of cols it spans
def get_horizontal_pos(board, letter, row):
    car_pos = []
    for i in range(len(board[0])):
        if(board[row][i] == letter):
            car_pos.append(i)

    return car_pos



# Find positions of vertical car
# Returns vertical positions in list of rows it spans
def get_vertical_pos(board, letter, column):
    car_pos = []
    for i in range(len(board[0])):
        if(board[i][column] == letter):
            car_pos.append(i)
      
    return car_pos


# calculates the blocking heuristic for the current board state
# returns the current boards score
def block_heuristic(curr_state):
    block_count = 1
    found_x = False
    pos_of_x = 0
    # row x resides in
    row_of_x = curr_state[2]

    for i in range(len(row_of_x)):
        if (row_of_x[i] == 'X'):
            found_x = True
            pos_of_x = i
        if((found_x) and (row_of_x[i] != '-') and (row_of_x[i] != 'X')):
            block_count = block_count + 1
        else:
            continue

    if block_count == 1 and pos_of_x == 5:
        return 0
    else:
        return block_count



# Own heuristic:
# if there is a piece in x's path +2
# every move that piece that is in x's path can make that moves piece out of x's way - 1
# if reached goal return 0
def custom_heuristic(curr_state):
    score = 1
    found_x = False
    letters_seen = {}
    pos_of_x = 0
    # row x resides in
    row_of_x = curr_state[2]
    for i in range(len(row_of_x)):
        if (row_of_x[i] == 'X'):
            found_x = True
            pos_of_x = i
        if((found_x) and (not (letters_seen.get(row_of_x[i]))) and (row_of_x[i] != '-') and (row_of_x[i] != 'X')):
            letters_seen[row_of_x[i]] = True
            # +2 for being in x's path
            score = score + 2
            # We know cars in front of x can only be vertical
            # Otherwise there would be no solution.
            # Getting list of rows that the vertical car spans in this column
            pos_of_blocking = get_vertical_pos(curr_state, row_of_x[i], i)
            head_row = pos_of_blocking[0]
            tail_row = pos_of_blocking[len(pos_of_blocking)-1]
            # check if blocking piece cannot move up
            if(not(head_row == 0 or curr_state[head_row - 1][i] != '-')):
                score = score 
            # If moving up will move the piece out of x's way
            elif(tail_row - 1 < 2):
                score = score - 1

            # Check if blocking piece cannot move down
            if(not(tail_row == len(row_of_x) - 1  or curr_state[tail_row + 1][i] != '-')):
                score = score 
            # If moving down will move the piece out of x's way
            elif(head_row - 1 < 2):
                score = score - 1       
        else:
            continue
    # X has reached its goal
    if (score == 1 and pos_of_x == len(row_of_x) - 1):
        return 0
    else: 
        return score



# return new state with positions moved up 1 space
# if move not possible, returns []
def move_up(positions, col, board):
    copy_board = [row[:] for row in board]
    # if on top row, cant move up
    if(positions[0] == 0):
        return []
    # the space above is not empty
    elif(copy_board[positions[0] - 1][col] != '-'):
        return []
    # Space above is open, move it up one
    else:
        for i in positions:
            copy_board[i - 1][col] = copy_board[i][col]
        copy_board[positions[len(positions)-1]][col] = '-'
        return copy_board




# Returns new state with positions moved down 1 space
# If not possible returns []   
def move_down(positions, col, board):
    copy_board = [row[:] for row in board]
    #if on bottom row, cant move down
    if(positions[len(positions)-1] == 5):
        return []
    # the space below is not empty
    elif(copy_board[positions[len(positions)-1] + 1][col] != '-'):
        return []
    # Space below is open, move it down one
    else:
        for i in positions:
            copy_board[i + 1][col] = copy_board[i][col]
        copy_board[positions[0]][col] = '-'
        return copy_board



# Returns new state with positions moved 1 space to the right
# If not possible returns []
def move_right(positions, row, board):
    copy_board = [row[:] for row in board]
    # if rightmost is on right side of board
    if(positions[len(positions)-1] == len(board[0])-1):
        return []
    # if there is a block on the right
    elif(board[row][positions[len(positions)-1]+1] != '-'):
        return []
    # if there is a move possible, do it
    else:
        for i in positions:
            copy_board[row][i + 1] = copy_board[row][i]
        copy_board[row][positions[0]] = '-' 
        return copy_board



# Returns new state with positions moved 1 space to the left
# If not possible returns []
def move_left(positions, row, board):
    copy_board = [row[:] for row in board]
    # if leftmost is on left side of board
    if(positions[0] == 0):
        return []
    # if there is a block on the left
    elif(board[row][positions[0]-1] != '-'):
        return []
    # if there is a move possible, do it
    else:
        for i in positions:
            copy_board[row][i - 1] = copy_board[row][i]
        copy_board[row][positions[len(positions)-1]] = '-' 
        return copy_board



# Generates all possible moves from a given state
# Returns new moves as a list of states
def generate_new_moves(curr_state):
    result = []
    # keep track of seen letters 
    # so don't have to try and do same moves 
    seen_letters = {}
    for row in range(len(curr_state)):
        for col in range(len(curr_state[0])):
            letter = curr_state[row][col]
            # Letter of car we haven't made a move for 
            # yet in this function call
            if (letter != '-' and 
            not(seen_letters.get(letter))):
                seen_letters[letter] = True

                # if letter belongs to vertical car            
                if(is_vertical(row, col, curr_state)):
                    positions = get_vertical_pos(curr_state, letter, col)
                    move = move_up(positions, col, curr_state)

                    # if a move up works
                    if(len(move)!=0):
                        result.append(move)     
                    move = move_down(positions, col, curr_state)

                    # If move down is possible
                    if(len(move) != 0):
                        result.append(move)

                # if letter belongs to horizontal car
                elif(is_horizontal(row, col, curr_state)):
                    positions = get_horizontal_pos(curr_state, letter, row)
                    move = move_right(positions, row, curr_state)

                    # if a move right works
                    if(len(move) != 0):
                        result.append(move)     
                    move = move_left(positions, row, curr_state)

                    # If move left is possible
                    if(len(move) != 0):
                        result.append(move)
    return result

# Performs A star search. 
def astar(heuristic, board):
    # keep track of number of states explored
    explored = 0
    # convert to 2d list of chars
    board = convert(board)

    # key is child node, value is its parent
    # used to trace back moves used
    trace_dict = {}

    # Get initial score of board
    if (heuristic == 0):
        front_score = block_heuristic(board)
    elif (heuristic == 1):
        front_score = custom_heuristic(board)

    # Each index of frontier is a 4-tuple
    # 4-Tuple holds: (h(n) + g(n), state, blockscore h(n), depth g(n))
    frontier = []

    # Dictionary of seen states to prevent looping
    seen = {}

    # Sort based off of f(n) = g(n) + h(n)
    heapq.heappush(frontier, (front_score + 0, board, front_score, 0))
    seen[str(board)] = True
    trace_dict[str(board)] = None

    # A star Algorithm
    while True:
        # No path can be found
        if(len(frontier) == 0):
            print([])
            break

        frontier_front = heapq.heappop(frontier)
        explored = explored + 1

        # Frontier front is goal state
        if(frontier_front[2] == 0):
            # prints out final traceback
            trace_back(trace_dict, frontier_front[1])
            print("Total states explored: ", explored)
            break

        # Get new moves
        else:
            new_states = generate_new_moves(frontier_front[1])
            for state in new_states:
                # state has not been explored 
                if (not(seen.get(str(state)))):
                    #Blocking heuristic
                    if (heuristic == 0):
                        score = block_heuristic(state)
                    # My heuristic
                    elif (heuristic == 1): 
                        score = custom_heuristic(state)
                    new_depth = frontier_front[3] + 1
                    heapq.heappush(frontier,(score + new_depth, state, score, new_depth))
                    seen[str(state)]= True
                    trace_dict[str(state)] = str(frontier_front[1])

def rushhour(heuristic, board):
    astar(heuristic,board)
