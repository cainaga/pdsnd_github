
# 05/01/2024

# US Bikeshare Data in python

## Description
In this project, I developed a script in Python that take into consideration the data from a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. I compared the system usage between three large cities: Chicago, New York City, and Washington, DC.

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns and 2 aditional for Chicago and New York City:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)
- Gender
- Birth Year

### Descriptive Statistics Computed

1 **Popular times of travel (i.e., occurs most often in the start time)**
- most common month
- most common day of week
- most common hour of day

2 **Popular stations and trip**
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

3 **Trip duration**
- total travel time
- average travel time

4 **User info**
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## Files used
- bikeshare.py 
- chicago.csv
- new_york_city.csv
- washington.csv

## Credits
Project completed with the support of the materials in the Udaicty course: "Programming for Data Science with Python and Udacity GPT for code optimization, detecting typos and debugging asistance.

