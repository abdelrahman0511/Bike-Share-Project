import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington']
    x = True
    while x:
        try:
            city = input(
                'Enter the city name to be analysed from the list [chicago, new york city, washington]: ').lower()
        except:
            print('Invalid Input\nPlease try again')
        else:
            if city in city_list:
                x = False
                print('You entered {} '.format(city))
                print('_'*40)
            else:
                print('The city you entered is not in the list\nplease Try again')

    # get user input for month (all, january, february, ... , june)
    month_list = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december', 'all']
    x = True
    while x:
        try:
            month = input(
                "Enter the Month to be filltered by or enter 'all' for no filtering to be applied as in the list (all, january, february, ... , june): ").lower()
        except:
            print('Invalid Input\nPlease try again')
        else:
            if month in month_list:
                x = False
                print('You entered {} '.format(month))
                print('_'*40)
            else:
                print('The month you entered is not in the list\nPlease try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    x = True
    while x:
        try:
            day = input(
                "Enter the day to be filltered by or enter 'all' for no filtering to be applied as in the list (all, monday, tuesday, ... sunday): ").lower()
        except:
            print('Invalid Input\nPlease try again')
        else:
            if day in day_list:
                x = False
                print('You entered {} '.format(day))
            else:
                print('The day you entered is not in the list\nPlease try again')

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['Month'] == month.title()]

    if day != 'all':
        df = df[df['Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if df['Month'].size != 0:
        com_month = df['Month'].value_counts().index[0]
        print('The most common month: {}'.format(com_month))

        # display the most common day of week
        com_day = df['Day'].value_counts().index[0]
        print('The most common day of the week: {}'.format(com_day))

        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        com_hour = df['Hour'].value_counts().index[0]
        print('The most common hour: {}'.format(com_hour))
    else:
        print('No Data to Display')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    if df['Start Station'].size != 0:
        com_start_station = df['Start Station'].value_counts().index[0]
        print('The most commonly used start station: {}'.format(com_start_station))

        # display most commonly used end station
        com_end_station = df['End Station'].value_counts().index[0]
        print('The most commonly used end station: {}'.format(com_end_station))

        # display most frequent combination of start station and end station trip
        df['Combination'] = 'From ' + df['Start Station'] + ' To ' + df['End Station']
        com_combination = df['Combination'].value_counts().index[0]
        print('The most frequent combination of start and end station trip: {}'.format(com_combination))
    else:
        print('No Data to Display')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    if df['Trip Duration'].size != 0:
        # display total travel time
        total_time = df['Trip Duration'].sum()
        print('Total travel time: {}'.format(total_time))

        # display mean travel time
        mean_time = df['Trip Duration'].mean()
        print('Mean travel time: {}'.format(mean_time))
    else:
        print('No Data to Display')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    if df['User Type'].size != 0:
        # Display counts of user types
        count_user_type = df['User Type'].value_counts()
        print('Counts of user types:\n{}'.format(count_user_type))

        # Display counts of gender
        if 'Gender' in df.columns:
            count_gender = df['Gender'].fillna('Nan').value_counts()
            print('\nCounts of gender:\n{}'.format(count_gender))
        else:
            print('No gender data to display')

        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            earliest = int(sorted(df['Birth Year'].dropna(axis=0))[0])
            recent = int(sorted(df['Birth Year'].dropna(axis=0))[-1])
            com_year = int((df['Birth Year'].dropna(axis=0)).value_counts().index[0])
            print('\nThe most common year: {}'.format(com_year))
            print('The earliest year: {}'.format(earliest))
            print('The most recent year: {}'.format(recent))
        else:
            print('No birth years data to display')
    else:
        print('No Data to Display')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        if df['Start Time'].size != 0:
            # Continue Displaying 5 rows from the data as requested from the user
            x = True
            i = 0
            while x:
                try:
                    display = input(
                        '\nWould you like to see 5 rows from the data? enter [yes/no]: ').lower()
                except:
                    print('Invalied input\nPlease try again')
                else:
                    if display == 'yes':
                        print(df.iloc[range(i, i+5)])
                        i += 5
                    elif display == 'no':
                        x = False
                    else:
                        print("Please enter yes or no\nTry again")

        # Asking to restart the program
        restart = input('\nWould you like to restart? Enter [yes/no]: ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
