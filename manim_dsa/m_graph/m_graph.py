from __future__ import annotations

from abc import ABC, abstractmethod
from math import *
from typing import Self, override

import networkx as nx
from manim import *
from manim.typing import Point3D, Vector3D

from manim_dsa.constants import *
from manim_dsa.m_collection.m_collection import *
from manim_dsa.utils.utils import *


class MGraph(VDict, Labelable):
    """Manim Graph: a class for visualizing the graph data structure using the Manim animation engine.

    Parameters
    ----------
    graph : :class:`GraphType`
        The graph representation, which can be weighted or unweighted. Can be:
        - ``list[list[str]]`` or ``dict[str, list[str]]`` for unweighted graph
        - ``list[list[tuple[str, str | int]]]`` or ``dict[str, list[tuple[str, str | int]]]`` for weighted graph
    nodes_position : dict[str, :class:`~manim.typing.Vector3D`], optional
        A dictionary mapping node labels to their positions as 3D vectors. Defaults to an empty dict.
    style : :class:`MGraphStyle._DefaultStyle`, optional
        The style configuration to be applied to the graph. Defaults to ``MGraphStyle.DEFAULT``.
    """

    def __init__(
        self,
        graph: GraphType,
        nodes_position: dict[str, Vector3D] = {},
        style: MGraphStyle._DefaultStyle = MGraphStyle.DEFAULT,
    ):
        super().__init__()

        self.nodes: dict[str, MGraph.Node] = {}
        self.edges: dict[tuple[str, str], MGraph.Edge] = {}
        self.style = style

        nxGraph = get_nx_graph(graph)

        for node in nxGraph.nodes():
            pos: Vector3D = nodes_position.get(str(node), ORIGIN)
            self.add_node(str(node), pos)

        for u, v, wt in nxGraph.edges.data("weight"):
            if wt:
                self.add_edge(u, v, wt)
            else:
                self.add_edge(u, v)

        if not nodes_position:
            self.node_layout()

    class Node(VGroup, Highlightable):
        """A class that represents a node (or vertex) of the graph.

        Parameters
        ----------
        circle : :class:`~manim.mobject.geometry.arc.Circle`
            The circular shape that visually represents the node.
        label : :class:`~manim.mobject.text.text_mobject.Text`
            The text label associated with the node.
        """

        def __init__(self, circle: Circle, label: Text):
            super().__init__()
            self.circle = circle.set_z_index(2)
            self.label = label.set_z_index(3)
            self._add_highlight(self.circle)

            self += self.circle
            self += self.label

        def get_radius(self) -> float:
            """Returns the radius of the node's circle.

            Returns
            -------
            float
                The radius of the node's circle.
            """
            return self.width / 2

    class Edge(VGroup, Highlightable, ABC):
        """An abstract class that represents an edge in the graph.

        Parameters
        ----------
        line : :class:`~manim.mobject.geometry.line.Line` or :class:`~manim.mobject.geometry.arc.ArcBetweenPoints`
            The line or arc that visually represents the edge between two nodes.
        start : :class:`~manim.typing.Point3D`
            The starting point of the edge.
        end : :class:`~manim.typing.Point3D`
            The ending point of the edge.
        arrow : :class:`~manim.mobject.geometry.tips.ArrowTriangleFilledTip` or ``None``
            The arrow tip to be added to the edge, if any.
        """

        def __init__(
            self,
            line: Line | ArcBetweenPoints,
            start: Point3D,
            end: Point3D,
            arrow: ArrowTriangleFilledTip | None,
        ):
            super().__init__()
            self.label: Text = None
            self.line: Line | ArcBetweenPoints = line.set_z_index(0)
            self.line.put_start_and_end_on(start, end)
            if arrow:
                self.line.add_tip(arrow)
            self += self.line

        def weighted(self, label: Text) -> Self:
            """Assigns a label to the edge, indicating that it is weighted.

            Parameters
            ----------
            label : :class:`~manim.mobject.text.text_mobject.Text`
                The label to be assigned to the edge, representing its weight or any other relevant information.

            Returns
            -------
            self
                The instance of the :class:`MGraph.Edge` with the applied highlight.
            """
            self.label: Text = label
            self += self.label
            return self

        def is_weighted(self) -> bool:
            """Checks if the edge is weighted by examining the presence of a label.

            Returns
            -------
            bool
                ``True`` if the edge has a label (indicating it is weighted), ``False`` otherwise.
            """
            return self.label is not None

        @override
        def highlight(
            self,
            stroke_color: ManimColor = RED,
            stroke_width: float = 8,
        ) -> Self:
            """Highlights the edge with a specified color and stroke width.

            Parameters
            ----------
            stroke_color : :class:`~manim.utils.color.ManimColor`, optional
                The color to be used for highlighting the edge. Defaults to ``RED``.
            stroke_width : float, optional
                The width of the stroke used for highlighting. Defaults to ``8``.

            Returns
            -------
            self
                The instance of the :class:`MGraph.Edge` with the applied highlight.
            """
            self.set_highlight(stroke_color, stroke_width)
            self.highlighting.move_to(self.line)
            self += self.highlighting
            return self

        @override_animate(highlight)
        def _highlight_animation(
            self,
            stroke_color: ManimColor = RED,
            stroke_width: float = 8,
            anim_args: dict = None,
        ) -> Create:
            """Returns the animation for highlighting the edge.

            Parameters
            ----------
            stroke_color : :class:`~manim.utils.color.ManimColor`, optional
                The color to be used for highlighting. Defaults to ``RED``.
            stroke_width : float, optional
                The width of the stroke used for highlighting. Defaults to ``8``.
            anim_args : dict, optional
                Additional arguments to be passed to the animation. Defaults to ``None``.

            Returns
            -------
            :class:`~manim.animation.creation.Create`
                The animation that highlights the edge.
            """
            self.highlight(stroke_color, stroke_width)
            return Create(self.highlighting, **anim_args)

        def set_highlight(
            self,
            stroke_color: ManimColor = RED,
            stroke_width: float = 8,
        ) -> Self:
            """Sets the highlight properties for the edge.

            Parameters
            ----------
            stroke_color : :class:`~manim.utils.color.ManimColor`, optional
                The color to be used for highlighting the edge. Defaults to ``RED``.
            stroke_width : float, optional
                The width of the stroke used for highlighting. Defaults to ``8``.

            Returns
            -------
            self
                The instance of the :class:`MGraph.Edge` with the applied highlight.
            """
            super().set_highlight(stroke_color, stroke_width)
            if self.line.has_tip():
                arrow_width: float = self.line.get_tip().get_width()
                self.highlighting.get_tip().set_stroke(width=arrow_width).set_color(
                    stroke_color
                ).set_opacity(1)
            return self

        @abstractmethod
        def _get_line_start_end(
            self,
            node1: Circle,
            node2: Circle,
            start_distance: float,
        ) -> tuple[Point3D, Point3D]:
            """Abstract method to determine the start and end points of a line between two nodes.

            This method should be implemented to calculate the exact positions where the line
            should start and end, taking into account the positions and radii of the nodes.

            Parameters
            ----------
            node1 : :class:`~manim.mobject.geometry.arc.Circle`
                The start node (circle) of the edge.
            node2 : :class:`~manim.mobject.geometry.arc.Circle`
                The destination node (circle) of the edge.
            start_distance : float
                Specifies how far the line starts from the node, rather than starting directly at its edge. Expressed as a percentage of the node’s radius.

            Returns
            -------
            tuple[:class:`~manim.typing.Point3D`, :class:`~manim.typing.Point3D`]
                A tuple containing two :class:`~manim.typing.Point3D` objects representing the start and end points
                of the line connecting the two nodes.
            """
            pass

        @abstractmethod
        def _get_label_position(self, label_distance: float) -> Point3D:
            """Abstract method to determine the position of the weight relative to the edge.

            Parameters
            ----------
            label_distance : float
                The distance from the line or edge where the label should be positioned.

            Returns
            -------
            :class:`~manim.typing.Point3D`
                The :class:`~manim.typing.Point3D` coordinates representing the position of the label.
            """
            pass

    class StraightEdge(Edge):
        """Represents a straight edge in the graph, connecting two nodes with a straight line.

        Parameters
        ----------
        line : :class:`~manim.mobject.geometry.line.Line`
            The Line object representing the edge.
        node1 : :class:`~manim.mobject.geometry.arc.Circle`
            The start node (circle) of the edge.
        node2 : :class:`~manim.mobject.geometry.arc.Circle`
            The destination node (circle) of the edge.
        arrow : :class:`~manim.mobject.geometry.tips.ArrowTriangleFilledTip` or ``None``
            The arrow tip to be added to the edge, if any.
        """

        def __init__(
            self,
            line: Line,
            node1: Circle,
            node2: Circle,
            arrow: ArrowTriangleFilledTip | None,
            start_distance: float,
        ):
            start, end = self._get_line_start_end(
                node1,
                node2,
                start_distance,
            )
            super().__init__(line, start, end, arrow)
            self._add_highlight(self.line)

        def weighted(
            self,
            label: Text,
            label_distance: float = 0.3,
        ) -> Self:
            """Assigns a label (the weight) to the edge and positions it relative to the edge.

            Parameters
            ----------
            label : :class:`~manim.mobject.text.text_mobject.Text`
                The label to be assigned to the edge.
            label_distance : float, optional
                The distance from the edge to position the label. Defaults to ``0.3``.

            Returns
            -------
            self
                The instance of the :class:`MGraph.Edge` with the applied highlight.ssigned label.
            """
            super().weighted(label)
            self.label_distance: float = label_distance
            label_position: Point3D = self._get_label_position(label_distance)
            self.label.move_to(label_position)
            return self

        def _get_line_start_end(
            self,
            node1: Circle,
            node2: Circle,
            start_distance: float,
        ) -> tuple[Point3D, Point3D]:
            """Determines the start and end points of the line based on node positions and radii.

            Parameters
            ----------
            node1 : :class:`~manim.mobject.geometry.arc.Circle`
                The start node (circle) of the edge.
            node2 : :class:`~manim.mobject.geometry.arc.Circle`
                The destination node (circle) of the edge.
            start_distance : float
                Specifies how far the line starts from the node, rather than starting directly at its edge. Expressed as a percentage of the node’s radius.

            Returns
            -------
            tuple[:class:`~manim.typing.Point3D`, :class:`~manim.typing.Point3D`]
                A tuple containing two :class:`~manim.typing.Point3D` objects representing the start and end points of the line.
            """
            c1, c2 = node1.get_center(), node2.get_center()
            r1, r2 = node1.get_radius(), node2.get_radius()

            direction = Line(c1, c2).get_unit_vector()
            start = c1 + direction * r1 * (1 + start_distance)
            end = c2 - direction * r2 * (1 + start_distance)

            if np.array_equal(start, end):
                start = LEFT
                end = RIGHT

            return start, end

        def _get_label_position(self, label_distance: float) -> Point3D:
            """Calculates the position of the label (the weight) relative to the edge.

            Parameters
            ----------
            label_distance : float
                The distance from the edge to position the label.

            Returns
            -------
            :class:`~manim.typing.Point3D`
                The 3D coordinates where the label should be positioned.
            """
            direction: Point3D = self.line.get_unit_vector()
            mean: Point3D = (
                self.line.get_start() + direction * self.line.get_length() / 2
            )
            orthogonal_dir: Point3D = np.array([direction[1], -direction[0], 0])
            position: Point3D = mean + orthogonal_dir * label_distance
            return position

    class CurvedEdge(Edge):
        """Represents a curved edge in the graph, connecting two nodes with an arc.

        Parameters
        ----------
        line : :class:`~manim.mobject.geometry.arc.ArcBetweenPoints`
            The ArcBetweenPoints object representing the edge.
        node1 : :class:`~manim.mobject.geometry.arc.Circle`
            The start node (circle) of the edge.
        node2 : :class:`~manim.mobject.geometry.arc.Circle`
            The destination node (circle) of the edge.
        arrow : :class:`~manim.mobject.geometry.tips.ArrowTriangleFilledTip` or ``None``
            The arrow tip to be added to the edge, if any.
        node_angle : float, optional
            The angle between the line connecting the nodes and the direction of the arc. Defaults to ``PI/3``.
        arc_angle : float, optional
            The angle of the arc between the two nodes. Defaults to ``PI/3``.
        """

        def __init__(
            self,
            line: ArcBetweenPoints,
            node1: Circle,
            node2: Circle,
            arrow: ArrowTriangleFilledTip | None,
            start_distance: float,
            node_angle: float = PI / 3,
            arc_angle: float = PI / 3,
        ):
            start, end = self._get_line_start_end(
                node1,
                node2,
                start_distance,
                node_angle,
            )
            super().__init__(line, start, end, arrow)
            self.arc_angle: float = arc_angle
            self._add_highlight(self.line)

        def weighted(
            self,
            label: Text,
            label_distance: float = 0.3,
        ) -> Self:
            """Assigns a label (the weight) to the edge and positions it relative to the edge.

            Parameters
            ----------
            label : :class:`~manim.mobject.text.text_mobject.Text`
                The label to be assigned to the edge.
            label_distance : float, optional
                The distance from the edge to position the label. Defaults to ``0.3``.

            Returns
            -------
            self
                The instance of the :class:`MGraph.Edge` with the applied highlight.ssigned label.
            """
            super().weighted(label)
            self.label_distance: float = label_distance
            label_position = self._get_label_position(label_distance)
            self.label.move_to(label_position)
            return self

        def _get_line_start_end(
            self,
            node1: Circle,
            node2: Circle,
            start_distance: float,
            start_angle: float = PI / 3,
        ) -> tuple[Point3D, Point3D]:
            """Calculates the start and end points of the arc considering node positions, radii, and the start angle.

            This method computes the positions where the edge should start and end relative to the given nodes,
            taking into account their radii and the starting angle.

            Parameters
            ----------
            node1 : :class:`~manim.mobject.geometry.arc.Circle`
                The start node (circle) of the edge.
            node2 : :class:`~manim.mobject.geometry.arc.Circle`
                The destination node (circle) of the edge.
            start_distance : float, optional
                Specifies how far the line starts from the node, rather than starting directly at its edge. Expressed as a percentage of the node’s radius.
            start_angle : float, optional
                The angle between the edge direction and the line's start direction. Defaults to ``PI/3``.

            Returns
            -------
            tuple[:class:`~manim.typing.Point3D`, :class:`~manim.typing.Point3D`]
                A tuple containing two :class:`~manim.typing.Point3D` objects representing the start and end points of the edge.
            """
            c1, c2 = node1.get_center(), node2.get_center()
            r1, r2 = node1.get_radius(), node2.get_radius()
            edge_dir = Line(c1, c2).get_unit_vector()
            edge_angle = acos(edge_dir[0])
            if edge_dir[1] < 0:
                edge_angle = -edge_angle

            vector_start = [
                cos(edge_angle - start_angle),
                sin(edge_angle - start_angle),
                0,
            ]

            vector_end = [
                cos(edge_angle - (PI - start_angle)),
                sin(edge_angle - (PI - start_angle)),
                0,
            ]

            start_dir = normalize(vector_start)
            end_dir = normalize(vector_end)

            start = c1 + start_dir * r1 * (1 + start_distance)
            end = c2 + end_dir * r2 * (1 + start_distance)

            return start, end

        def _get_label_position(self, label_distance: float) -> Point3D:
            """Calculates the position of the label relative to the edge.

            This method computes where the label should be placed based on the distance from the edge and the arc of the edge.

            Parameters
            ----------
            label_distance : float
                The distance from the edge at which the label should be positioned.

            Returns
            -------
            :class:`~manim.typing.Point3D`
                The 3D coordinates where the label should be positioned relative to the edge.
            """
            arc = ArcBetweenPoints(
                self.line.get_start(),
                self.line.get_end(),
                self.arc_angle,
            )
            line = Line(self.line.get_start(), self.line.get_end())
            direction = line.get_unit_vector()
            orthogonal_dir = np.array([direction[1], -direction[0], 0])
            position = (
                arc.get_boundary_point(orthogonal_dir)
                + orthogonal_dir * len(line) * label_distance
            )
            return position

    def add_node(self, name: str, position: Point3D = ORIGIN) -> Self:
        """Adds a new node to the graph with a specified name and position.

        Parameters
        ----------
        name : str
            The name of the node to be added.
        position : :class:`~manim.typing.Point3D`, optional
            The 3D position where the node will be placed. Defaults to ``ORIGIN``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with the new node added.
        """
        new_node = self.Node(
            Circle(**self.style.node_circle).move_to(position),
            Text(str(name), **self.style.node_label).move_to(position),
        )
        self.nodes[name] = new_node
        self.add([(name, new_node)])
        return self

    @override_animate(add_node)
    def _add_node_animation(
        self,
        name: str,
        position: Point3D = ORIGIN,
        anim_args: dict = None,
    ) -> Create:
        """Animates the addition of a new node to the graph.

        Parameters
        ----------
        name : str
            The name of the node to be added.
        position : :class:`~manim.typing.Point3D`, optional
            The 3D position where the node will be placed. Defaults to ``ORIGIN``.
        anim_args : dict, optional
            Additional arguments to be passed to the animation. Defaults to ``None``.

        Returns
        -------
        :class:`~manim.animation.creation.Create`
            The animation for adding the node.
        """
        self.add_node(name, position)
        return Create(self.nodes[name], **anim_args)

    def add_edge(
        self,
        node1_name: str,
        node2_name: str,
        weight: float = None,
        label_distance: float = 0.2,
    ) -> Self:
        """Adds a new edge between two nodes in the graph.

        Parameters
        ----------
        node1_name : str
            The name of the first node.
        node2_name : str
            The name of the second node.
        weight : float, optional
            The weight of the edge. If not provided, the edge will be unweighted.
        label_distance : float, optional
            The distance from the edge where the label should be placed. Defaults to ``0.2``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with the new edge added.
        """
        edge_name = (node1_name, node2_name)
        edge_name_rev = (node2_name, node1_name)

        node1 = self.nodes[node1_name].circle
        node2 = self.nodes[node2_name].circle

        reverse_exists = edge_name_rev in self.edges

        line = Line(**self.style.edge_line)
        arrow = (
            ArrowTriangleFilledTip(**self.style.edge_tip)
            if not reverse_exists
            else None
        )

        new_edge = self.StraightEdge(
            line,
            node1,
            node2,
            arrow,
            self.style.start_distance,
        )
        if weight:
            new_edge.weighted(
                Text(str(weight), **self.style.edge_weight),
                label_distance,
            )

        if edge_name_rev in self.edges:
            new_edge_rev_node = self.StraightEdge(
                line,
                node2,
                node1,
                None,
                self.style.start_distance,
            )
            if weight:
                new_edge.weighted(new_edge.label, label_distance)

            self.remove(edge_name_rev)
            self.edges[edge_name_rev] = new_edge_rev_node
            self.add([(edge_name_rev, new_edge_rev_node)])

        self.edges[edge_name] = new_edge
        self.add([(edge_name, new_edge)])
        return self

    @override_animate(add_edge)
    def _add_edge_animation(
        self,
        node1_name: str,
        node2_name: str,
        weight: float = None,
        label_distance: float = 0.3,
        anim_args: dict = None,
    ) -> Create:
        """Animates the addition of an edge between two nodes in the graph.

        Parameters
        ----------
        node1_name : str
            The name of the first node.
        node2_name : str
            The name of the second node.
        weight : float, optional
            The weight of the edge. If not provided, the edge will be unweighted.
        label_distance : float, optional
            The distance from the edge where the label should be placed. Defaults to ``0.3``.
        anim_args : dict, optional
            Additional arguments to be passed to the animation. Defaults to ``None``.

        Returns
        -------
        :class:`~manim.animation.creation.Create`
            The animation for adding the edge.
        """
        self.add_edge(node1_name, node2_name, weight, label_distance)

        return Create(
            self.edges[(node1_name, node2_name)],
            **anim_args,
        )

    def add_curved_edge(
        self,
        node1_name: str,
        node2_name: str,
        weight: float = None,
        label_distance: float = 0.3,
        node_angle: float = PI / 3,
        arc_angle: float = PI / 3,
    ) -> Self:
        """Adds a new curved edge between two nodes in the graph.

        Parameters
        ----------
        node1_name : str
            The name of the first node.
        node2_name : str
            The name of the second node.
        weight : float, optional
            The weight of the edge. If not provided, the edge will be unweighted.
        label_distance : float, optional
            The distance from the edge where the label should be placed. Defaults to ``0.2``.
        node_angle : float, optional
            The start angle of the arc between the two nodes. Defaults to ``PI/3``.
        arc_angle : float, optional
            The angle of the arc between the two nodes. Defaults to ``PI/3``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with the new curved edge added.
        """
        edge_name = (node1_name, node2_name)
        edge_name_rev = (node2_name, node1_name)

        node1 = self.nodes[node1_name].circle
        node2 = self.nodes[node2_name].circle

        reverse_exists = edge_name_rev in self.edges

        line = ArcBetweenPoints(LEFT, RIGHT, **self.style.edge_line, angle=arc_angle)
        arrow = (
            ArrowTriangleFilledTip(**self.style.edge_tip)
            if not reverse_exists
            else None
        )

        new_edge = self.CurvedEdge(
            line,
            node1,
            node2,
            arrow,
            self.style.start_distance,
            node_angle,
            arc_angle,
        )
        if weight:
            new_edge.weighted(
                Text(str(weight), **self.style.edge_weight),
                label_distance,
            )

        if edge_name_rev in self.edges:
            new_edge_rev = self.CurvedEdge(
                new_edge.line,
                node1,
                node2,
                None,
                self.style.start_distance,
                node_angle,
                arc_angle,
            )
            if weight:
                new_edge.weighted(
                    new_edge.label,
                    label_distance,
                )
            self.remove(edge_name_rev)
            self.edges[edge_name_rev] = new_edge_rev
            self.add([(edge_name_rev, new_edge_rev)])

        self.edges[edge_name] = new_edge
        self.add([(edge_name, new_edge)])
        return self

    @override_animate(add_curved_edge)
    def _add_curved_edge_animation(
        self,
        node1_name: str,
        node2_name: str,
        weight: float = None,
        label_distance: float = 0.3,
        node_angle: float = PI / 3,
        arc_angle: float = PI / 3,
        anim_args: dict = None,
    ) -> Create:
        """Animates the addition of a curved edge between two nodes in the graph.

        Parameters
        ----------
        node1_name : str
            The name of the first node.
        node2_name : str
            The name of the second node.
        weight : float, optional
            The weight of the edge. If not provided, the edge will be unweighted.
        label_distance : float, optional
            The distance from the edge where the label should be placed. Defaults to ``0.2``.
        node_angle : float, optional
            The start angle of the arc between the two nodes. Defaults to ``PI/3``.
        arc_angle : float, optional
            The angle of the arc between the two nodes. Defaults to ``PI/3``.
        anim_args : dict, optional
            Additional arguments to be passed to the animation. Defaults to ``None``.

        Returns
        -------
        :class:`~manim.animation.creation.Create`
            The animation for adding the curved edge.
        """
        self.add_curved_edge(
            node1_name,
            node2_name,
            weight,
            label_distance,
            node_angle,
            arc_angle,
        )

        return Create(
            self.edges[(node1_name, node2_name)],
            **anim_args,
        )

    # TODO
    def show_backward_edge(
        self,
        node1_name: str,
        node2_name: str,
        forward_weight: float,
        backward_weight: float,
        label_distance: float = 0.3,
        node_angle: float = PI / 6,
        arc_angle: float = PI / 6,
    ) -> Self:
        edge_name = (node1_name, node2_name)
        edge_name_rev = (node2_name, node1_name)

        node1 = self.nodes[node1_name].circle
        node2 = self.nodes[node2_name].circle

        line = ArcBetweenPoints(LEFT, RIGHT, **self.style.edge_line, angle=arc_angle)
        arrow = ArrowTriangleFilledTip(**self.style.edge_tip)

        new_edge_1 = self.CurvedEdge(line, node1, node2, arrow, node_angle, arc_angle)
        new_edge_1.weighted(
            Text(
                str(forward_weight),
                **self.style.edge_weight,
            ),
            label_distance,
        )

        line = ArcBetweenPoints(LEFT, RIGHT, **self.style.edge_line, angle=arc_angle)
        arrow = ArrowTriangleFilledTip(**self.style.edge_tip)

        new_edge_2 = self.CurvedEdge(
            line,
            node2,
            node1,
            arrow,
            node_angle,
        )
        new_edge_2.weighted(
            Text(
                str(backward_weight),
                **self.style.edge_weight,
            ),
            label_distance,
        )

        self.edges[edge_name] = self[edge_name] = new_edge_1
        self.edges[edge_name_rev] = new_edge_2
        self.add([(edge_name_rev, new_edge_2)])
        return self

    @override_animate(show_backward_edge)
    def _show_backward_edge_animation(
        self,
        node1_name: str,
        node2_name: str,
        forward_weight: float,
        backward_weight: float,
        label_distance: float = 0.3,
        node_angle: float = PI / 6,
        arc_angle: float = PI / 6,
        anim_args: dict = None,
    ):
        edge_name = (node1_name, node2_name)
        edge_name_rev = (node2_name, node1_name)
        old_edge = self.edges[edge_name]

        self.show_backward_edge(
            node1_name,
            node2_name,
            forward_weight,
            backward_weight,
            label_distance,
            node_angle,
            arc_angle,
        )

        return Succession(
            ReplacementTransform(
                old_edge,
                VGroup(
                    self.edges[edge_name],
                    self.edges[edge_name_rev],
                ),
                **anim_args,
            )
        )

    def _node_layout(
        self, pos: dict[str, tuple[float, float]], fit: bool = True
    ) -> Self:
        """Helper method that rearranges the nodes and edges based on the provided positions of the nodes.

        Parameters
        ----------
        pos : dict[str, tuple[float, float]]
            A dictionary mapping node labels to their positions as tuples of (x, y) coordinates.
        fit : bool, optional
            If ``True``, the graph will be scaled to fit within the frame. Defaults to ``True``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with nodes arranged according to the specified layout.
        """
        labels = list(pos.keys())

        x = [x for x, _ in pos.values()]
        y = [y for _, y in pos.values()]

        # Calculate coefficients to fit the graph within the frame
        coeff_x = config.frame_x_radius / (abs(max(x) - min(x))) if fit else 1
        coeff_y = config.frame_y_radius / (abs(max(y) - min(y))) if fit else 1

        positions = []

        for label in labels:
            positions.append(
                [
                    pos.get(label)[0] * coeff_x,
                    pos.get(label)[1] * coeff_y,
                    0,
                ]
            )

        nodes_and_positions = dict(zip(labels, positions, strict=False))
        for node in nodes_and_positions:
            self.nodes[node].move_to(nodes_and_positions[node])
        for edge in self.edges:
            node1 = self.nodes[edge[0]].circle
            node2 = self.nodes[edge[1]].circle
            start, end = self.edges[edge]._get_line_start_end(
                node1,
                node2,
                self.style.start_distance,
            )
            mEdge = self.edges[edge]
            # Workaround cause tipped lines can't be changed of start/end, we have to delete the tip for a moment
            if mEdge.line.has_tip():
                tip = mEdge.line.get_tip()
                mEdge.line.remove(tip)
                mEdge.line.put_start_and_end_on(start, end)
                mEdge.line.add_tip()
            else:
                mEdge.line.put_start_and_end_on(start, end)
            mEdge.highlighting.put_start_and_end_on(start, end)
            if mEdge.is_weighted():
                label_position = mEdge._get_label_position(mEdge.label_distance)
                mEdge.label.move_to(label_position)

        self.move_to(ORIGIN)
        return self

    def node_layout(self, layout: str = "kamada_kawai_layout") -> Self:
        """Applies a specified layout algorithm to arrange the nodes in the graph.

        Parameters
        ----------
        layout : str, optional
            The name of the layout algorithm to be applied to the nodes.
            Defaults to 'kamada_kawai_layout'. Other common layout options may include 'spring_layout', 'circular_layout',
            'shell_layout', and others supported by the underlying graph library.
            A full list of available layouts can be found in the NetworkX documentation:
            https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with nodes arranged according to the specified layout.
        """
        G = nx.DiGraph()
        G.add_edges_from(self.edges.keys())

        try:
            layout_function = eval(f"nx.{layout}")
            pos: dict[str, tuple[float, float]] = layout_function(G)

        except AttributeError:
            print("Layout not available")
            pos: dict[str, tuple[float, float]] = nx.kamada_kawai_layout(G)

        return self._node_layout(pos)

    def set_nodes_highlight(
        self,
        color: ManimColor = RED,
        width: float = 8,
    ) -> Self:
        """This method iterates through all the nodes in the graph and applies the specified highlight color and stroke width.

        Parameters
        ----------
        color : :class:`~manim.utils.color.ManimColor`, optional
            The color to be used for highlighting the nodes.
            Defaults to ``RED``.
        width : float, optional
            The stroke width of the highlight.
            Defaults to ``8``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with all nodes highlighted.
        """
        for node in self.nodes:
            self.nodes[node].set_highlight(color, width)
        return self

    def set_edges_highlight(
        self,
        color: ManimColor = RED,
        width: float = 8,
    ) -> Self:
        """This method iterates through all the edges in the graph and applies the specified highlight color and stroke width.

        Parameters
        ----------
        color : :class:`~manim.utils.color.ManimColor`, optional
            The color to be used for highlighting the edges.
            Defaults to ``RED``.
        width : float, optional
            The stroke width of the highlight.
            Defaults to ``8``.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with all edges highlighted.
        """
        for edge in self.edges:
            self.edges[edge].set_highlight(color, width)
        return self

    def add_label(
        self,
        text: Text,
        direction: Vector3D = UP,
        buff: float = 0.5,
        **kwargs,
    ) -> Self:
        """Adds a label to the graph with specified alignment and buffer.

        Parameters
        ----------
        text : :class:`~manim.mobject.text.text_mobject.Text`
            The label text to be added to the graph.
        direction : :class:`~manim.typing.Vector3D`, optional
            The direction in which the label should be positioned relative to the graph.
            Defaults to ``UP``.
        buff : float, optional
            The distance between the graph and the label.
            Defaults to ``0.5``.
        **kwargs
            Additional keyword arguments that are passed to the function next_to() of the
            underlying add_label method.

        Returns
        -------
        self
            The updated instance of the :class:`MGraph` with the label added.
        """
        super().add_label(text, direction, buff, **kwargs)
        self["label"] = self.label
        return self
