class Graph(object):
    def __init__(self, vertices=[], adj=[]):
        self.vertices=vertices[:]
        self.adj=adj[:]

    def add(self, n):
        if type(n) != Vertex:
            print("Value error")
        else:
            self.vertices.append(n)
            
        self.manageAdj()

    def delete(self, n):
        if n in self.vertices == False:
            print("Vertex not present in graph, nothing to delete")
        else:
            for v in self.vertices:
                if n in v.edges:
                    v.edges.remove(n)
                
            self.vertices.remove(n)
            self.manageAdj()

    def manageAdj(self):
        self.adj=[]
        self.adj.extend([[0 for i in range(len(self.vertices))]
                            for j in range(len(self.vertices))])
        
        for v in self.vertices:
            for w in v.edges:
                self.adj[self.vertices.index(v)][self.vertices.index(w)] = 1
            
    def printout(self):
        for v in self.vertices:
            print(str(v))

    def printAdj(self):
        for row in self.adj:
            print(row)

class WeightedGraph(Graph):
    def __init__(self, vertices=[], adj=[]):
        self.vertices=vertices[:]
        self.adj=adj[:]

class Vertex(object):
    def __init__(self,name="",edges=[]):
        self.name=name
        self.edges=edges[:]

    def addEdges(self, verts):
        l=self.edges.copy()
        l.extend(verts)
        for v in verts:
            if (self in v.edges) == False and (v in l) == True:
                v.edges.extend([self])
        self.edges=l

    def removeEdges(self, verts):
        l=self.edges.copy()
        for v in verts:
            if v in l:
                l.remove(v)
            if (self in v.edges) == True and (v in l) == False:
                v.edges.remove(self)
        self.edges=l
    
    def printEdges(self):
        l = []
        for c in self.edges:
            l.append(c.name)
        return l

    def __str__(self):
        return "Node '" + self.name + "' with edges " + str(self.printEdges())

    def __repr__(self):
        return "Node '" + self.name + "' with edges " + str(self.printEdges())
    
class Edge(object):
    def __init__(self,x,y,distance=None):
        self.x=x
        self.y=y
        self.distance=distance

    def __repr__(self):
        return "Edge from '" + self.x.name + "' to '" + self.y.name + "' with distance " + str(self.distance)

g=Graph()

a=Vertex("a")
b=Vertex("b")
c=Vertex("c")
d=Vertex("d")
e=Vertex("e")

g.add(a)
g.add(b)
g.add(c)
g.add(d)
g.add(e)

a.addEdges([b,c])
e.addEdges([d])
e.addEdges([e])
g.manageAdj()

g.printout()
g.printAdj()

c.removeEdges([a])
g.delete(e)

g.printout()
g.printAdj()
