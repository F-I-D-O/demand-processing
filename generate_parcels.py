import math
import os.path
import random

import overpy

import config as cfg


def random_geo(center, radius):
    y0 = center[0]
    x0 = center[1]
    rd = radius / 111300  # about 111300 meters in one degree

    u = random.random()
    v = random.random()

    w = rd * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)

    lat = y + y0
    lon = x + x0

    return lat, lon


def get_random_location(center, radius):
    loc = tuple()
    while len(loc) == 0 or cfg.MAP_ENVELOPE[2] < loc[0] < cfg.MAP_ENVELOPE[0] or cfg.MAP_ENVELOPE[3] < loc[1] < \
            cfg.MAP_ENVELOPE[1]:
        loc = random_geo(center, radius)

    return loc


def get_random_popularity():
    return random.uniform(0, 1)


def take_most_popular_from_each(count, types, places):
    postal = {}
    food = {}
    shop = {}

    for place, place_type in types.items():
        if place_type == "POSTAL":
            postal[place] = places.get(place)
        elif place_type == "FOOD":
            food[place] = places.get(place)
        elif place_type == "SHOP":
            shop[place] = places.get(place)
    print(len(postal), len(food), len(shop))

    sorted_dicts = [sorted(postal, key=postal.get, reverse=True), sorted(food, key=food.get, reverse=True),
                    sorted(shop, key=shop.get, reverse=True)]
    new_places = {}
    new_types = {}

    for i in range(len(sorted_dicts)):
        loop_range = count if len(sorted_dicts[i]) > count else len(sorted_dicts[i])
        for j in range(loop_range):
            new_places[sorted_dicts[i][j]] = places[sorted_dicts[i][j]]
            new_types[sorted_dicts[i][j]] = types[sorted_dicts[i][j]]

    return new_types, new_places


def main():
    random.seed(cfg.SEED)

    api = overpy.Overpass()

    result = api.query(cfg.QUERY)

    types = {}
    places = {}

    for node in result.nodes:
        place = (float(node.lat), float(node.lon))
        place_type = node.tags.get("amenity", "n/a")
        if place_type == "n/a":
            place_type = node.tags.get("shop", "n/a")

        if place_type in cfg.TYPES.get("POSTAL"):
            types[place] = "POSTAL"
        elif place_type in cfg.TYPES.get("FOOD"):
            types[place] = "FOOD"
        elif place_type in cfg.TYPES.get("SHOP"):
            types[place] = "SHOP"
        else:
            print("Place type not supported.")
            continue

        places[place] = get_random_popularity()

    types, places = take_most_popular_from_each(100, types, places)

    with open(os.path.join(cfg.OUTPUT_DIR, cfg.PARCEL_TRIPS_FILE_PATH), mode='w') as file:
        seconds_elapsed = 0
        minutes_init = cfg.STARTING_TIME[1]
        seconds_init = cfg.STARTING_TIME[2]
        for h in range(cfg.STARTING_TIME[0], 24):
            for m in range(minutes_init, 60):
                for s in range(seconds_init, 60):
                    time = ((h * 60 + m) * 60 + s) * 1000
                    for place, place_type in types.items():
                        hourly_rate = cfg.AVERAGE_PACKAGES.get(place_type)[h]
                        second_rate = hourly_rate / 3600 * places.get(place)
                        probability = (math.e ** (-second_rate) * second_rate) * cfg.GENERATION_COEF
                        if random.uniform(0, 1) < probability:
                            r_loc = get_random_location(place, cfg.RADIUS_LIMIT)
                            file.write(str(time) + " " + str(place[0]) + " " + str(place[1]) + " " + str(r_loc[0])
                                       + " " + str(r_loc[1]) + " 1\n")
                    seconds_elapsed += 1
                seconds_init = 0
            minutes_init = 0


if __name__ == '__main__':
    main()
