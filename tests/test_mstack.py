from manim import *

from manim_dsa.m_collection.m_stack import *


class Random(Scene):
    def construct(self):
        stack = MStack([1], style=MStackStyle.BLUE)
        self.play(Create(stack))
        self.play(stack.animate.append(8))
        self.play(stack.animate.pop())
        self.play(stack.animate.pop())
        self.play(stack.animate.scale(5))
        self.wait()


class StackOverflow(Scene):
    def construct(self):
        stack = MStack([1,2,3], style=MStackStyle.BLUE).scale(0.8).shift(DOWN * 2)
        self.play(Create(stack))
        self.play(stack.animate.append(8))
        self.play(stack.animate.append(9))
        self.play(stack.animate.append(10))
        self.play(stack.animate.append(11))
