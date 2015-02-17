class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        m = len(board)
        if m < 3 : return 
        n = len(board[0])
        if n < 3 : return 
        
        def setB(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == 'O':
                board[x] = board[x][:y] + 'B' + board[x][y+1:]
                setB(x-1, y)
                setB(x+1, y)
                setB(x, y+1)
                setB(x, y-1)
        
        for i in range(m):
            setB(i, 0)
            setB(i, n-1)
        for i in range(n):
            setB(0, i)
            setB(m-1, i)
        
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'O':
                    board[x] = board[x][:y] + ['X'] + board[x][y+1:]
                elif board[x][y] == 'B':
                    board[x] = board[x][:y] + 'O' + board[x][y+1:]


