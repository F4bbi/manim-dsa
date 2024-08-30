from manim import *

from manim_dsa.m_collection.m_array import *
from manim_dsa.m_collection.m_stack import *
from manim_dsa.m_graph.m_graph import *
from manim_dsa.m_variable.m_variable import *


class DfsIterative(Scene):
    def dfs(self, graph, mGraph, mStack, start):
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
        start = "0"

        title = Text("Depth-First Search in un grafo", font="Cascadia Code").to_edge(UP)
        self.play(Create(title))
        mGraph = (
            MGraph(graph, style=GraphStyle.PURPLE).node_layout().to_edge(LEFT).shift(DR)
        )
        mStack = (
            MStack([1, 2, 3], style=StackStyle.BLUE).scale(0.7).to_edge(RIGHT).shift(DL)
        )
        mArray = MArray([1, 2, 3], style=ArrayStyle.BLUE).add_indexes().scale(0.5)
        self.play(Create(mGraph))
        self.play(Create(mStack))

        # self.dfs(graph, mGraph, mStack, start)
        # TODO
        # Add MTree, fix MGraph add curved edge and backward edge, add MPointer, add MSlidingWindow, add weight inside line
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
        mGraph = MGraph(
            graph, nodes_and_positions, graph_config=GraphStyle.GREEN
        ).move_to(ORIGIN)

        self.play(Create(mGraph))
        self.play(mGraph.animate.add_node("8", position=DOWN * 2), run_time=5)
        self.play(mGraph.animate.add_edge("3", "8", 1))
        self.play(mGraph.animate.shift(UP))
        mGraph["0"].set_highlight(RED, 8.0)
        self.play(mGraph["0"].animate.highlight())
        self.play(mGraph[("0", "1")].animate.highlight())
        self.play(mGraph["1"].animate.highlight())
        self.wait()


class FourNodes(Scene):
    def construct(self):
        graph = {
            "A": [("B", 5), ("C", 11), ("D", 7)],
            "B": [("A", 5), ("C", 3)],
            "C": [("A", 11), ("B", 3)],
            "D": [("A", 7)],
        }
        mGraph = MGraph(graph, style=GraphStyle.BLUE)
        mGraph.node_layout("canial").scale(1.5)
        self.play(Create(mGraph))
        self.play(mGraph.animate.add_curved_edge("C", "D", 4))
        self.play(mGraph.animate.add_curved_edge("D", "C", 4))
        mGraph[("C", "D")].highlighting.rotate(PI)
        mGraph[("C", "D")].highlighting.flip(DL)
        self.play(mGraph[("C", "D")].animate.highlight())


"""
class NodeLayout(Scene):
    def construct(self):
        graph = {
            "0": ["1", "2"],
            "1": ["3", "4"],
            "2": ["5", "6"],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
        }
        mGraph = MTree(graph, "0")
        self.play(Create(mGraph))
        self.wait()
"""


class Test(Scene):
    def construct(self):
        graph = {
            "0": ["1", "2"],
            "1": [],
            "2": [],
        }
        nodes_and_pos = {
            "0": LEFT * 5,
            "1": RIGHT,
            "2": DOWN,
        }
        mGraph = MGraph(graph, nodes_and_pos)
        self.play(Create(mGraph))
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
            MArray([1, 2, 3], style=ArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array", font="Cascadia Code"))
            .to_edge(LEFT, 1)
        )

        mStack = (
            MStack([3, 7, 98, 1], style=StackStyle.GREEN)
            .scale(0.8)
            .add_label(Text("Stack", font="Cascadia Code"))
            .move_to(ORIGIN)
        )

        mGraph = (
            MGraph(graph, nodes_and_positions, GraphStyle.PURPLE)
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
        #dsa = Text("DSA", font="CMU Serif").scale(2).next_to(manim, DOWN, DEFAULT_MOBJECT_TO_MOBJECT_BUFFER, RIGHT).shift(RIGHT*2)
        #obj = VGroup(manim, dsa).move_to(ORIGIN)
        style = ArrayStyle.GREEN
        style.value["font"] = "Javiera"
        mArray = (
            MArray(["D", "S", "A"], style=style)
            .add_indexes(DOWN)
            .shift(DOWN * 1.3 + RIGHT * 2.5)
        )
        self.play(Create(manim))
        self.play(Create(mArray))
        
        vertices = [1, 2, 3, 4]
        edges = [(1, 2), (2, 3), (3, 4), (1, 3), (1, 4)]
        g = Graph(vertices, edges, layout="planar", vertex_config={1: {"fill_color": ManimColor("#38f4af")}, 2: {"fill_color": ManimColor("#38f4af")}, 3: {"fill_color": ManimColor("#38f4af")}, 4: {"fill_color": ManimColor("#38f4af")}})
        g[2].move_to([0, 0, 0])
        g[1].move_to([3, -.1, 0])
        g[3].move_to([2.2, -.4, 0])
        g[4].move_to([2.5, -0.8, 0])
        self.play(Create(g.shift([.7, .37, 0])))
        self.play(VGroup(manim, mArray, g).animate.move_to(ORIGIN))
        self.wait()