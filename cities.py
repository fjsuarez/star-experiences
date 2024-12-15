from haversine import haversine, Unit

locations = {    
    "Araucária": (-25.590073461729695, -49.39968702096306),
    "Balsa Nova": (-25.58317719189806, -49.63247764945997),
    "Campo Largo":(-25.458339447746724, -49.53354919354369),
    "Canoinhas": (-26.174681226717173, -50.39492268485765),
    "Contenda": (-25.67880611724633, -49.53682854048068),
    "Curitiba":(-25.42690433846765, -49.265228936617405),
    "Irati": (-25.47756705270271, -50.6488859230641),
    "Mafra": (-26.11573520662963, -49.81017162011909),
    "Lapa": (-25.769806998108056, -49.71596485109956),
    "Palmeira":(-25.417968028975743, -49.99879326816664),
    "Paulo Frontin": (-26.041503589847807, -50.831534016295926),
    "Porto União":(-26.23487829688134, -51.083764170342626),
    "São José dos Pinhais": (-25.534481583397998, -49.20389204524083),
    "São Mateus": (-25.868221612820456, -50.38445839730463),
    "Tijucas do Sul": (-25.9251917660384, -49.17863328660894),
    "Três Barras": (-26.12077936766008, -50.30743885554545),
}

adjacency_matrix = {
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

# straight_line_distance = {
#     "Araucária": 23,
#     "Balsa Nova": 41,
#     "Campo Largo": 27,
#     "Canoinhas": 141,
#     "Contenda": 39,
#     "Curitiba": 0,
#     "Irati": 139,
#     "Mafra": 94,
#     "Lapa": 59,
#     "Palmeira": 74,
#     "Paulo Frontin": 172,
#     "Porto União": 203,
#     "São José dos Pinhais": 13,
#     "São Mateus": 123,
#     "Tijucas do Sul": 56,
#     "Três Barras": 131,
# }

straight_line_distance = {destination: {
                            city: haversine(locations[destination], details, unit=Unit.KILOMETERS) 
                                for city, details in locations.items()} 
                          for destination in locations.keys()}
    
