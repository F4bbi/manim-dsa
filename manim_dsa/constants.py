from __future__ import annotations

from manim import *


class MGraphStyle:
    class _DefaultStyle:
        def __init__(self):
            self.node_circle: dict = {"color": WHITE, "stroke_width": 6, "radius": 0.33}
            self.node_label: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 32,
                "weight": BOLD,
            }
            self.edge_line: dict = {
                "color": GRAY,
                "stroke_width": 7,
            }
            self.edge_tip: dict = {
                "stroke_width": 0.5,
                "fill_opacity": 1,
                "color": GRAY,
            }
            self.edge_weight: dict = {
                "color": WHITE,
                "font_size": 21,
                "font": "Javiera",
                "weight": BOLD,
            }
            self.start_distance: float = 0.2

    class _BlueStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.node_circle: dict = {
                "color": BLUE_B,
                "fill_color": BLUE_D,
                "stroke_width": 6,
                "fill_opacity": 0.75,
                "radius": 0.33,
            }

    class _PurpleStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.node_circle: dict = {
                "color": ManimColor("#eb97fc"),
                "fill_color": ManimColor("#8c46d6"),
                "stroke_width": 6,
                "fill_opacity": 0.75,
                "radius": 0.33,
            }

    class _GreenStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.node_circle: dict = {
                "color": ManimColor("#b2ff8c"),
                "fill_color": ManimColor("#2ea556"),
                "stroke_width": 6,
                "fill_opacity": 0.75,
                "radius": 0.33,
            }

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class CollectionStyle:
    class _DefaultStyle:
        def __init__(self):
            self.square: dict = {
                "color": WHITE,
                "stroke_width": 6,
                "width": 1,
                "height": 1,
            }
            self.value: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 48,
                "weight": BOLD,
            }

    class _BlueStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.square: dict = {
                "color": BLUE_B,
                "fill_color": BLUE_D,
                "stroke_width": 6,
                "fill_opacity": 1,
                "width": 1,
                "height": 1,
            }

    class _PurpleStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.square: dict = {
                "color": ManimColor("#eb97fc"),
                "fill_color": ManimColor("#8c46d6"),
                "fill_opacity": 1,
                "stroke_width": 6,
                "width": 1,
                "height": 1,
            }

    class _GreenStyle(_DefaultStyle):
        def __init__(self):
            super().__init__()
            self.square: dict = {
                "color": ManimColor("#b2ff8c"),
                "fill_color": ManimColor("#2ea556"),
                "fill_opacity": 1,
                "stroke_width": 6,
                "width": 1,
                "height": 1,
            }

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MStackStyle(CollectionStyle):
    class _DefaultStyle(CollectionStyle._DefaultStyle):
        def __init__(self):
            super().__init__()
            self.container: dict = {"color": RED}

    class _BlueStyle(_DefaultStyle, CollectionStyle._BlueStyle):
        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, CollectionStyle._PurpleStyle):
        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, CollectionStyle._GreenStyle):
        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MArrayStyle(CollectionStyle):
    class _DefaultStyle(CollectionStyle._DefaultStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 31,
            }

    class _BlueStyle(_DefaultStyle, CollectionStyle._BlueStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": BLUE_D,
                "font": "Cascadia Code",
                "font_size": 31,
            }

    class _PurpleStyle(_DefaultStyle, CollectionStyle._PurpleStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": ManimColor("#fabcff"),
                "font": "Cascadia Code",
                "font_size": 31,
            }

    class _GreenStyle(_DefaultStyle, CollectionStyle._GreenStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 31,
            }

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class VariableStyle(CollectionStyle):
    pass


# -----------Label configs-----------
DEFAULT_LABEL_ARGS: dict = {"color": BLUE_A, "font": "Cascadia Code", "font_size": 40}
