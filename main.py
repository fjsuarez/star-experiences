import streamlit as st
import pandas as pd
import cities
from init import initialize
import base64
import itertools
import utils

st.set_page_config(
    page_title="STAR Experiences",
    page_icon="🌟"
)

tabs = ["1: Travel Details", "2: Select Attractions", "3: Pick Temptations", "4: Choose Transport", "5: Choose Plan"]
transport_options = ["🚌 Bus", "🚁 Helicopter"]
attractions = {attraction['Marker']: location for location, attraction in itertools.islice(cities.attractions.items(), 8, 16)}
temptations = {temptation['Marker']: location for location, temptation in itertools.islice(cities.attractions.items(), 8)}

initialize(st.session_state, tabs)

# Title
st.title("STAR Experiences")

# Create tabs
current_tab = st.segmented_control("Select Step", tabs, key="active_tab")

# Step 1: Travel Details
if current_tab == tabs[0]:
    st.header("Travel Details")
    st.session_state.sel_num = st.selectbox("Number of People", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key="num_people")
    st.session_state.sel_arr = st.selectbox("Arriving City", cities.lat_long.keys(), key="arriving_city")
    st.session_state.sel_dep = st.selectbox("Departing City", cities.lat_long.keys(), key="departing_city")

# Step 2: Select Attractions
elif current_tab == tabs[1]:
    st.header("Select Attractions")
    for location, attraction in itertools.islice(cities.attractions.items(), 8, 16):
        st.session_state[f"sel_{attraction['Marker']}"] = st.checkbox(f"{attraction['Icon']} {attraction['Activity']}", value=st.session_state[f"sel_{attraction['Marker']}"], key=attraction['Marker'])

# Step 3: Pick Temptations
elif current_tab == tabs[2]:
    st.header("Pick Temptations")
    for location, attraction in itertools.islice(cities.attractions.items(), 8):
        st.session_state[f"sel_{attraction['Marker']}"] = st.checkbox(f"{attraction['Icon']} {attraction['Activity']}", value=st.session_state[f"sel_{attraction['Marker']}"], key=attraction['Marker'])

# Step 4: Choose Transport
elif current_tab == tabs[3]:
    st.session_state.sel_transport = st.radio("Select your method of transportation", 
                                              transport_options, 
                                              index=transport_options.index(st.session_state.sel_transport)
)

# Step 5: Choose Plan
elif current_tab == tabs[4]:
    if not st.session_state.plan_selected:
        st.header("Choose Plan")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.header("50€")
                st.subheader("Basic Plan")
                if st.button("Select Basic Plan"):
                    st.session_state.plan_selected = "basic"
                    st.rerun()
        with col2:
            with st.container(border=True):
                st.header("200€")
                st.subheader("Premium Plan")
                if st.button("Select Premium Plan"):
                    st.session_state.plan_selected = "premium"
                    st.rerun()
    else:
        with st.spinner('Wait for it...'):
            for key in st.session_state.keys():
                if key.startswith("sel_"):
                    option = key.split("_", 1)[1]
                    if st.session_state[key] and option in attractions:
                        st.session_state.selected_attractions.add(attractions[option])
            for key in st.session_state.keys():
                if key.startswith("sel_"):
                    option = key.split("_", 1)[1]
                    if st.session_state[key] and option in temptations:
                        st.session_state.selected_temptations.add(temptations[option])
            must_visit = st.session_state.selected_attractions.union(st.session_state.selected_temptations)
            search = utils.a_star_search if st.session_state.plan_selected == "premium" else utils.greedy_search
            graph = cities.adjacency_list if st.session_state.sel_transport == "🚌 Bus" else cities.fully_connected_graph
            heuristics = cities.straight_line_distance if (st.session_state.sel_transport == "🚌 Bus" and st.session_state.departing_city == "Curitiba" and not must_visit) else cities.haversine_distance_matrix
            path, cost = utils.optimal_path(graph, st.session_state.arriving_city, must_visit.copy(), st.session_state.departing_city, search, heuristics)
            map_url = utils.path_to_map(st.secrets["GMAPS_API_KEY"], path, cities.lat_long, cities.attractions, must_visit)
            itinerary = pd.DataFrame(columns=["City", "Icon", "Activity", "Description", "Price"])
            for node in path:
                if node in must_visit:
                    attraction = cities.attractions[node]
                    itinerary.loc[len(itinerary)] = {"City": node, "Icon": attraction["Icon"], "Activity": attraction["Activity"], "Description": attraction["Description"], "Price": attraction["Price"]*st.session_state.num_people}
                else:
                    itinerary.loc[len(itinerary)] = {"City": node, "Icon": "", "Activity": "", "Description": "", "Price": 0}
        st.balloons()
        st.header("Summary")
        st.write(f"Number of People: {st.session_state.num_people}")
        st.write(f"Selected Transport: {st.session_state.sel_transport}")
        st.write(f"Arriving City: {st.session_state.arriving_city}")
        st.write(f"Departing City: {st.session_state.departing_city}")
        st.subheader("Itinerary")
        st.dataframe(itinerary, use_container_width=True)
        activities_cost = itinerary["Price"].sum()
        st.write(f"Activities Cost: {activities_cost}€")
        transport_fee = 0 if st.session_state.sel_transport == "🚌 Bus" else 150
        transport_cost = transport_fee * st.session_state.num_people
        st.write(f"Transportation Cost: {transport_cost}€")
        plan_cost = 50 if st.session_state.plan_selected == "basic" else 200
        st.write(f"Plan Selected: {st.session_state.plan_selected.capitalize()} Plan: {plan_cost}€")
        st.success(f"Total Cost: {activities_cost + transport_cost + plan_cost}€")
        st.image(map_url)

with st.container():
    cols = st.columns(3)
    with cols[0]:
        if st.button("Back", disabled=current_tab == tabs[0] or not current_tab):
            prev_tab = tabs.index(current_tab) - 1
            del st.session_state.active_tab
            st.session_state.active_tab = tabs[prev_tab]
            st.rerun()
    with cols[1]:
        if st.button("Restart"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.session_state.active_tab = tabs[0]
            st.rerun()
    with cols[2]:
        if st.button("Next", disabled=current_tab == tabs[-1] or not current_tab):
            next_tab = tabs.index(current_tab) + 1
            del st.session_state.active_tab
            st.session_state.active_tab = tabs[next_tab]
            st.rerun()

st.markdown('''
<style>
    span[data-testid="stHeaderActionElements"] {
            display:none
    }
    div[data-testid="stColumn"] {
        text-align: center;
    } 
    div[data-testid="stVerticalBlock"]:last-child > div[data-testid="stHorizontalBlock"]:last-child > div[data-testid="stColumn"] {
        width: calc(33.3333% - 1rem) !important;
        flex: 1 1 calc(33.3333% - 1rem) !important;
        min-width: calc(33% - 1rem) !important;
    }

    [data-testid="stMainBlockContainer"] {
            background-color: rgba(64, 64, 64, 0.5);
            border-radius: 20px;
    }
</style>
            ''', unsafe_allow_html=True)

st.markdown(
    f"""
<style>
    .stApp {{
            background: url(data:image/jpg;base64,{base64.b64encode(open('bg.jpg', "rb").read()).decode()});
            background-size: cover
         }}
</style>
    """, unsafe_allow_html=True)