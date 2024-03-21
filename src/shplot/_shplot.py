from __future__ import annotations

import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Generator, Optional, Tuple

if sys.version_info < (3, 9):
    from typing_extensions import Annotated, Literal
else:
    from typing import Annotated, Literal

import matplotlib as mpl
from corgy import Corgy, corgychecker, corgyparser
from corgy.types import KeyValuePairs
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from .profiles.builtin import SH_BUILTIN_PROFILES

__all__ = ["ShPlot"]


class ShPlot(Corgy):
    """Wrapper around a `matplotlib` figure.

    `ShPlot` represents a single figure, optionally associated with a
    built-in profile from
    [SH_BUILTIN_PROFILES][shplot.profiles.builtin.SH_BUILTIN_PROFILES].

    `ShPlot` inherits from `Corgy`, which provides a "dataclass" like
    interface. Public attributes are exposed as properties, and can also
    be set during initialization as keyword only arguments. All
    attributes are optional; refer to their descriptions for details.
    Refer to the [Corgy docs][corgy.Corgy] for details on the interface.

    Examples:
        >>> from tempfile import NamedTemporaryFile
        >>> from shplot import ShPlot
        >>> with NamedTemporaryFile() as save_file:
        ...     shplot = ShPlot(
        ...         file=save_file.name,
        ...         builtin_profile_name="paper",
        ...         width=3.0,
        ...         aspect=3/2,
        ...     )
        ...     fig, ax = shplot.open()  # also activates paper profile
        ...     # plot using (fig, ax)
        ...     shplot.close()  # saves plot and restores rcParams
        ...     # `ShPlot` can also be used as a context manager.
        ...     with shplot.context() as (fig, ax):
        ...         pass
        ...     # `shplot.close` will be called automatically.

    """

    file: Annotated[
        str, "Plot save file (extension will be automatically added if not provided)."
    ]
    builtin_profile_name: Annotated[
        Literal["paper", "book", "web_light", "web_dark", "presentation"],
        "Name of a built-in profile.",
        ["--shprofile"],
    ]
    profile_args: Annotated[
        KeyValuePairs,
        "Arguments for the builtin-profile. Refer to the individual "
        "profiles for details.",
    ]
    width: Annotated[
        float,
        "Plot width, in inches (if greater than 1), or as a "
        "fraction of the configured plot width (if less than or equal to 1).",
    ]
    aspect: Annotated[
        float,
        "Plot aspect ratio, width/height. When provided as a command line "
        "argument, can be passed as a single number or a ratio in the form "
        "`width;height`.",
    ]

    __slots__ = ("_fig", "_ax", "_profile", "_profile_ctx")

    def __init__(self, **kwargs):
        if "profile_args" in kwargs and not isinstance(
            kwargs["profile_args"], KeyValuePairs
        ):
            kwargs["profile_args"] = KeyValuePairs(kwargs["profile_args"])
        super().__init__(**kwargs)
        self._fig = None
        self._ax = None
        self._profile_ctx = None
        if not hasattr(self, "builtin_profile_name"):
            self._profile = None
            return

        profile_args = getattr(self, "profile_args", {})
        self._profile = SH_BUILTIN_PROFILES[self.builtin_profile_name](**profile_args)

    @corgyparser("aspect", metavar="float[;float]")
    @staticmethod
    def _parse_aspect(s: str) -> float:
        _s_parts = s.split(";")
        if len(_s_parts) == 1:
            return float(_s_parts[0])
        if len(_s_parts) == 2:
            return float(_s_parts[0]) / float(_s_parts[1])
        raise ValueError("expected one or two values")

    @corgychecker("width", "aspect")
    @staticmethod
    def _ensure_non_negative(val: float):
        if val <= 0:
            raise ValueError("expected positive value")

    def get_plot_size(self) -> Tuple[float, float]:
        """Get computed size (width, height) of the plot in inches."""
        cfg_width, cfg_height = mpl.rcParams["figure.figsize"]

        plot_width: float
        try:
            plot_width = self.width if self.width > 1 else cfg_width * self.width
        except AttributeError:
            plot_width = cfg_width

        plot_aspect: float
        try:
            plot_aspect = self.aspect
        except AttributeError:
            plot_aspect = cfg_width / cfg_height

        plot_height = plot_width / plot_aspect
        return (plot_width, plot_height)

    def get_plot_path(self) -> Optional[Path]:
        """Get the plot save path with added extension."""
        try:
            plot_path = Path(self.file)
            if plot_path.suffix:
                return plot_path
            ext = "." + mpl.rcParams["savefig.format"]
            return plot_path.with_suffix(ext)
        except AttributeError:
            return None

    def open(self, **kwargs: Any) -> Tuple[Figure, Axes]:
        """Open the plot, and activate the profile if present.

        `TypeError` is raised if `open` is called on an already open
        plot.

        Args:
            **kwargs: passed to `matplotlib.pyplot.subplots`.
        """
        if self._fig is not None:
            raise TypeError("plot already open")
        if self._profile is not None:
            self._profile_ctx = self._profile.context()
            self._profile_ctx.__enter__()
        self._fig, self._ax = plt.subplots(**kwargs)
        self._fig.set_size_inches(self.get_plot_size())
        return (self._fig, self._ax)

    def close(self):
        """Close the figure.

        `TypeError` is raised if called on an unopened plot.
        """
        if self._fig is None:
            raise TypeError("plot not open")
        if (plot_path := self.get_plot_path()) is not None:
            self._fig.savefig(plot_path)
        plt.close(self._fig)
        if self._profile is not None:
            self._profile_ctx.__exit__(None, None, None)
            self._profile_ctx = None
        self._fig = self._ax = None

    @contextmanager
    def context(self, **kwargs: Any) -> Generator[Tuple[Figure, Axes], None, None]:
        """Context manager wrapper which opens and closes the plot.

        Args:
            **kwargs: passed to `matplotlib.pyplot.subplots`.

        Examples:
            >>> from shplot import ShPlot
            >>> shplot = ShPlot()
            >>> with shplot.context() as (fig, ax):
            ...     pass

        """
        self.open(**kwargs)
        try:
            yield (self._fig, self._ax)
        finally:
            self.close()
