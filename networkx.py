#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:55:26 2018

@author: nataliecedeno
"""
#%%

G = {
        "a":["b","c"],
        "b":["d"],
        "c":["d"],
        "d":["e"],
        "e":[],
        "f":[]
        }

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from(["a","b","c","d","e","f"])
G.add_edges_from([("a", "b"), ("a", "c"), ("b", "d"), ("c", "d"), ("d","e")])

nx.draw(G,with_labels=True)
plt.draw()
plt.show()
#%%
def has_path(G,source,target):
    try:
        nx.shortest_path(G, source, target)
    except nx.NetworkXNoPath:
        return False
    return True

#%%
def shortest_path(G, source, target, weight, method='dijkstra'):
    if method not in ('dijkstra'):
        raise ValueError('method not supported: {}'.format(method))
    method = 'unweighted' if weight is None else method
    if source is None:
        if target is None:
            if method == 'unweighted':
                paths = dict(nx.all_pairs_shortest_path(G))
            elif method == 'dijkstra':
                paths = dict(nx.all_pairs_dijkstra_path(G, weight=weight))
        else:
            with nx.utils.reversed(G):
                if method == 'unweighted':
                    paths = nx.single_source_shortest_path(G, target)
                elif method == 'dijkstra':
                    paths = nx.single_source_dijkstra_path(G, target,weight=weight)
                for target in paths:
                    paths[target] = list(reversed(paths[target]))
    else:
        if target is None:
            if method == 'unweighted':
                paths = nx.single_source_shortest_path(G, source)
            elif method == 'dijkstra':
                paths = nx.single_source_dijkstra_path(G, source, weight=weight)
        else:
            if method == 'unweighted':
                paths = nx.bidirectional_shortest_path(G, source, target)
            elif method == 'dijkstra':
                paths = nx.dijkstra_path(G, source, target, weight)
    return paths
#%%
