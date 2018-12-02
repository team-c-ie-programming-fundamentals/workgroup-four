#%%

from graphs import find_path

def test_there_is_no_path(): 
    
    
    value =  {
                "a": ["b","c"],
                "b": ["c"],
                "c" : ["b", "d"],
                "d" : ["b"],
                }


    for case in value:
        
        assert find_path(case) == None