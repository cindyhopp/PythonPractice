"""Unit tests for the temperature module"""

__author__ = 'James Rapaport'

import unittest

import temperature


class TemperatureTest(unittest.TestCase):
    """Test case for the temperature functions"""

    def test_celsius_to_fahrenheit(self):
        """Test converting from Celsius to Fahrenheit"""
        self.assertEqual(68, temperature.celsius_to_fahrenheit(20))

    def test_fahrenheit_to_celsius(self):
        """Test converting from Fahrenheit to Celsius"""
        self.assertEqual(20, temperature.fahrenheit_to_celsius(68))
