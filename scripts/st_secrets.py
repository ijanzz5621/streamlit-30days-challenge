import streamlit as st

# the secret can either be stored in the streamlit cloud or .streamlit/secrets.toml
# https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management

st.title('st.secrets')

st.write(st.secrets['message'])

