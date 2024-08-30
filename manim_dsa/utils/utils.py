from __future__ import annotations

from manim import *
from manim.typing import Vector3D


def set_text(old_manim_text: Text, new_text: str):
    NewText = type(old_manim_text)
    res = (
        NewText(
            str(new_text), font=old_manim_text.font, font_size=old_manim_text.font_size
        )
        .match_style(old_manim_text)
        .move_to(old_manim_text)
    )
    return res


def TextReplace(scene, scene_mobj1, mObj1: Text, mObj2: Text):
    old_mobj = mObj1.copy()
    scene_mobj1 -= mObj1
    mObj1 = set_text(mObj1, str(mObj2.text))
    scene_mobj1 += mObj1
    new_mobj = mObj1.copy()
    mObj1.set_opacity(0)
    scene.play(
        ReplacementTransform(mObj2.copy(), new_mobj),
        ApplyMethod(old_mobj.set_opacity, 0),
    )
    mObj1.set_opacity(1)
    new_mobj.set_opacity(0)


class Labelable:
    def __init__(self):
        super().__init__()
        self.label = None

    def add_label(
        self, text: Text, direction: Vector3D = UP, buff: float = 0.5, **kwargs
    ):
        self.label = text
        self.label.next_to(self, direction, buff, **kwargs)
        return self

    def has_label(self):
        return self.label is not None


class Highlightable:
    def __init__(self):
        super().__init__()
        self.__target = None
        self.highlighting = None

    def _add_highlight(self, target: VMobject):
        self.__target = target
        self.highlighting = (
            target.copy().set_fill(opacity=0).set_z_index(self.__target.z_index + 1)
        )
        self.set_highlight()

    def highlight(self, stroke_color: ManimColor = RED, stroke_width: float = 8):
        self.set_highlight(stroke_color, stroke_width)
        # Since the target object could have been scaled or moved, scale and move self.highlighting
        self.highlighting.width = self.__target.width
        self.highlighting.height = self.__target.height
        self.highlighting.move_to(self.__target)
        self += self.highlighting
        return self

    @override_animate(highlight)
    def _highlight_animation(
        self, stroke_color: ManimColor = RED, stroke_width: float = 8, anim_args=None
    ):
        self.highlight(stroke_color, stroke_width)
        return Create(self.highlighting, **anim_args)

    def set_highlight(self, stroke_color: ManimColor = RED, stroke_width: float = 8):
        self.highlighting.set_stroke(stroke_color, stroke_width)

    def unhighlight(self):
        self -= self.highlighting
        return self

    @override_animate(unhighlight)
    def _unhighlight_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}

        self.unhighlight()
        return FadeOut(self.highlighting, **anim_args)
