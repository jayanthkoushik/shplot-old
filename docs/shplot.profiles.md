# shplot.profiles package


### _class_ shplot.profiles.ProfileBase(\*\*args)
Bases: `Corgy`

Base class for profiles.

Profile classes are thin wrappers around subsets of `matplotlib`
parameters. Once instantiated, they can be used to generate a
dictionary, which can be used to update `matplotlib.rcParams`.

Profile classes have a dataclass-like interface. All attributes are
exposed as properties, and can be set either at initialization (as
keyword arguments) or later. Unless specified otherwise, attributes
directly correspond to `matplotlib` parameters with the same name.

### Examples

```python
>>> from shplot.profiles import ColorProfile
>>> profile = ColorProfile(fg_secondary="gray")
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'gray'}
```

```python
>>> profile.grid_alpha = 0.5
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'gray',
'grid.alpha': 0.5}
```


#### rc()
Return profile configuration as a `dict` of `rcParams`.

Unset attributes are not included in the returned dictionary so
that different profiles can be combined together.


* **Return type**

    *Dict*[str, *Any*]



#### config(reload_mpl=True)
Update `matplotlib.rcParams` with profile configuration.


* **Parameters**

    **reload_mpl** (*bool*) – Whether to reload `matplotlib` and `pyplot`
    modules before applying the configuration. Reloading is
    necessary for fonts to be updated.


### Examples

```python
>>> import matplotlib as mpl
>>> print(mpl.rcParams["grid.color"])
#b0b0b0
>>> color_prof = ColorProfile(fg_secondary="gray")
>>> color_prof.config()
>>> print(mpl.rcParams["grid.color"])
gray
```


#### context(reload_mpl=True)
Context manager for `config` method.


* **Parameters**

    **reload_mpl** (*bool*) – Whether to first reload `matplotlib` and
    `pyplot` modules.


### Examples

```python
>>> mpl.rcParams["grid.color"] = 'black'
>>> print(mpl.rcParams["grid.color"])
black
>>> color_prof = ColorProfile(fg_secondary="red")
>>> with color_prof.context():
...     print(mpl.rcParams["grid.color"])
red
>>> print(mpl.rcParams["grid.color"])
black
```


