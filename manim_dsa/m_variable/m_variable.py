from __future__ import annotations

from typing import Any

from manim import *
from manim.typing import Vector3D

from manim_dsa.constants import *
from manim_dsa.m_collection.m_collection import MElement
from manim_dsa.utils.utils import *


class MVariable(MElement, Labelable):
    """Manim Variable: a class for visualizing a variable using the Manim animation engine.

    Parameters
    ----------
    value : Any
        The initial value of the variable to be displayed.
    style : :class:`MVariableStyle._DefaultStyle`, optional
        The style configuration to be applied to the variable. Defaults to ``MVariableStyle.DEFAULT``.
    """

    def __init__(
        self,
        value: Any,
        style: MVariableStyle._DefaultStyle = MVariableStyle.DEFAULT,
    ):
        self.style = style
        super().__init__(
            Rectangle(**self.style.square), Text(str(value), **self.style.value)
        )

    def add_label(
        self,
        text: Text,
        direction: Vector3D = UP,
        buff: float = 0.5,
        **kwargs,
    ):
        """Adds a label to the variable, positioned relative to its elements.

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
            The instance of the :class:`MVariable` with the added label.
        """
        super().add_label(text, direction, buff, **kwargs)
        self += self.label
        return self
