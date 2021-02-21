This small repo is made for demand data generation and transformation, currently exclusively for the input format used in the Amodsim project. 
You can generate random demand, or transform a public taxi trips dataset.

# Instructions:
As a prerequisite for the random demand generation, you need a map in the `geojson` format. You can obtain such a map using the [Roadmaptools](https://github.com/aicenter/roadmap-processing) library.

## Random Demand
1. Open the script `generate_random_demand.py` and configure the settings on the top
	- `map_path`: path to the geojson file
	- `demand_file_path` path to the output file
	- `start_time` and `end_time` in minutes
	- the `size` of the demand
2. Run the script.

## Transforming an Existing Dataset
1. Find data you want prior to 2016. You can use for example this dataset [this New York dataset from 2014](https://data.cityofnewyork.us/Transportation/2014-Yellow-Taxi-Trip-Data/gn7m-em8n) which contains data of trips in New York in 2014. You can also search your fo your own dataset, just be aware of required data format. Searching for combination of "New York taxi csv data 20xx" should give you a relevant output. 
2. Unzip the downloaded file.
3. Edit config.py.
	- Change `data_dir` to the path where the downloaded data are stored
	- Change `city_envelopes` to values you used to generate the map. This ensures that created demand fits into the map.
	- Don't change `data_to_extract` unless you know why you want to change it. It corresponds to Amodsim data format.
4. run the script: `python3 trips_process.py`
   
Following these steps, a trips.txt file with the demand in Amodsim format should appear in the `data_dir` directory.
