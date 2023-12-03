import streamlit as st
import pandas as pd

# more info: https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
# configuration: 

st.title('st.file_uploader')

st.subheader('Input csv')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive statistics')
    st.write(df.describe())
else:
    st.info('Upload a csv file')