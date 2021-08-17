from .. import core
from .._version import __version__  # noqa: F401
from ..data_model import Simulator
import functools
import brian2

__all__ = [
    '__version__',
    'get_simulator_version',
    'exec_sed_task',
    'exec_sedml_docs_in_combine_archive',
]


def get_simulator_version():
    """ Get the version of pyNeuroML

    Returns:
        :obj:`str`: version
    """
    return brian2.__version__


exec_sed_task = functools.partial(core.exec_sed_task, simulator=Simulator.brian2)

exec_sedml_docs_in_combine_archive = functools.partial(core.exec_sedml_docs_in_combine_archive, simulator=Simulator.brian2)
