import csv
import os
from tqdm import tqdm

input_file_path = r"O:\AIC data\data\trips\Manhattan-IDB-2013/trip_data_5.csv"
output_file_path = r"O:\AIC data\data\trips\Manhattan-IDB-2013/2013-05-10.csv"

target_day = 10

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    reader = csv.reader(input_file)
    print("Loading csv file from: {}".format(os.path.realpath(input_file_path)))

    # header
    header = next(reader)
    output_file.write(",".join([name.strip() for name in header]) + "\n")

    for row in tqdm(reader):
        start = row[5]
        start_day = int(start.split(" ")[0].split("-")[2])
        if start_day == target_day:
            output_file.write(",".join(row) + "\n")
        elif start_day > target_day:
            break
