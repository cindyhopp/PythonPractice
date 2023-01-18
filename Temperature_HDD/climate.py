"""Climate functions

Functions based on the ECCC glossary definitions
found at:

https://climate.weather.gc.ca/glossary_e.html
"""

__author__ = 'Cindy Lu'

import argparse
import temperature


# Define function to calculate heating degree-days
def heating_degree_days(mean_temperature: float) -> float:
    """The number of degrees Celcius with daily mean temperature below 18 °C
    If the daily mean temperature is greater or equal to 18°C then return 0.
    If the daily mean temperature is less than 18°C, 
    then return number of Celsius degrees that is below 18 °C.

    Keyword arguments:
    mean_temperature -- The average temperature of the day
    """
    # Set baseline temperature in Celsius as 18
    # this value can be changed should the baseline temperature changes
    baseline_t = 18

    if mean_temperature >= baseline_t:
        return 0
    else:
        return baseline_t - mean_temperature


if __name__ == '__main__':
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description = 'Parse heating degree-days arguments')
    # An argument for the lowest temperature of the day
    parser.add_argument('min', type = float, 
        help = 'The minimum temperature of the day')
    # An argument for the highest temperature of the day
    parser.add_argument('max', type = float, 
        help = 'The maximum temperature of the day')
    # An argument for the unit of the min and max temperature arguments
    parser.add_argument('from_unit', type = str, 
        choices = ['f', 'c', 'fahrenheit', 'celsius'], 
        help = 'The unit of the temperature argument')
    
    # Parse the arguments
    args = parser.parse_args()

    # Set conditional logic where the output is determined by 
    # the unit of the input temperature
    if args.from_unit == 'c' or args.from_unit == 'celsius':
        meantemperature = (args.min + args.max)/2
        # Heating_degree_days() is called to calculate 
        # the heating degree-days in °C
        print (f'The mean temperature is {meantemperature} °C which results'
        + f' in {heating_degree_days(meantemperature)} heating degree-days')
    else:
        # Since the heating_degree_days() operates in °C, 
        # convert unit from °F to °C first 
        # by calling the functions from temperature.py
        min_c = temperature.fahrenheit_to_celsius(args.min)
        max_c = temperature.fahrenheit_to_celsius(args.max)
        # Calculate the mean temperature in both °F and °C
        # Both will be used in the final output
        meantemperature_f = (args.min + args.max)/2
        meantemperature_c = (min_c + max_c)/2
        # Call heating_degree_days() to retrieve heating degree-days in °C
        # and convert that to heating degree days in °F
        hdd_c = heating_degree_days(meantemperature_c)
        # Apply scale factor to convert the heating degree-days from °C 
        # to corresponding scale in °F
        hdd_f = hdd_c * (9 / 5)
        print (f'The mean temperature is {meantemperature_f} °F which results'
        + f' in {hdd_f} heating degree-days')

