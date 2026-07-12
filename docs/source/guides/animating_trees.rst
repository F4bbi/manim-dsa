Animating Trees
================

Manim Tree - MTree
--------------------

In this section, you'll find all the methods available to manipulate a ``MTree`` (short for Manim Tree 😄). Like all ``MObject`` structures, you can animate these methods using the ``.animate`` method, allowing you to animate each operation provided by Manim DSA.
Otherwise, methods will run without any animations.

As with other data structures provided by the library, you can access individual nodes and edges in an ``MTree`` using the ``[]`` operator. To access a node, specify its name. To access an edge, use a tuple containing the names of the two nodes it connects.

Creating a MTree
----------------

You can create a tree by initializing an ``MTree`` object. The first parameter defines the nodes and edges of the tree, which can be specified using one of the following structures:

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

The second parameter allows you to specify the root node of the tree. If not specified, topological sorting is used to determine the root node.

Additionally, you can customize the theme of the ``MTree`` (see :ref:`customizing_a_mtree`).

Below are two examples of creating a tree:

1. A tree of 7 nodes without specifying names.
2. A tree where nodes have specified names and edges have weights.

.. manim:: BasicTree
    :quality: high

    from manim_dsa import *

    class BasicTree(Scene):
        def construct(self):
            tree = [["1", "2"], ["3", "4"], ["5", "6"], [], [], [], []]
            mTree = MTree(tree)
            self.play(Create(mTree))
            self.wait()

.. manim:: AdvancedTree
    :quality: high

    from manim_dsa import *

    class AdvancedTree(Scene):
        def construct(self):
            tree = {
                "0": [("1", 5), ("2", 3)],
                "1": [("3", 2), ("4", 7)],
                "2": [("5", 4), ("6", 1)],
                "3": [("7", 6), ("8", 3)],
                "4": [("9", 2)],
                "5": [("11", 8), ("12", 5)],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
                "11": [],
                "12": [],
            }
            mTree = MTree(tree)
            self.play(Create(mTree))
            self.wait()

Note how the node positioning is performed automatically using a hierarchical layout!

.. _customizing_a_mtree:

Customizing a MTree
--------------------

ManimDSA provides various options for customizing the colors and styles of a ``MTree``. You can use these options by passing a predefined style configuration from the ``MTreeStyle`` class using the ``style`` parameter. Refer to ``MTreeStyle`` for more details. Alternatively, you can define a custom style to suit your needs.

In the following example, we use the ``PURPLE`` style for the ``MTree``.

.. manim:: CustomCreation
    :quality: high

    from manim_dsa import *

    class CustomCreation(Scene):
        def construct(self):
            tree = {
                "0": [("1", 5), ("2", 3)],
                "1": [("3", 2), ("4", 7)],
                "2": [("5", 4), ("6", 1)],
                "3": [("7", 6), ("8", 3)],
                "4": [("9", 2)],
                "5": [("11", 8), ("12", 5)],
                "6": [],
                "7": [],
                "8": [],
                "9": [],
                "11": [],
                "12": [],
            }
            mTree = MTree(tree, style=MTreeStyle.PURPLE)
            self.play(Create(mTree))
            self.wait()
