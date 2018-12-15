from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.m=vertices
        self.tr=[[0 for j in range(self.m)] for i in range(self.m)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def  dsf(self,v,t):
        self.tr[v][t]=1
        ##print(v,end=" ")
        for i in self.graph[v]:
            if self.tr[v][i]==0:
                self.dsf(v,i)
    def tra(self):
       for i in range(self.m):
           
             self.dsf(i,i)
       print(self.tr) 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

g.tra()        
        
