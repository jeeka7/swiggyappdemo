import streamlit as st
purchase__quantity = 0
if purchase__quantity == 0:
pizza = 500
def purchase ():
   global pizza
   global purchase__quantity
   purchase__quantity += 1
   pizza += 100
if st.button("Buy 1 more pizza"):
    purchase()
st.write(pizza)
