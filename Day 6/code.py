import networkx as nx

file = open("input.txt","r")
lines = file.readlines()
file.close()

G=nx.DiGraph()

for line in lines:
    mass = line[0:3]
    orbit = line[4:7]

    G.add_nodes_from([mass,orbit])
    G.add_edge(mass,orbit)

paths_graph = nx.transitive_closure(G)
print(paths_graph.size())

G_undirected = G.to_undirected()
print(nx.shortest_path_length(G_undirected,source='SAN',target='YOU')-2)