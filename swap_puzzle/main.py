

#------------ Imports ------------

from grid import Grid
from graph import Graph
from node import Node
import heapq
import numpy as np
import copy

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

ligne = 2
colonne = 2

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
    # for move in possible_moves:
    #     print(move)
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

#========================================== BFS =======================================

def bfs(graph_bis, src, dst): 
        """
        Finds a shortest path from src to dst by BFS.  

        Parameters: 
        -----------
        src: NodeType
            The source node.
        dst: NodeType
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
                node_tuple = tuple(tuple(li) for li in node.state)
                neighbours = graph_bis.graph[node_tuple]
                for neighbor in neighbours:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    if neighbor == dst:
                        return("The shortest path from {} to {} is : {}".format(src,dst,new_path))
                visited.append(node)
        return("no path between {} and {}".format(src,dst))

#==================================== A* algorithm ====================================
    
def distance(grid):
    """distance from a given grid to destination (euclid's)
    grid : Grid object
    """
    dist=0
    for i in range (1, grid.n*grid.m):
        x1,y1 = grid.find_index(i)
        x2,y2 = grid.find_index_when_sorted(i)
        gap = np.sqrt((x2-x1)**2 + (y2-y1)**2)
        dist += gap
    return dist

def a_star(graph,src,dst):

    # On initialise 2 listes : open -> file d'attente prioritaire contenant (f(noeud),noeud)
    # triée en fonction de f(noeud) ; closed_list -> noeuds visités
    open = []
    heapq.heappush(open, Node(src,0))
    closed_list = set()
    
    #Parents : dict pour récuper les parent-fils
    #g_scores : plus petite distance entre le noeud n et le noeud src, s'actualise
    parents = {src: None}
    g_scores = {node: float("inf") for node in graph.nodes}
    g_scores[src] = 0
    
    while open:
        current_node = heapq.heappop(open).node
        closed_list.add(current_node)
        if current_node == dst:
            path = []
            while current_node:
                path.append(parents(current_node))
                current_node = parents(current_node)
            return path                          #renvoie le chemin trouvé avec A_star

        else:
            current_node_tupple = convert_grid_object_to_tuple(current_node)
            for neighboor_node in graph.graph[current_node_tupple]:
                print(neighboor_node)
                if neighboor_node in closed_list:
                    continue

                test_g_score = g_scores[current_node] + 1 #1 car distance de 1 entre 2 noeuds séparés par un swap
                if test_g_score < g_scores[neighboor_node]:
                    parents[neighboor_node] = current_node
                    g_scores[neighboor_node] = test_g_score
                    f_score = g_scores[neighboor_node] + distance(convert_tuple_to_grid_object(neighboor_node)) # f = g + h avec g cout réel entre src et node et h cout estimé entre node et dst

                    neighbour_found_in_open = False
                    for node in open:
                        if node.node == neighboor_node:
                            if f_score < node.f_score:
                                node.f_score = f_score
                                heapq.heapify(open)
                        neighbour_found_in_open = True
                    
                if not neighbour_found_in_open:
                    heapq.heappush(open,Node(neighboor_node,f_score))
    
    return None

# grid_to_sort = Grid(2,2,[[4,2],[3,1]])
# grille_triée = Grid(2,2,[])
# print(graph.graph[((1,2),(3,4))])

#================================= Exemples =============================
grid_to_sort = Grid(2,2,[[4,2],[3,1]])
grille_triée = Grid(2,2,[])
print(bfs(graph,grid_to_sort,grille_triée))