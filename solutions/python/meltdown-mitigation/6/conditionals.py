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
    return temperature < 800 and neutrons_emitted>500 and temperature * neutrons_emitted < 500000
        

    

def reactor_efficiency(voltage: int | float, current: int | float, theoretical_max_power: int | float, /) -> str:
    """Assess reactor efficiency zone.

    Parameters:
        voltage: Voltage value.
        current : Current value.
        theoretical_max_power: The power level that corresponds to a 100% efficiency.

    Returns:
        eff = efficiency
        One of ('green': eff >= 80% , 'orange': 80%>eff=>60%, 'red': 60%>eff=>30%, or 'black': eff<30%).

    """
    if theoretical_max_power <= 0:
        raise ValueError('theoretical_max_power must be positive')
        
    generated_power = voltage * current
    efficiency_percentage = (generated_power/theoretical_max_power) * 100
    
    if efficiency_percentage >= 80:
        return 'green'
    if efficiency_percentage >= 60:
        return 'orange'
    if efficiency_percentage >= 30:
        return 'red'
    return 'black'
    


   
def fail_safe(temperature: float | int, neutrons_produced_per_second: int | float, threshold: int | float, /) -> str | None:
    """Assess and return status code for the reactor.

    Parameters:
        temperature: The value of the temperature in kelvin.
        neutrons_produced_per_second: The neutron flux.
        threshold: The threshold for the category.

    Returns:
        temperature_neutron_product = tnp
        One of ('LOW':`tnp` < 90%, 'NORMAL': ``tnp` +/- 10% , 'DANGER':`tnp` is not in the above-stated ranges ) of `treshold`.
        
    """
    
    temperature_neutron_product = temperature * neutrons_produced_per_second
    
    if temperature_neutron_product < threshold * 0.9:
        return 'LOW'
    if temperature_neutron_product <= threshold * 0.9 or temperature_neutron_product <= threshold * 1.1:
        return 'NORMAL'
    else:
        return 'DANGER'
    return None

    
