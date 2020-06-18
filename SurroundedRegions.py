class Solution:
    def capture(self, board, i, j):
        board[i][j] = 'S'
        if i > 0 and board[i - 1][j] == 'O':
            self.capture(board, i - 1, j)
        if j > 0 and board[i][j - 1] == 'O':
            self.capture(board, i, j - 1)
        if i < len(board) - 1 and board[i + 1][j] == 'O':
            self.capture(board, i + 1, j)
        if j < len(board[0]) - 1 and board[i][j + 1] == 'O':
            self.capture(board, i, j + 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []

        for i in range(0, len(board)):
            if board[i][0] == 'O':
                self.capture(board, i, 0)
            if board[i][len(board[0]) - 1] == 'O':
                self.capture(board, i, len(board[0]) - 1)

        for j in range(1, len(board[0]) - 1):
            if board[0][j] == 'O':
                self.capture(board, 0, j)
            if board[len(board) - 1][j] == 'O':
                self.capture(board, len(board) - 1, j)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'