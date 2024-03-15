# shplot package


### _class_ shplot.ShPlot(\*\*kwargs)
Bases: `Corgy`

Wrapper around a `matplotlib` figure.

`ShPlot` represents a single figure, optionally associated with a
`shplot` built-in profile
([SH_BUILTIN_PROFILES][shplot.profiles.builtin.SH_BUILTIN_PROFILES]).

`ShPlot` inherits from `Corgy`, which provides a “dataclass” like
interface. Public attributes are exposed as properties, and can also
be set during initialization as keyword only arguments. All
attributes are optional; refer to their descriptions for details.
Refer to the [Corgy docs][corgy.Corgy] for details on the interface.

### Examples

```python
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
```


#### _property_ file(_: str_ )
Plot save file (extension will be automatically added if not provided).


#### _property_ builtin_profile_name(_: Literal['paper', 'book', 'web_light', 'web_dark', 'presentation']_ )
Name of a built-in profile.


#### _property_ profile_args(_: KeyValuePairs_ )
Arguments for the builtin-profile. Refer to the individual profiles for details.


#### _property_ width(_: float_ )
Plot width, in inches (if greater than 1), or as a fraction of the configured plot width (if less than or equal to 1).


#### _property_ aspect(_: float_ )
Plot aspect ratio, width/height. When provided as a command line argument, can be passed as a single number or a ratio in the form `width;height`.


#### get_plot_size()
Get computed size (width, height) of the plot in inches.


* **Return type**

    *Tuple*[float, float]



#### get_plot_path()
Get the plot save path with added extension.


* **Return type**

    *Optional*[*Path*]



#### open(\*\*kwargs)
Open the plot, and activate the profile if present.

`TypeError` is raised if `open` is called on an already open
plot.


* **Parameters**

    **\*\*kwargs** (*Any*) – passed to `matplotlib.pyplot.subplots`.



* **Return type**

    *Tuple*[*Figure*, *Axes*]



#### close()
Close the figure.

`TypeError` is raised if called on an unopened plot.


#### context(\*\*kwargs)
Context manager wrapper which opens and closes the plot.


* **Parameters**

    **\*\*kwargs** (*Any*) – passed to `matplotlib.pyplot.subplots`.



* **Return type**

    *Generator*[*Tuple*[*Figure*, *Axes*], None, None]


### Examples

```python
>>> from shplot import ShPlot
>>> shplot = ShPlot()
>>> with shplot.context() as (fig, ax):
...     pass
```

## Subpackages


* [shplot.profiles package](shplot.profiles.md)
