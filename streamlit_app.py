import streamlit as st
import pandas as pd

st.title('Medical cost')

st.write('Hello world!')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")

with st.epander ('Data'):
  st.write("X")
  X_raw = df.drop('', axis=1)

st.dataframe(X_raw)

st.write ("y")
y_raw = df.species
st.dataframe(y_raw)

with st.sidebar:
  st.header("Введите признаки: ")
  island = st.selection('Island', ('Torgersen', 'Dream', 'Biscoe'))
