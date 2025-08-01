Some Utility Functions
======================

This section introduces additional utility functions common to all data structures provided by ManimDSA. These include the ability to add a label to a created data structure and to highlight specific elements within it.

.. _adding_a_label:

Adding a label to a data structure
----------------------------------

The ``add_label()`` method allows you to attach text to a created data structure, effectively giving it a name. The first parameter specifies the text to associate with the structure. Additionally, you can define the position and distance of the label relative to the structure. 

Once the method is called, the label can be accessed via the ``label`` attribute of the data structure, enabling further customizations.

In the example below, we create a ``MArray`` and use the ``add_label()`` method to add the text *"Array"* below the structure.

.. manim:: AddLabel
    :quality: high

    from manim_dsa import *

    class AddLabel(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3],
                    style=MArrayStyle.BLUE
                )
                .add_indexes(UP)
                .add_label(
                    Text("Array", font="Cascadia Code"),
                    DOWN
                )
            )
            self.play(Create(mArray))
            self.wait()

Highlighting and Unhighlighting elements
-----------------------------------------

The ``highlight()`` method allows you to highlight an element of any data structure provided by ManimDSA. You can specify the color and thickness of the highlight. Once the method is invoked, the highlight can be accessed through the element's ``highlighting`` attribute. 

To remove the highlight, you can use the ``unhighlight()`` method.

In the example below, we create a ``MGraph`` with two nodes and a ``MArray`` with three elements. We then use the ``highlight()`` method:

- First, to highlight the edge connecting nodes ``0`` and ``1`` in the ``MGraph``.
- Then, to highlight the first element of the ``MArray``.

.. manim:: Highlight
    :quality: high

    from manim_dsa import *

    class Highlight(Scene):
        def construct(self):
            graph = {
                '0': [('1', 5)],
                '1': [],
            }
            nodes_and_positions = {
                '0': LEFT * 2,
                '1': RIGHT * 2,
            }

            mGraph = (
                MGraph(
                    graph,
                    nodes_and_positions,
                    style=MGraphStyle.PURPLE
                )
                .shift(LEFT * 3)
            )

            mArray = (
                MArray(
                    [1, 2, 3],
                    style=MArrayStyle.BLUE
                )
                .add_indexes(UP)
                .shift(RIGHT * 3)
            )

            self.play(Create(mGraph))
            self.play(Create(mArray))
            self.play(mGraph[('0', '1')].animate.highlight(GREEN))
            self.play(mArray[0].animate.highlight(RED))
            self.wait()