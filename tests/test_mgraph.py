import heapq

from manim import *

from manim_dsa.m_collection.m_array import *
from manim_dsa.m_collection.m_stack import *
from manim_dsa.m_graph.m_graph import *
from manim_dsa.m_variable.m_variable import *


class IterativeDfs(Scene):
    def dfs(self, graph, start):
        mGraph = (
            MGraph(graph, style=MGraphStyle.PURPLE)
            .scale(0.9)
            .node_layout()
            .to_edge(LEFT)
            .shift(DR)
        )
        mStack = MStack(style=MStackStyle.BLUE).scale(0.7).to_edge(RIGHT).shift(DL)
        self.play(Create(mGraph))
        self.play(Create(mStack))
        visited = {}
        stack = [start]
        prevList = [None]
        self.play(mStack.animate.append(start))
        for node in graph:
            visited[node] = False
        while stack:
            node = stack.pop()
            self.play(mStack.animate.pop())
            prev = prevList.pop()
            if prev and not visited[node]:
                self.play(mGraph[(prev, node)].animate.highlight())
            if not visited[node]:
                self.play(mGraph[node].animate.highlight())
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    self.play(mStack.animate.append(neighbor))
                    prevList.append(node)

    def construct(self):
        graph = {
            "0": ["1", "2"],
            "1": ["0", "2", "3", "4"],
            "2": ["0", "1"],
            "3": ["1", "5"],
            "4": ["1"],
            "5": ["3", "6", "7", "8"],
            "6": ["5"],
            "7": ["5", "8"],
            "8": ["5", "7", "9"],
            "9": ["8"],
        }
        start = "0"
        title = Text("Depth-First Search in a graph", font="Cascadia Code").to_edge(UP)
        self.play(Create(title))
        self.dfs(graph, start)
        self.wait()


class Random(Scene):
    def construct(self):
        graph = {
            "0": [("1", 2), ("2", 4)],
            "1": [("0", 2), ("2", 1), ("3", 5)],
            "2": [("0", 4), ("1", 1)],
            "3": [("1", 5), ("4", 2)],
            "4": [("3", 2), ("5", 2), ("6", 1)],
            "5": [("4", 2), ("6", 6)],
            "6": [("4", 1), ("5", 6), ("7", 3)],
            "7": [("6", 3)],
        }

        nodes_and_positions = {
            "0": LEFT * 4,
            "1": LEFT * 2 + UP,
            "2": LEFT * 2 + DOWN,
            "3": ORIGIN,
            "4": RIGHT * 2,
            "5": RIGHT * 4 + DOWN,
            "6": RIGHT * 4 + UP,
            "7": RIGHT * 7 + UP,
        }
        mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.GREEN).move_to(
            ORIGIN
        )

        self.play(Create(mGraph))
        self.play(mGraph.animate.add_node("8", position=DOWN * 2), run_time=5)
        self.play(mGraph.animate.add_edge("3", "8", 1))
        self.play(mGraph.animate.shift(UP))
        mGraph["0"].set_highlight(RED, 8.0)
        self.play(mGraph["0"].animate.highlight())
        self.play(mGraph[("0", "1")].animate.highlight())
        self.play(mGraph["1"].animate.highlight())
        self.wait()


class ShowBackwardsEdge(Scene):
    def construct(self):
        graph = {"0": [("1", 4), ("2", 3)], "1": [], "2": []}

        nodes_and_positions = {
            "0": LEFT * 2 + UP * 2,
            "1": LEFT * 2 + DOWN * 2,
            "2": RIGHT * 2 + UP * 2,
        }

        mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.GREEN)

        self.play(Create(mGraph))
        self.play(mGraph.animate.show_backward_edge("0", "2", 3, 0))
        self.wait()


class ReadMe(Scene):
    def construct(self):
        graph = {
            "A": [("C", 11), ("D", 7)],
            "B": [("A", 5), ("C", 3)],
            "C": [("A", 11), ("B", 3)],
            "D": [("A", 7), ("C", 4)],
        }
        nodes_and_positions = {
            "A": LEFT * 1.5,
            "B": UP * 2,
            "C": RIGHT * 1.5,
            "D": DOWN * 2,
        }

        mArray = (
            MArray([1, 2, 3], style=MArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array", font="Cascadia Code"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=MStackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack", font="Cascadia Code"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, MGraphStyle.PURPLE)
            .add_label(Text("Graph", font="Cascadia Code"))
            .to_edge(RIGHT, 1)
        )

        self.play(Create(mArray))
        self.play(Create(mStack))
        self.play(Create(mGraph))
        self.wait()


