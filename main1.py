import streamlit as st
if 'pizza' not in st.session_state:
  st.session_state.pizza = 0
if 'purchase_quantity' not in st.session_state:
  st.session_state.purchase_quantity = 0
def purchase ():
   global st.session_state.pizza
   global st.session_state.purchase_quantity
   purchase_quantity += 1
   pizza += 100
if st.button("Buy 1 more pizza"):
    purchase()
st.write(pizza)
