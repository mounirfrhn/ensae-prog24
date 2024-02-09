


#------------ Imports ------------
from grid import Grid
from graph import Graph

#------------ Functions -----------

def convert_grid_object_to_tuple(grid):
    tuples_list = []
    for line in grid.state:
        tuples_list.append(tuple(line))
    return tuple(tuples_list)

def convert_tuple_to_grid_object(tup):
    grid = []
    for line in tup:
        grid.append(list(line))
    return Grid(len(grid),len(grid[0]),grid)

def swap_grid_tuple(tup,swap):
    grid = Grid(len(tup),len(tup[0]),convert_tuple_to_grid_object(tup))
    grid.swap(swap[0],swap[1])
    return convert_grid_object_to_tuple(grid)



#def swap_grid_tuple(grid_tup,swap):
    


#------------ Program -------------

grid_to_sort = Grid(2,2,[[1,2],[3,4]])

"""
Construction of the graph:
1. Create all nodes
2. Create all possible edges for each nodes

Ex : grid_1 =   [[1,2]
                 [3,4]]
move = ((0,0),(0,1))

grid2 = grid_1.moved(move) ->  [[2,1]
                                [3,4]]

then  : graph.add_edge(grid_1, grid2)                         
"""

graph = Graph(grid_to_sort.permutations_to_grids())

# for node in graph.graph:

#     node_grid = convert_tuple_to_grid_object(node)
#     node_possible_moves = node_grid.grid_possible_moves()

#     for move in node_possible_moves:
#         grid_2 = swap_grid_tuple(node,move)
#         if (((node,grid_2) not in graph.edges) or ((grid_2,node) not in graph.edges)):
#             graph.add_edge(node,grid_2)

print(graph.nodes)