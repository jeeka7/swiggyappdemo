import streamlit as st
purchase__quantity = 0
if purchase__quantity == 0:
    pizza = 500
def purchase ():
   purchase__quantity += 1
   pizza += 100
if st.button("Buy 1 more pizza"):
    purchase()
st.write('the price of the pizza is')
st.metric('cost of pizza',pizza)
