from importlib.metadata import version

from .constants import MArrayStyle, MGraphStyle, MStackStyle, MTreeStyle, MVariableStyle
from .m_collection.m_array import MArray
from .m_collection.m_stack import MStack
from .m_graph.m_graph import MGraph
from .m_graph.m_tree import MTree
from .m_variable.m_variable import MVariable

__version__ = version(__name__)

__all__ = [
    "MArray",
    "MStack",
    "MGraph",
    "MTree",
    "MVariable",
    "MArrayStyle",
    "MStackStyle",
    "MGraphStyle",
    "MTreeStyle",
    "MVariableStyle",
]