### _class_ shplot.profiles.ColorProfile(\*\*args)
Bases: [`ProfileBase`](#shplot.profiles.ProfileBase)

Wrapper for color-related matplotlib params.


#### _property_ palette(_: List[str]_ )
`axes.prop_cycle` colors.


#### _property_ fg(_: str_ )
Primary foreground color, used for text, axes lines, ticks, etc.


#### _property_ fg_secondary(_: str_ )
Secondary foreground color, used for grid lines and legend frame.


#### _property_ bg(_: str_ )
Axes and figure face color.


#### _property_ grid_alpha(_: float_ )

#### _property_ legend_frame_alpha(_: float_ )

#### _property_ transparent(_: bool_ )
Whether to save figures with transparent background.


### _class_ shplot.profiles.FontProfile(\*\*args)
Bases: [`ProfileBase`](#shplot.profiles.ProfileBase)

Wrapper for font-related matplotlib params.


#### _property_ family(_: List[str]_ )

#### _property_ style(_: Literal['normal', 'italic', 'oblique']_ )

#### _property_ variant(_: Literal['normal', 'small-caps']_ )

#### _property_ weight(_: Literal['normal', 'bold', '100', '200', '300', '400', '500', '600', '700', '800', '900']_ )

#### _property_ stretch(_: Literal['ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded', 'wider', 'narrower']_ )

#### _property_ serif(_: List[str]_ )

#### _property_ sans_serif(_: List[str]_ )

#### _property_ monospace(_: List[str]_ )

#### _property_ cursive(_: List[str]_ )

#### _property_ fantasy(_: List[str]_ )

#### _property_ text_usetex(_: bool_ )

#### _property_ latex_preamble(_: List[str]_ )

#### _property_ math_fontset(_: Literal['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']_ )

#### _property_ custom_math_rm(_: str_ )

#### _property_ custom_math_sf(_: str_ )

#### _property_ custom_math_tt(_: str_ )

#### _property_ custom_math_it(_: str_ )

#### _property_ custom_math_bf(_: str_ )

#### _property_ custom_math_cal(_: str_ )

#### _property_ math_fallback(_: Literal['cm', 'stix', 'stixsans', 'None']_ )

#### _property_ math_default(_: Literal['rm', 'cal', 'it', 'tt', 'sf', 'bf', 'default', 'bb', 'frak', 'scr', 'regular']_ )

#### _property_ pgf_rcfonts(_: bool_ )

#### _property_ set_pgf_preamble(_: bool_ )
Whether to set `pgf.preamble` using `latex_preamble`.


### _class_ shplot.profiles.FloatOrStr()
Bases: `ABC`

Float or string type.


### _class_ shplot.profiles.PlotScaleProfile(\*\*args)
Bases: [`ProfileBase`](#shplot.profiles.ProfileBase)

Wrapper for plot scale-related matplotlib params.


#### _property_ font_size(_: float_ )

#### _property_ axes_title_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ axes_label_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ xtick_label_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ ytick_label_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ legend_font_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ legend_title_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ figure_title_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ figure_label_size(_: [FloatOrStr](#shplot.profiles.FloatOrStr)_ )

#### _property_ marker_size(_: float_ )

#### _property_ line_width(_: float_ )

#### _property_ full_width_in(_: float_ )
Default figure width in inches.


#### _property_ default_aspect_wh(_: float_ )
Default figure aspect ratio (width/height).


#### _property_ legend_marker_scale(_: float_ )

#### _property_ subplot_left(_: float_ )

#### _property_ subplot_right(_: float_ )

#### _property_ subplot_bottom(_: float_ )

#### _property_ subplot_top(_: float_ )

#### _property_ subplot_hspace(_: float_ )

#### _property_ subplot_wspace(_: float_ )

#### _property_ autolayout(_: bool_ )

#### _property_ constrained_layout(_: bool_ )

#### _property_ constrained_layout_hspace(_: float_ )

#### _property_ constrained_layout_wspace(_: float_ )

### _class_ shplot.profiles.AxesProfile(\*\*args)
Bases: [`ProfileBase`](#shplot.profiles.ProfileBase)

Wrapper for axes-related matplotlib params.


#### _property_ grid_axes(_: Literal['x', 'y', 'both', 'none']_ )
which axes to draw grid lines on


#### _property_ grid_lines(_: Literal['major', 'minor', 'both']_ )
which grid lines to draw


#### _property_ spines(_: Set[Literal['left', 'right', 'bottom', 'top']]_ )
which sides to draw spines on


#### _property_ axis_below(_: Literal['all', 'line', 'none']_ )
where to draw axis grid lines and ticks


#### _property_ xticks_top(_: Literal['none', 'major', 'both']_ )
which tick lines to draw on the top x-axis


#### _property_ xticks_bottom(_: Literal['none', 'major', 'both']_ )
which tick lines to draw on the bottom x-axis


#### _property_ xlabels_top(_: bool_ )
whether to show labels on the top x-axis


#### _property_ xlabels_bottom(_: bool_ )
whether to show labels on the bottom x-axis


#### _property_ xtick_direction(_: Literal['in', 'out', 'inout']_ )
direction of x-axis ticks


#### _property_ xtick_alignment(_: Literal['left', 'center', 'right']_ )
alignment of x-axis tick labels


#### _property_ xlabel_position(_: Literal['left', 'center', 'right']_ )
position of x-axis label


#### _property_ yticks_left(_: Literal['none', 'major', 'both']_ )
which tick lines to draw on the left y-axis


#### _property_ yticks_right(_: Literal['none', 'major', 'both']_ )
which tick lines to draw on the right y-axis


#### _property_ ylabels_left(_: bool_ )
whether to show labels on the left y-axis


#### _property_ ylabels_right(_: bool_ )
whether to show labels on the right y-axis


#### _property_ ytick_direction(_: Literal['in', 'out', 'inout']_ )
direction of y-axis ticks


#### _property_ ytick_alignment(_: Literal['bottom', 'center', 'top', 'baseline', 'center_baseline']_ )
alignment of y-axis tick labels


#### _property_ ylabel_position(_: Literal['bottom', 'center', 'top']_ )
position of y-axis labels


### _class_ shplot.profiles.PlottingProfile(\*\*kwargs)
Bases: [`ProfileBase`](#shplot.profiles.ProfileBase)

Wrapper for color, font, scale, and axes profiles.

All arguments for initialization are optional, and must be passed as
keyword arguments. Arguments other than `color`, `font`, `scale`,
and `axes` are used to update `matplotlib.rcParams` directly, and
will override any values set by the profile.

### Examples

```python
>>> from shplot.profiles import PlottingProfile, ColorProfile
>>> color_profile = ColorProfile(fg_secondary="gray")
>>> rc_extra = {"backend": "Agg", "legend.edgecolor": "black"}
>>> profile = PlottingProfile(color=color_profile, **rc_extra)
>>> profile.rc()
{'grid.color': 'gray', 'legend.edgecolor': 'black',
'backend': 'Agg'}
```


#### _property_ color(_: [ColorProfile](#shplot.profiles.ColorProfile)_ )

#### _property_ font(_: [FontProfile](#shplot.profiles.FontProfile)_ )

#### _property_ scale(_: [PlotScaleProfile](#shplot.profiles.PlotScaleProfile)_ )

#### _property_ axes(_: [AxesProfile](#shplot.profiles.AxesProfile)_ )
## Submodules


* [shplot.profiles.builtin module](shplot.profiles.builtin.md)
