#------------ Imports ------------

from grid import Grid
from graph import Graph
import heapq
import numpy as np
import copy

"""
This is a python program that provides different methods to sort a grid object
"""

#------------ Functions -----------

def convert_grid_object_to_tuple(grid_bis):
    tuples_list = []
    for line in grid_bis.state:
        tuples_list.append(tuple(line))
    return tuple(tuples_list)

def convert_tuple_to_grid_object(tup):
    grid_bis = []
    for line in tup:
        grid_bis.append(list(line))
    return Grid(len(grid_bis),len(grid_bis[0]),grid_bis)

#------------ Creation of the Graph -------------

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

def creation_of_the_graph(m,n):
    
    ligne = m
    colonne = n

    grid = Grid(ligne,colonne,[])
    graph = Graph(grid.permutations_to_grids()) # Initialistion du graphe

    for node in graph.graph:
        node_grid = convert_tuple_to_grid_object(node)
        possible_moves = []
        for i in range(node_grid.m):                 #on itère sur les lignes
            for j in range(node_grid.n):             #on itère sur les colonne

                if i==0:                        #première ligne
                    if j == 0:                  #première colonne
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                    elif j == grid.n-1:         #dernière colonne
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j-1)])      #gauche
                    else:                       #entre les deux
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                        possible_moves.append([(i,j),(i,j-1)])      #gauche

                elif i==grid.m-1:               #dernière ligne
                    if j == 0:                  #première colonne
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                    elif j == grid.n-1:         #dernière colonne
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i,j-1)])      #gauche
                    else:                       #entre les deux
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                        possible_moves.append([(i,j),(i,j-1)])      #gauche

                else:                           #entre les deux
                    if j == 0:                  #première colonne
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                    elif j == grid.n-1:         #dernière colonne
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j-1)])      #gauche
                    else:                       #entre les deux
                        possible_moves.append([(i,j),(i-1,j)])      #haut
                        possible_moves.append([(i,j),(i+1,j)])      #bas
                        possible_moves.append([(i,j),(i,j+1)])      #droite
                        possible_moves.append([(i,j),(i,j-1)])      #gauche

        grid_stock = node_grid.state

        for move in possible_moves:
            grid_copy2 = copy.deepcopy(grid_stock)  # list
            grid2 = Grid(ligne,colonne,grid_copy2)            #grid object
            grid2.swap(move[0],move[1])             #method
            grid1_tuple = convert_grid_object_to_tuple(Grid(ligne,colonne,grid_stock))
            grid2_tuple = convert_grid_object_to_tuple(grid2)
            if (((grid1_tuple,grid2_tuple) not in graph.edges) or ((grid1_tuple,grid2_tuple) not in graph.edges)):
                graph.add_edge(grid1_tuple,grid2_tuple)

    for node in graph.graph:                            #supprime les doublons car probleme dans les lignes précédentes mais pas de solutions trouvés
        voisins_avec_doublons = graph.graph[node]
        voisins_sans_doublons = list(set(graph.graph[node]))
        graph.graph[node] = voisins_sans_doublons

    return graph

#========================================== BFS =======================================

def bfs(graph_bis, src, dst): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: Node as a tuple
            The source node.
        dst: Node as a tuple
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 

        visited = []
        queue = [[src]]
        if src == dst:
            return("same node")
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = graph_bis.graph[node]
                for neighbor in neighbours:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == dst:
                        return("The shortest path from {} to {} is : {}".format(src,dst,new_path))
                visited.append(node)
        return("no path between {} and {}".format(src,dst))

#==================================== A* algorithm ====================================
    
def a_star(graph, src, dst):
    """
        Finds a shortest path from src to dst by A*.  

        Parameters: 
        -----------
        src: Node as a tuple
            The source node.
        dst: Node as a tuple
            The destination node.

        Output: 
        -------
        path: list[NodeType] | None
            The shortest path from src to dst. Returns None if dst is not reachable from src
        """ 
    
    open_set = []
    heapq.heappush(open_set, (0 + distance2(src), 0, src, None))  # (f_score, g_score, current_node, parent)
    parents = {}

    g_score = {node: float('inf') for node in graph.nodes}
    g_score[src] = 0

    f_score = {node: float('inf') for node in graph.nodes}
    f_score[src] = distance2(src)

    closed_set = set()

    while open_set:
        _, current_g, current, parent = heapq.heappop(open_set)

        if current == dst:
            return reconstruct_path(parents, current)

        parents[current] = parent
        closed_set.add(current)

        for neighbor in graph.graph[current]:
            tentative_g_score = current_g + 1  # Assumes each step costs 1

            if neighbor in closed_set:
                continue  # Skip the neighbor which is already evaluated.

            if tentative_g_score < g_score[neighbor]:
                parents[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + distance2(neighbor)
                heapq.heappush(open_set, (f_score[neighbor], g_score[neighbor], neighbor, current))

    return []

def reconstruct_path(parents, current):
    """
    """
    path = []
    while current in parents:
        path.append(current)
        current = parents[current]
    path.reverse()  # Reverse the path since it was constructed from goal to start
    return("the shortest path from {} to {} using A* algorithm is : ".format(path[0],path[-1]),path)

def distance2(tup):
    """distance from a given grid to destination (euclid's)
    tup : n x m size
    """
    dist = 0 
    m = len(tup)
    n = len(tup[0])
    grid = Grid(n,m,[])
    for i in range(1,n*m +1):
        x1,y1 = convert_tuple_to_grid_object(tup).find_index(i)
        x2,y2 = grid.find_index(i)
        gap = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        dist += gap
    return dist