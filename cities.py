from haversine import haversine, Unit

adjacency_list = {
    "Araucária": {"Curitiba": 37, "Contenda": 18},
    "Balsa Nova": {"Curitiba": 51, "Campo Largo": 22, "Contenda": 19},
    "Campo Largo": {"Palmeira": 55, "Curitiba": 29, "Balsa Nova": 22},
    "Canoinhas": {"Porto União": 78, "Três Barras": 12, "Mafra": 66},
    "Contenda": {"Balsa Nova": 19, "Lapa": 26, "Araucária": 18},
    "Curitiba": {"São José dos Pinhais": 15, "Araucária": 37, "Balsa Nova": 51, "Campo Largo": 29},
    "Irati": {"Palmeira": 75, "Paulo Frontin": 75, "São Mateus": 57},
    "Mafra": {"Lapa": 57, "Tijucas do Sul": 99, "Canoinhas": 66},
    "Lapa": {"São Mateus": 60, "Contenda": 26, "Mafra": 57},
    "Palmeira": {"Irati": 75, "Campo Largo": 55, "São Mateus": 77},
    "Paulo Frontin": {"Irati": 75, "Porto União": 46},
    "Porto União": {"Paulo Frontin": 46, "Canoinhas": 78, "São Mateus": 87},
    "São José dos Pinhais": {"Tijucas do Sul": 49, "Curitiba": 15},
    "São Mateus": {"Irati": 57, "Palmeira": 77, "Porto União": 87, "Três Barras": 43, "Lapa": 60},
    "Tijucas do Sul": {"Mafra": 99, "São José dos Pinhais": 49},
    "Três Barras": {"Canoinhas": 12, "São Mateus": 43},
}

straight_line_distance = {"Curitiba" : {
    "Araucária": 23,
    "Balsa Nova": 41,
    "Campo Largo": 27,
    "Canoinhas": 141,
    "Contenda": 39,
    "Curitiba": 0,
    "Irati": 139,
    "Lapa": 74,
    "Mafra": 94,
    "Palmeira": 59,
    "Paulo Frontin": 172,
    "Porto União": 203,
    "São José dos Pinhais": 13,
    "São Mateus": 123,
    "Tijucas do Sul": 56,
    "Três Barras": 131,
}}

graph_positions = {
    "Irati": (-2, 8), # -25.495597, -50.647429
    "Palmeira": (1, 8), # -25.434515, -49.996895
    "Paulo Frontin": (-3.5, 6), # -26.038595, -50.829811
    "Porto União": (-4, 4), # -26.2563182,-51.0703989
    "Canoinhas": (-3, 0.5), # -26.178960, -50.395358
    "Três Barras": (-1.4, 2.5), # -26.120313, -50.307488
    "São Mateus": (-0.8, 4.5), # -25.868069, -50.387397
    "Lapa": (1.3, 3), # -25.764821, -49.737214
    "Mafra": (1.1, 1), # -26.123575, -49.793325
    "Tijucas do Sul": (2.5, 0), # -25.924059, -49.178500
    "São José dos Pinhais": (4.5, 1), # -25.533234, -49.194583
    "Curitiba": (5, 4), # -25.417841, -49.268557
    "Campo Largo": (4, 8), # -25.443639, -49.505429
    "Balsa Nova": (3, 6.5), # -25.572357, -49.631682
    "Contenda": (1.5, 5), # -25.684722, -49.535008
    "Araucária": (3.2, 3.5), # -25.570677, -49.387030
    }

lat_long = {    
    "Araucária": (-25.590073461729695, -49.39968702096306),
    "Balsa Nova": (-25.58317719189806, -49.63247764945997),
    "Campo Largo": (-25.458339447746724, -49.53354919354369),
    "Canoinhas": (-26.174681226717173, -50.39492268485765),
    "Contenda": (-25.67880611724633, -49.53682854048068),
    "Curitiba": (-25.42690433846765, -49.265228936617405),
    "Irati": (-25.47756705270271, -50.6488859230641),
    "Lapa": (-25.769806998108056, -49.71596485109956),
    "Mafra": (-26.11573520662963, -49.81017162011909),
    "Palmeira": (-25.417968028975743, -49.99879326816664),
    "Paulo Frontin": (-26.041503589847807, -50.831534016295926),
    "Porto União": (-26.23487829688134, -51.083764170342626),
    "São José dos Pinhais": (-25.534481583397998, -49.20389204524083),
    "São Mateus": (-25.868221612820456, -50.38445839730463),
    "Tijucas do Sul": (-25.9251917660384, -49.17863328660894),
    "Três Barras": (-26.12077936766008, -50.30743885554545),
}

