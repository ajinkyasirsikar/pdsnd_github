import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    # Start an error-handling block
        try:
            city = input("Enter city name: ").casefold()
        except ValueError:
        # jump to the top of the loop and start-over
            continue
        if city in ('new york city', 'chicago', 'washington'):
        # If so, break the loop because we got valid input
            break
    
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
    # Start an error-handling block
        try:
            month = input("Enter a month: ").casefold()
        except:
        # jump to the top of the loop and start-over
            continue
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
        # If so, break the loop because we got valid input
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter a day of week: ").casefold()
        except:
            continue
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day'] == day.title()]
    return df
    

start_time = time.time()
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    
    # TO DO: display the most common month
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most popular month is : {}".format(popular_month))

    # TO DO: display the most common day of week
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print("The most popular day is : {}".format(popular_day))
   
# TO DO: display the most common start hour
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour is  : {}".format(popular_hour))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)

start_time = time.time()
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    

    # TO DO: display most commonly used start station
    most_common_start_station=df[['Start Station']].mode().loc[0]
    print("The most common end station is : {}".format(most_common_start_station))
    
    # TO DO: display most commonly used end station
    most_common_end_station=df[['End Station']].mode().loc[0]
    print("The most end common station is : {}".format(most_common_end_station))
    
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=df[['Start Station', 'End Station']].mode().loc[0]
    print("The most common start and end station is : {}".format(most_common_start_end_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time']=pd.to_datetime(df['End Time'])
    
    # TO DO: display total travel time
    total_travel_time=(df['End Time'] - df['Start Time']).dt.seconds / 60
    print(total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time=total_travel_time.mean()
    print("Mean Travel Time is : {}".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    
    print(user_type)
    
    # TO DO: Display counts of gender
    while True:
    # Start an error-handling block
        try:
            gender= df['Gender'].value_counts()
            first_birthday= df['Birth Year'].min()
            latest_birthday=df['Birth Year'].max()
            most_common_birthday=df['Birth Year'].mode()[0]
            print(gender)
    # TO DO: Display earliest, most recent, and most common year of birth
            print("First birth year is:{}".format(first_birthday))
            print("Latest birth year is : {}".format(latest_birthday))
            print("Most common birth year is : {}".format(most_common_birthday))
            break
        except:
            print("There is no such column")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def data(df):
    

    """Prompt user if they would like to see lines of raw data"""
    raw_data = 0
    while True:
        answer = input("\nDo you want to see 5 lines of raw data? Yes or No.\n").lower()
        if answer not in ['yes','no']:
            print("\nInvalid input. Please enter Yes or No.\n")
            continue
        if answer == 'yes':
            while True:
                raw_data += 5
                print(df.iloc[raw_data : raw_data +5])
                break

            display_more = input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
        if display_more == 'no':
            answer = "no"
            break
        if answer == "no":
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
