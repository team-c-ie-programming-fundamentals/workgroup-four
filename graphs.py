#%%

class DirectedGraph: 
    def __init__(self, dictionary): 
        self.dictionary = dictionary
        
    def find_path(self, start, end, path=[]):
        
        # first thing, we add the current start to the path
        path = path + [start]
        
        
        # then , if the start is the same as the end, we have finished, we can
        # return the path!
        if start == end:
            return path
    
        # Also, if the start is not in the graph, we return None
        if start not in self.dictionary:
            return None
    
        # Here we iterate over all of start's edges
        for node in self.dictionary[start]:
            # if the edge is not in the path (we haven't visited it yet)
            if node not in path:
                # We try to find its path to end
                newpath = self.find_path(node, end, path)
    
                # and, if it didn't return None, we return the path 
                if newpath is not None:
                    return newpath
      
        # If we got to this point it means there's no path from start to end
        return None
    
    

graph10 =  {
            "a": ["b","c"],
            "b": ["c"],
            "c" : ["b", "d"],
            "d" : ["b"],
            }

graph = DirectedGraph(graph10)

graph.find_path("a","b")

#%%

#Alternative Solution

class Node:
    def __init__(self, label, edges):
        self.label = label
        self.edges = edges
    
    def new_edge(self, edge):
        self.edges.append(edge)

a = Node("a", [])
b = Node("b", [])
c = Node("c", [])
d = Node("d", [])

a.new_edge(b)
a.new_edge(c)
b.new_edge(c)
c.new_edge(b)
c.new_edge(d)
d.new_edge(b)

class Dir_Graph:
    def __init__(self, lst):
        self.lst = lst
        
    def find_connection(self, edge):
        return edge.edges
    
    def find_path_alt(self, start, end, path=[]):
        
        path = path + [start]
        
        if start == end:
            return path
    
        
        if start not in self.lst:
            return None
    

        for node in self.find_connection(start):

            if node not in path:

                newpath = self.find_path_alt(node, end, path)

                if newpath is not None:
                    return newpath
      
        return None
    
    def return_connection(self,start,end):
        lst = self.find_path_alt(start,end)
        connections = []
        for i in lst:
            connections.append(i.label)
        return connections

graph_dir = Dir_Graph([a,b,c,d])
