from graphics import *
import math


def draw_line(x1, y1, x2, y2, win):

    ln = Line(Point(x1, y1), Point(x2, y2))
    ln.setOutline(color_rgb(0, 0, 0))
    ln.setWidth(2)
    ln.draw(win)


def draw_edge(e, edges_count, win, origin_x, origin_y):
    v1 = e.vertices[0]
    v2 = e.vertices[1]

    scale = 200
    text_scale = scale + 20

    x1 = scale * math.cos(2 * math.pi / edges_count * v1) + origin_x
    y1 = scale * math.sin(2 * math.pi / edges_count * v1) + origin_y
    t1 = Text(Point(text_scale * math.cos(2 * math.pi / edges_count * v1) + origin_x,
                    text_scale * math.sin(2 * math.pi / edges_count * v1) + origin_y), str(v1))
    t1.draw(win)

    x2 = scale * math.cos(2 * math.pi / edges_count * v2) + origin_x
    y2 = scale * math.sin(2 * math.pi / edges_count * v2) + origin_y
    t2 = Text(Point(text_scale * math.cos(2 * math.pi / edges_count * v2) + origin_x,
                    text_scale * math.sin(2 * math.pi / edges_count * v2) + origin_y), str(v2))
    t2.draw(win)

    r = 8
    c1 = Circle(Point(x1, y1), radius=r)
    c1.setFill(color_rgb(0,0,0))
    c1.draw(win)
    c2 = Circle(Point(x2, y2), radius=r)
    c2.setFill(color_rgb(0, 0, 0))
    c2.draw(win)

    draw_line(x1, y1, x2, y2, win)

    weight_text = Text(Point((x1 + x2) / 2, (y1 + y2) / 2), str(e.weight))
    weight_text.setFill(color_rgb(3, 161, 252))
    weight_text.setSize(25)
    weight_text.draw(win)


def draw(edge_set, mst, edges_count):
    w = 1200
    h = 700

    win = GraphWin('output', w, h)
    win.setBackground(color_rgb(245, 245, 245))
    for ed in edge_set:  # for drawing main graph
        draw_edge(ed, edges_count, win, w // 4, h // 2)

    for ed in mst:  # for drawing answer graph
        draw_edge(ed, edges_count, win, 3 * w // 4, h // 2)

    win.getMouse()
    win.close()


class Edge:
    def __init__(self, weight, vertex1, vertex2):
        self.weight = weight
        self.vertices = []
        self.vertices.append(vertex1)
        self.vertices.append(vertex2)

    def __str__(self):
        return str(self.vertices) + "   w="+str(self.weight)


def contains_cycle(sets, v):  # checks for cycle if we add the edge
    for s in sets:
        if v[0] in s and v[1] in s:
            return True
    return False


print()
print("If there is no edge between A and B put 0 in input")
print("Input number of vertices then enter the adjacency matrix")
print("Sample input for program you might wanna use:")
print("""
6
0 10 8 0 0 3
10 0 3 7 0 0
8 3 0 0 11 0
0 7 0 0 0 9
0 0 11 0 0 0
3 0 0 9 0 0
        """)
print(20*"- ")
n = int(input("Number of vertices: "))  # number of vertices
all_edges = []
for i in range(n):
    input_value = input().split()

    for j, value in enumerate(input_value):
        w = int(value)
        if i >= j or w == 0:  # we don't need to get all the values in adjacency matrix
            continue
        all_edges.append(Edge(w, i, j))

all_edges = sorted(all_edges, key=lambda edge: edge.weight)
print("~ ~ ~ ~ ~ INPUTS ~ ~ ~ ~ ~")
for e in all_edges:
    print(e)

sets = []   # for initial we have n sets containing each vertix
for i in range(n):
    sets.append([])
    sets[i].append(i)
T = []

copy_edges = all_edges.copy()  # make a copy of all edges

while len(T) < n-1:
    e = all_edges[0]  # pick the edge with least weight
    v = e.vertices
    if contains_cycle(sets, v):
        all_edges.remove(e)
    else:
        s1 = None
        s2 = None
        T.append(e)
        for i in sets:
            if v[0] in i:
                s1 = i

            if v[1] in i:
                s2 = i

        sets.remove(s2)
        sets.remove(s1)
        sets.append(s1 + s2)  # we merge two subsets

print("~ ~ ~ ~ ~ ANSWER ~ ~ ~ ~ ~")
for t in T:
    print(t)

# draw output
draw(copy_edges, T, n)

#
# 4
# 0 1 5 10
# 1 0 2 0
# 5 2 0 4
# 10 0 4 0

# 6
# 0 10 8 0 0 3
# 10 0 3 7 0 0
# 8 3 0 0 11 0
# 0 7 0 0 0 9
# 0 0 11 0 0 0
# 3 0 0 9 0 0
