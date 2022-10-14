import streamlit as st
if purchase__quantity == 0:
    pizza = 500 
purchase__quantity = 0
def purchase ():
   purchase__quantity += 1
   pizza += 100
if st.button():
    purchase()
st.write('the price of the pizza is')
st.metric('cost of pizza',pizza)
