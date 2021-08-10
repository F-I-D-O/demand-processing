import pandas as pd
import numpy as np
import config


def data_valid(row):
    return(float(row[1]) > config.city_envelopes[0] and float(row[2]) > config.city_envelopes[1]
           and float(row[3]) < config.city_envelopes[2] and float(row[4]) < config.city_envelopes[3])


def convert_time(time):
    time = time.split(' ')
    time = time[1]
    hrs,mins,secs = time.split(':')
    time = int(hrs)*3600 + int(mins)*60 + int(secs)
    time = int(time) * 1000
    return str(time)


def write_data(row):
    fw.write(row[0])
    for i in range(1,6):
        fw.write(' ' + str(row[i]))
    fw.write("\n")


def initialize():
    df = pd.read_csv(config.data_dir,nrows=1)
    first_day = str(df['tpep_pickup_datetime'])[10:15]
    return first_day


if __name__ == "__main__":
    first_day = initialize()
    df = pd.read_csv(config.data_dir,nrows=config.MAX_NO_TRIPS)
    df = df[config.data_to_extract]
    df = df[df['tpep_pickup_datetime'].str[5:10]==first_day]
    df_numpy = df.to_numpy()
    data_list = np.array([[]])
    with open(config.output_dir, 'w', encoding='utf-8') as fw:
        for row in df_numpy:
            if data_valid(row):
                row[0] = convert_time(row[0])
                write_data(row)
