import streamlit as st
import pandas as pd
import cities
from init import initialize

st.set_page_config(
    page_title="STAR Experiences",
    page_icon="🌟"
)

# Sample data for cities and attractions
attractions = {'museum': '🖼️ Museum', 'park': '⛲ Park', 'theater': '🎭 Theater', 'zoo': '🦍 Zoo', 'aquarium': '🦈 Aquarium'}
temptations = {'restaurant': '⭐ Michelin Restaurant', 'shopping': '🛍️ Shopping', 'spa': '💆‍♀️ Spa', 'nightclub': '💃 Nightclub', 'casino': '🎰 Casino'}
tabs = ["Step 1: Travel Details", "Step 2: Select Attractions", "Step 3: Pick Temptations", "Step 4: Choose Plan"]

initialize(st.session_state, tabs)

# Title
st.title("STAR Experiences")

# Create tabs
current_tab = st.segmented_control("Select Step", tabs, key="active_tab")

# Step 1: Travel Details
if current_tab == tabs[0]:
    st.header("Travel Details")
    st.session_state.sel_num = st.selectbox("Number of People", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key="num_people")
    st.session_state.sel_arr = st.selectbox("Arriving City", cities.locations.keys(), key="arriving_city")
    st.session_state.sel_dep = st.selectbox("Departing City", cities.locations.keys(), key="departing_city")

# Step 2: Select Attractions
elif current_tab == tabs[1]:
    st.header("Select Attractions")
    st.session_state.sel_museum = st.checkbox(attractions['museum'], value=st.session_state.sel_museum, key="museum")
    st.session_state.sel_park = st.checkbox(attractions['park'], value=st.session_state.sel_park, key="park")
    st.session_state.sel_theater = st.checkbox(attractions['theater'], value=st.session_state.sel_theater, key="theater")
    st.session_state.sel_zoo = st.checkbox(attractions['zoo'], value=st.session_state.sel_zoo, key="zoo")
    st.session_state.sel_aquarium = st.checkbox(attractions['aquarium'], value=st.session_state.sel_aquarium, key="aquarium")

# Step 3: More Options
elif current_tab == tabs[2]:
    st.header("Pick Temptations")
    st.session_state.sel_restaurant = st.checkbox(temptations['restaurant'], value=st.session_state.sel_restaurant, key="restaurant")
    st.session_state.sel_shopping = st.checkbox(temptations['shopping'], value=st.session_state.sel_shopping, key="shopping")
    st.session_state.sel_spa = st.checkbox(temptations['spa'], value=st.session_state.sel_spa, key="spa")
    st.session_state.sel_nightclub = st.checkbox(temptations['nightclub'], value=st.session_state.sel_nightclub, key="nightclub")
    st.session_state.sel_casino = st.checkbox(temptations['casino'], value=st.session_state.sel_casino, key="casino")

# Step 4: Choose Plan
elif current_tab == tabs[3]:
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
        st.balloons()
        st.header(f"{st.session_state.plan_selected.capitalize()} Plan Selected")
        st.image(f"Map.png")
        st.subheader("Summary")
        st.write(f"Number of People: {st.session_state.num_people}")
        st.write(f"Arriving City: {st.session_state.arriving_city}")
        st.write(f"Departing City: {st.session_state.departing_city}")
        st.write("Selected Attractions:")
        for key in st.session_state.keys():
            if key.startswith("sel_"):
                option = key.split("_")[1]
                if st.session_state[key] and option in attractions:
                    st.session_state.selected_attractions.add(attractions[option])
        for attraction in st.session_state.selected_attractions:
            st.write(f"- {attraction}")
        st.write("Selected Temptations:")
        for key in st.session_state.keys():
            if key.startswith("sel_"):
                option = key.split("_")[1]
                if st.session_state[key] and option in temptations:
                    st.session_state.selected_temptations.add(temptations[option])
        for temptation in st.session_state.selected_temptations:
            st.write(f"- {temptation}")
        st.write(f"Plan Selected: {st.session_state.plan_selected.capitalize()} Plan")
        st.write("Total Cost: $1000")

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

st.markdown(
    """
    <style>
        span[data-testid="stHeaderActionElements"]
        {
            display:none
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        div[data-testid="stColumn"]
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)