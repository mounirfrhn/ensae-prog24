from grid import Grid 
from graph import Graph
from main import *
import random as rd
from matplotlib.widgets import Button
from matplotlib.backend_bases import key_press_handler

def generate_grid(m,n):
    numbers=list(range(1, n*m +1))
    rd.shuffle(numbers)
    grid=[]
    for k in range(m):
        line=[]
        for i in range(n):
            line.append(numbers[0]) #adds first element
            numbers.pop(0)  #pops it so it doesnt repeat
            numbers.append(0)   #add a decoy element so that length stays the same for the loop
        grid.append(line)
    return grid

#---- let's implement the game in an interactive window, that allows us to navigate through the different stages of our grid

m=int(input("Choisissez le nombre de lignes de votre grille."))
n=int(input("Choisissez le nombre de colonnes de votre grille."))
A=Grid(m,n,generate_grid(m,n))

while A.is_sorted()==False:
    A.plot_grid()
    c11=int(input("i1?"))
    c12=int(input("j1?"))
    c21=int(input("i2?"))
    c22=int(input("j2?"))
    cell1=(c11,c12)
    cell2=(c21,c22)
    A.swap(cell1,cell2)
    if c11=="Q":
        continue        #Pygame didn't work, hence it being on a rather prosaic version of matplotlib