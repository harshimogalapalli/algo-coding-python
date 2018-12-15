from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add(self,u,v):
        self.graph[u].append(v)
    def BFS(self,s):
        visited=[False]*(len(self.graph))
        q=[]
        q.append(s)
        visited[s]=True
        while q:
            a=q.pop(0)
            print(a,end=" ")
            for i in self.graph[a]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True
                    
g=Graph()

g.add(0,1)
g.add(0,2)
g.add(1,2)
g.add(2,0)
g.add(2,3)
g.add(3,3)

g.BFS(2)        
