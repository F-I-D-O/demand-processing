import osmnx as ox
import pandas as pd
import geopandas as gpd
import os

area_name = "Manhattan"

input_file_path = r"O:\AIC data\data\trips\Manhattan-IDB-2013/2013-05-10.csv"
output_file_path = r"O:\AIC data\data\trips\Manhattan-IDB-2013/2013-05-10-Manhattan.csv"

print("Loading area: {}".format(area_name))
target_area = ox.geocode_to_gdf(area_name)
target_area_shape = target_area.loc[0, 'geometry']

print("Loading data from {}".format(os.path.realpath(input_file_path)))
# df = pd.read_csv(input_file_path)
# data = gpd.GeoDataFrame(df,
#                         origin=gpd.points_from_xy(df.pickup_latitude, df.pickup_longitude),
#                         destination=gpd.points_from_xy(df.dropoff_latitude, df.dropoff_longitude))
data = gpd.read_file(input_file_path)

print("Creating geometry columns")
data['origin'] = gpd.points_from_xy(data.pickup_longitude, data.pickup_latitude)
data['destination'] = gpd.points_from_xy(data.dropoff_longitude, data.dropoff_latitude)

print("Filtering data")
filtered_data = data[data.origin.within(target_area_shape) & data.destination.within(target_area_shape)]
# filtered_data = data.loc[mask]

print("Saving filtered data to: {}".format(os.path.realpath(output_file_path)))
filtered_data.to_csv(output_file_path)