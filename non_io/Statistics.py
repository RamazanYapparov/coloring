import non_io.First_algorythm as First
import non_io.DualAlgorythm as Dual
import networkx as nx
import matplotlib.pyplot as plt

nodes = [5, 7, 10, 30, 55, 80, 100, 150]
nodes = [30]

# res = open("results", 'w')
# print()
#
# n = 5000
# m = 100000
# G = nx.gnm_random_graph(n, m)
# G = nx.gnp_random_graph(n, m)
# print(max(dict(G.degree()).values()))
# print(len(G.edges()))

for n in nodes:
    G = nx.complete_graph(n)
    m = 0
    result = Dual.do(G)
    nx.draw(G, pos=nx.circular_layout(G), edge_color=result[2])
    # picture = "complete_{}.png".format(n)
    # plt.savefig(picture)

# print(First.do(n, m, G))
# print(result)


plt.show()
