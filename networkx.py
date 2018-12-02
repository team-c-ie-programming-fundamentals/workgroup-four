import networkx as nx
import matplotlib.pyplot as plt


# Here we create a directed graph with the functions that are included in 
#networkx library


g = nx.DiGraph()

g.add_edge('a', 'b',weight=5)
g.add_edge('a', 'c',weight=5)
g.add_edge('b', 'd',weight=5)
g.add_edge('c', 'd',weight=10)
g.add_node('e')
g.add_edge('d', 'e', weight=1)
g.add_node('f')

#Network X Functions:
#%%
nx.has_path(g, 'a', 'd') #True
#%%
nx.has_path(g, 'a', 'e') #True
#%%
nx.has_path(g, 'a', 'f') #Fale
#%%
nx.dijkstra_path_length(g,"a","e") 
#%%
nx.dijkstra_path_length(g,"a","b") 
#%%
nx.shortest_path(g, 'a', 'e', weight='weight')


#%% 
#Drawing the graph with different attributes
nx.draw(g, node_size = 800, node_color="yellow", with_labels = True, font_weight="bold")
plt.show()