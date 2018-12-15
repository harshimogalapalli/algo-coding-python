from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.m=vertices
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def  dsf(self,v,visited):
        visited[v]=True
       
        for i in self.graph[v]:
            if visited[i]==False:
                self.dsf(i,visited)
    def dfsmother(self):
        
        visited=[False]*(self.m)
        #  print(visited)
        v=0
        for i in range(self.m):
            if visited[i]==False:
                self.dsf(i,visited)
                v=i
       
        visited=[False]*(self.m)
        self.dsf(v,visited)
        if any(i==False for i in visited):
            return -1
        else:
            return v
        
                         
g=Graph(7) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 3) 
g.addEdge(4, 1) 
g.addEdge(6, 4) 
g.addEdge(5, 6) 
g.addEdge(5, 2) 
g.addEdge(6, 0) 

k=g.dfsmother()
print(k)

        
