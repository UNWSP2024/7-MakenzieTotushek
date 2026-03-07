# Author: Makenzie Totushek
# Date: March 5, 2026
# Title: 3-dimensional Coordinates

# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math


# Now write a mainline that has the user enter the two tuples.
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)

def distance(t1, t2):
    total = math.sqrt((t2[0] - t1[0])**2 + (t2[1] - t1[1])**2 + (t1[2] - t2[2])**2)
    return total

def main():
    # Get the coordinates
    # Split the coordinates and make them tuples
    try:
        first_coordinate = tuple(map(int, input('Enter the first distance coordinate in the form (x y z): ').split()))
        second_coordinate = tuple(map(int, input('Enter the second distance coordinate in the form (x y z): ').split()))
        # return the results
        result = distance(first_coordinate, second_coordinate)
        return result
    except:
        print('The coordinates entered are invalid. Make sure the coordinates entered are only numbers, and have a single space in between each number.')

if __name__ == '__main__':
    total_distance = main()
    print(f'The total distance between those two points is {total_distance:.2f} units')