from ._version import __version__  # noqa: F401
# :obj:`str`: version

from .core import exec_sed_task, exec_sedml_docs_in_combine_archive  # noqa: F401

__all__ = [
    '__version__',
    'exec_sed_task',
    'exec_sedml_docs_in_combine_archive',
]
