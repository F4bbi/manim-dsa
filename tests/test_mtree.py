from manim import *

from manim_dsa.m_graph.m_tree import *


class Init(Scene):
    def construct(self):
        tree = [["1", "2"], ["3", "4"], ["5", "6"], [], [], [], []]
        mTree = MTree(tree)
        self.play(Create(mTree))
        self.wait()


class ManyNodes(Scene):
    def construct(self):
        graph = {
            "0": [("1", 5), ("2", 3)],
            "1": [("3", 2), ("4", 7)],
            "2": [("5", 4), ("6", 1)],
            "3": [("7", 6), ("8", 3)],
            "4": [("9", 2)],
            "5": [("11", 8), ("12", 5)],
            "6": [],
            "7": [],
            "8": [],
            "9": [],
            "11": [],
            "12": [],
        }
        mGraph = MTree(graph)
        self.play(Create(mGraph))
        self.wait()
