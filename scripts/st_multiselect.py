import streamlit as st

# more info: https://docs.streamlit.io/library/api-reference/widgets/st.multiselect

st.header('st.multiselect')

options = st.multiselect(
    'What are your  favourite colors: ',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)

st.write('You selected: ', options)