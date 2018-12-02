
graph =  {
                "a": ["b","c"],
                "b": ["c"],
                "c" : ["b"],
                "d" : []
                }
    



import all_graph_functions

def test_there_is_no_path(): 
    
        
    assert all_graph_functions.find_path(graph, "a", "d") == None
    

#from all_graph_functions import find_all_paths
#
#def test_there_is_two_paths():
#    
#    graph2 = {
#           "a":["b","c"],
#           "b":["d"],
#           "c":["d"],
#           "d":["e"],
#           "e":["a"],
#           "f":[],
#           "g":["c"]
#           }
#     
#    assert find_all_paths(graph2, "a", "d") == ['a', 'b', 'd']
#    
#
#from all_graph_functions_weighted import find_path
#    
#
#from all_graph_functions_weighted import find_all_paths

    

