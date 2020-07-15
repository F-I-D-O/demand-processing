data_dir = '/home/tomas/Downloads/yellow_tripdata_2015-01-06.csv'
#order matters!
data_to_extract = ['tpep_pickup_datetime','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude','passenger_count']
output_dir = 'trips.txt'
MAX_NO_TRIPS = 1000000
#Manhattan
city_envelopes=[40.73,-74.04,40.82,-73.89]
