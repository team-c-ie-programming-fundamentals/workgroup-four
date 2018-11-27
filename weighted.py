#%%

class WeightedDirected:
    def __init__(self, dictionary): 
        self.dictionary = dictionary 
        
        
        
    
    def find_all_paths(self, start, end, path=[], weight=0):
        path = path + [{"node": start, "weight": weight}]
    
        if start == end:
            return [path]
    
        if not start in self.dictionary:
            return []
    
        paths = []
        
        for conn in self.dictionary[start]:
            if conn not in path:
                newpaths = self.find_all_paths(conn["node"], end, path, conn["weight"])
                                
                for newpath in newpaths:
                    paths.append(newpath)
        
        return paths

                
    
    def cheapest_path(self, start, end):
        all_paths = WeightedDirected.find_all_paths(self, start, end)
        
        cheapest = None
        
        for path in all_paths:
            cost = 0
            
            for step in path:
                cost += step["weight"]
                
            if cheapest is None or cost < cheapest:
                cheapest = cost
        
        
        return  "the cheapest is " + str(cheapest) + " weights, the path is " + str(path)



graph2 = {
    "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
    "b": [{"node": "d", "weight": 3}],
    "c": [{"node": "d", "weight": 1}],
    "d": [{"node": "e", "weight": 3}],
    "e": [{"node": "f", "weight": 3}]
}


graph_ts = WeightedDirected(graph2)


