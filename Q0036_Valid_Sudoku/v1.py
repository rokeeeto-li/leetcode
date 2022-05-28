class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(L):
            dic = Counter(L)
            for key in dic.keys():
                if key != '.' and dic[key] > 1:
                    return False
            return True
        
        for i in range(9):
            if not check(board[i]): return False
            if not check([x[i] for x in board]): return False
        for i in range(3):
            for j in range(3):
                temp = board[3*i][3*j:3*j+3] + board[3*i+1][3*j:3*j+3] + board[3*i+2][3*j:3*j+3]
                if not check(temp): return False
        return True
