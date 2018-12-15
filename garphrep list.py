class adj:
    def __init__(self,data):
        self.vertex=data
        self.next=None
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[None]*self.V

    def add(self,src,des):
        #source to destination
        node=adj(des)
        node.next=self.graph[src]
        self.graph[src]=node
        #destination tto sourec
        node=adj(src)
        node.next=self.graph[des]
        self.graph[des]=node
    def printg(self):
        for i in range(self.V):
            print("the  adjacency list of {}\n".format(i),end="")
            temp=self.graph[i]
            while temp:
                print("->{}".format(temp.vertex),end="")
                temp=temp.next
            print("\n")
if __name__=="__main__":
    V=4
    g=Graph(V)
    g.add(0,1)
    g.add(1,2)
    g.add(2,3)
    g.printg()
