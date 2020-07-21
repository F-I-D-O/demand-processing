This tool is made for creating **agentpolis** format data from public taxi trips datasets.

## instructions:
1. Find data you want prior to 2016. You can use for example this dataset:
	-  https://data.cityofnewyork.us/Transportation/2014-Yellow-Taxi-Trip-Data/gn7m-em8n which contains data of trips in New York in 2014. Such data is parsable for our script.
	- you can search your own, just be aware of required data format. Searching for combination of "New York taxi csv data 20xx" should give your relevant output. Or you can simply use data from link above.
2. unzip the downloaded file
3. edit config.py. (in **data_dir** you specify the path to your downloaded data in .csv format)   
4. run the script.
	 `python3 trips_process.py`
5. This creates trips.txt in the directory. trips.txt is demand file in agentpolis format, ready for simulation. 
