DATA_DIR = '/home/tomas/Downloads/'
SOURCE_FILE_PATH = 'yellow_tripdata_2015-01-06.csv'
# order matters!
DATA_TO_EXTRACT = ['tpep_pickup_datetime', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude',
                   'dropoff_longitude', 'passenger_count']
OUTPUT_DIR = ''
TRIPS_FILE_PATH = 'trips.txt'
PARCEL_TRIPS_FILE_PATH = 'parcel.txt'
MAX_NO_TRIPS = 1000000
# Manhattan
MAP_ENVELOPE = (40.70, -74.06, 40.82, -73.87)

# Parcel generation
SEED = 42
QUERY = """
        (
            node[amenity=post_office]""" + str(MAP_ENVELOPE) + """;
            node[shop!=laundry][shop!=dry_cleaning][delivery=yes]""" + str(MAP_ENVELOPE) + """;
        );
        (._;>;);
        out body;
        """
TYPES = {
    "POSTAL": ["post_office"],
    "FOOD": ["cafe", "bar", "pub", "ice_cream", "restaurant", "fast_food", "deli", "pastry", "confectionery", "bakery"],
    "SHOP": ["pharmacy", "department_store", "chemist", "supermarket", "alcohol", "convenience", "pet", "books",
             "hardware", "craft", "photo", "florist"]
}
# avg every hour
AVERAGE_PACKAGES = {
    "POSTAL": [1, 0, 0, 0, 0, 0, 1, 10, 23, 33, 40, 48, 56, 57, 56, 57, 61, 66, 62, 51, 35, 20, 9, 3],
    "FOOD": [7, 4, 2, 1, 0, 1, 1, 3, 6, 9, 12, 25, 40, 44, 36, 31, 32, 35, 42, 45, 41, 32, 22, 13],
    "SHOP": [0, 0, 0, 0, 0, 0, 0, 3, 11, 43, 56, 62, 62, 60, 57, 56, 48, 18, 8, 3, 1, 0, 0, 0]
}
RADIUS_LIMIT = 8046.72  # 5 miles in meters

# h, m, s
# 81850000
STARTING_TIME = (22, 44, 10)
GENERATION_COEF = 1.0
