
import pandas as pd
import matplotlib as plt
import numpy as np
import datetime


df1 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202203-divvy-tripdata.csv')
df2 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202204-divvy-tripdata.csv')
df3 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202205-divvy-tripdata.csv')
df4 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202206-divvy-tripdata.csv')
df5 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202207-divvy-tripdata.csv')
df6 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202208-divvy-tripdata.csv')
df7 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202209-divvy-tripdata.csv')
df8 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202210-divvy-tripdata.csv')
df9 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202211-divvy-tripdata.csv')
df10 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202212-divvy-tripdata.csv')
df11 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202301-divvy-tripdata.csv')
df12 = pd.read_csv('E:\\Giri\\Case Study\\Cyclistic bike-share\\divvy-tripdata-12months\\202302-divvy-tripdata.csv')

all_trips = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])

print(all_trips.dtypes)

#Calculate ride length each trips
all_trips['started_at'] = pd.to_datetime(all_trips['started_at'])
all_trips['ended_at'] = pd.to_datetime(all_trips['ended_at'])

all_trips['ride_length'] = (all_trips['ended_at'] - all_trips['started_at']) / datetime.timedelta(minutes=1)
all_trips['ride_length'] = all_trips['ride_length'].astype('int32')

all_trips[all_trips['ride_length'] <= 0].count()
all_trips = all_trips.drop(all_trips[all_trips.ride_length <= 0].index)

#Create new column Hour, Day of week, Month
all_trips['hour'] = all_trips['started_at'].dt.hour
all_trips['day'] = all_trips['started_at'].dt.day_name()
all_trips['month'] = all_trips['started_at'].dt.month_name()

print(all_trips.head(3))

#Compare member and casual users 
total_customer = all_trips.groupby('member_casual', as_index=True)[['ride_id']].count()
print(total_customer)

mean_user = all_trips.groupby('member_casual', as_index=True)[['ride_length']].mean()
print(mean_user)

median_user = all_trips.groupby('member_casual', as_index=True)[['ride_length']].median()
print(median_user)

max_user = all_trips.groupby('member_casual', as_index=True)[['ride_length']].max()
print(max_user)

min_user = all_trips.groupby('member_casual', as_index=True)[['ride_length']].min()
print(min_user)

#Average ride time by each day for members vs casual users
avg_user_ride = all_trips.groupby(['member_casual', 'day'], as_index=True)[['ride_length']].mean()
print(avg_user_ride)

