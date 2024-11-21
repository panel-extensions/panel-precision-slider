import panel as pn

from panel_precision_slider import PrecisionSlider

pn.extension()


def test_initialization():
    slider = PrecisionSlider()
    # Check default values
    assert slider.value == 5
    assert slider.min == 0
    assert slider.max == 10
    assert slider.step == 0.1
    assert not slider.show_step
    assert not slider.swap


def test_value_range():
    slider = PrecisionSlider()
    assert slider._value_input.start == slider.min
    assert slider._value_input.end == slider.max
    assert slider._value_slider.start == slider.min
    assert slider._value_slider.end == slider.max


def test_step_slider_visibility():
    slider = PrecisionSlider(show_step=True)
    assert slider._step_slider.visible

    slider.show_step = False
    assert not slider._step_slider.visible


def test_value_step():
    slider = PrecisionSlider(step=0.05)
    assert slider._value_input.step == 0.05
    assert slider._value_slider.step == 0.05


def test_swap_behavior():
    slider = PrecisionSlider(swap=True)
    assert slider._placeholder.object is slider._value_input

    slider.swap = False
    assert isinstance(slider._placeholder.object, pn.Column)
    assert slider._placeholder.object.objects[0] is slider._value_slider
    assert slider._placeholder.object.objects[1] is slider._step_slider


def test_toggle_icons():
    slider = PrecisionSlider()
    assert isinstance(slider._swap_icon, pn.widgets.ToggleIcon)
    assert isinstance(slider._show_icon, pn.widgets.ToggleIcon)


def test_update_on_swap_trigger():
    slider = PrecisionSlider()
    slider.swap = True
    assert slider._placeholder.object is slider._value_input

    slider.swap = False
    assert isinstance(slider._placeholder.object, pn.Column)
