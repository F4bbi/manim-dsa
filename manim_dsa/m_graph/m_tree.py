from typing import Self

import networkx as nx
from manim import *

from manim_dsa.constants import GraphType, MTreeStyle
from manim_dsa.m_graph.m_graph import MGraph
from manim_dsa.utils.utils import get_nx_graph


class MTree(MGraph):
    """Manim Tree: a class for visualizing the tree data structure using the Manim animation engine.

    Parameters
    ----------
    tree : :class:`GraphType`
        The tree representation, which can be weighted or unweighted. Can be:
        - ``list[list[str]]`` or ``dict[str, list[str]]`` for unweighted tree
        - ``list[list[tuple[str, str | int]]]`` or ``dict[str, list[tuple[str, str | int]]]`` for weighted tree
    root : str | None, optional
        The root node of the tree. If ``None``, topological sorting is used to determine the root.
    style : :class:`MTreeStyle._DefaultStyle`, optional
        The style configuration to be applied to the tree. Defaults to ``MTreeStyle.DEFAULT``.
    """

    def __init__(
        self,
        tree: GraphType,
        root: str | None = None,
        style: MTreeStyle._DefaultStyle = MTreeStyle.DEFAULT,
    ):
        self.root = self._get_root(tree, root)
        super().__init__(tree, style=style)

    def _get_root(self, tree: GraphType, root: str | None) -> str:
        if root is not None:
            return root
        G = get_nx_graph(tree)
        if root is None and isinstance(G, nx.DiGraph):
            root = next(
                iter(nx.topological_sort(G))
            )  # allows back compatibility with nx version 1.11
        return root

    def _hierarchy_pos(
        self,
        G: nx.Graph,
        root: str,
        horizontal_gap: float,
        vertical_gap: float,
    ):
        """Calculate the positions of nodes in a tree for hierarchical layout.

        Parameters
        ----------
        G : :class:`~networkx.Graph`
            The graph representing the tree structure.
        root : str
            The root node of the tree.
        horizontal_gap : float
            The horizontal distance between nodes.
        vertical_gap : float
            The vertical distance between nodes.

        Returns
        -------
        dict
            A dictionary mapping each node to its ``(x, y)`` position in the layout.
        """

        def __hierarchy_pos(
            G,
            root,
            width,
            vert_gap,
            x,
            y,
            pos,
            parent,
        ):
            """Recursive function to calculate positions of nodes in a tree."""
            pos[root] = (x, y)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)
            if len(children) != 0:
                dx = width / len(children)
                nextx = x - width / 2 - dx / 2
                for child in children:
                    nextx += dx
                    pos = __hierarchy_pos(
                        G, child, dx, vert_gap, nextx, y - vert_gap, pos, root
                    )
            return pos

        return __hierarchy_pos(G, root, horizontal_gap, vertical_gap, 0, 0, {}, None)

    def node_layout(self) -> Self:
        """Applies a hierarchical layout to the nodes of the tree.

        Returns
        -------
        self
            The updated instance of the :class:`MTree` with nodes arranged according to the hierarchical layout.
        """
        G = nx.DiGraph()
        G.add_edges_from(self.edges.keys())
        pos = self._hierarchy_pos(
            G, self.root, self.style.horizontal_gap, self.style.vertical_gap
        )
        return self._node_layout(pos, False)
