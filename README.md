# panel-precision-slider

[![CI](https://img.shields.io/github/actions/workflow/status/panel-extensions/panel-precision-slider/ci.yml?style=flat-square&branch=main)](https://github.com/panel-extensions/panel-precision-slider/actions/workflows/ci.yml)
[![pypi-version](https://img.shields.io/pypi/v/panel-precision-slider.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-precision-slider)
[![python-version](https://img.shields.io/pypi/pyversions/panel-precision-slider?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-precision-slider)

A versatile slider with fine-tuned control, adjustable precision, and direct text input for exact values.

## Features

- **Toggle Between Slider and Input:** Switch between a slider and a direct input field for value selection.
- **Adjustable Step Size:** Show or hide the step size adjustment slider to control the precision of the value.
- **Customizable Icons:** Use toggle icons to enhance the user interface for swapping views and showing steps.

## Installation

Install it via `pip`:

```bash
pip install panel-precision-slider
```

## Development

This project is managed by [pixi](https://pixi.sh).
You can install the package in development mode using:

```bash
git clone https://github.com/panel-extensions/panel-precision-slider
cd panel-precision-slider

pixi run pre-commit-install
pixi run postinstall
pixi run test
```

## Usage

The `PrecisionSlider` is a custom Panel component that provides a synchronized slider and input field for selecting numerical values with adjustable precision. Users can toggle between a slider and a direct input field, as well as show or hide the step size adjustment.

### Basic Example

```python
import panel as pn
from panel_precision_slider import PrecisionSlider

pn.extension()

# Instantiate the PrecisionSlider
precision_slider = PrecisionSlider(
    value=5,
    min=0,
    max=10,
    step=0.1,
    show_step=True,
    swap=False
)

# Display the slider
precision_slider
```

### Integrating with Other Panel Components

You can integrate `PrecisionSlider` with other Panel widgets and layouts to build interactive dashboards.

```python
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

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.
