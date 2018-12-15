from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def  dsf(self,v,visited):
        visited[v]=True
        print(v,end=" ")
        for i in self.graph[v]:
            if visited[i]==False:
                self.dsf(i,visited)
    def dfs(self,v):
        visited=[False]*(len(self.graph))
        self.dsf(v,visited)
        
g=Graph()

g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)

g.dfs(2)        
        
