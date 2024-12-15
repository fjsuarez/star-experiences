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
    if 'sel_museum' not in state:
        state.sel_museum = False
    if 'sel_park' not in state:
        state.sel_park = False
    if 'sel_theater' not in state:
        state.sel_theater = False
    if 'sel_zoo' not in state:
        state.sel_zoo = False
    if 'sel_aquarium' not in state:
        state.sel_aquarium = False
    if 'sel_restaurant' not in state:
        state.sel_restaurant = False
    if 'sel_shopping' not in state:
        state.sel_shopping = False
    if 'sel_spa' not in state:
        state.sel_spa = False
    if 'sel_nightclub' not in state:
        state.sel_nightclub = False
    if 'sel_casino' not in state:
        state.sel_casino = False
    if 'plan_selected' not in state:
        state.plan_selected = None
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
    if 'sel_museum' not in state:
        state.sel_museum = False
    if 'sel_park' not in state:
        state.sel_park = False
    if 'sel_theater' not in state:
        state.sel_theater = False
    if 'sel_zoo' not in state:
        state.sel_zoo = False
    if 'sel_aquarium' not in state:
        state.sel_aquarium = False
    if 'sel_restaurant' not in state:
        state.sel_restaurant = False
    if 'sel_shopping' not in state:
        state.sel_shopping = False
    if 'sel_spa' not in state:
        state.sel_spa = False
    if 'sel_nightclub' not in state:
        state.sel_nightclub = False
    if 'sel_casino' not in state:
        state.sel_casino = False
    if 'plan_selected' not in state:
        state.plan_selected = None
    if 'selected_attractions' not in state:
        state.selected_attractions = set()
    if 'selected_temptations' not in state:
        state.selected_temptations = set()