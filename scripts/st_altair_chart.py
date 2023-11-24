import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# more charts from altair: altair.streamlit.app

st.set_page_config(layout='wide')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(x='a', y='b', size='c', color='c', tooltip=['a','b','c'])
)

st.altair_chart(c, use_container_width=True)

# With theme
from vega_datasets import data

source = data.cars()

chart = alt.Chart(source).mark_circle().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
).interactive()

tab1, tab2, tab3 = st.tabs(['Streamlit theme (default)', 'Altair native theme', 'Custome theme'])

with tab1:
    # Use the streamlit theme
    st.altair_chart(chart, theme='streamlit', use_container_width=True)
    
with tab2:
    # Use the native altair chart theme
    st.altair_chart(chart, theme=None, use_container_width=True)

with tab3:
    source = data.seattle_weather()
    scale = alt.Scale(
        domain=['sun', 'fog', 'drizzle', 'rain', 'snow'],
        range=['#e7ba52', '#a7a7a7', '#aec7e8', '#1f77b4', '#9467bd']
    )
    
    color = alt.Color('weather:N', scale=scale)
    
    # 2 selections:
    # brush that active on top of the panel
    # a multi-click that is active on the bottom panel
    brush = alt.selection_interval(encodings=['x'])
    click = alt.selection_multi(encodings=['color'])
    
    points = (
        alt.Chart()
        .mark_point()
        .encode(
            alt.X('monthdate(date):T', title="Date"),
            alt.Y(
                'temp_max:Q',
                title='Maximum Daily Temperature (C)',
                scale=alt.Scale(domain=[-5, 40])
            ),
            color=alt.condition(brush, color, alt.value('lightgray')),
            size=alt.Size('precipitation:Q', scale=alt.Scale(range=[5, 200]))
        )
        .properties(width=550, height=300)
        .add_selection(brush)
        .transform_filter(click)
    )
    
    bars = (
        alt.Chart()
        .mark_bar()
        .encode(
            x='count()',
            y='weather:N',
            color=alt.condition(click, color, alt.value('lightgray'))
        )
        .transform_filter(brush)
        .properties(
            width=550
        )
        .add_selection(click)
    )
    
    chart = alt.vconcat(points, bars, data=source, title='Seattle Weather: 2012-2015')
    
    st.altair_chart(chart, theme='streamlit', use_container_width=True)