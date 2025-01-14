# Examples

```{.python pycafe-embed pycafe-embed-style="border: 1px solid #e6e6e6; border-radius: 8px;" pycafe-embed-width="100%" pycafe-embed-height="400px" pycafe-embed-scale="1.0"}
import panel as pn
import numpy as np
import holoviews as hv
from panel_precision_slider import PrecisionSlider

hv.extension('bokeh')
pn.extension()

def sine_wave(frequency):
    x = np.linspace(0, 10, 500)
    y = np.sin(2 * np.pi * frequency * x)
    return hv.Curve((x, y), 'x', 'sin(2πfx)')

precision_slider = PrecisionSlider(name="Select Value", value=2.5, min=0, max=5, step=0.05)
sine_plot = pn.bind(sine_wave, precision_slider.param.value)

layout = pn.Column(
    "### Precision Slider Example",
    precision_slider,
    sine_plot
)

layout.servable()
```
