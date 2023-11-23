import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# page config
st.set_page_config(layout='wide', )

# functions

@st.cache_data
def load_data():
    #load data
    df_agg = pd.read_csv('files/Aggregated_Metrics_By_Video.csv').iloc[1:,:]
    df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes',
        'Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration',
        'Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)']
    df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time'], format='%b %d, %Y')
    df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x,'%H:%M:%S'))
    df_agg['Avg_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.second + x.minute*60 + x.hour*3600)
    df_agg['Engagement_ratio'] =  (df_agg['Comments added'] + df_agg['Shares'] +df_agg['Dislikes'] + df_agg['Likes']) /df_agg.Views
    df_agg['Views / sub gained'] = df_agg['Views'] / df_agg['Subscribers gained']
    df_agg.sort_values('Video publish time', ascending = False, inplace = True) 

    df_agg_sub = pd.read_csv('files/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('files/All_Comments_Final.csv')
    df_time = pd.read_csv('files/Video_Performance_Over_Time.csv')
    df_time['Date'] = pd.to_datetime(df_time['Date'], format='%d %b %Y')

    return df_agg, df_agg_sub, df_comments, df_time

# call load data function
df_agg, df_agg_sub, df_comments, df_time = load_data()

placeholder = st.empty()

#with placeholder:    

#sidebar
add_sidebar = st.sidebar.selectbox('Aggregate or Individual Video', ('-- Select One --', 'Aggregate Metrics','Individual Video Analysis'))

if add_sidebar == '-- Select One --':
    # test show data
    st.dataframe(df_agg, use_container_width=True, hide_index=True)
    st.dataframe(df_agg_sub, use_container_width=True, hide_index=True)
    st.dataframe(df_comments, use_container_width=True, hide_index=True)
    st.dataframe(df_time, use_container_width=True, hide_index=True)

elif add_sidebar == 'Aggregate Metrics':
    
    #placeholder.empty()
    st.write('Ken Jee Youtube Aggregared Data')        
    df_agg_metrics = df_agg[['Video publish time','Views','Likes','Subscribers','Shares','Comments added','RPM(USD)','Average % viewed',
                             'Avg_duration_sec', 'Engagement_ratio','Views / sub gained']]
    metric_date_6mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months =6)
    metric_date_12mo = df_agg_metrics['Video publish time'].max() - pd.DateOffset(months =12)
    metric_medians6mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_6mo].iloc[1:,:].median()
    metric_medians12mo = df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_12mo].median()
    
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    
    count = 0
    
    # drop date value
    metric_medians6mo.drop(index=metric_medians6mo.index[0], axis=0, inplace=True)
    metric_medians12mo.drop(index=metric_medians12mo.index[0], axis=0, inplace=True)
        
    #st.write(df_agg_metrics[df_agg_metrics['Video publish time'] >= metric_date_12mo].iloc[1:,:].median())    
    #st.write(df_agg_metrics['Video publish time'].max())
    
    for i in metric_medians6mo.index:
        with columns[count]:
            delta = (metric_medians6mo[i] - metric_medians12mo[i])/metric_medians12mo[i]
            #st.write(metric_medians6mo[i])
            st.metric(label = i, value = round(metric_medians6mo[i], 1), delta = '{:.25}'.format(delta))
            
            count += 1
            if count >= 5:
                count = 0
    
elif add_sidebar == 'Individual Video Analysis':
    
    #placeholder.empty()
    #with placeholder:
    videos = tuple(df_agg['Video title'])
    st.write("Individual Video Performance")
    video_select = st.selectbox('Pick a Video:', videos)




