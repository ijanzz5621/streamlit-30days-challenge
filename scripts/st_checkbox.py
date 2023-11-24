import streamlit as st

st.header('st.checkbox')

st.write('What would you like to order?')

icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Coca Cola')

if icecream:
    st.write('Great! here some more :icecream:')
    
if coffee:
    st.write('Okay, here some coffee :coffee:')
    
if cola:
    st.write('Cola is not good but just take it!')
    
    