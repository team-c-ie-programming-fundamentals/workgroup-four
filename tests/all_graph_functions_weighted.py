#%%
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["d"],
    "d": ["e"],
    "e": [],
    "f": []
}

def find_path_weighted(graph, start, end, path=[]):
    
    # first thing, we add the current start to the path
    path = path + [start]
    
    
    # then , if the start is the same as the end, we have finished, we can
    # return the path!
    if start == end:
        return path

    # Also, if the start is *not* in the graph, we return None
    if start not in graph:
        return None

    # Here we iterate over all of start's edges
    for node in graph[start]:
        # if the edge is not in the path (we haven't visited it yet)
        if node not in path:
            # We try to find its path to end
            newpath = find_path(graph, node, end, path)

            # and, if it didn't return None, we return the path 
            if newpath is not None:
                return newpath
  
    # If we got to this point it means there's no path from start to end
    return None


def find_all_paths_weighted(graph, start, end, path=[]):

    path = path + [start]
    
    
    # then , if the start is the same as the end, we have finished, we can
    # return the path!
    if start == end:
        return [path]

    # Also, if the start is *not* in the graph, we return None
    if start not in graph:
        return []


    paths = []
    
    # Here we iterate over all of start's edges
    for node in graph[start]:
        # if the edge is not in the path (we haven't visited it yet)
        if node not in path:
  
            # We try to find all its paths to end
            new_paths = find_all_paths(graph, node, end, path)

            # and, if it didn't return None, we return the path 
            for new_path in new_paths:
                paths.append(new_path)
  
    # If we got to this point it means there's no path from start to end
    return paths
