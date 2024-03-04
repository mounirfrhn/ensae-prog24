

#------------ Imports ------------

from grid import Grid
from graph import Graph
from graph import a_star

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

#------------ Program -------------

grid_to_sort = Grid(2,2,[[4,2],[3,1]])

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

for node in graph.graph:

    node_grid = convert_tuple_to_grid_object(node)
    node_possible_moves = node_grid.grid_possible_moves()

    for move in node_possible_moves:
        grid = convert_tuple_to_grid_object(node)
        grid.swap(move[0],move[1])
        grid_2 = convert_grid_object_to_tuple(grid)
        if (((node,grid_2) not in graph.edges) or ((grid_2,node) not in graph.edges)):
            graph.add_edge(node,grid_2)

src = convert_grid_object_to_tuple(grid_to_sort)
dst = convert_grid_object_to_tuple(Grid(grid_to_sort.m,grid_to_sort.n,[]))

#print(graph.bfs(src,dst))

grid_to_sort = Grid(2,2,[[4,2],[3,1]])
grille_triée = Grid(2,2,[])
a_star(graph,grid_to_sort,grille_triée)
