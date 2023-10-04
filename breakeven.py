import pandas as pd
import streamlit as st

st.title("Restaurant Breakeven Analysis")
costs = st.number_input("Daily Restaurant Cost (Pesos)", key="costs", value=2700)
corn_dogs_price = st.number_input("Corn Dogs Price (Pesos)", key="corn_dogs", value=35)
onion_rings_price = st.number_input(
    "Onion Rings Price (Pesos)", key="onion_rings", value=35
)
corn_dogs = st.slider("Corn Dogs Orders Sold", value=30)
onion_rings = st.slider("Onion Rings Orders Sold", value=20)
st.write(f"Assumed Total Daily Restaurant Cost (Pesos): {costs}")
profit = (
    (corn_dogs * corn_dogs_price) + (onion_rings * onion_rings_price) - costs
)
st.write(f"The restauraunt's projected daily profit is ${profit:,} pesos.")
data = {"profit": {"$ pesos": profit}}
df = pd.DataFrame.from_dict(data)
st.bar_chart(df, color="#0c9618")
