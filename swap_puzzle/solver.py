from grid import Grid

class Solver(Grid): 

    """
    A solver class, to be implemented.
    """

    def correct_spot(self,number):
         swap_list=[]
         correct_row = self.find_index_when_sorted(number)[0]
         correct_column = self.find_index_when_sorted(number)[1]
         while (correct_row,correct_column) != self.find_index(number): #while the number isn't properly positionned
             if self.find_index(number)[1] > correct_column:    #number is on the right of its right spot
                 for k in range(self.find_index(number)[1]-correct_column): #move it so that it is positionned in the same column as if it was sorted
                      self.swap(self.find_index(number),(self.find_index(number)[0],self.find_index(number)[1]-k-1))
                      if self.find_index(number)[1]-k-1 != -1:
                        swap_list.append((self.find_index(number),(self.find_index(number)[0],self.find_index(number)[1]-k-1)))
                      else:
                           swap_list.append((self.find_index(number),(self.find_index(number)[0],self.n -1)))
             elif self.find_index(number)[1] < correct_column:      #same leftwards
                 for k in range(self.find_index(number)[1]-correct_column):
                      self.swap(self.find_index(number),(self.find_index(number)[0],self.find_index(number)[1]+k+1))
                      swap_list.append((self.find_index(number),(self.find_index(number)[0],self.find_index(number)[1]+k+1)))
             elif self.find_index(number)[1] == correct_column:     #if on the same column, move it upwards so that it's in the right row
                 if self.find_index(number)[0]>correct_row:
                      for k in range(self.find_index(number)[0]-correct_row):
                            self.swap(self.find_index(number),(self.find_index(number)[0]-k-1,self.find_index(number)[1]))
                            if self.find_index(number)[0]-k-1 != -1:
                                swap_list.append((self.find_index(number),(self.find_index(number)[0]-k-1,self.find_index(number)[1])))
                            else:
                                 swap_list.append((self.find_index(number),(self.m -1,self.find_index(number)[1])))
                 if self.find_index(number)[0]<correct_row:
                     for k in range(correct_row - self.find_index(number)[0]):
                            self.swap(self.find_index(number),(self.find_index(number)[0]+k+1,self.find_index(number)[1])) 
                            swap_list.append((self.find_index(number),(self.find_index(number)[0]+k+1,self.find_index(number)[1])))    
         return swap_list
                   

 
    def get_solution(self):

        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """

        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        # raise NotImplementedError
        
        path = []

        for i in range(1,self.n*self.m+1):
            tup_list = self.correct_spot(i)
            for tup in tup_list:
                 path.append(tup)
        
        return path
             
 
a=Solver(2,2,[[4,3],[2,1]])

#print(a.get_solution())