import pandas as pd
import streamlit as st

# https://docs.streamlit.io/library/api-reference
st.title("Restaurant Profit Analysis")
col1, col2, col3 = st.columns(3)
with col1:
    costs = st.number_input(
        "Daily Restaurant Costs (Pesos)", key="costs", value=2700, step=50
    )
    four_corn_dogs_price = st.number_input(
        "Corn Dogs Price x 4 (Pesos)", key="four_corn_dogs", value=35
    )
    six_corn_dogs_price = st.number_input(
        "Corn Dogs Price x 6 (Pesos)", key="six_corn_dogs", value=50
    )
    come_todo_corn_dogs_price = st.number_input(
        "Corn Dogs Price x Come Todo (Pesos)", key="todo_corn_dogs", value=80
    )
    onion_rings_price = st.number_input(
        "Onion Rings Price (Pesos)", key="onion_rings", value=35
    )
with col2:
    four_corn_dogs_sold = st.slider("Corn Dogs x 4 Orders Sold", value=20)
    six_corn_dogs_sold = st.slider("Corn Dogs x 6 Orders Sold", value=15)
    come_todo_corn_dogs_sold = st.slider("Corn Dogs x Come Todo Orders Sold", value=5)
    onion_rings_sold = st.slider("Onion Rings Orders Sold", value=20)
    profit = (
        (four_corn_dogs_sold * four_corn_dogs_price)
        + (six_corn_dogs_sold * six_corn_dogs_price)
        + (come_todo_corn_dogs_sold * come_todo_corn_dogs_price)
        + (onion_rings_sold * onion_rings_price)
        - costs
    )
    result = f"${profit:,}".replace("$-", "-$")
with col3:
    st.metric("pesos profit", result)
    data = {"profit": {"$ pesos": profit}}
    df = pd.DataFrame.from_dict(data)
    if "-" in str(profit):
        st.bar_chart(df, color="#a30311")
    else:
        st.bar_chart(df, color="#0c9618")
st.subheader("How profit is calculated:")
st.text(
    "profit = (corn dogs sold x corn dogs price) + (onion rings sold x onion rings price) -  costs"
)
