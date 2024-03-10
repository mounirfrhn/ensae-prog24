from grid import Grid
from graph import Graph
from main import convert_grid_object_to_tuple,convert_tuple_to_grid_object, a_star
import copy

ligne = 3
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


src = Grid(2,2,[[2,4],[1,3]])
dst = Grid(2,2,[])
print(a_star(graph,src,dst))