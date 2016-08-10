import networkx as nx
import time

colors_dict = {0: "darkred", 1: "blue", 2: "red", 3: "green", 4: "yellow", 5: "purple", 6: "orange", 7: "white",
               8: "black"}


def remove_redundant_nodes(g):
    degrees = g.degrees()
    for i in g.nodes():
        if degrees[i] == 0:
            g.remove_node(i)


def add_color(node, k, color_dict, colored_nodes):
    temp = list(color_dict[k])
    temp.append(tuple(node))
    color_dict[k] = temp
    colored_nodes.append(node)


def color_node(g, color_dict, colored_nodes):
    color_dict[0] = [(g.nodes()[0])]
    colored_nodes.append((g.nodes()[0]))


def color_graph(g, color_dict, colored_nodes):
    k = -1
    while len(colored_nodes) != len(g.nodes()):
        k += 1
        do_iter(g, k, color_dict, colored_nodes)


def do_iter(g, k, color_dict, colored_nodes):
    # выбор неокрашенной вершины
    for node in g.nodes():

        if node in colored_nodes:
            continue

        try:
            color_dict[k]
        except KeyError:
            color_dict[k] = [node]
            colored_nodes.append(node)
            continue

        # если вершина не смежна с остальными вершинами цвета k - окрашиваем ее
        flag = True
        for node_ in color_dict[k]:
            if (node not in g.neighbors_iter(node_)) and (node != node_):
                pass
            else:
                flag = False
        if flag:
            add_color(node, k, color_dict, colored_nodes)


def create_colormap(g, edge_colors):
    colors = []
    for i in g.edges():
        colors.append(edge_colors[i])
    return colors


def do(l):
    remove_redundant_nodes(l)
    # превращение нашего графа в двойственный
    g = nx.line_graph(l)

    # список цветов и соответствующим им вершин
    color_dict = dict()
    # список покрашенных вершин
    colored_nodes = []

    # начало отсчета времени работы алгоритма
    init_time = time.clock()

    # покраска первой вершины
    color_node(g, color_dict, colored_nodes)
    # покраска остальных вершин
    color_graph(g, color_dict, colored_nodes)

    # окончание работы алгоритма
    end_time = time.clock()

    # нахождение количества цветов

    max_color = len(color_dict.keys())
    return round(end_time - init_time, ndigits=4), max_color
