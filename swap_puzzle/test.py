from grid import Grid
from graph import Graph
from main import *
from solver import Solver
import time
import random

#================================= Exemples =============================

# -------- Exemple d'une grid carrée m = 2 ; n = 2 --------

grid_to_sort = Grid(2,2,[[4,2],[3,1]])
sorted_grid = Grid(2,2,[])

# --------- Algorithme naif ---------

ex_1_naif_start_time = time.time()
grid_to_sort_solver = Solver(2,2,[[4,2],[3,1]])
print(grid_to_sort_solver.get_solution())
ex_1_naif_end_time = time.time()
print("temps necessaire avec algo naif : ", ex_1_naif_end_time-ex_1_naif_start_time)
print("\n")

""" Resultats
[((1, 0), (1, 1)), ((0, 0), (1, 0)), ((1, 0), (1, 1))]
temps necessaire avec algo naif :  0.00014281272888183594
"""

# -------- BFS --------

ex_1_bfs_start_time = time.time()
graph = creation_of_the_graph(2,2)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_bfs_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec BFS : ", ex_1_bfs_end_time-ex_1_bfs_start_time)
print("\n")

""" Resultats
The shortest path from ((4, 2), (3, 1)) to ((1, 2), (3, 4)) is : [((4, 2), (3, 1)), ((4, 1), (3, 2)), ((1, 4), (3, 2)), ((1, 2), (3, 4))]
temps necessaire avec BFS :  0.0035398006439208984
"""

# -------- A* --------
ex_1_a_star_start_time = time.time()
graph = creation_of_the_graph(2,2)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_a_star_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec A* : ", ex_1_a_star_end_time-ex_1_a_star_start_time)
print("\n")

""" Resultats : 
The shortest path from ((4, 2), (3, 1)) to ((1, 2), (3, 4)) is : [((4, 2), (3, 1)), ((4, 1), (3, 2)), ((1, 4), (3, 2)), ((1, 2), (3, 4))]
temps necessaire avec A* :  0.0033767223358154297
"""

# -------- Exemple d'une grid carrée m = 2 ; n = 3 --------

grid_to_sort = Grid(2,3,[[4,6,1],[5,3,2]])
sorted_grid = Grid(2,3,[])

# --------- Algorithme naif ---------

ex_1_naif_start_time = time.time()
grid_to_sort_solver = Solver(2,3,[[4,6,1],[5,3,2]])
print(grid_to_sort_solver.get_solution())
ex_1_naif_end_time = time.time()
print("temps necessaire avec algo naif : ", ex_1_naif_end_time-ex_1_naif_start_time)
print("\n")

""" Resultats
"""

# -------- BFS -------

ex_1_bfs_start_time = time.time()
graph = creation_of_the_graph(2,3)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_bfs_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec BFS : ", ex_1_bfs_end_time-ex_1_bfs_start_time)
print("\n")

""" Resultats
The shortest path from ((4, 2), (3, 1)) to ((1, 2), (3, 4)) is : [((4, 2), (3, 1)), ((4, 1), (3, 2)), ((1, 4), (3, 2)), ((1, 2), (3, 4))]
temps necessaire avec BFS :  0.0035398006439208984
"""

# -------- A* --------
ex_1_a_star_start_time = time.time()
graph = creation_of_the_graph(2,3)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_a_star_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec A* : ", ex_1_a_star_end_time-ex_1_a_star_start_time)
print("\n")

""" Resultats : 
The shortest path from ((4, 2), (3, 1)) to ((1, 2), (3, 4)) is : [((4, 2), (3, 1)), ((4, 1), (3, 2)), ((1, 4), (3, 2)), ((1, 2), (3, 4))]
temps necessaire avec A* :  0.0033767223358154297
"""

# -------- Exemple d'une grid carrée m = 4 ; n = 4 --------

m, n = 3, 4 
total_elements = m * n 
permutation = random.sample(range(1, total_elements + 1), total_elements)
grid = [permutation[i * n:(i + 1) * n] for i in range(m)]


grid_to_sort = Grid(4,4,[[4,6,1],[5,3,2]])
sorted_grid = Grid(4,4,[])

# --------- Algorithme naif ---------

ex_1_naif_start_time = time.time()
grid_to_sort_solver = Solver(2,3,[[4,6,1],[5,3,2]])
print(grid_to_sort_solver.get_solution())
ex_1_naif_end_time = time.time()
print("temps necessaire avec algo naif : ", ex_1_naif_end_time-ex_1_naif_start_time)
print("\n")

""" Resultats
"""

# -------- BFS -------

ex_1_bfs_start_time = time.time()
graph = creation_of_the_graph(2,3)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_bfs_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec BFS : ", ex_1_bfs_end_time-ex_1_bfs_start_time)
print("\n")

""" Resultats
"""

# -------- A* --------
ex_1_a_star_start_time = time.time()
graph = creation_of_the_graph(2,3)
grid_to_sort_tuple = convert_grid_object_to_tuple(grid_to_sort)
grid_triée_tuple = convert_grid_object_to_tuple(sorted_grid)
ex_1_a_star_end_time = time.time()
print(bfs(graph,grid_to_sort_tuple,grid_triée_tuple))
print("temps necessaire avec A* : ", ex_1_a_star_end_time-ex_1_a_star_start_time)
print("\n")

""" Resultats : 
"""