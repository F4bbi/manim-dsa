from __future__ import annotations

from manim import *
from manim.typing import Vector3D

from manim_dsa.constants import *
from manim_dsa.m_collection.m_collection import MElement
from manim_dsa.utils.utils import *


class MVariable(MElement, Labelable):
    def __init__(
        self,
        value: str,
        style=VariableStyle.DEFAULT,
    ):
        self.style = style
        super().__init__(
            Rectangle(**self.style.square), Text(str(value), **self.style.value)
        )

    def add_label(
        self,
        text: Text,
        direction: Vector3D = UP,
        buff: float = 0.5,
        **kwargs,
    ):
        super().add_label(text, direction, buff, **kwargs)
        self += self.label
        return self
