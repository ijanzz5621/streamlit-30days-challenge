import streamlit as st

# can create .streamlit folder on the root project folder and create the config.toml

# documentation: https://docs.streamlit.io/library/advanced-features/theming

st.title('Customizing the theme of the Streamlit App')
st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""

    [theme]
    primaryColor="#F39C12"
    backgroundColor="#2E86C1"
    secondaryBackgroundColor="#AED6F1"
    textColor="#FFFFFF"        
    font="monospace"
        
""", line_numbers=True)

number = st.sidebar.slider('Select a number', 0, 10, 5)
st.write('Selected number from slider widget is: ', number)