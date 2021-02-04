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
    city = input('Would you like to see data for chicago, new york city or washington?').lower()
    cities =['chicago','new york city','washington']
    while city not in cities:
        print('Invalid input- Please choose from only 3 cities asked')
        city = input('Would you like to see data for chicago, new york or washington?').lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which data between the months from january to june are you interested in?').lower()
    months =['january','february','march','april','may','june']
    
    while month not in  months:
        print('Invalid input- Please choose months between january and june only')
        month = input('Which data between the months from January to June are you interested in?').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('What day of the week are you interested in picking the data?').lower()
    days =['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    
    while day not in days:
        print('Invalid input- Select only a day from the week')
        day = input('What day of the week are you interested in picking the data?').lower()
    
    print("Selection has been made based on:\n City:{} \n Month:{} \n Day:{}".format(city.title(),month.title(),day.title()))
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
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months =['january','february','march','april','may','june']
        month = months.index(month) + 1
        df[df['month'] == month]
        
    if day != 'all':
        df[df['day_of_week'] == day.title()]
        
    
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
       
    # TO DO: display the most common month
    
    #There is no need to display the month since it has been captured above
    

    # TO DO: display the most common day of week
    
    
    #There is no need to  display the day since it has been captured above
        
    # TO DO: display the most common start hour
    df ['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    print("The most common hour of the day is {} hours".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    
    print ('Most commonly used start station is {}'.format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    
    print('Most commonly used end station is {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    freq_comb_start_end_station =(df['Start Station'] + " "+ df['End Station']).mode()[0]
    print('Most frequent combination of start station and  end station trip is {}'.format(freq_comb_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60/60/24
    
    print('The total travel time is {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = (df['Trip Duration'].mean())/60
    print('The mean travel time is {}'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print (user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns: #capturing gender for Chicago and new york
        gender = df['Gender'].value_counts()
        print(gender)
    else: # display message in the case of washington 
        print("Gender column not captured in washington city")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:#capturing birth year for Chicago and new york
        earliest_yob = df['Birth Year'].min()
        print('The earliest year of birth is {}'.format(earliest_yob))

        current_yob = df['Birth Year'].max()
        print('The most recent year of birth is {}'.format(current_yob))

        popular_yob = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}'.format(popular_yob))
    else: # display message in the case of washington 
        print("Birth Year column not captured in washington city")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    user_input = input("Would you like to view 5 rows of data?\n Please enter yes or no: ").lower()
    if user_input == "yes":
       h = 0 
       while True:
            print(df.iloc[h:h+5])
            h += 5
            more_data = input("Do you wish to continue?\n Please enter yes or no: ").lower()            
            if more_data != "yes":
                break
      
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
