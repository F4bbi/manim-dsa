from __future__ import annotations

from typing import TypeAlias

import networkx as nx
from manim import BLUE_B, BLUE_D, BOLD, GRAY, RED, WHITE, ManimColor

GraphType: TypeAlias = (
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
"""Type alias for graph representations.

This union type defines all the acceptable formats for representing graphs in Manim DSA:

- :class:`networkx.DiGraph`: A NetworkX directed graph object
- ``list[list[str]]``: Adjacency list with indexes as node names
- ``dict[str, list[str]]``: Adjacency dictionary with string node names
- ``list[list[tuple[str, str | int]]]``: Weighted adjacency list with (node, weight) tuples and indexes as node names
- ``dict[str, list[tuple[str, str | int]]]``: Weighted adjacency dictionary with (node, weight) tuples

"""


class MGraphStyle:
    """Style configuration for :class:`~manim_dsa.m_graph.m_graph.MGraph` visualization.

    This class provides predefined style configurations that control the appearance
    of graph nodes, edges, labels, and other visual elements. Each style variant
    includes settings for colors, fonts, sizes, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MGraphStyle._DefaultStyle`
        A default style configuration for graphs.
    BLUE : :class:`MGraphStyle._BlueStyle`
        A blue style configuration for graphs.
    PURPLE : :class:`MGraphStyle._PurpleStyle`
        A purple style configuration for graphs.
    GREEN : :class:`MGraphStyle._GreenStyle`
        A green style configuration for graphs.
    """

    class _DefaultStyle:
        """Default style configuration for graphs.

        Provides a clean, minimal appearance with white elements on transparent backgrounds.
        This serves as the base style that other variants can inherit from and modify.

        Attributes
        ----------
        node_circle : dict
            Configuration for the appearance of graph nodes, including color, stroke width, and radius.
        edge_line : dict
            Configuration for the appearance of graph edges, including color and stroke width.
        edge_tip : dict
            Configuration for the appearance of edge tips, including stroke width, fill opacity, and color.
        edge_weight : dict
            Configuration for the appearance of edge weight labels, including color, font size, and font.
        start_distance : float
            Distance from edge to the weight label.
        """

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
        """Blue style configuration for graphs.

        Inherits from :class:`~manim_dsa.constants.MGraphStyle._DefaultStyle` and modifies the node circle color
        and fill color to blue shades, providing a visually distinct appearance for graph nodes.
        """

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
        """Purple style configuration for graphs.

        Inherits from :class:`~manim_dsa.constants.MGraphStyle._DefaultStyle` and modifies the node circle color
        and fill color to purple shades, providing a visually distinct appearance for graph nodes.
        """

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
        """Green style configuration for graphs.

        Inherits from :class:`~manim_dsa.constants.MGraphStyle._DefaultStyle` and modifies the node circle color
        and fill color to green shades, providing a visually distinct appearance for graph nodes.
        """

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
    """Style configuration for :class:`~manim_dsa.m_graph.m_tree.MTree` visualization.

    This class provides predefined style configurations that control the appearance
    of tree nodes, edges, labels, and layout properties. Each style variant
    includes settings for colors, fonts, sizes, spacing, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MTreeStyle._DefaultStyle`
        A default style configuration for trees.
    BLUE : :class:`MTreeStyle._BlueStyle`
        A blue style configuration for trees.
    PURPLE : :class:`MTreeStyle._PurpleStyle`
        A purple style configuration for trees.
    GREEN : :class:`MTreeStyle._GreenStyle`
        A green style configuration for trees.
    """

    class _DefaultStyle(MGraphStyle._DefaultStyle):
        """Default style configuration for trees.

        Inherits from :class:`~manim_dsa.constants.MGraphStyle._DefaultStyle` and adds tree-specific
        layout properties for horizontal and vertical spacing between nodes.

        Attributes
        ----------
        horizontal_gap : float
            The horizontal spacing between sibling nodes in the tree.
        vertical_gap : float
            The vertical spacing between parent and child nodes in the tree.
        """

        def __init__(self):
            super().__init__()
            self.horizontal_gap: float = 10.0
            self.vertical_gap: float = 2.0

    class _BlueStyle(_DefaultStyle, MGraphStyle._BlueStyle):
        """Blue style configuration for trees.

        Combines the tree layout properties from :class:`~manim_dsa.constants.MTreeStyle._DefaultStyle`
        with the blue color scheme from :class:`~manim_dsa.constants.MGraphStyle._BlueStyle`.
        """

        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, MGraphStyle._PurpleStyle):
        """Purple style configuration for trees.

        Combines the tree layout properties from :class:`~manim_dsa.constants.MTreeStyle._DefaultStyle`
        with the purple color scheme from :class:`~manim_dsa.constants.MGraphStyle._PurpleStyle`.
        """

        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, MGraphStyle._GreenStyle):
        """Green style configuration for trees.
        Combines the tree layout properties from :class:`~manim_dsa.constants.MTreeStyle._DefaultStyle`
        with the green color scheme from :class:`~manim_dsa.constants.MGraphStyle._GreenStyle`.
        """

        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MCollectionStyle:
    """Style configuration for :class:`~manim_dsa.m_collection.m_collection.MCollection` visualization.

    This class provides predefined style configurations that control the appearance
    of collection elements including squares, text values, and other visual properties.
    Each style variant includes settings for colors, fonts, sizes, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MCollectionStyle._DefaultStyle`
        A default style configuration for collections.
    BLUE : :class:`MCollectionStyle._BlueStyle`
        A blue style configuration for collections.
    PURPLE : :class:`MCollectionStyle._PurpleStyle`
        A purple style configuration for collections.
    GREEN : :class:`MCollectionStyle._GreenStyle`
        A green style configuration for collections.
    """

    class _DefaultStyle:
        """Default style configuration for collections.

        Provides a clean, minimal appearance with white elements on transparent backgrounds.
        This serves as the base style that other collection variants can inherit from and modify.

        Attributes
        ----------
        square : dict
            Configuration for the appearance of collection element squares, including color, stroke width, and dimensions.
        value : dict
            Configuration for the appearance of text values within collection elements, including color, font, and size.
        """

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
        """Blue style configuration for collections.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and modifies the square color
        and fill color to blue shades, providing a visually distinct appearance for collection elements.
        """

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
        """Purple style configuration for collections.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and modifies the square color
        and fill color to purple shades, providing a visually distinct appearance for collection elements.
        """

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
        """Green style configuration for collections.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and modifies the square color
        and fill color to green shades, providing a visually distinct appearance for collection elements.
        """

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
    """Style configuration for :class:`~manim_dsa.m_collection.m_stack.MStack` visualization.

    This class provides predefined style configurations that control the appearance
    of stack elements, containers, and other visual properties. Each style variant
    includes settings for colors, fonts, sizes, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MStackStyle._DefaultStyle`
        A default style configuration for stacks.
    BLUE : :class:`MStackStyle._BlueStyle`
        A blue style configuration for stacks.
    PURPLE : :class:`MStackStyle._PurpleStyle`
        A purple style configuration for stacks.
    GREEN : :class:`MStackStyle._GreenStyle`
        A green style configuration for stacks.
    """

    class _DefaultStyle(MCollectionStyle._DefaultStyle):
        """Default style configuration for stacks.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and adds stack-specific
        container styling properties.

        Attributes
        ----------
        container : dict
            Configuration for the appearance of the stack container, including color.
        """

        def __init__(self):
            super().__init__()
            self.container: dict = {"color": RED}

    class _BlueStyle(_DefaultStyle, MCollectionStyle._BlueStyle):
        """Blue style configuration for stacks.

        Combines the stack container properties from :class:`~manim_dsa.constants.MStackStyle._DefaultStyle`
        with the blue color scheme from :class:`~manim_dsa.constants.MCollectionStyle._BlueStyle`.
        """

        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, MCollectionStyle._PurpleStyle):
        """Purple style configuration for stacks.

        Combines the stack container properties from :class:`~manim_dsa.constants.MStackStyle._DefaultStyle`
        with the purple color scheme from :class:`~manim_dsa.constants.MCollectionStyle._PurpleStyle`.
        """

        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, MCollectionStyle._GreenStyle):
        """Green style configuration for stacks.

        Combines the stack container properties from :class:`~manim_dsa.constants.MStackStyle._DefaultStyle`
        with the green color scheme from :class:`~manim_dsa.constants.MCollectionStyle._GreenStyle`.
        """

        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()


