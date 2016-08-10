import time

colors_dict = {0: "darkred", 1: "blue", 2: "red", 3: "green", 4: "yellow", 5: "purple", 6: "orange", 7: "white", 8: "black"}


def remove_redundant_nodes(g):
    degrees = g.degree()
    for i in range(len(degrees)):
        if degrees[i] == 0:
            g.remove_node(i)


def add_color(index, color, node_colors):
    temp = node_colors[index].copy()
    temp.append(color)
    node_colors[index] = temp


def color_graph(g, sortdict, node_colors, edge_colors):
    # прохождение по всем ребрам графа
    for node in sortdict:
        # список цветов смежных ребер
        except_colors = node_colors[node[0]].copy()
        for nodes in g.neighbors_iter(node[0]):
            # проверка раскрашенности ребра
            try:
                var = edge_colors[tuple(sorted([node[0]] + [nodes]))]
                continue
            except KeyError:
                if len(node_colors[nodes]) != 0:
                    except_colors.extend(node_colors[nodes])
            # нахождение подходящего цвета
            for color in range(len(g.nodes()) * 2):
                if color not in except_colors:
                    edge_colors[tuple(sorted([node[0]] + [nodes]))] = color
                    add_color(node[0], color, node_colors)
                    add_color(nodes, color, node_colors)
                    except_colors.append(color)
                    break


def do(g):
    remove_redundant_nodes(g)

    # вершины, отсортированные по степеням
    sortdict = sorted(dict(g.degree()).items(), key=lambda x: x[1], reverse=True)

    # цвета ребер
    edge_colors = dict()

    # цвета задействованные в вершинах
    node_colors = dict.fromkeys(g.nodes(), list())

    # начало отсчета времени работы алгоритма
    init_time = time.clock()

    # раскраска графа
    color_graph(g, sortdict, node_colors, edge_colors)

    # окончание работы алгоритма
    end_time = time.clock()

    # нахождение количества цветов
    max_color = max(edge_colors.values())
    return round(end_time - init_time, ndigits=4), max_color + 1

