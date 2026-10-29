"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature: float, neutrons_emitted: int | float, /) -> bool:
    """Verify criticality is balanced.

    Parameters:
        temperature: The temperature value in kelvin.
        neutrons_emitted: The number of neutrons emitted per second.

    Returns:
    
        Is criticality balanced?

    Note:
        A reactor is said to be balanced in criticality if it satisfies the following conditions:
            - The temperature is less than 800 K.
            - The number of neutrons emitted per second is greater than 500.
            - The product of temperature and neutrons emitted per second is less than 500000.

    """
    if temperature < 800 and neutrons_emitted>500 and temperature * neutrons_emitted < 500000:
        return True
    return False

    


def reactor_efficiency(voltage: int | float, current: int | float, theoretical_max_power: int | float, /) -> str:
    """Assess reactor efficiency zone.

    Parameters:
        voltage: Voltage value.
        current : Current value.
        theoretical_max_power: The power level that corresponds to a 100% efficiency.

    Returns:
        One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        where generated power = voltage * current
    """
    if theoretical_max_power <= 0:
        raise ValueError("theoretical_max_powr must be positive")
        
    generated_power = voltage * current
    kpd = (generated_power/theoretical_max_power) * 100
    
    if kpd >= 80:
        return 'green'
    elif kpd >= 60:
        return 'orange'
    elif kpd >= 30:
        return 'red'
    else:
        return 'black'
    



    

    


def fail_safe(temperature: float | int, neutrons_produced_per_second: int | float, threshold: int | float, /) -> str:
    """Assess and return status code for the reactor.

    Parameters:
        temperature: The value of the temperature in kelvin.
        neutrons_produced_per_second: The neutron flux.
        threshold: The threshold for the category.

    Returns:
        One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    
    temperature_neutron_product = temperature * neutrons_produced_per_second
    
    if temperature_neutron_product < threshold * 0.9:
        return 'LOW'
    elif temperature_neutron_product <= threshold * 0.9 or temperature_neutron_product <= threshold * 1.1:
        return 'NORMAL'
    elif temperature_neutron_product > threshold * 1.1:
        return 'DANGER'

    