class MArrayStyle(MCollectionStyle):
    """Style configuration for :class:`~manim_dsa.m_collection.m_array.MArray` visualization.

    This class provides predefined style configurations that control the appearance
    of array elements, indices, and other visual properties. Each style variant
    includes settings for colors, fonts, sizes, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MArrayStyle._DefaultStyle`
        A default style configuration for arrays.
    BLUE : :class:`MArrayStyle._BlueStyle`
        A blue style configuration for arrays.
    PURPLE : :class:`MArrayStyle._PurpleStyle`
        A purple style configuration for arrays.
    GREEN : :class:`MArrayStyle._GreenStyle`
        A green style configuration for arrays.
    """

    class _DefaultStyle(MCollectionStyle._DefaultStyle):
        """Default style configuration for arrays.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and adds array-specific
        index styling properties.

        Attributes
        ----------
        index : dict
            Configuration for the appearance of array index labels, including color, font, and size.
        """

        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": WHITE,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _BlueStyle(_DefaultStyle, MCollectionStyle._BlueStyle):
        """Blue style configuration for arrays.

        Combines the array index properties from :class:`~manim_dsa.constants.MArrayStyle._DefaultStyle`
        with the blue color scheme from :class:`~manim_dsa.constants.MCollectionStyle._BlueStyle`.
        """

        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": BLUE_D,
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _PurpleStyle(_DefaultStyle, MCollectionStyle._PurpleStyle):
        """Purple style configuration for arrays.

        Combines the array index properties from :class:`~manim_dsa.constants.MArrayStyle._DefaultStyle`
        with the purple color scheme from :class:`~manim_dsa.constants.MCollectionStyle._PurpleStyle`.
        """

        def __init__(self):
            super().__init__()
            self.index: dict = {
                "color": ManimColor("#fabcff"),
                "font": "Cascadia Code",
                "font_size": 32,
                "disable_ligatures": True,
            }

    class _GreenStyle(_DefaultStyle, MCollectionStyle._GreenStyle):
        """Green style configuration for arrays.

        Combines the array index properties from :class:`~manim_dsa.constants.MArrayStyle._DefaultStyle`
        with the green color scheme from :class:`~manim_dsa.constants.MCollectionStyle._GreenStyle`.
        """

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
    """Style configuration for :class:`~manim_dsa.m_variable.m_variable.MVariable` visualization.

    This class provides predefined style configurations that control the appearance
    of variable elements and their values. Each style variant includes settings for
    colors, fonts, sizes, and other visual properties.

    Attributes
    ----------
    DEFAULT : :class:`MVariableStyle._DefaultStyle`
        A default style configuration for variables.
    BLUE : :class:`MVariableStyle._BlueStyle`
        A blue style configuration for variables.
    PURPLE : :class:`MVariableStyle._PurpleStyle`
        A purple style configuration for variables.
    GREEN : :class:`MVariableStyle._GreenStyle`
        A green style configuration for variables.
    """

    class _DefaultStyle(MCollectionStyle._DefaultStyle):
        """Default style configuration for variables.

        Inherits from :class:`~manim_dsa.constants.MCollectionStyle._DefaultStyle` and provides the base
        styling for variable visualization elements.
        """

        def __init__(self):
            super().__init__()

    class _BlueStyle(_DefaultStyle, MCollectionStyle._BlueStyle):
        """Blue style configuration for variables.
        Combines the variable properties from :class:`~manim_dsa.constants.MVariableStyle._DefaultStyle`
        with the blue color scheme from :class:`~manim_dsa.constants.MCollectionStyle._BlueStyle`.
        """

        def __init__(self):
            super().__init__()

    class _PurpleStyle(_DefaultStyle, MCollectionStyle._PurpleStyle):
        """Purple style configuration for variables.
        Combines the variable properties from :class:`~manim_dsa.constants.MVariableStyle._DefaultStyle`
        with the purple color scheme from :class:`~manim_dsa.constants.MCollectionStyle._PurpleStyle`.
        """

        def __init__(self):
            super().__init__()

    class _GreenStyle(_DefaultStyle, MCollectionStyle._GreenStyle):
        """Green style configuration for variables.

        Combines the variable properties from :class:`~manim_dsa.constants.MVariableStyle._DefaultStyle`
        with the green color scheme from :class:`~manim_dsa.constants.MCollectionStyle._GreenStyle`.
        """

        def __init__(self):
            super().__init__()

    DEFAULT = _DefaultStyle()
    BLUE = _BlueStyle()
    PURPLE = _PurpleStyle()
    GREEN = _GreenStyle()
