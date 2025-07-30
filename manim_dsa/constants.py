from __future__ import annotations

import networkx as nx
from manim import BLUE_A, BLUE_B, BLUE_D, BOLD, GRAY, RED, WHITE, ManimColor

type GraphType = (
    nx.DiGraph
    # Example: [['1','2'], ['0'], ['0']] is (1)---(0)---(2)
    | list[list[str]]
    # Example: {'A':['B','C'], 'B':[], 'C':[]]} is (B)<--(A)-->(C)
    | dict[str, list[str]]
    # Example: [[('1', 3), ('2', 1)], [('0', 3)], [('0', 1)]] is (1)--<3>-(0)-<1>--(2)
    | list[list[tuple[str, str | int]]]
    # Example: {'A':[('B', 9), ('C', 2)], 'B':[], 'C':[]} is (B)<-<9>-(A)-<2>->(C)
    | dict[str, list[tuple[str, str | int]]]
)


class MGraphStyle:
    class _DefaultStyle:
        def __init__(self):
            self.node_circle: dict = {"color": WHITE, "stroke_width": 6, "radius": 0.33}
            self.node_label: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
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
                "font_size": 24,
                "disable_ligatures": True,
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


class MTreeStyle(MGraphStyle):
    class _DefaultStyle(MGraphStyle._DefaultStyle):
        def __init__(self):
            super().__init__()
            self.horizontal_gap: float = 10.0
            self.vertical_gap: float = 2.0

    class _BlueStyle(_DefaultStyle, MGraphStyle._BlueStyle):
        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, MGraphStyle._PurpleStyle):
        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, MGraphStyle._GreenStyle):
        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MCollectionStyle:
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
                "disable_ligatures": True,
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


class MStackStyle(MCollectionStyle):
    class _DefaultStyle(MCollectionStyle._DefaultStyle):
        def __init__(self):
            super().__init__()
            self.container: dict = {"color": RED}

    class _BlueStyle(_DefaultStyle, MCollectionStyle._BlueStyle):
        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, MCollectionStyle._PurpleStyle):
        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, MCollectionStyle._GreenStyle):
        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MArrayStyle(MCollectionStyle):
    class _DefaultStyle(MCollectionStyle._DefaultStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _BlueStyle(_DefaultStyle, MCollectionStyle._BlueStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": BLUE_D,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _PurpleStyle(_DefaultStyle, MCollectionStyle._PurpleStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": ManimColor("#fabcff"),
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _GreenStyle(_DefaultStyle, MCollectionStyle._GreenStyle):
        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MVariableStyle(MCollectionStyle):
    pass


# -----------Label configs-----------
DEFAULT_LABEL_ARGS: dict = {"color": BLUE_A, "font": "Cascadia Code", "font_size": 40}
