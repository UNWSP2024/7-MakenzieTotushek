# Author: Makenzie Totushek
# Date: March 5, 2026
# Title: Rainfall

# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

rainfall = []
index = 0
for r in range (1,13):
    rain = float(input('Enter the amount of rainfall for month ' + str(r) + ': '))
    rainfall.append(rain)
min_value = min(rainfall)
min_index = rainfall.index(min_value)

total_rainfall = sum(rainfall)
average = total_rainfall / len(rainfall)

print(f'The total amount of rainfall is {total_rainfall:.2f}')
print(f'The average rainfall for each month is {average:.2f}')
print(f'The month with the lowest amount of rainfall is {min_index} with {min_value}')