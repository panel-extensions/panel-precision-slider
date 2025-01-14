# ✨ panel-precision-slider

[![CI](https://img.shields.io/github/actions/workflow/status/panel-extensions/panel-precision-slider/ci.yml?style=flat-square&branch=main)](https://github.com/panel-extensions/panel-precision-slider/actions/workflows/ci.yml)
[![pypi-version](https://img.shields.io/pypi/v/panel-precision-slider.svg?logo=pypi&logoColor=white&style=flat-square)](https://pypi.org/project/panel-precision-slider)
[![python-version](https://img.shields.io/pypi/pyversions/panel-precision-slider?logoColor=white&logo=python&style=flat-square)](https://pypi.org/project/panel-precision-slider)

A versatile slider with fine-tuned control, adjustable precision, and direct text input for exact values.

![Export-1732234916141](https://github.com/user-attachments/assets/5ac903ae-5bcf-4d8e-af17-40d76c5d9fb3)

## Features

- **Toggle Between Slider and Input:** Switch between a slider and a direct input field for value selection.
- **Adjustable Step Size:** Show or hide the step size adjustment slider to control the precision of the value.
- **Customizable Icons:** Use toggle icons to enhance the user interface for swapping views and showing steps.

## Pin your version!

This project is **in its early stages**, so if you find a version that suits your needs, it’s recommended to **pin your version**, as updates may introduce changes.

## Installation

Install it via `pip`:

```bash
pip install panel-precision-slider
```

## Usage

```python
import panel_precision_slider
```

## Development

```bash
git clone https://github.com/panel-extensions/panel-precision-slider
cd panel-precision-slider
```

For a simple setup use [`uv`](https://docs.astral.sh/uv/):

```bash
uv venv
source .venv/bin/activate # on linux. Similar commands for windows and osx
uv pip install -e .[dev]
pre-commit run install
pytest tests
```

For the full Github Actions setup use [pixi](https://pixi.sh):

```bash
pixi run pre-commit-install
pixi run postinstall
pixi run test
```

This repository is based on [copier-template-panel-extension](https://github.com/panel-extensions/copier-template-panel-extension) (you can create your own Panel extension with it)!

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

Note: `copier` will show `Conflict` for files with manual changes during an update. This is normal. As long as there are no merge conflict markers, all patches applied cleanly.

## ❤️ Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please ensure your code adheres to the project's coding standards and passes all tests.
