import streamlit as st
import pandas as pd
import numpy as np

st.header('st.line_chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

line_chart = st.line_chart(chart_data)

