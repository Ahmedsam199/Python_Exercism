"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?
    """
    if (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    ):
        return True
    else:
        return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone."""
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor."""
    reactor_output = temperature * neutrons_produced_per_second
    lower_limit = threshold * 0.9
    upper_limit = threshold * 1.1

    if reactor_output < lower_limit:
        return 'LOW'
    elif lower_limit <= reactor_output <= upper_limit:
        return 'NORMAL'
    else:
        return 'DANGER'
