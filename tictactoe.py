import copy

X = "X"
O = "O"
EMPTY = None
INFINITY = 1000


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY] * 3 for _ in range(3)]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_empty = sum(row.count(EMPTY) for row in board)
    return O if num_empty % 2 == 0 else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    result_board[action[0]][action[1]] = player(board)
    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or \
       board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    return all(cell != EMPTY for row in board for cell in row) or winner(board) is not None


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    return 1 if result == X else -1 if result == O else 0

# minimax algorithm
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)
        
        v = -INFINITY
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        
        v = INFINITY
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if player(board) == X:
        max_action = None
        max_val = -INFINITY
        for action in actions(board):
            val = min_value(result(board, action))
            if val > max_val:
                max_val = val
                max_action = action
        return max_action
    else:
        min_action = None
        min_val = INFINITY
        for action in actions(board):
            val = max_value(result(board, action))
            if val < min_val:
                min_val = val
                min_action = action
        return min_action

# add memoization to minimax algorithm
def MemoMinimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    maxMemo = {}
    def max_value(board):
        if terminal(board):
            return utility(board)
        
        board_tuple = tuple(map(tuple, board))
        if board_tuple in maxMemo:
            return maxMemo[board_tuple]

        v = -INFINITY
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        
        maxMemo[board_tuple] = v
        return v

    minMemo = {}
    def min_value(board):
        if terminal(board):
            return utility(board)
        
        board_tuple = tuple(map(tuple, board))
        if board_tuple in minMemo:
            return minMemo[board_tuple]

        v = INFINITY
        for action in actions(board):
            v = min(v, max_value(result(board, action)))

        minMemo[board_tuple] = v
        return v

    if player(board) == X:
        max_action = None
        max_val = -INFINITY
        for action in actions(board):
            val = min_value(result(board, action))
            if val > max_val:
                max_val = val
                max_action = action
        return max_action
    else:
        min_action = None
        min_val = INFINITY
        for action in actions(board):
            val = max_value(result(board, action))
            if val < min_val:
                min_val = val
                min_action = action
        return min_action

# implement Alpha-Beta Pruning in your minimax function for Tic-Tac-Toe
def AlphaBetaMinimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        
        v = -INFINITY
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board)
        
        v = INFINITY
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

    if player(board) == X:
        max_action = None
        max_val = -INFINITY
        alpha = -INFINITY
        beta = INFINITY
        for action in actions(board):
            val = min_value(result(board, action), alpha, beta)
            if val > max_val:
                max_val = val
                max_action = action
            alpha = max(alpha, val)
        return max_action
    else:
        min_action = None
        min_val = INFINITY
        alpha = -INFINITY
        beta = INFINITY
        for action in actions(board):
            val = max_value(result(board, action), alpha, beta)
            if val < min_val:
                min_val = val
                min_action = action
            beta = min(beta, val)
        return min_action

# apply depth limitation to minimax algorithm
def depthLimitedMinimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    MAX_DEPTH = 3  # You can adjust this depth limit as needed
    def max_value(board, depth):
        if terminal(board) or depth == 0:
            return utility(board)
        
        v = -INFINITY
        for action in actions(board):
            v = max(v, min_value(result(board, action), depth - 1))
        return v

    def min_value(board, depth):
        if terminal(board) or depth == 0:
            return utility(board)
        
        v = INFINITY
        for action in actions(board):
            v = min(v, max_value(result(board, action), depth - 1))
        return v

    if player(board) == X:
        max_action = None
        max_val = -INFINITY
        for action in actions(board):
            val = min_value(result(board, action), MAX_DEPTH - 1)
            if val > max_val:
                max_val = val
                max_action = action
        return max_action
    else:
        min_action = None
        min_val = INFINITY
        for action in actions(board):
            val = max_value(result(board, action), MAX_DEPTH - 1)
            if val < min_val:
                min_val = val
                min_action = action
        return min_action

# apply depth limitation to Alpha-Beta Pruning minimax algorithm
def AlphaBetaDepthLimitedMinimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    MAX_DEPTH = 5  # You can adjust this depth limit as needed
    def max_value(board, alpha, beta, depth):
        if terminal(board) or depth == 0:
            return utility(board)
        
        v = -INFINITY
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta, depth - 1))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v

    def min_value(board, alpha, beta, depth):
        if terminal(board) or depth == 0:
            return utility(board)
        
        v = INFINITY
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta, depth - 1))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

    if player(board) == X:
        max_action = None
        max_val = -INFINITY
        alpha = -INFINITY
        beta = INFINITY
        for action in actions(board):
            val = min_value(result(board, action), alpha, beta, MAX_DEPTH - 1)
            if val > max_val:
                max_val = val
                max_action = action
            alpha = max(alpha, val)
        return max_action
    else:
        min_action = None
        min_val = INFINITY
        alpha = -INFINITY
        beta = INFINITY
        for action in actions(board):
            val = max_value(result(board, action), alpha, beta, MAX_DEPTH - 1)
            if val < min_val:
                min_val = val
                min_action = action
            beta = min(beta, val)
        return min_action
