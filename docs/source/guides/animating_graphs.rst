Animating Graphs
================

Manim Graph - MGraph
--------------------

In this section, you'll find all the methods available to manipulate a ``MGraph`` (short for Manim Graph 😄).
As stated in the acknowledgements, this part of the library is a refactoring of the `ManimGraphLibrary <https://verdianapasqualini.github.io/ManimGraphLibrary>`_, a project by Verdiana Pasqualini focused on graph visualization. Check it out! 🔥

Key actions of ``MGraph`` include adding and removing nodes and edges, adding weights to the edges, changing the layout of the graph and other cool operations. Like all ``MObject`` structures, you can animate these methods using the ``.animate`` method, allowing you to animate each operation provided by Manim DSA.
Otherwise, methods will run without any animations.

As with other data structures provided by the library, you can access individual nodes and edges in an ``MGraph`` using the ``[]`` operator. To access a node, specify its name. To access an edge, use a tuple containing the names of the two nodes it connects.

Creating a MGraph
-----------------

You can create a graph by initializing an ``MGraph`` object. The first parameter defines the nodes and edges of the graph, which can be specified using one of the following structures:

.. code-block:: python

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

The second parameter optionally allows you to specify the position of each node using a dictionary where the key is the node name and the value is its position. If no positions are specified, a default arrangement is computed using the ``node_layout()`` function (see it's dedicated section :ref:`node_layout`).

Additionally, you can customize the theme of the ``MGraph`` (see :ref:`customizing_a_mgraph`).

Below are two examples of creating a graph:

1. A graph of 3 nodes without specifying names or positions.
2. A graph where nodes have specified names and positions, and edges have weights. Note that if two nodes are mutually connected, the edge between them is rendered as a line rather than an arrow.

.. manim:: BasicGraph
    :quality: high

    from manim_dsa import *

    class BasicGraph(Scene):
        def construct(self):
            mGraph = MGraph(
                [['1', '2'], ['0'], ['0']],
            )
            self.play(Create(mGraph))
            self.wait()

.. manim:: AdvancedGraph
    :quality: high

    from manim_dsa import *

    class AdvancedGraph(Scene):
        def construct(self):
            graph = {
                'a':[('b', 4), ('c', 5)], 'b':[('c', 7), ('d', 2)],
                'c':[('b', 7), ('e', 99)], 'd':[('b', 2), ('e', 3)],
                'e':[('c', 99), ('d', 3)], 'f':[('d', 5), ('e', 1)]
            }
            nodes_and_positions = {
                'a': LEFT * 4,
                'b': LEFT * 2 + UP * 2,
                'c': LEFT* 2 + DOWN * 2,
                'd': RIGHT * 2 + UP * 2,
                'e': RIGHT * 2 + DOWN * 2,
                'f': RIGHT * 4
            }
            mGraph = MGraph(
                graph,
                nodes_and_positions
            )
            self.play(Create(mGraph))
            self.wait()

.. _customizing_a_mgraph:

Customizing a MGraph
--------------------

ManimDSA provides various options for customizing the colors and styles of a MGraph. You can use these options by passing a predefined style configuration from the ``MGraphStyle`` class using the ``style`` parameter. Refer to ``MGraphStyle`` for more details. Alternatively, you can define a custom style to suit your needs.

In the following example, we use the ``PURPLE`` style for the ``MGraph``.

.. manim:: CustomCreation
    :quality: high

    from manim_dsa import *

    class CustomCreation(Scene):
        def construct(self):
            graph = {
                'a':[('b', 4), ('c', 5)], 'b':[('c', 7), ('d', 2)],
                'c':[('b', 7), ('e', 99)], 'd':[('b', 2), ('e', 3)],
                'e':[('c', 99), ('d', 3)], 'f':[('d', 5), ('e', 1)]
            }
            nodes_and_positions = {
                'a': LEFT * 4,
                'b': LEFT * 2 + UP * 2,
                'c': LEFT* 2 + DOWN * 2,
                'd': RIGHT * 2 + UP * 2,
                'e': RIGHT * 2 + DOWN * 2,
                'f': RIGHT * 4
            }
            mGraph = MGraph(
                graph,
                nodes_and_positions
            )
            self.play(Create(mGraph))
            self.wait()

Adding a node to a MGraph
-------------------------

The ``add_node()`` method allows you to add a new node to a MGraph. You must specify the name of the node and its position. The newly added node automatically inherits the properties specified in the configuration dictionaries.

In the example below, we create a ``MGraph`` with three nodes and then use the ``add_node()`` method to add a fourth node to the graph.

.. manim:: AddNode
    :quality: high

    from manim_dsa import *

    class AddNode(Scene):
        def construct(self):
            graph = {
                '0': [('1', 1), ('2', 1)],
                '1': [],
                '2': []
            }
            nodes_and_positions = {
                '0': LEFT * 2 + UP * 2,
                '1': LEFT * 2 + DOWN * 2,
                '2': RIGHT * 2 + UP * 2,
            }

            mGraph = MGraph(
                graph,
                nodes_and_positions,
                style=MGraphStyle.GREEN
            )
            self.play(Create(mGraph))

            self.play(
                mGraph.animate.add_node(
                    '3',
                    RIGHT * 2 + DOWN * 2
                )
            )
            self.wait()

Adding an edge to a MGraph
--------------------------

The ``add_edge()`` method allows you to add an edge between two nodes in a ``MGraph``. You must specify the source node and the target node, and optionally you can specify the weight of the edge. Additionally, you can customize the distance of the weight label from the edge.

In the example below, we create a MGraph with three nodes and then use the ``add_edge()`` method twice:

- The first edge is directed and has no weight.
- The second edge is undirected and has a weight of 2. 

Note that when an edge between nodes "0" and "2" already exists, adding an edge in the opposite direction (from "2" to "0") automatically converts the edge into an undirected one, removing the arrow.

.. manim:: AddEdge
    :quality: high

    from manim_dsa import *

    class AddEdge(Scene):
        def construct(self):
            graph = {
                '0': ['1', '2'],
                '1': [],
                '2': []
            }
            nodes_and_positions = {
                '0': LEFT * 2 + UP * 2,
                '1': LEFT * 2 + DOWN * 2,
                '2': RIGHT * 2 + UP * 2,
            }

            mGraph = MGraph(
                graph,
                nodes_and_positions,
                style=MGraphStyle.BLUE
            )

            self.play(Create(mGraph))
            self.play(mGraph.animate.add_edge("1", "2"))
            self.play(mGraph.animate.add_edge("2", "0", 2))
            self.wait()

Adding a curved edge to a MGraph
--------------------------------

The ``add_curved_edge()`` method allows you to add a curved edge between two nodes in a MGraph. This is particularly useful for visualizing flow network problems. You must specify the source node and the target node, and optionally you can specify:

- The weight of the edge.
- The distance of the weight label from the edge.
- The curvature of the edge.
- The starting angle of the edge relative to the node.

In the example below, we create a ``MGraph`` with three nodes and then use the ``add_curved_edge()`` method twice:

- The first curved edge is directed and has no weight.
- The second curved edge is undirected and has a weight of ``2``.

Note that when an edge between nodes ``0`` and ``2`` already exists, adding a curved edge in the opposite direction (from ``2`` to ``0``) automatically converts the edge into an undirected one, removing the arrow.

.. manim:: AddCurvedEdge
    :quality: high

    from manim_dsa import *

    class AddCurvedEdge(Scene):
        def construct(self):
            graph = {
                '0': ['1', '2'],
                '1': [],
                '2': []
            }

            nodes_and_positions = {
                '0': LEFT * 2 + UP * 2,
                '1': LEFT * 2 + DOWN * 2,
                '2': RIGHT * 2 + UP * 2,
            }

            mGraph = MGraph(
                graph,
                nodes_and_positions,
                style=MGraphStyle.PURPLE
            )

            self.play(Create(mGraph))
            self.play(mGraph.animate.add_curved_edge('1', '2'))
            self.play(mGraph.animate.add_curved_edge('2', '0', 2))
            self.wait()

Showing a backward edge in a MGraph
-----------------------------------

The ``show_backward_edge()`` method transforms an undirected edge into two directed curved edges:

- A forward curved edge with a specified weight.
- A backward curved edge with its own specified weight.

This feature is particularly useful for visualizing flow network problems. To use this method, you need to specify:

- The source and target nodes of the edge to be replaced.
- The weights for the forward and backward edges.

Optionally, you can also configure:

- The distance of the weight labels from their respective edges.
- The curvature of the edges.
- The starting angle of the edges relative to the nodes.

In the example below, we create a MGraph with three nodes and use the ``show_backward_edge()`` method to transform the directed edge between nodes ``0`` and ``2`` into two weighted curved edges:

- A forward edge from node ``0`` to node ``2`` with a weight of ``3``.
- A backward edge from node ``2`` to node ``0`` with a weight of ``0``.

.. manim:: ShowBackwardEdge
    :quality: high

    from manim_dsa import *

    class ShowBackwardEdge(Scene):
        def construct(self):
            graph = {
                '0': [('1', 4), ('2', 3)],
                '1': [],
                '2': []
            }

            nodes_and_positions = {
                '0': LEFT * 2 + UP * 2,
                '1': LEFT * 2 + DOWN * 2,
                '2': RIGHT * 2 + UP * 2,
            }

            mGraph = MGraph(
                graph,
                nodes_and_positions,
                style=MGraphStyle.GREEN
            )

            #self.play(Create(mGraph))
            #self.play(mGraph.animate.show_backward_edge("0", "2", 3, 0))
            self.play(Create(Text("FIX ME").scale(3)))
            self.wait()

.. _node_layout:

Automatically positioning nodes in a MGraph
-------------------------------------------

The ``node_layout()`` method allows you to automatically position the nodes of a ``MGraph`` without manually specifying their coordinates. Simply provide the name of the desired layout as a parameter. The available layouts are powered by the `NetworkX library <https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout>`_.

Some of the common layouts you can use include:

- ``spring_layout``
- ``circular_layout``
- ``kamada_kawai_layout``
- ``spectral_layout``
- ``random_layout``

In the example below, we create a ``MGraph`` with four nodes and then use the ``node_layout()`` method to automatically position the nodes using the ``kamada_kawai_layout``.

.. manim:: NodeLayout
    :quality: high

    from manim_dsa import *

    class NodeLayout(Scene):
        def construct(self):
            graph = {
                'a': ['b', 'c', 'd'],
                'b': ['a', 'c'],
                'c': ['a', 'b', 'd'],
                'd': ['a', 'c']
            }

            mGraph = MGraph(
                graph,
                style=MGraphStyle.BLUE
            )

            mGraph.node_layout("kamada_kawai_layout")
            self.play(Create(mGraph))
            self.wait()
