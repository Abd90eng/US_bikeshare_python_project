import time
import pandas as pd
import numpy as np
import csv 

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city = ['chicago','new york city','washington']
months = ['january','february','march','april','may','june','all'] 
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

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
        city = input ("Please enter city name you want to retrieve info for : "). lower()
        
        if city not in CITY_DATA:
            print (" The city you looking for is not part of the study. Please write one of the following: chicago, new york city or Washington ")
            continue    
        else:   
            break    

    # TO DO: get user input for month (all, january, february, ... , june)
    months =[ 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input ("Please enter the month you want to retrieve info for or enter all for complete data: "). lower() 
        if month not in months and month != "all" :
            print (" The month you looking for is not part of the study. Please input a month within Jan-Jun inclusive ")
            continue    
        else:    
            break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    while True:
        day = input ("Please enter the day you want to retrieve info for or enter all for complete data: "). lower() 
        if day not in days and day != "all" :
            print (" The day you looking for is not part of the study. Please check your spelling")
            continue    
        else:    
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
       # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time/End time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month, day of week, and hour from Start Time to create new columns(month, day_of_week, hour)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month 
    if month != 'all':
        # use the index of the months list to get the corresponding int, filter by month to create the new dataframe
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week 
    if day != 'all':
    # filter by day of week to create the new dataframe
        df= df[df['day_of_week'] == day.title()]
        
    return df
    #filter by hour 
    if hour != 'all':
       #filter by hour to create new df
       df = df[df['hour'] == hour]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    Common_Month = df['month'].mode()[0]-1
    print('Most common month', Common_Month)
    

    # TO DO: display the most common day of week
    Common_day = df['day_of_week'].mode()[0]
    print('Most common day of week', Common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    Common_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', Common_hour)
    
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")
    print(user_types)
    if city == 'chicago.csv' or city == 'new_york_city.csv':

    # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        most_recent_birth = df['Birth Year'].max()
        print('Most recent birth from the given fitered data is:{}\n'.format(most_recent_birth)) 
        most_common_birth = df['Birth Year'].mode()[0]
        print('Most common birth from the given fitered data is: {}\n'.format(most_common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    #ask for raw data first 3 and then next 3 raw data rows
    while True:
        view_input_three = input('\nWould you like to see first 3 rows of data? Please enter yes or no:').lower()
        if view_input_three in ('yes', 'y'):
            n = 0
            print(df.iloc[n:n+3])
        n += 3
        break
    while True:
        view_more_data = input('Would you like to see next 3 rows of data? Please enter yes or no:').lower()
        if view_more_data != ('yes', 'y'):
            m = 1
            print(df.iloc[m:m+6])
        m += 12
        break
        print(view_more_data)
    return


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