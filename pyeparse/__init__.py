# Authors: Denis Engemann <d.engemann@fz-juelich.de>
#
# License: BSD (3-clause)

from . import utils  # noqa
from .edf._raw import RawEDF  # noqa
Raw = RawEDF  # noqa
from .epochs import Epochs  # noqa
from . import constants  # noqa
from . import viz  # noqa
from . import edf  # noqa

__version__ = 0.01
