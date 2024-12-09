#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:13:06 2024

@author: marks_old
"""
# Example Problem 9: Calculate average temperature and count below-average days

def calculate_average(temperatures):
    """
    Function to calculate the average of a list of temperatures.
    """
    total = sum(temperatures)
    return total / len(temperatures)

def count_below_average(temperatures, average):
    """
    Function to count how many days have below-average temperatures.
    """
    below_count = 0
    for temp in temperatures:
        if temp < average:
            below_count += 1
    return below_count

# Main program
daily_temperatures = []

print("Enter the daily temperatures for the month (-1 to end):")
while True:
    temperature = float(input("Temperature: "))
    if temperature == -1:
        break
    daily_temperatures.append(temperature)

if len(daily_temperatures) == 0:
    print("No temperatures entered. Exiting program.")
else:
    average_temperature = calculate_average(daily_temperatures)
    below_average_days = count_below_average(daily_temperatures, average_temperature)

    print("Average Temperature:", average_temperature)
    print("Number of days with below-average temperatures:", below_average_days)
