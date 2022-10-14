import streamlit as st
if "pizza" not in st.session_state:
	st.session_state.pizza = 0
if "quantity" not in st.session_state:
 	 st.session_state.quantity = 0
def purchase ():
   global pizza
   global quantity
   quantity += 1
   pizza += 100
if st.button("Buy 1 more pizza"):
    purchase()
st.write(pizza)
