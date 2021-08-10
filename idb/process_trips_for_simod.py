import csv
import os
from tqdm import tqdm
from datetime import time

input_file_path = r"O:\AIC data\data\trips\Manhattan-IDB-2013/2013-05-10-Manhattan.csv"
output_file_path = r"C:\AIC Experiment Data\VGA Manhattan/trips.txt"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    reader = csv.reader(input_file)
    print("Loading csv file from: {}".format(os.path.realpath(input_file_path)))

    # skip header
    header = next(reader)

    for row in tqdm(reader):
        start_time = time.fromisoformat(row[6].split(" ")[1])
        millis = (start_time.hour * 3600 + start_time.minute * 60 + start_time.second) * 1000

        out = "{} {} {} {} {}\n".format(millis, row[12], row[11], row[14], row[13])
        output_file.write(out)