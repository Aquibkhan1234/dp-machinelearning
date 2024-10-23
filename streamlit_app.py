import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
st.title('🎈Machine learning App ')

st.info("This is app builds a machine learning model!")

with st.expander('Data'):
 st.write("**Raw data**")
 df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
 df  

st.write("**X**")
X_raw = df.drop("species", axis=1)
X_raw

st.write("**y**")
y_raw = df.species
y_raw

