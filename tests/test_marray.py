from manim import *

from manim_dsa.m_collection.m_array import *


class Init(Scene):
    def construct(self):
        mArray = (
            MArray([1, 2, 3, 4, 5], style=MArrayStyle.BLUE)
            .add_indexes()
            .scale(0.9)
            .add_label(Text("Array", font="Cascadia Code"))
        )
        self.play(Create(mArray))
        self.wait()


class RandomOperations(Scene):
    def construct(self):
        arr = [1, 2, 3]
        mArray = (
            MArray(arr, style=MArrayStyle.PURPLE)
            .add_indexes(DOWN)
            .add_label(Text("Array", font="Cascadia Code"), DOWN)
        )
        mArray.shift(UP * 1.5 + LEFT * 4)
        self.play(Create(mArray))
        self.play(mArray.animate.append(4))
        self.play(mArray.animate.append(5))
        self.play(mArray.animate.scale(0.5))
        self.play(mArray.animate.append(6))
        self.play(mArray.animate.append(7))
        self.play(mArray.animate.pop(0))
        self.play(mArray.animate.shift(RIGHT))
        self.play(mArray.animate.pop(2))
        self.play(mArray[0].value.animate.set_fill(RED))
        self.play(mArray[0].index.animate.set_fill(RED))
        self.play(mArray.animate.swap(0, 3, path_arc=PI / 2))
        self.play(mArray[0].value.animate.set_fill(GREEN))
        self.play(mArray[0].index.animate.set_fill(GREEN))
        self.wait(1)
