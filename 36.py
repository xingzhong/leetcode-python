class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        
        def test(xs):
            t = [False]*9
            for x in xs:
                if x == '.': continue
                elif t[int(x)-1]:
                    return False
                else:
                    t[int(x)-1] = True
            return True
        t1 = all(map(test, board))
        if not t1 : return False
        b2 = [[board[j][i] for j in range(9)] for i in range(9)]
        t2 = all(map(test, b2))
        if not t2 : return False
        for i in range(3):
            for j in range(3):
                b3 = [board[ii][jj] for ii in range(3*i, 3*(i+1)) for jj in range(3*j, 3*(j+1))]
                if not test(b3): return False
        return True
