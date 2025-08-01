Animating Variables
===================

Manim Variable - MVariable
--------------------------

In this section, you'll find all the methods available to manipulate a ``MVariable`` (short for Manim Variable 😄).
It can be useful to visualize variables in algorithms, their assignments, updates, and other operations.
Like all ``MObject`` structures, you can animate these methods using the ``.animate`` method, allowing you to animate each operation provided by Manim DSA. Otherwise, methods will run without any animations.

You can also access the value of a ``MVariable`` directly and customize its appearance with labels and styling options.

Creating a MVariable
--------------------

To represent a variable, initialize an object of type ``MVariable``. As the first parameter, provide the initial value for the variable. The value can be of any type and will be automatically converted to its string representation for display. Optionally, you can customize the theme of the ``MVariable`` (see :ref:`customizing_a_mvariable`).

Here's an example that creates a ``MVariable`` and adds a label to it. Refer to :ref:`adding_a_label` if you miss the section on how to add labels to data structures!

.. manim:: Creation
    :quality: high

    from manim_dsa import *

    class Creation(Scene):
        def construct(self):
            mVariable = MVariable(5).add_label(
                Text("myVar", font="Cascadia Code", font_size=36),
                LEFT
            )
            self.play(Create(mVariable))
            self.wait()

.. _customizing_a_mvariable:

Customizing a MVariable
-----------------------

ManimDSA provides various options for customizing the colors and styles of a ``MVariable``. You can use these options by passing a predefined style configuration from the ``MVariableStyle`` class using the ``style`` parameter. Refer to ``MVariableStyle`` for more details. Alternatively, you can define a custom style to suit your needs.

In the following example, we use the ``BLUE`` style for the ``MVariable``.

.. manim:: CustomCreation
    :quality: high

    from manim_dsa import *

    class CustomCreation(Scene):
        def construct(self):
            mVariable = MVariable(5, style=MVariableStyle.BLUE).add_label(
                Text("myVar", font="Cascadia Code", font_size=36),
                LEFT
            )
            self.play(Create(mVariable))
            self.wait()

Updating the value of a MVariable
---------------------------------

The ``set_value()`` method allows you to change the value of a ``MVariable``. The new value can be of any type and will be automatically converted to its string representation for display. This is particularly useful for demonstrating variable assignments and updates in algorithms.

In the example below, we create a ``MVariable`` with an initial value and then use the ``set_value()`` method to update it to a new value.

.. manim:: SetValue
    :quality: high

    from manim_dsa import *

    class SetValue(Scene):
        def construct(self):
            mVariable = MVariable(5, style=MVariableStyle.BLUE).add_label(
                Text("myVar", font="Cascadia Code", font_size=36),
                LEFT
            )
            self.play(Create(mVariable))
            self.wait()
            self.play(mVariable.animate.set_value(10))
            self.wait()