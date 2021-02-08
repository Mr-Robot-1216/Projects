


from pprint import pprint
from collections import Counter
from copy import deepcopy


class Sudoku():
    def __init__(self, grid):
        '''
            Initializes the grid
        '''
        self.grid = grid
        self.sub_grid = self.create_sub_grid(self.grid)

    def create_sub_grid(self, grid):
        ''' 
            Creates a Sub grid, containing the possible numbers within a cell
            Returns a Sub grid
        '''
        sub_grid = []
        for i in range(9):
            sub = []
            for j in range(9):
                if grid[i][j] == 0:
                    sub.append(self.missing_numbers(i,j))
                else:
                    sub.append([grid[i][j]])
            sub_grid.append(sub)
            del sub
        return sub_grid


    def missing_numbers(self, row, column):
        '''
            Returs the possible set of numbers of a particular row and column
        '''

        rrow, ccolumn = self.row_and_column(self.grid, row, column)
        cell = self.cell_3by3(row, column)
        
        missing_num = list({i for i in range(1, 10)} - set(rrow + ccolumn + cell))
        return missing_num



    def cell_3by3(self, row, column):
        '''
            Returns grid of 3 X 3
        '''

        cell = []
        a = row // 3
        b = column // 3
        for i in range(9):
            for j in range(9):
                if i // 3 == a and j // 3 == b : 
                    cell.append(grid[i][j])
        return cell

    def row_and_column(self, grid, row, column): 
        '''
            Returns rows and columns
        '''
        r = grid[row]
        c = []
        for j in range(9):
            c.append(grid[j][column])
        return r, c




    def step_1(self, sub_grid, num):
        '''
            Reducing a list of clues to a single value based on row and column elimination
            Returns a refined sub grid
        '''


        row,column = self.row_and_column(sub_grid,num,num)

        row_flatten = sum(row,[])
        single_values = [i for i,j in Counter(row_flatten).items() if j == 1 ]

        # For Rows
        for i in range(len(sub_grid)):
            for j in single_values:
                if j in sub_grid[num][i] and len(sub_grid[num][i]) != 1:
                    sub_grid[num][i] = [j] 

        # For Columns
        column_flatten = sum(column, [])
        column_single_values = [i for i,j in Counter(column_flatten).items() if j == 1 ]
        for i in range(len(sub_grid)):
            for j in column_single_values:
                if j in sub_grid[i][num] and len(sub_grid[i][num]) != 1:
                    sub_grid[i][num] = [j]



        return sub_grid

    def step_2(self, sub_grid, num):
        '''
            Removes a number 'n' that fits at its correct position from other lists corresponding its row and column
            Returns refined sub grid
        '''

        row,column = self.row_and_column(sub_grid,num,num)

        # For Rows
        single_value_list = []
        for i in range(len(row)):
            if len(sub_grid[num][i]) == 1:
                single_value_list.append(sub_grid[num][i])
        single_value_list_flatten = sum(single_value_list, [])

        for i in range(len(sub_grid)):
            if len(sub_grid[num][i]) != 1: 
                for j in single_value_list_flatten:
                    if j in sub_grid[num][i]:
                        sub_grid[num][i].remove(j)

        # For Columns
        single_value_list = []
        for i in range(len(column)):
            if len(sub_grid[i][num]) == 1:
                single_value_list.append(sub_grid[i][num])
        single_value_list_flatten = sum(single_value_list, [])

        for i in range(len(sub_grid)):
            if len(sub_grid[i][num]) != 1: 
                for j in single_value_list_flatten:
                    if j in sub_grid[i][num]:
                        sub_grid[i][num].remove(j)

        return sub_grid

    def step_3(self, sub_grid, num):
        pass

            


    def perform(self):
        '''
            Performs the step_1 and step_2 untill the Sub grid is solved
            Returns None
        '''

        temp = []
        while self.sub_grid != temp: 
            temp = deepcopy(self.sub_grid)  
            for i in range(len(grid)):
                self.sub_grid = self.step_1(self.sub_grid, i)
                self.sub_grid = self.step_2(self.sub_grid, i)


    def solve(self):
        '''
            Solves the Sub grid and prints the sub grid
            Returns None
        '''

        self.perform()
        for i in range(9):
            for j in range(9):
                print(self.sub_grid[i][j], end=' ')
            print()


# grid = [
#         [0,3,0,0,1,0,0,6,0],
#         [7,5,0,0,3,0,0,4,8],
#         [0,0,6,9,8,4,3,0,0],
#         [0,0,3,0,0,0,8,0,0],
#         [9,1,2,0,0,0,6,7,4],
#         [0,0,4,0,0,0,5,0,0],
#         [0,0,1,6,7,5,2,0,0],
#         [6,8,0,0,9,0,0,1,5],
#         [0,9,0,0,4,0,0,3,0]
# ]

# grid = [
#          [6,0,0,1,0,8,2,0,3],
#          [0,2,0,0,4,0,0,9,0],
#          [8,0,3,0,0,5,4,0,0],
#          [5,0,4,6,0,7,0,0,9],
#          [0,3,0,0,0,0,0,5,0],
#          [7,0,0,8,0,3,1,0,2],
#          [0,0,1,7,0,0,9,0,6],
#          [0,8,0,0,3,0,0,2,0],
#          [3,0,2,9,0,4,0,0,5]
# ]
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

mat = Sudoku(grid)
mat.solve()
