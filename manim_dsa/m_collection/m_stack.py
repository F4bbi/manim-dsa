from __future__ import annotations

from manim.typing import Point3D

from manim_dsa.m_collection.m_collection import *

class MStack(MCollection):
    """Manim Stack: a class for visualizing the stack data structure using the Manim animation engine.

    Parameters
    ----------
    arr : list, optional
        The initial list of values to populate the stack. Default is an empty list.
    buff : float, optional
        The buffer (margin) between elements in the stack. Default is ``0.1``.
    style : :class:`MStackStyle._DefaultStyle`, optional
        The style configuration for the stack elements. Default is ``MStackStyle.DEFAULT``.
    """

    def __init__(
        self,
        arr: list = [],
        buff: float = 0.1,
        style: MStackStyle._DefaultStyle = MStackStyle.DEFAULT,
    ):
        super().__init__(arr, UP, buff, style)

        elem = self.elements[0].square if self.elements else self._hidden_element.square
        container_height = (
            (len(arr) + 3) * elem.height
            if arr
            else self._hidden_element.square.height * 7
        )

        self.bottom_line: Line = Line(ORIGIN, [elem.width + 2 * buff, 0, 0]).next_to(
            elem, DOWN, buff
        )
        self.left_line: Line = Line([0, container_height, 0], ORIGIN).next_to(
            self.bottom_line, UL, 0
        )
        self.right_line: Line = self.left_line.copy().next_to(self.bottom_line, UR, 0)

        self.container: VGroup = VGroup(
            self.left_line, self.bottom_line, self.right_line
        )
        self += self.container
        self.move_to(ORIGIN)
        self.spawnpoint: Point3D = None

        # When the stack is scaled or moved,
        # the spawn_point of the objects must be changed as well
        def update_stack_attr(obj):
            obj.spawnpoint = obj.get_spawn_point()
            obj.margin = buff * self._hidden_element.square.width

        self.add_updater(update_stack_attr)

    def _grow_container(self) -> None:
        """Extends the container's side lines upwards if the elements exceed them."""
        if not hasattr(self, "container") or not self.elements:
            return

        top_elem = self.elements[-1].square
        required_top = top_elem.get_top()[1] + self.margin
        for line in (self.left_line, self.right_line):
            start, end = line.get_start_and_end()
            if required_top > start[1]:
                line.put_start_and_end_on(
                    np.array([start[0], required_top, start[2]]), end
                )

    def get_spawn_point(self) -> Point3D:
        """Calculates the drop point for new elements in the stack.

        Returns
        -------
        :class:`~manim.typing.Point3D`
            The spawn point position in 3D space.
        """
        return (
            self.bottom_line.get_center()
            + (UP * self.right_line.height)
            + UP * self._hidden_element.square.width
        )

    def append(self, value: Any) -> Self:
        """Appends a new value to the top of the stack.

        Parameters
        ----------
        value : Any
            The value to be added to the stack. It will be converted to a string representation.

        Returns
        -------
        self
            The instance of the :class:`MStack` with the newly appended element.
        """
        super().append(value)
        self._grow_container()
        return self

    @override_animate(append)
    def _append_animation(self, value: Any, anim_args: dict = None) -> Succession:
        """Creates an animation for appending a new value to the stack.

        Parameters
        ----------
        value : Any
            The value to be added to the stack. It will be converted to a string representation.
        anim_args : dict, optional
            Additional animation arguments.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            The animation object representing the append operation.
        """
        old_top = self.left_line.get_start()[1]
        self.append(value)
        new_pos = self.elements[-1].get_center()
        # The spawn point is recomputed instead of using the cached
        # self.spawnpoint, so that it lies above the walls even when
        # the append made the container grow
        self.elements[-1].move_to(self.get_spawn_point())

        # The wall growth is animated together with the element creation:
        # if it ran as a separate step, the new element (already part of the
        # group) would be visible before its Create animation starts
        spawn_anims = [Create(self.elements[-1])]
        growth = self.left_line.get_start()[1] - old_top
        if growth > 0:
            # Revert the walls to their pre-append height so the growth
            # can be animated instead of jumping instantly
            for line in (self.left_line, self.right_line):
                start, end = line.get_start_and_end()
                line.put_start_and_end_on(start + DOWN * growth, end)
                spawn_anims.append(ApplyMethod(line.put_start_and_end_on, start, end))

        return Succession(
            AnimationGroup(*spawn_anims),
            ApplyMethod(self.elements[-1].move_to, new_pos),
            **anim_args,
            group=self,
        )

    @override
    def pop(self) -> Self:
        """Removes the top element from the stack.

        Returns
        -------
        self
            The instance of the :class:`MStack` with the top element removed.
        """
        return super().pop(len(self.elements) - 1)

    @override_animate(pop)
    def _pop_animation(self, anim_args: dict = None) -> Succession:
        """Creates an animation for removing the top element from the stack.

        Parameters
        ----------
        anim_args : dict, optional
            Additional animation arguments.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            The animation object representing the pop operation.
        """
        popped_element = self.elements[-1].copy()
        self.pop()
        return Succession(
            ApplyMethod(popped_element.move_to, self.spawnpoint),
            FadeOut(popped_element),
            **anim_args,
            group=VGroup(self, popped_element),
        )

    def add_label(
        self,
        text: Text,
        direction: Vector3D = UP,
        buff: float = 0.5,
        **kwargs,
    ) -> Self:
        """Adds a label to the stack.

        Parameters
        ----------
        text : :class:`~manim.mobject.text.text_mobject.Text`
            The label text.
        direction : :class:`~manim.typing.Vector3D`, optional
            The direction in which to position the label. Default is ``UP``.
        buff : float, optional
            The distance (buffer) between the stack and the label. Default is 0.5.
        **kwargs :
            Additional keyword arguments that are passed to the ``next_to()`` method of the
            underlying ``add_label`` method.

        Returns
        -------
        self
            The instance of the :class:`MStack` with the label added.
        """
        super().add_label(text, direction, buff, **kwargs)
        self.label.move_to(self.get_spawn_point())
        return self
