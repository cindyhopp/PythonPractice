"""Temperature conversion"""

__author__ = 'Cindy Lu'

import argparse
from random import choices


# Define temperature conversion functions
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature in Celsius to Fahrenheit
    
    Keyword arguments:
    celsius -- The temperature in Celsius
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert a temperature in Fahrenheit to Celsius
    
    Keyword arguments:
    fahrenheit -- The temperature in Fahrenheit
    """
    return (fahrenheit - 32) * 5 / 9


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Parse temperature arguments')
    # An argument for the temperature that will be converted
    parser.add_argument('temperature', type=float, 
        help='The temperature to convert')
    # An argument for the from unit - this will be the unit 
    # of the temperature argument
    parser.add_argument('from_unit', type=str, 
        choices=['f', 'c', 'fahrenheit', 'celsius'], 
        help='The unit of the temperature argument')
    
    # Parse the arguments
    args = parser.parse_args()

    # Set conditional logic where the output is determined by 
    # the unit of the input temperature
    if args.from_unit == 'f' or args.from_unit == 'fahrenheit':
        # fahrenheit_to_celsius() is called to convert the temperature
        # from Fahtrenheit to Celsius
        print(f'The temperature is'
        + f' {fahrenheit_to_celsius(args.temperature)} Celsius')
    else:
        # 'c' and 'celsius' as available input units that don't meet 
        # the previous if condition
        # celsius_to_fahrenheit() is called to convert the temperature
        # from Celsius to Fahtrenheit
        print(f'The temperature is' 
        + f' {celsius_to_fahrenheit(args.temperature)} Fahrenheit')
