"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state

    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def is_sorted(self):
        """
        Checks is the current state of the grid is sorte and returns the answer as a boolean.
        """
        return self.state == Grid(self.m,self.n, []).state
    
    def swap(self, cell1, cell2):
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        cell1_stock = cell1
        cell2_stock = cell2

        if (cell1[0]==cell2[0] and abs(cell1[1]-cell2[1])==1) or (cell1[1]==cell2[1] and abs(cell1[0]-cell2[0])==1):
            self.state[cell1[0]][cell1[1]], self.state[cell2[0]][cell2[1]] = self.state[cell2[0]][cell2[1]], self.state[cell1[0]][cell1[1]]
            return None
        else:
            print("swap non autorisé")

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        
        for pair in cell_pair_list:            
                self.swap(pair[0],pair[1])   

        #Finds the position of an integer n in a grid
    def find_index(self,n):
        for i in range (self.m):
                for j in range (self.n):
                    if n ==self.state[i][j]:
                        return (i,j) 

    #finds the index of an integer "number" if the grid was sorted                
    def find_index_when_sorted(self,number):
        a=Grid(self.m,self.n,[])
        return  a.find_index(number)

    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid
    
    def plot_grid(self):
        """
        Takes a list of lists as input and plots it using matplotlib as a grid without color fill.
        Each cell is smaller compared to the previous plot.
        """
        # Convert the list of lists to a 2D NumPy array
        matrix = np.array(self.state)

        nrows, ncols = matrix.shape
        fig, ax = plt.subplots(figsize=(ncols, nrows))  # Set figure size based on the number of rows and columns

        # Create a table to display the matrix
        table = plt.table(
            cellText=matrix,
            loc='center',
            cellLoc='center',
            bbox=[0, 0, 1, 1]  # Use full extent of the axes, making cells smaller if necessary
        )

        # Style the table
        table.auto_set_font_size(False)  # Prevent auto-setting of font-size
        table.set_fontsize(14)  # Small font size for table text
        table.scale(1, 1.5)  # Increase cell height a bit
        
        # Turn off the axis
        ax.axis('off')

        # Adjust layout to make room for the table:
        plt.tight_layout()
        plt.show()

#==================================== Creation of the Graph ====================================

    def permutations_to_grids(self):
        numbers_list = range(1,self.n*self.m+1)
        perms = permutations(numbers_list)
        grids = []

        for perm in perms:
            grids.append(tuple(tuple(perm[i * self.n:(i + 1) * self.n] for i in range(self.m))))
        return grids
    
    def possible_moves(self,cell):      #tells if a move is possible, in order to be able to build the graph of all possible nodes for a given grid and the way to access it
        list_of_possible_moves=[]
        upward_cell=(cell[0]-1,cell[1])
        downward_cell=(cell[0]+1,cell[1])
        leftward_cell=(cell[0],cell[1]-1)
        rightward_cell=(cell[0],cell[1]+1)
        if abs(cell[0])>=self.m or abs(cell[1])>=self.n:
            print("not possible")
        else:
            if cell[0]==0 and cell[1]==0:
                list_of_possible_moves=[(cell,downward_cell),(cell,rightward_cell)]
            if cell[0]==0 and cell[1]!=0 and cell[1]!= self.n -1:
                list_of_possible_moves=[(cell,downward_cell),(cell,leftward_cell),(cell,rightward_cell)]
            if cell[0]==0 and cell[1]==self.n -1:
                list_of_possible_moves=[(cell,downward_cell),(cell,leftward_cell)]
            if cell[0]!=0 and cell[1]==0:
                list_of_possible_moves=[(cell,upward_cell),(cell,downward_cell),(cell,rightward_cell)]
            if cell[0]!=0 and cell[1]==self.n -1:
                list_of_possible_moves=[(cell,upward_cell),(cell,downward_cell),(cell,leftward_cell)]
            if cell[0]==self.m -1 and cell[1]==0:
                list_of_possible_moves=[(cell,upward_cell),(cell,rightward_cell)]
            if cell[0]==self.m -1 and cell[1]!=0 and cell[1]!=self.n -1:
                list_of_possible_moves=[(cell,upward_cell),(cell,leftward_cell),(cell,rightward_cell)]
            if cell[0]==self.m -1 and cell[1]==self.n -1:
                list_of_possible_moves=[(cell,upward_cell),(cell,leftward_cell)]
            if cell[0]!=0 and cell[0]!=self.m-1 and cell[1]!=0 and cell[1]!=self.n -1:
                list_of_possible_moves=[(cell,upward_cell),(cell,downward_cell),(cell,leftward_cell),(cell,rightward_cell)]
            return list_of_possible_moves
    
    def create_graph(self):
        nodes = self.permutations_to_grids()
        for node in nodes:
            possible_moves = []
            for i in range(self.m):                 #on itère sur les lignes
                for j in range(self.n):             #on itère sur les colonne

                    if i==0:                        #première ligne
                        if j == 0:                  #première colonne
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                        elif j == self.n-1:         #dernière colonne
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i-1,j)])      #gauche
                        else:                       #entre les deux
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                            possible_moves.append([(i,j),(i-1,j)])      #gauche

                    elif i==self.m-1:               #dernière ligne
                        if j == 0:                  #première colonne
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                        elif j == self.n-1:         #dernière colonne
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i-1,j)])      #gauche
                        else:                       #entre les deux
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                            possible_moves.append([(i,j),(i-1,j)])      #gauche

                    else:                           #entre les deux
                        if j == 0:                  #première colonne
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                        elif j == self.n-1:         #dernière colonne
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i-1,j)])      #gauche
                        else:                       #entre les deux
                            possible_moves.append([(i,j),(i,j-1)])      #haut
                            possible_moves.append([(i,j),(i,j+1)])      #bas
                            possible_moves.append([(i,j),(i+1,j)])      #droite
                            possible_moves.append([(i,j),(i-1,j)])      #gauche



    def grid_possible_moves(self):
        final_list=[]
        for i in range(0,self.m):
            for j in range(0,self.n):
                final_list.append(self.possible_moves((i,j)))
        return [couple for liste in final_list for couple in liste]

