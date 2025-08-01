from __future__ import annotations

from typing import Any, override

from manim import *
from manim.typing import Vector3D

from manim_dsa.constants import *
from manim_dsa.m_collection.m_collection import *
from manim_dsa.utils.utils import *


class MIndexedElement(MElement):
    """An extension of the :class:`MElement` class that includes an index for each element.

    Parameters
    ----------
    square : :class:`~manim.mobject.geometry.polygram.Rectangle`
        The rectangle representing the visual boundary of the element.
    value : :class:`~manim.mobject.text.text_mobject.Text`
        The text representing the value contained in the element.
    """

    def __init__(self, square: Rectangle, value: Text):
        super().__init__(square, value)

    def set_index(self, new_index: Any) -> Self:
        """
        Updates the index of the element to a new value.

        Parameters
        ----------
        new_index : Any
            The new index value to set. It will be converted to a string representation.

        Returns
        -------
        self
            The instance of the :class:`MIndexedElement` with the updated index.
        """
        self -= self.index
        self.index = set_text(self.index, str(new_index))
        self += self.index
        return self

    def add_index(
        self,
        index: Text,
        direction: Vector3D = UP,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    ) -> Self:
        """
        Adds an index to the element, positioning it relative to the element.

        Parameters
        ----------
        index : :class:`~manim.mobject.text.text_mobject.Text`
            The text object representing the index.
        direction : :class:`~manim.typing.Vector3D`, optional
            The direction in which to position the index relative to the element. Default is ``UP``.
        buff : float, optional
            The distance (buffer) between the element and the index.
            Default is ``DEFAULT_MOBJECT_TO_MOBJECT_BUFFER``.

        Returns
        -------
        self
            The instance of the :class:`MIndexedElement` with the updated index.
        """
        self.index = index.next_to(self.square, direction, buff)
        self += self.index
        return self


