import random
import roadmaptools.inout

map_path = r"O:\AIC data\Shared\amod-data\Amodsim_test\Plzen\maps/nodes.geojson"
demand_file_path = r"O:\AIC data\Shared\amod-data\Amodsim_test\Plzen\trips.txt"
start_time = 420 # 7:00
end_time = 450 # 7:30
size = 100

nodes = roadmaptools.inout.load_geojson(map_path)
node_list = []
for node in nodes["features"]:
    node_list.append(node["geometry"]["coordinates"])

demand = []
for i in range(size):
    request = []
    request.append(random.randint(start_time, end_time) * 60 * 1000)
    from_node = node_list[random.randrange(len(node_list))]
    request.append(from_node[1])
    request.append(from_node[0])

    to_node = node_list[random.randrange(len(node_list))]
    request.append(to_node[1])
    request.append(to_node[0])
    demand.append(request)

roadmaptools.inout.save_csv(demand, demand_file_path, delimiter=" ")







