#%%
from graphs import DirectedGraph


def test_there_is_no_path(): 
    
    
    graph =  {
                "a": ["b","c"],
                "b": ["c"],
                "c" : ["b"],
                "d" : [],
                }
    
    
#    directed_graph = DirectedGraph(graph)
    
#    value = [["a", "d"]]
#
#    for case in value:
        
    assert directed_graph.find_path("a", "d") == None
    
    
#%%