class MArray(MCollection):
    """Manim Array: a class for visualizing the array data structure using the Manim animation engine.

    Parameters
    ----------
    arr : list, optional
        The initial list of values to populate the array. Default is an empty list.
    direction : :class:`~manim.typing.Vector3D`, optional
        The direction in which to arrange the elements. Default is ``RIGHT``.
    margin : float, optional
        The margin between elements in the array. Default is 0.
    style : :class:`MArrayStyle._DefaultStyle`, optional
        The style configuration for the elements. Default is ``MArrayStyle.DEFAULT``.
    """

    def __init__(
        self,
        arr: list = [],
        direction: Vector3D = RIGHT,
        style: MArrayStyle._DefaultStyle = MArrayStyle.DEFAULT,
    ):
        self._index_enabled: bool = False
        self._index_dir = None

        super().__init__(arr, direction, 0, style)

        self._hidden_element = MIndexedElement(
            self._hidden_element.square,
            self._hidden_element.value,
        )
        self += self._hidden_element

    def append(self, value: Any) -> Self:
        """Appends a new element to the end of the array. If indexing is enabled,
        the new element will also be assigned an index based on its position in the array.

        Parameters
        ----------
        value : Any
            The value to append. It will be converted to a string representation.

        Returns
        -------
        self
            The instance of the :class:`MArray` with the newly appended element.
        """
        self._update_style()

        new_elem = MIndexedElement(
            Rectangle(**self.style.square), Text(str(value), **self.style.value)
        )

        self._append_helper(new_elem)

        if self._index_enabled:
            index = Text(str(len(self.elements) - 1), **self.style.index)
            self.elements[-1].add_index(index, self._index_dir, self._get_index_buff())

        return self

    @override_animate(append)
    def _append_animation(self, value: Any, anim_args: dict = None) -> Animation:
        """Animates the addition of a new element to the array.

        Parameters
        ----------
        value : Any
            The value to append. It will be converted to a string representation.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        :class:`~manim.animation.creation.Write`
            An animation that displays the new element being written into the array.
        """
        return super()._append_animation(value, anim_args)

    @override
    def _update_style(self) -> None:
        super()._update_style()
        if self._index_enabled:
            self.style.index["font_size"] = self._hidden_element.index.font_size

    def pop(self, index: int = -1) -> Self:
        """Removes the element at the specified index and shifts all subsequent elements accordingly.
        If indexing is enabled, it also updates the indices of the remaining elements.

        Parameters
        ----------
        index : int, optional
            The index of the element to be removed. Default is ``-1``, which removes the last element.

        Returns
        -------
        self
            The instance of the :class:`MArray` with the specified element removed.
        """
        if len(self.elements):
            popped_element = self.elements[index].copy()
            super().pop(index)

            if self._index_enabled:
                self._set_index_from(
                    index, len(self.elements) - 1, popped_element.index
                )
        return self

    @override_animate(pop)
    def _pop_animation(self, index: int = -1, anim_args: dict = None) -> Animation:
        """Animates the removal of an element from the array.

        Parameters
        ----------
        index : int, optional
            The index of the element to be removed. Default is ``-1``, which removes the last element.
        anim_args : dict, optional
            Additional arguments for the animation. Default is ``None``.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            An animation showing the element being removed and the indices being updated.
        """
        popped_element = self._logic_pop(index)

        elem_shift = VGroup(*self.elements[index:])

        anims = [
            FadeOut(popped_element),
            ApplyMethod(elem_shift.shift, -(self._dir * popped_element.square.width)),
        ]

        if self._index_enabled:
            anims.append(
                ApplyMethod(
                    self._set_index_from,
                    index,
                    len(self.elements) - 1,
                    popped_element.index.copy(),
                )
            )

        return Succession(*anims, **anim_args, group=VGroup(self, popped_element))

    def _set_index_from(self, start: int, end: int, popped_index: MElement) -> Self:
        old_index = popped_index
        for i in range(start, end + 1):
            curr = self.elements[i]
            new_index = old_index.copy().move_to(curr.index)
            old_index = curr.index
            curr -= curr.index
            curr.index = new_index
            curr += curr.index
        return self

    def _get_index_buff(self) -> float:
        square_center = self._hidden_element.square.get_center()
        index_center = self._hidden_element.index.get_center()
        offset = self._hidden_element.square.width / 2

        if np.array_equal(self._dir, UP) or np.array_equal(self._dir, DOWN):
            offset += self._hidden_element.index.width / 2
            direction_offset = [offset, 0, 0]
        else:
            offset += self._hidden_element.index.height / 2
            direction_offset = [0, offset, 0]

        if np.array_equal(self._index_dir, UP) or np.array_equal(
            self._index_dir, RIGHT
        ):
            return (index_center - square_center - direction_offset)[1]
        else:
            return (square_center - index_center - direction_offset)[1]

    def _visual_swap(self, i: int, j: int) -> None:
        elem_i = self.elements[i]
        elem_j = self.elements[j]
        elem_i_group = VGroup(elem_i.square, elem_i.value)
        temp = elem_i_group.copy()
        elem_j_group = VGroup(elem_j.square, elem_j.value)
        elem_i_group.move_to(elem_j_group, DOWN)
        elem_j_group.move_to(temp, DOWN)

    def _logic_swap(self, i: int, j: int) -> None:
        # Element swap
        # We have to remove first them from the scene to work correctly
        self -= self.elements[i]
        self -= self.elements[j]

        self.elements[i], self.elements[j] = self.elements[j], self.elements[i]

        if self._index_enabled:
            # Index swap
            # We have to remove first them from the scene to work correctly
            self.elements[i] -= self.elements[i].index
            self.elements[j] -= self.elements[j].index

            self.elements[i].index, self.elements[j].index = (
                self.elements[j].index,
                self.elements[i].index,
            )

            # We can add the indexes again
            self.elements[i] += self.elements[i].index
            self.elements[j] += self.elements[j].index

        # We can add the elements again
        self += self.elements[i]
        self += self.elements[j]

    def add_indexes(
        self,
        direction: Vector3D = UP,
        buff: float = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    ) -> Self:
        """Adds indexes to each element in the array, displaying them in the specified direction.

        Parameters
        ----------
        direction : :class:`~manim.typing.Vector3D`, optional
            The direction in which to display the indices relative to the elements.
            Default is ``UP``.
        buff : float, optional
            The buffer distance between the element and its index.
            Default is ``DEFAULT_MOBJECT_TO_MOBJECT_BUFFER``.

        Returns
        -------
        self
            The instance of the :class:`MArray` with the indices added to each element.

        Raises
        ------
        Exception
            If the specified direction is parallel to the array's growth direction.

        Notes
        -----
        If indices are already enabled, this method returns immediately without making any changes.
        """
        if self._index_enabled:
            return self
        if np.array_equal(np.abs(self._dir), np.abs(direction)):
            raise Exception(
                "The direction given is parallel to array growth direction!"
            )

        self._index_enabled = True
        self._index_dir = direction

        self._hidden_element.add_index(
            Text("0", **self.style.index, fill_opacity=0), direction, buff
        )
        for i in range(len(self.elements)):
            self.elements[i].add_index(
                Text(str(i), **self.style.index), direction, buff
            )

        return self
