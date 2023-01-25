import time
import pandas as pd
import numpy as np
# This file describes the bikeshare data from the following cities

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input("Which of the following cities would you like to filter by: Chicago, Washington, New York City").title()
    
      if city not in ('Chicago','Washington','New York City'):
        print(" Incorect, Please Try again.")
        continue
      else:
        print('You are now filter for', city)
        break
 # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("Which of the following months would you like to filter by? January, February, March, April, May, June or  'all' ?").title()
    
      if month not in ('January', 'February', 'March', 'April', 'May', 'June'):
            
        print("Please Try Again.")
        continue
      else:
        print('You are now filtering for', month)
        break   
 # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Which of the following weekdays would you like to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or 'all'").title()
    
      if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','all'):
            
        print("Please Try Again.")
        continue
        
      else:
        print('You are now filtering for', day)
        break   
        
 
    print('-'*40)
    return city, month, day


    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    
    df = pd.read_csv(CITY_DATA[city])
# This section is providing the filtered data for month and day

 # converting the Start Time to datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

 # extracting the month, day and hour of week from Start Time to have new columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour

 # filtering by month if applicable
    if month != 'all':
        
        month = months.index(month) + 1

  # filtering by month in order to create a new dataframe
        df = df[df['month'] == month]

 # filter by day of week if applicable
    if day != 'all':
 # filtering by day of week to create a new dataframe
        df = df[df['day_of_week'] == day.title()]
 
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
   

# TO DO: display the most common month

    common_month = df['month'].mode()[0]
    
    print('most common month:', common_month)
 

# TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    
    print('most common day of week:', common_day)     
  
    
# TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
          
    print('most common hour:', common_hour)
  



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().max()
    
    print('most commonly used start station:', start_station)

    # TO DO: display most commonly used end station
    
    end_station = df['End Station'].value_counts().idxmax()
    
    print('most commonly used end station:', end_station)
 

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination_station= df.groupby(['Start Station','End Station']).count()
    
    print('most frequent combination of start and end station:', start_station,"and", end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_duration_time = df['Trip Duration'].sum()
    print("total duration time:", (total_duration_time))

    # TO DO: display mean travel time
    travel_mean = df['Trip Duration'].mean()
    print("Mean travel time :",(travel_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    
    print('user types:', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print(' Gender Types',gender_types)
    except KeyError:
      print("No data is available.")

            

    # TO DO: Display earliest, most recent, and most common year of birth
    
    # Earliest Birth Year
    try:
      earliest_year = df['Birth Year'].min()
      print('Earliest Year:', earliest_year)
    except KeyError:
      print("No data is available.")
    
    # Most Recent Birth year
    try:
      recent_year = df['Birth Year'].max()
      print(' Recent Year:', recent_year)
    except KeyError:
      print("No data isavailable.")
    
    # Common birth year
    try:
      common_year = df['Birth Year'].value_counts().idxmax()
      print('Most Common Year:', common_year)
    except KeyError:
      print("No data is available.")
    

  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
def display_data(df):

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc=0
    while(view_data=='yes'):       
        print(df.iloc[start_loc:start_loc+5])
        start_loc +=5
        view_data= input("Do you wish to continue?:").lower()
           
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
