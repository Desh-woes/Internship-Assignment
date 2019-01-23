# Import necessary libraries for analysis
import pandas as pd
import math

# Reading in four numerical inputs: lat_min, lat_max, long_min, long_max and labels("Analysis_area")
# Note the function currently uses a local directory
filename = 'AU_proj_coords.csv'
data_frame = pd.read_csv(filename, sep=',',
                         usecols=['MIN_longitude', 'MAX_longitude', 'MIN_latitude', 'MAX_latitude', 'analysis_area'])
# print(data_frame.head(4))


# Defining function for Printing out the area in km^2 of the input “rectangle”.
def print_area():
    # r = earth's radius in km
    r = 6371

    for x in range(0, len(data_frame)):

        # Area formula.
        area = (math.pi / 180) * (pow(r, 2)) * (
            abs(math.sin(math.radians(abs(data_frame['MAX_latitude'][x]))) - math.sin(math.radians(abs(data_frame['MIN_latitude'][x]))))) * (
                   abs(data_frame['MAX_longitude'][x] - data_frame['MIN_longitude'][x]))

        # Print
        print(data_frame['analysis_area'][x]+':', area, 'Km^2')


# Call print_area function
print_area()


# Defining function that returns the list of areas in the AU_project_coords.csv file (only the “analysis_area”
# names/strings) that overlap with the input area. Function takes in area number as input

def find_overlap(input_area):
    # List that would be returned
    overlap = []

    # Loop to find overlapping areas
    for x in range(0, len(data_frame)):

        # Check first instance of overlap
        if (data_frame['MIN_latitude'][input_area] <= data_frame['MAX_latitude'][x] < data_frame['MAX_latitude'][input_area]) and (data_frame['MIN_longitude'][input_area] <= data_frame['MIN_longitude'][x] < data_frame['MAX_longitude'][input_area]):
            overlap.append(data_frame['analysis_area'][x])

        # Check second instance of overlap if the first instance returns false
        elif (data_frame['MIN_latitude'][x] <= data_frame['MAX_latitude'][input_area] < data_frame['MAX_latitude'][x]) and (data_frame['MIN_longitude'][x] <= data_frame['MIN_longitude'][input_area] < data_frame['MAX_longitude'][x]):
            overlap.append(data_frame['analysis_area'][x])

    # Return the list of overlapping areas
    return overlap


# Call find_overlap function
print(find_overlap(107))





