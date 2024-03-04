class Node():
    def __init__(self,node,score):
        self.f_score = score
        self.node = node
    
    def __lt__(self,other):
        return self.f_score < other.f_score
    