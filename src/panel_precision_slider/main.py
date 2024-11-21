import panel as pn
import param


class PrecisionSlider(pn.custom.PyComponent):
    """
    PrecisionSlider is a custom Panel component that provides a synchronized
    slider and input field for selecting numerical values with adjustable precision.
    Users can toggle between a slider and a direct input field, as well as show or hide
    the step size adjustment.
    """

    value = param.Number(default=5, doc="The current value of the slider/input field.")

    min = param.Number(default=0, doc="The minimum allowable value.")

    max = param.Number(default=10, doc="The maximum allowable value.")

    step = param.Number(default=0.1, bounds=(1e-6, None), doc="The step size for the slider/input field.")

    show_step = param.Boolean(
        default=True, label="", doc="Display the step size adjustment slider."
    )

    swap = param.Boolean(
        default=False,
        label="",
        doc="Flag to toggle between the slider and input field.",
    )

    def __init__(self, **params):
        """
        Initializes the PrecisionSlider component with the given parameters.

        Args:
            **params: Additional parameters to override the default settings.
        """
        super().__init__(**params)

        self._swap_icon = pn.widgets.ToggleIcon.from_param(
            self.param.swap,
            icon="numbers",
            active_icon="adjustments-horizontal",
            margin=0,
        )
        self._show_icon = pn.widgets.ToggleIcon.from_param(
            self.param.show_step,
            icon="eye",
            active_icon="eye-off",
            margin=0,
        )
        self._placeholder = pn.pane.Placeholder()
        self._value_slider = pn.widgets.FloatSlider.from_param(
            self.param.value,
            start=self.param.min,
            end=self.param.max,
            step=self.param.step,
        )
        self._step_slider = pn.widgets.FloatSlider.from_param(
            self.param.step,
            start=1e-6,
            step=0.1,
            visible=self.param.show_step,
        )
        self._value_input = pn.widgets.FloatInput(
            start=self.param.min,
            end=self.param.max,
            step=self.param.step,
            width=params.get("width"),
            min_width=params.get("min_width"),
            max_width=params.get("max_width"),
        )
        self._value_slider.link(self._value_input, value="value", bidirectional=True)
        self.param.trigger("swap")

    @param.depends("swap", watch=True)
    def _swap_widgets(self):
        """
        Updates the displayed widgets based on the swap parameter.
        If swap is True, shows the value input field.
        Otherwise, shows the value slider and step size slider.
        """
        if self.swap:
            self._placeholder.update(pn.Column(self._value_input, self._step_slider))
        else:
            self._placeholder.update(pn.Column(self._value_slider, self._step_slider))

    def __panel__(self):
        """
        Constructs the Panel layout for the PrecisionSlider component.

        Returns:
            pn.Column: A vertical layout containing the main widget and control icons.
        """
        return pn.Column(
            self._placeholder,
            pn.Row(self._swap_icon, self._show_icon, margin=(1, 10)),
        )