haversine_curitiba = {
    city: round(haversine(lat_long["Curitiba"], details, unit=Unit.KILOMETERS), 0)
    for city, details in lat_long.items()
}

haversine_distance_matrix = {destination: {
                            city: haversine(lat_long[destination], details, unit=Unit.KILOMETERS) 
                                for city, details in lat_long.items()} 
                          for destination in lat_long.keys()}

fully_connected_graph = {
    destination: {
        city: round(haversine(lat_long[destination], details, unit=Unit.KILOMETERS), 0) 
            for city, details in lat_long.items() if city != destination}
    for destination in lat_long.keys()
}
    
attractions = {
    "Araucária": {'Activity': 'Off-road Biking Trails', 'Description': 'Experience off-road biking through nature.', 'Icon': '🚲', 'Price': 37.5, 'Marker': 'bicycle'},
    "Balsa Nova": {'Activity': 'Luxury Spa Retreat', 'Description': 'Relax at a luxury countryside spa and retreat.', 'Icon': '♨️', 'Price': 169, 'Marker': 'hot_springs'},
    "Campo Largo": {'Activity': 'Craft Beer Tasting', 'Description': 'Visit craft breweries and enjoy beer tasting sessions.', 'Icon': '🍺', 'Price': 56.90, 'Marker': 'beer_mug'},
    "Canoinhas": {'Activity': 'Jungle Adventure', 'Description': 'Explore a jungle trek and wildlife tours.', 'Icon': '🐒', 'Price': 77.90, 'Marker': 'monkey'},
    "Contenda": {'Activity': 'Cheese-Making Classes', 'Description': 'Try a local cheese-making class with small farmers.', 'Icon': '🧀', 'Price': 59.99, 'Marker': 'cheese_wedge'},
    "Curitiba": {'Activity': 'Samba Soirée', 'Description': 'A mountaintop dance party celebrating samba under the stars.', 'Icon': '👯‍♀️', 'Price': 41.99, 'Marker': 'people_with_bunny_ears'},
    "Irati": {'Activity': 'Mountain Biking', 'Description': '', 'Icon': '⛰️', 'Price': 29.99, 'Marker': 'mountain'},
    "Lapa": {'Activity': 'Bossa Nova Bubble Bar', 'Description': 'A floating cocktail lounge with live Bossa Nova performances.', 'Icon': '🍸', 'Price': 64.99, 'Marker': 'cocktail_glass'},
    "Mafra": {'Activity': 'Museums & Historical Sites', 'Description': 'Visit local museums showcasing regional history and heritage.', 'Icon': '🏛️', 'Price': 42.50, 'Marker': 'classical_building'},
    "Palmeira": {'Activity': 'Coffee Farm Tours', 'Description': 'Tour local coffee farms and learn about coffee production.', 'Icon': '☕', 'Price': 21.99, 'Marker': 'hot_beverage'},
    "Paulo Frontin": {'Activity': 'Hot Air Balloon Ride', 'Description': 'Enjoy a hot air balloon ride over scenic valleys.', 'Icon': '☁️', 'Price': 119.0, 'Marker': 'cloud'},
    "Porto União": {'Activity': 'Voices of the Amazon', 'Description': 'A storytelling center featuring myths passed down by Indigenous communities.', 'Icon': '🗿', 'Price': 39.99, 'Marker': 'moai'},
    "São José dos Pinhais": {'Activity': 'Comedy Show', 'Description': 'Enjoy a lively night-time comedy show with local talent.', 'Icon': '😆', 'Price': 69.99, 'Marker': 'grinning_squinting_face'},
    "São Mateus": {'Activity': 'Kayaking', 'Description': 'Enjoy a scenic kayaking trip on the Rio Iguaçu', 'Icon': '🛶', 'Price': 89.99, 'Marker': 'canoe'},
    "Tijucas do Sul": {'Activity': 'Shopping Spree', 'Description': 'Explore local artisan markets and seasonal fairs.', 'Icon': '🛍️', 'Price': 16.99, 'Marker': 'shopping_bags'},
    "Três Barras": {'Activity': 'River Rafting', 'Description': 'Try white-water rafting in the nearby rivers.', 'Icon': '🏞️', 'Price': 79.99, 'Marker': 'national_park'},
}