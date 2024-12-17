import cities

def initialize(state, tabs):
    # Initialize session state
    if 'active_tab' not in state:
        state.active_tab = tabs[0]
    if 'sel_num' not in state:
        state.sel_num = 1
    if 'sel_arr' not in state:
        state.sel_arr = "Curitiba"
    if 'sel_dep' not in state:
        state.sel_dep = "Curitiba"
    if 'num_people' not in state:
        state.num_people = state.sel_num
    if 'arriving_city' not in state:
        state.arriving_city = state.sel_arr
    if 'departing_city' not in state:
        state.departing_city = state.sel_dep

    for location, attraction in cities.attractions.items():
        if f'sel_{attraction['Marker']}' not in state:
            state[f'sel_{attraction['Marker']}'] = False

    if 'sel_transport' not in state:
        state.sel_transport = "🚌 Bus"
    if 'transport' not in state:
        state.transport = state.sel_transport
    if 'plan_selected' not in state:
        state.plan_selected = None
    if 'selected_attractions' not in state:
        state.selected_attractions = set()
    if 'selected_temptations' not in state:
        state.selected_temptations = set()