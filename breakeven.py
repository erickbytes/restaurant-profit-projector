import pandas as pd
import streamlit as st

# https://docs.streamlit.io/library/api-reference
st.title("Restaurant Profit Analysis")
costs = st.number_input("Daily Restaurant Costs (Pesos)", key="costs", value=2700, step=50)
corn_dogs_price = st.number_input("Corn Dogs Price (Pesos)", key="corn_dogs", value=35)
onion_rings_price = st.number_input(
    "Onion Rings Price (Pesos)", key="onion_rings", value=35
)
corn_dogs_sold = st.slider("Corn Dogs Orders Sold", value=30)
onion_rings_sold = st.slider("Onion Rings Orders Sold", value=20)
profit = (
    (corn_dogs_sold * corn_dogs_price) + (onion_rings_sold * onion_rings_price) - costs
)
result = f"${profit:,}".replace("$-","-$")
st.metric("pesos profit", result)
data = {"profit": {"$ pesos": profit}}
df = pd.DataFrame.from_dict(data)
if "-" in str(profit):
    st.bar_chart(df, color="#a30311")
else:
    st.bar_chart(df, color="#0c9618")
st.subheader("How profit is calculated:")
st.text("profit = (corn dogs sold * corn dogs price) + (onion rings sold * onion rings price) -  costs")