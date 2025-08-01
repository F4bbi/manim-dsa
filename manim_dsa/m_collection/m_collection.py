from __future__ import annotations

from abc import ABC
from typing import Any, Self, override

from manim import *
from manim.typing import Vector3D

from manim_dsa.constants import *
from manim_dsa.utils.utils import *


class MElement(VGroup, Highlightable):
    """Represents an element in a visual collection, consisting of a square and a value.

    Parameters
    ----------
    square : :class:`~manim.mobject.geometry.polygram.Rectangle`
        The square that visually represents the element.
    value : :class:`~manim.mobject.text.text_mobject.Text`
        The text that displays the value of the element.
    """

    def __init__(self, square: Rectangle, value: Text):
        super().__init__()
        self.square = square
        self.value = value.move_to(self.square)
        self._add_highlight(self.square)
        self += self.square
        self += self.value

    def set_value(self, new_value: Any) -> Self:
        """Updates the value of the element.

        This method is necessary because the ``set_text`` method of the :class:`~manim.mobject.text.text_mobject.Text` class in Manim
        does not function as expected. Instead, this method manually removes the current text
        object and replaces it with a new one, re-centering it within the square.

        Parameters
        ----------
        new_value : Any
            The new value to set. It will be converted to a string representation.

        Returns
        -------
        self
            The updated instance of :class:`MElement` with the new value.
        """
        self -= self.value
        self.value = set_text(self.value, str(new_value))
        self += self.value
        return self

    @override_animate(set_value)
    def _set_value_animation(self, new_value: Any, anim_args: dict = None) -> Indicate:
        """Creates an animation for updating the value of the element.

        Parameters
        ----------
        value : Any
            The value to append. It will be converted to a string representation.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        Indicate
            An animation indicating the value change.
        """
        self.set_value(new_value)
        return Indicate(self.value, **anim_args)


