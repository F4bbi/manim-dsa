from manim import *

from manim_dsa.m_collection.m_stack import *


class Random(Scene):
    def construct(self):
        stack = MStack([1], style=StackStyle.BLUE)
        self.play(Create(stack))
        self.play(stack.animate.append(8))
        self.play(stack.animate.pop())
        self.play(stack.animate.pop())
        self.play(stack.animate.scale(5))
        self.wait()
