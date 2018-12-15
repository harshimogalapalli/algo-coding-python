from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.m=vertices
       ## self.tr=[[0 for j in range(self.m)] for i in range(self.m)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def cycel(self,v,visited,s):
        visited[v]=True
        s[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                if self.cycel(i,visited,s)==True:
                    return True
            elif s[i]==True:
                    return True
        s[v]=False
        return False
    def cycle(self):
        visited=[False]*self.m
        s=[False]*self.m
        for i in range(self.m):
           if visited[i]==False:
                if self.cycel(i,visited,s)==True:
                    return True

        return False
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

if g.cycle()==True:
    print("CYCLE")
else :
    print("NO CYCLE")
    
        