class Logo(Scene):
    def construct(self):
        manim = Text("Manim", font="CMU Serif").scale(2).move_to(ORIGIN)
        # dsa = Text("DSA", font="CMU Serif").scale(2).next_to(manim, DOWN, DEFAULT_MOBJECT_TO_MOBJECT_BUFFER, RIGHT).shift(RIGHT*2)
        # obj = VGroup(manim, dsa).move_to(ORIGIN)
        style = MArrayStyle.PURPLE
        style.value["font"] = "Javiera"
        style.value["weight"] = BOLD
        mArray = (
            MArray(["D", "S", "A"], style=style)
            .add_indexes(DOWN)
            .shift(DOWN * 1.3 + RIGHT * 2.5)
        )
        self.play(Create(manim))
        self.play(Create(mArray))

        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(
            vertices,
            edges,
            layout="planar",
            vertex_config={
                1: {"fill_color": ManimColor("#38f4af")},
                2: {"fill_color": ManimColor("#38f4af")},
                3: {"fill_color": ManimColor("#38f4af")},
                4: {"fill_color": ManimColor("#38f4af")},
            },
        )
        g[2].move_to([0, 0, 0])
        g[1].move_to([3, -0.1, 0])
        g[3].move_to([2.2, -0.4, 0])
        g[4].move_to([2.5, -0.8, 0])
        self.play(Create(g.shift([0.7, 0.37, 0])))
        self.play(VGroup(manim, mArray, g).animate.move_to(ORIGIN))
        self.wait()


class DfsRecursive(Scene):
    def dfs_helper(self, graph, mGraph, visited, prev, root):
        visited[root] = True
        self.play(mGraph[root].animate.highlight())
        for adj in graph[root]:
            if not visited[adj]:
                self.play(mGraph[(root, adj)].animate.highlight())
                self.dfs_helper(graph, mGraph, visited, prev, adj)
                self.play(mGraph[(root, adj)].animate.unhighlight())
        self.play(mGraph[root].animate.unhighlight())

    def dfs(self, graph, mGraph):
        visited = {}

        for node in graph:
            visited[node] = False

        for node in graph:
            if not visited[node]:
                self.dfs_helper(graph, mGraph, visited, None, node)

    def construct(self):
        graph = {
            "0": ["1", "2"],
            "1": ["0", "2", "3", "4"],
            "2": ["0", "1"],
            "3": ["1", "5"],
            "4": ["1"],
            "5": ["3", "6", "7", "8"],
            "6": ["5"],
            "7": ["5", "8"],
            "8": ["5", "7", "9"],
            "9": ["8"],
        }

        nodes_and_positions = {
            "0": LEFT * 6,
            "1": LEFT * 4 + UP,
            "2": LEFT * 4 + DOWN,
            "3": LEFT * 2,
            "4": LEFT * 2 + UP * 2,
            "5": ORIGIN,
            "6": LEFT * 2 + DOWN * 2,
            "7": RIGHT * 2 + DOWN * 2,
            "8": RIGHT * 2 + UP * 2,
            "9": RIGHT * 4 + UP * 2,
        }

        mGraph = (
            MGraph(graph, nodes_and_positions, style=MGraphStyle.BLUE)
            .move_to(ORIGIN)
            .shift(DOWN / 2)
        )

        title = Text("Depth-First Search in a graph", font="Cascadia Code").to_edge(UP)

        self.play(Create(title))
        self.play(Create(mGraph))

        self.dfs(graph, mGraph)
        self.wait()


