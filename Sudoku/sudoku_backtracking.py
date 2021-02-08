'''
    Author:: Shanmukha Srinivas Jonnabatla <1216shanmukha@gmail.com>
    Author:: Ganesh Nagasai Ponnada <ganeshnagasai2000@gmail.com>
'''


class Sudoku():

    def __init__(self):
        '''
            Initiates the board, x_dimension and y_dimension to None, 0(Zero) and 0(Zer0) respectively 
        '''

        self.board = None
        self.x_dimension = 0
        self.y_dimension = 0
    
    def set_board(self, board, x_dimension, y_dimension):
        '''
            Sets the board, x_dimension, y_dimension and solve the board
        '''
        self.board = board
        self.x_dimension = x_dimension
        self.y_dimension = y_dimension
        self.solve(self.board)

    def solve(self, board):
        '''
           Solves the board 
        '''

        check = self.empty(board)   # Postions of first occurance of 0(zero) are returned  
        if not check: 
            return True
        else:
            row, col = check

            for i in range(1, len(board)+1):
                if self.entry(board, i, (row,col)):
                    board[row][col] = i
                    if self.solve(board):
                        return True
                    board[row][col]=0
            
            return False

    def empty(self, board):
        '''
            Returns postions of first occurance of 0(zero) in the board
            else False
        '''

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    return (i,j)

        return False


    def entry(self, board, num, pos):

        '''
            Returns True if num is not in the specified pos of row, column and box respectively
        '''

        # For Rows
        for i in range(len(board)):
            if board[pos[0]][i] == num and pos[1] != i:
                return False
        
        # For Columns
        for i in range(len(board)):
            if board[i][pos[1]] == num and pos[0] != i:
                return False
        
        # For Box
        x = pos[0] // self.x_dimension
        y = pos[1] // self.y_dimension
        for i in range(x * self.x_dimension, x * self.x_dimension + self.x_dimension):
            for j in range(y * self.y_dimension, y * self.y_dimension + self.y_dimension):
                if board[i][j] == num and pos != (i,j):
                    return False

        return True

    # def display(self):
    #     for i in range(len(board)):
    #         for j in range(len(board)):
    #             print(board[i][j],end=' ')
    #         print('\n')

    def print_board(self):
        '''
            Prints the Board
        '''

        for i in range(len(self.board)):
            if i % self.x_dimension == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(self.board[0])):
                if j % self.y_dimension == 0 and j != 0:
                    print(" | ", end="")

                if j == len(self.board)-1:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")


# 9X9 Sudoku with 3X3 grid
grid = [
        [8,0,6,0,0,0,4,0,9],
        [0,0,0,0,0,0,0,0,0],
        [0,9,2,0,0,0,5,0,8],
        [0,0,9,0,7,1,3,0,0],
        [5,0,8,0,0,0,0,2,0],
        [0,0,4,0,5,0,0,0,0],
        [0,0,0,0,0,7,9,1,0],
        [0,0,0,9,0,0,0,0,7],
        [0,7,0,0,0,3,0,0,4],
]

# 6X6 sudoku with 3X2 grid
# grid = [
#         [1,0,3,4,0,0],
#         [4,0,6,0,0,3],
#         [2,0,1,0,6,0],
#         [5,0,4,2,0,0],
#         [3,0,2,0,4,0],
#         [6,0,5,0,0,2]
# ]


dimension = int(input("Enter the dimension of sudoku board as N if NxN: "))
print("Enter grid dimensions:")
x_dimension = int(input("X dimension:"))
y_dimension = int(input("Y dimension:"))

sudoku = Sudoku()
sudoku.set_board(grid, x_dimension, y_dimension)
sudoku.print_board()
