Animating Arrays
================

Manim Array - MArray
--------------------

In this section, you'll find all the methods available to manipulate a ``MArray`` (short for Manim Array 😄).
Key actions include adding and removing elements, swapping elements, and other essential operations. Like all ``MObject`` structures, you can animate these methods using the ``.animate`` method, allowing you to animate each operation provided by Manim DSA.
Otherwise, methods will run without any animations.

You can also access each element in a ``MArray`` using the ``[]`` operator and specifying the element’s index.

Creating a MArray
------------------

To represent an array, initialize an object of type ``MArray``. As the first parameter, provide a list of values to insert into the ``MArray``. Optionally, you can specify the direction and customize the theme of the ``MArray`` (see :ref:`customizing_a_marray`).

Here's an example that creates a ``MArray`` with a list of five numbers. By default, the array direction is to the right.

.. manim:: Creation
    :quality: high

    from manim_dsa import *

    class Creation(Scene):
        def construct(self):
            mArray = MArray([1, 2, 3, 4, 5])
            self.play(Create(mArray))
            self.wait()

.. _customizing_a_marray:

Customizing a MArray
--------------------

ManimDSA provides various options for customizing the colors and styles of a MArray. You can use these options by passing a predefined style configuration from the ``MArrayStyle`` class using the ``style`` parameter. Refer to ``MArrayStyle`` for more details. Alternatively, you can define a custom style to suit your needs.

In the following example, we use the ``BLUE`` style for the ``MArray``.

.. manim:: CustomCreation
    :quality: high

    from manim_dsa import *

    class CustomCreation(Scene):
        def construct(self):
            mArray = MArray(
                [1, 2, 3, 4, 5],
                style=MArrayStyle.BLUE
            )
            self.play(Create(mArray))
            self.wait()

Adding indexes to a MArray
--------------------------

The ``add_indexes()`` method allows you to add indexes to a MArray. You can specify the position and spacing of the indexes relative to the ``MArray``, as well as customize the properties of the indexes themselves.

In the following example, after creating a ``MArray``, we use the ``add_indexes()`` method to add indexes above each element. Additionally, we customize the color of the indexes, choosing the purple configuration provided by ManimDSA.

.. manim:: AddIndexes
    :quality: high

    from manim_dsa import *

    class AddIndexes(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3, 4, 5],
                    style=MArrayStyle.PURPLE
                )
                .add_indexes()
            )
            self.play(Create(mArray))
            self.wait()


Updating the value of an element in a MArray
--------------------------------------------
The ``set_value()`` method allows you to change the value of an element in a MArray. As stated earlier, it is sufficient to use the ``[]`` operator to access the element and then call the ``set_value()`` method on it.

In the example below, we create a ``MArray`` with five elements and then use the ``set_value()`` method to update the third element to a new value.

.. manim:: SetValue
    :quality: high

    from manim_dsa import *

    class SetValue(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3, 4, 5],
                    style=MArrayStyle.BLUE
                )
                .add_indexes()
            )
            self.play(Create(mArray))
            self.play(mArray[2].animate.set_value(10))
            self.wait()


Appending an element to a MArray
--------------------------------

The ``append()`` method allows you to add an element to the end of a ``MArray``. The new element automatically inherits the properties specified in the configuration dictionaries. Furthermore, if indexes have been added to the ``MArray``, the new element will also include a corresponding index.

In the example below, we create a ``MArray`` with indexes and then use the ``append()`` method to add a new element.

.. manim:: Append
    :quality: high

    from manim_dsa import *

    class Append(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3, 4, 5],
                    style=MArrayStyle.BLUE,
                )
                .add_indexes()
            )
            self.play(Create(mArray))
            self.play(mArray.animate.append(6))
            self.wait()

Removing an element from a MArray
---------------------------------

The ``pop()`` method allows you to remove an element from a MArray by specifying the position of the element to be removed. After the removal, the elements that follow the removed one shift left by one position, and their corresponding indexes (if present) are decremented by one.

In the example below, we create a ``MArray`` with indexes and use the ``pop()`` method to remove the third element.

.. manim:: Pop
    :quality: high

    from manim_dsa import *

    class Pop(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3, 4, 5],
                    style=MArrayStyle.BLUE
                )
                .add_indexes()
            )
            self.play(Create(mArray))
            self.play(mArray.animate.pop(2))
            self.wait()


Swapping elements in a MArray
-----------------------------

The ``swap()`` method allows you to swap two elements in a MArray by specifying their indices. This can be useful for visualizing algorithms that involve element rearrangement.

In the example below, we create a ``MArray`` with five elements and then use the ``swap()`` method to swap the second and fourth elements.

.. manim:: Swap
    :quality: high

    from manim_dsa import *

    class Swap(Scene):
        def construct(self):
            mArray = (
                MArray(
                    [1, 2, 3, 4, 5],
                    style=MArrayStyle.BLUE
                )
                .add_indexes()
            )
            self.play(Create(mArray))
            self.play(mArray.animate.swap(1, 3))
            self.wait()