class Kruskal(Scene):
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self, graph, nodes_and_positions):
        mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.PURPLE).move_to(
            ORIGIN
        )
        self.play(Create(mGraph))

        edges = []
        for u in graph:
            for v, weight in graph[u]:
                if (weight, u, v) not in edges and (weight, v, u) not in edges:
                    edges.append((weight, u, v))
        edges.sort()

        parent = {}
        rank = {}

        for node in graph:
            parent[node] = node
            rank[node] = 0

        mst_weight = 0

        for edge in edges:
            wt, u, v = edge
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                self.play(mGraph[(u, v)].animate.highlight(GREEN, 12))
                mst_weight += wt
                self.union(parent, rank, x, y)
            else:
                self.play(mGraph[(u, v)].animate.highlight(RED, 12))

        return mst_weight

    def construct(self):
        graph = {
            "0": [("1", 2), ("2", 4)],
            "1": [("0", 2), ("2", 1), ("3", 5), ("4", 5)],
            "2": [("0", 4), ("1", 1)],
            "3": [("1", 5), ("5", 2)],
            "4": [("1", 5)],
            "5": [("3", 2), ("6", 7), ("7", 2), ("8", 1)],
            "6": [("5", 7)],
            "7": [("5", 2), ("8", 6)],
            "8": [("5", 1), ("7", 6), ("9", 3)],
            "9": [("8", 3)],
        }

        nodes_and_positions = {
            "0": LEFT * 6,
            "1": LEFT * 4 + UP * 2,
            "2": LEFT * 4 + DOWN * 2,
            "3": LEFT * 2,
            "4": LEFT * 2 + UP * 2,
            "5": ORIGIN + RIGHT,
            "6": LEFT + DOWN * 2,
            "7": RIGHT * 3 + DOWN * 2,
            "8": RIGHT * 3 + UP * 2,
            "9": RIGHT * 5 + UP * 2,
        }

        title = (
            Text("Kruskal’s Algorithm for Minimum Spanning Tree", font="Cascadia Code")
            .scale(0.7)
            .to_edge(UP)
        )
        self.play(Create(title))
        total_weight = self.kruskal(graph, nodes_and_positions)
        text = Text("Total: " + str(total_weight), font="Cascadia Code").to_edge(DOWN)
        self.play(Create(text))
        self.wait()


class Prim(Scene):
    def prim(self, graph, nodes_and_positions, start):
        pq = []
        visited = {}
        mGraph = MGraph(graph, nodes_and_positions, style=MGraphStyle.PURPLE).move_to(
            ORIGIN
        )
        self.play(Create(mGraph))

        for node in graph:
            visited[node] = False

        res = 0

        heapq.heappush(pq, (0, None, start))

        while pq:
            wt, prev_node, u = heapq.heappop(pq)
            if visited[u]:
                self.play(mGraph[(prev_node, u)].animate.highlight(RED))
                continue

            visited[u] = True
            res += wt

            if prev_node is not None:
                self.play(mGraph[(prev_node, u)].animate.highlight(GREEN))

            self.play(mGraph[u].animate.highlight(GREEN))

            for adj in graph[u]:
                v, weight = adj
                if not visited[v]:
                    heapq.heappush(pq, (weight, u, v))
                    self.play(mGraph[(u, v)].animate.highlight(BLUE))

        return res

    def construct(self):
        graph = {
            "0": [("1", 2), ("2", 4)],
            "1": [("0", 2), ("2", 1), ("3", 5), ("4", 5)],
            "2": [("0", 4), ("1", 1)],
            "3": [("1", 5), ("5", 2)],
            "4": [("1", 5)],
            "5": [("3", 2), ("6", 7), ("7", 2), ("8", 1)],
            "6": [("5", 7)],
            "7": [("5", 2), ("8", 6)],
            "8": [("5", 1), ("7", 6), ("9", 3)],
            "9": [("8", 3)],
        }

        nodes_and_positions = {
            "0": LEFT * 6,
            "1": LEFT * 4 + UP,
            "2": LEFT * 4 + DOWN,
            "3": LEFT * 2,
            "4": LEFT * 2 + UP * 2,
            "5": ORIGIN,
            "6": LEFT * 2 + DOWN * 2,
            "7": RIGHT * 2 + DOWN * 2,
            "8": RIGHT * 2 + UP * 2,
            "9": RIGHT * 4 + UP * 2,
        }

        title = (
            Text("Prim's Algorithm for Minimum Spanning Tree", font="Cascadia Code")
            .scale(0.7)
            .to_edge(UP)
        )
        self.play(Create(title))
        total_weight = self.prim(graph, nodes_and_positions, "0")
        text = Text("Total: " + str(total_weight), font="Cascadia Code").to_edge(DOWN)
        self.play(Create(text))
        self.wait()
