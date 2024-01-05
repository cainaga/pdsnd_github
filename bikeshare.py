import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. Would you like to see data for Chicago, New York, or Washington?

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
     city = input("Would you like to see data for Chicago, New York or Washington? ")
     city = city.lower()
     if city in ("chicago", "new york", "washington"):
        break
     else:
        print("Sorry, choose a city out of the three proposed ")

    # get user input for month (all, january, february, ... , june)
    while True:
     month = input("Which month? January, February, March, April, May, June or all to skip the filtering by month. ").casefold()
     if month in ("january", "february", "march", "april", "may", "june", "all"):
        break
     else:
        print("Sorry, choose a month as it is written from the proposed list ")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
     day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all to skip the filtering by day. ")
     if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "all"):
        break
     else:
        print("Sorry, choose a day as it is written from the proposed list ")

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable. Would you like to filter the data by month, day, or not at all? (If they chose month) Which month - January, February, March, April, May, or June? (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

   # filter by month if applicable
    if month != 'all':
        
   # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

   # filter by month to create the new dataframe
        df = df[df['month'] == month]

   # filter by day of week if applicable
    if day != 'all':
        
   # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert Start Time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract and display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].value_counts().idxmax()
    print('Most common month:', common_month)

    # extract and display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    common_day = df['day_of_week'].value_counts().idxmax()
    print('Most common day of the week:', common_day)

    # extract and display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('_'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trips."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # extract and display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', common_start_station)

    # extract and display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', common_end_station)

    # extract and display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most frequent combination of start and end station:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # extract and display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # extract and display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # extract and display counts of user types considering missing vaues
    user_type = df['User Type'].value_counts(dropna=False)
    print(user_type)

    # extract and display counts of gender considering missing values
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts(dropna=False)
        print(gender_counts)
    else:
        gender_counts = None

    # convert Birth Year column to integer data type and remove missing values if the column exists in the DataFrame

    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year'].dropna().astype(int)

    # extract and display earliest, most recent, and most common year of birth or nothing if the column doesn't exist in the Dataframe
        earliest_year = birth_year.min()
        print('Earliest year of birth:',earliest_year)
        most_recent_year = birth_year.max()
        print('Most recent year of birth:',most_recent_year)
        most_common_year = birth_year.mode()[0]
        print('Most common year of birth:',most_common_year)
    else: 
        birth_year = None
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start_loc = 0
    while True:
        view_data = input("Would you like to see 5 lines (more if applicable) of individual trip data? Type Yes or No. ").lower()
        if view_data != 'yes':
            break

        if start_loc >= len(df):
            print("No more individual trip data")
            break

        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