class MCollection(ABC, VGroup, Labelable):
    """An abstract base class representing a collection of :class:`MElement` objects.

    Parameters
    ----------
    arr : list, optional
        The initial list of values to populate the collection. Default is an empty list.
    direction : :class:`~manim.typing.Vector3D`, optional
        The direction in which to arrange the elements. Default is ``RIGHT``.
    margin : float, optional
        The distance between elements in the collection. Default is ``0``.
    style : :class:`MCollectionStyle._DefaultStyle`, optional
        The style configuration for the elements. Default is ``MCollectionStyle.DEFAULT``.
    """

    def __init__(
        self,
        arr: list = [],
        direction: Vector3D = RIGHT,
        margin: float = 0,
        style: MCollectionStyle._DefaultStyle = MCollectionStyle.DEFAULT,
    ):
        super().__init__()
        self.elements = []
        self.style = style
        self.margin = margin

        self._hidden_element = MElement(
            Rectangle(**style.square).set_opacity(0),
            Text("0", **style.value).set_opacity(0),
        )
        self += self._hidden_element

        self._dir = direction
        self._dir_map = {
            UP.data.tobytes(): RIGHT,
            DOWN.data.tobytes(): RIGHT,
            RIGHT.data.tobytes(): UP,
            LEFT.data.tobytes(): UP,
        }

        for v in arr:
            self.append(v)
        self.move_to(ORIGIN)

    def append(self, value: Any) -> Self:
        """Appends a new element to the collection, styled according to the current configuration.

        Parameters
        ----------
        value : Any
            The value to append. It will be converted to a string representation.

        Returns
        -------
        self
            The instance of the :class:`MCollection` with the newly appended element.
        """
        self._update_style()

        new_elem = MElement(
            Rectangle(**self.style.square), Text(str(value), **self.style.value)
        )

        self._append_helper(new_elem)
        return self

    def _append_helper(self, new_element: MElement) -> None:
        self.elements.append(new_element)

        if len(self.elements) > 1:
            self.elements[-1].next_to(self.elements[-2].square, self._dir, self.margin)
        else:
            self.elements[-1].move_to(self._hidden_element.square)

        self += self.elements[-1]

    def _update_style(self) -> None:
        self.style.square["width"] = self.style.square["height"] = (
            self._hidden_element.square.width
        )
        self.style.value["font_size"] = self._hidden_element.value.font_size

    @override_animate(append)
    def _append_animation(self, value: Any, anim_args: dict = None) -> Write:
        """Animates the addition of a new element to the collection.

        Parameters
        ----------
        value : Any
            The value to append. It will be converted to a string representation.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        :class:`~manim.animation.creation.Write`
            An animation that displays the new element being written into the collection.
        """
        self.append(value)
        return Write(self.elements[-1], **anim_args)

    def _logic_pop(self, index) -> MElement:
        popped_element = self.elements[index]
        self -= popped_element
        self.elements.pop(index)
        return popped_element

    def pop(self, index: int = -1) -> Self:
        """Removes the element at the specified index and shifts all subsequent elements accordingly.

        Parameters
        ----------
        index : int, optional
            The index of the element to be removed. Default is ``-1``, which removes the last element.

        Returns
        -------
        self
            The instance of the :class:`MCollection` with the specified element removed.
        """
        if len(self.elements):
            popped_element = self._logic_pop(index)

            VGroup(*self.elements[index:]).shift(
                -(self._dir * popped_element.square.width)
            )
        return self

    @override_animate(pop)
    def _pop_animation(self, index: int = -1, anim_args: dict = None) -> Succession:
        """Animates the removal of an element from the collection.

        Parameters
        ----------
        index : int, optional
            The index of the element to be removed. Default is ``-1``, which removes the last element.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            An animation that shows the element being faded out and the remaining elements being shifted.
        """
        popped_element = self._logic_pop(index)

        elem_shift = VGroup(*self.elements[index:])

        anims = [
            FadeOut(popped_element),
            ApplyMethod(elem_shift.shift, -(self._dir * popped_element.square.width)),
        ]

        return Succession(*anims, **anim_args, group=VGroup(self, popped_element))

    def _visual_swap(self, i: int, j: int):
        elem_i = self.elements[i]
        elem_j = self.elements[j]
        temp = elem_i.copy()
        elem_i.move_to(elem_j, DOWN)
        elem_j.move_to(temp, DOWN)

    def _logic_swap(self, i: int, j: int):
        # Element swap
        # We have to remove first them from the scene to work correctly
        self -= self.elements[i]
        self -= self.elements[j]

        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

        # We can add the elements again
        self += self.elements[i]
        self += self.elements[j]

    def swap(self, i: int, j: int) -> Self:
        """Swaps the positions of two elements in the collection.

        Parameters
        ----------
        i : int
            The index of the first element to be swapped.
        j : int
            The index of the second element to be swapped.

        Returns
        -------
        self
            The instance of the :class:`MCollection` with the swapped elements.
        """
        self._visual_swap(i, j)
        self._logic_swap(i, j)
        return self

    @override_animate(swap)
    def _swap_animation(
        self,
        i: int,
        j: int,
        path_arc: float = PI / 2,
        anim_args: dict = None,
    ) -> ApplyMethod:
        """Animates the swap of two elements in the collection.

        Parameters
        ----------
        i : int
            The index of the first element to be swapped.
        j : int
            The index of the second element to be swapped.
        path_arc : float, optional
            The arc angle for the path of the swap animation. Default is ``PI/2``.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        :class:`~manim.animation.transform.ApplyMethod`
            An animation that shows the elements being swapped.
        """
        anim = ApplyMethod(self._visual_swap, i, j, path_arc=path_arc, **anim_args)
        self._logic_swap(i, j)
        return anim

    def _get_square_else_spawnpoint(self, index: int):
        return (
            self.elements[index].square
            if self.elements
            else self._hidden_element.square
        )

    @override
    def add_label(
        self,
        text: Text,
        direction: Vector3D = UP,
        buff: float = 0.5,
        **kwargs,
    ) -> Self:
        """Adds a label to the collection, positioned relative to its elements.

        Parameters
        ----------
        text : :class:`~manim.mobject.text.text_mobject.Text`
            The text label to be added.
        direction : :class:`~manim.typing.Vector3D`, optional
            The direction in which to position the label. Default is ``UP``.
        buff : float, optional
            The buffer distance between the label and the element. Default is 0.5.
        **kwargs :
            Additional keyword arguments that are passed to the ``next_to()`` method of the
            underlying ``add_label`` method.

        Returns
        -------
        self
            The instance of the :class:`MCollection` with the added label.
        """
        super().add_label(text, direction, buff, **kwargs)

        # If label position is parallel to array growth direction,
        # the label have to be centered
        if np.array_equal(self._dir, direction):
            reference_element = self._get_square_else_spawnpoint(-1)
        elif np.array_equal(self._dir, -direction):
            reference_element = self._get_square_else_spawnpoint(0)
        else:
            reference_element = None

        if reference_element:
            self.label.next_to(reference_element, direction, buff)

        self += self.label
        return self
