import streamlit as st
import pandas as pd
import plotly.express as px
from main import config

df = pd.read_csv(config['Dataset']['df_path'])


st.title('Зависимости!!!')
st.header('Влияет ли количество полицейских машин на кол-во краж авто?')

col_cars = st.radio(
    "Отсортируем по кол-ву людей!",
    ('< 50 тысяч', '50..100 тысяч', '100..500 тысяч', '>= 500 тысяч'))

if col_cars == '< 50 тысяч':
    df_cars = df[df['population'] <= 50000]
elif col_cars == '50..100 тысяч':
    df_cars = df[(50000 <= df['population']) & (df['population'] <= 100000)]
elif col_cars == '100..500 тысяч':
    df_cars = df[(100000 <= df['population']) & (df['population'] <= 500000)]
else:
    df_cars = df[df['population'] >= 500000]
df_cars = df_cars[['PolicCars', 'autoTheft']].dropna()
fig = px.scatter(x=df_cars.PolicCars, y=df_cars.autoTheft, labels={'x': 'Количество полицейских машин', 'y': 'Количество краж авто'})
st.plotly_chart(fig)

st.markdown('Кажется есть прямая зависимость! Чем больше машин - тем больше краж. Видимо это связано с тем, что в плохих районах закупают больше машин?')
