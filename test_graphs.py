 #%%
import all_graph_functions

def test_there_is_no_path(): 
    
    
    graph =  {
                "a": ["b","c"],
                "b": ["c"],
                "c" : ["b"],
                "d" : [],
                }
    

        
    assert find_path(graph, "a", "d") == None
    
    
#%%
    
import all_graph_functions_weighted 