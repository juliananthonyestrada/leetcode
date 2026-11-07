class TicTacToe:

    def __init__(self, n: int):
        self.dimensions = n
        self.board = [['x' for _ in range(n)] for _ in range(n)]
        

    def winner(self, row: int, col: int) -> bool:
        player = self.board[row][col]

        # horizontal
        if all(self.board[row][c] == player for c in range(self.dimensions)):
            return True

        # vertical
        if all(self.board[r][col] == player for r in range(self.dimensions)):
            return True

        # main diagonal
        if row == col and all(self.board[i][i] == player for i in range(self.dimensions)):
            return True

        # anti-diagonal
        if row + col == self.dimensions - 1 and all(self.board[i][self.dimensions - 1 - i] == player for i in range(self.dimensions)):
            return True

        return False

    def move(self, row: int, col: int, player: int) -> int:
        # place the move
        self.board[row][col] = player

        if self.winner(row, col):
            return player

        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
