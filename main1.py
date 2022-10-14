import streamlit as st
if 'pizza' not in st.session_state:
  st.session_state.pizza = 0
if 'purchase__quantity' not in st.session_state:
    st.session_state.purchase__quantity = 0
def purchase ():
   global pizza
   global purchase__quantity
   purchase__quantity += 1
   pizza += 100
if st.button("Buy 1 more pizza"):
    purchase()
st.write(pizza)
