from heapq import heappush, heappop
import networkx as nx
import matplotlib.pyplot as plt
import requests
from io import BytesIO
from PIL import Image
from itertools import permutations

def path_to_graph(adjacency_list, path, pos, heuristic=None):
    G = nx.Graph()

    for node in adjacency_list:
        G.add_node(node)

    for node in adjacency_list:
        for neighbor in adjacency_list[node]:
            G.add_edge(node, neighbor, weight=adjacency_list[node][neighbor])

    nx.draw(G, pos)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    node_labels = {node: f"{node}\n{heuristic[node]}" if heuristic else f"{node}" for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    path_edges = list(zip(path, path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

def a_star_search(graph, start, goal, heuristics):
    queue = []
    # print(f"Searching path from {start} to {goal} using heuristic {heuristics}")
    heappush(queue, (heuristics[start], start, [start], 0))  # Initialize g_cost to 0
    visited = set()

    while queue:
        # print(queue)
        (f_cost, current, path, g_cost) = heappop(queue)
        if current in visited:
            continue
        if current == goal:
            return path, g_cost  # Return actual accumulated cost
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                tentative_g_cost = g_cost + graph[current][neighbor]
                f_cost = tentative_g_cost + heuristics[neighbor]
                # print('Pushing to queue:', f_cost, neighbor, path + [neighbor], tentative_g_cost)
                heappush(queue, (f_cost, neighbor, path + [neighbor], tentative_g_cost))
    return None, float('inf')

def greedy_search(graph, start, goal, heuristics):
    queue = []
    # print(f"Searching path from {start} to {goal} using heuristic {heuristics}")
    heappush(queue, (heuristics[start], start, [start], 0))  # Initialize with zero cost
    visited = set()

    while queue:
        # print(queue)
        (heuristic, current, path, cost) = heappop(queue)
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            return path, cost  # Return the actual cost without heuristic
        for neighbor in graph[current]:
            if neighbor not in visited:
                total_cost = cost + graph[current][neighbor]  # Accumulate the actual cost
                # print('Pushing to queue:', (heuristics[neighbor], neighbor, path + [neighbor], total_cost))
                heappush(queue, (heuristics[neighbor], neighbor, path + [neighbor], total_cost))
    return None, float('inf')

def show_map(map_url):
    response = requests.get(map_url)
    fig = plt.figure(figsize=(10, 8))
    img = Image.open(BytesIO(response.content))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def path_to_map(GMAPS_API_KEY, path, lat_long, attractions, must_visit=[]):
    map_url = f"""https://maps.googleapis.com/maps/api/staticmap?center=-25.77258916306187,-50.18262294971848&scale=2&zoom=8&size=600x400&maptype=roadmap&key={GMAPS_API_KEY}&path=color:0xff0000|weight:5|"""
    for i, node in enumerate(path):
        lat, long = lat_long[node]
        map_url += f"{lat},{long}|" if i < len(path) - 1 else f"{lat},{long}"
    for i, node in enumerate(path):
        lat, long = lat_long[node]
        if i == 0:
            map_url += f"&markers=color:red|label:A|{lat},{long}"
        elif i == len(path) - 1:
            map_url += f"&markers=color:green|label:D|{lat},{long}"
        else:
            if node in must_visit:
                map_url += f"&markers=anchor:center|icon:https://emojiapi.dev/api/v1/{attractions[node]['Marker']}/64.png|label:{node[0]}|{lat},{long}"
    return map_url

def optimal_path(graph, start, must_visit, end, search, heuristics):
    min_cost = float('inf')
    best_path = None
    if start in must_visit:
        must_visit.remove(start)
    if end in must_visit:
        must_visit.remove(end)
        
    for perm in permutations(must_visit):
        nodes = [start] + list(perm) + [end]
        # print(nodes)
        total_path = []
        total_cost = 0
        valid_path = True

        for i in range(len(nodes) - 1):
            path, cost = search(graph, nodes[i], nodes[i+1], heuristics[nodes[i+1]])
            if path is None:
                valid_path = False
                break
            if total_path and path:
                total_path.extend(path[1:])
            else:
                total_path.extend(path)
            total_cost += cost

        # print(total_cost)

        if valid_path and total_cost < min_cost:
            min_cost = total_cost
            best_path = total_path
    # print(f"Optimal path: {best_path}, Cost: {min_cost}")
    return best_path, min_cost