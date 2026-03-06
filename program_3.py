# Program #3: US_Population
def main():
    # Have the user input (using a loop) various information that contains three pieces of data: 
    # year, name of state, and population.  
    # Store all of this information in a list of lists.  For example it might be stored like this:
    
    # [[2010, "Maine", 1987435], [2010,"Minnesota",6873202], [2011, "Iowa", 3421988]]
    all_entered_values = []
    again = 'y'
    while again == 'y':
        date = input('Enter the year: ')
        state = input('Enter the state: ')
        population = input('Enter the population: ')
        all_entered_values.append([date, state, population])
        again = input('Do you want to add another set? [y/n]: ')

    # Now have the user enter a year.
    year = input('Enter a year that you would like the total population for: ')
    
    # The program will add the populations from all states in the list of list for that year only.
    # Pass the list and year to the sum_population_for_year
    sum_population_for_year(all_entered_values, year)

def sum_population_for_year(all_entered_values, year_to_sum):
    total = 0
    # Loop through and sum the populations for the appropriate year.
    for i in range (len(all_entered_values)):
        if all_entered_values[i][0] == year_to_sum:
            all_entered_values[i][2] = int(all_entered_values[i][2])
            total += all_entered_values[i][2]
    print(f'The total population for that year is {total}')


    # e.g. for the list on line 7 the total would be 8,860,637 if the user enterd 2010 for the year to sum,
    # or 3,421,988 if they enterd 2011 for the year to sum.

    # print the totalled population


# Call the main function.
if __name__ == '__main__':
    main()