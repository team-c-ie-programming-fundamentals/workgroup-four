
graph1 =  {
                "a": ["b","c"],
                "b": ["c"],
                "c" : ["b"],
                "d" : []
                }
    

graph2 = {
           "a":["b","c", "e"],
           "b":["d"],
           "c":["d"],
           "d":["e"],
           "e":["a"],
           "f":[],
           "g":["c"]
           }


graph3 = {
        "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
        "b": [{"node": "d", "weight": 3}],
        "c": [{"node": "d", "weight": 1}],
        "d": [{"node": "e", "weight": 3}],
        "e": [{"node": "f", "weight": 3}]
#
        }     


graph4 = {
        "a": [{"node": "b", "weight": 1}, {"node": "c", "weight": 2}],
        "b": [{"node": "d", "weight": 3}],
        "c": [{"node": "d", "weight": 1}],
        "d": [{"node": "e", "weight": 3}],
        "e": [{"node": "f", "weight": 3}]
#
        }     

from all_graph_functions import find_path
from all_graph_functions import find_all_paths
from all_graph_functions_weighted import find_path_weighted
from all_graph_functions_weighted import find_all_paths_weighted



def test_there_is_no_path(): 
    
    assert find_path(graph1, "a", "d") == None
    

def test_there_is_two_paths():

    assert find_all_paths(graph2, "a", "d") == ['a', 'b', 'd']
        

def test_there_is_three_path(): 
    
    assert find_all_paths(graph1, "a", "e") == [['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['a', 'e']]

def test_there_is_one_path(): 
    
    assert find_all_paths(graph1, "b", "d") == [['b', 'd']]

