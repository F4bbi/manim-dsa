from manim import *

from manim_dsa.m_variable.m_variable import *


class Init(Scene):
    def construct(self):
        mVariable = MVariable(5).add_label(
            Text("myVar", font="Cascadia Code", font_size=36), LEFT
        )
        self.play(Create(mVariable))
        self.wait()


class CustomCreation(Scene):
    def construct(self):
        mVariable = MVariable(5, style=MVariableStyle.BLUE).add_label(
            Text("myVar", font="Cascadia Code", font_size=36), LEFT
        )
        self.play(Create(mVariable))
        self.wait()


class SetValue(Scene):
    def construct(self):
        mVariable = MVariable(5, style=MVariableStyle.BLUE).add_label(
            Text("myVar", font="Cascadia Code", font_size=36), LEFT
        )
        self.play(Create(mVariable))
        self.wait()
        self.play(mVariable.animate.set_value(10))
        self.wait()


class TwoVariables(Scene):
    def construct(self):
        mVariable1 = MVariable(5, style=MVariableStyle.BLUE)
        mVariable2 = MVariable(10, style=MVariableStyle.BLUE).next_to(
            mVariable1, DOWN, buff=0
        )

        style = {"font": "Cascadia Code", "font_size": 18}

        weight_label = Text("Weight", **style)
        node_label = Text("Node", **style)

        mVariable1.add_label(node_label, LEFT)
        mVariable2.add_label(weight_label, LEFT)

        self.play(Create(mVariable1))
        self.play(Create(mVariable2))
        self.play(mVariable2.animate.highlight())
        self.wait()
