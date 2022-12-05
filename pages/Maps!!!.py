import streamlit as st
import pandas as pd
import plotly.express as px
from main import config

df = pd.read_csv(config['Dataset']['df_path'])

st.header('А тут будем смотреть на самые преступные в среднем штаты!')
names = {
    'Убийства': 'murdPerPop',
    'Изнасилования': 'rapesPerPop',
    'Ограбления': 'robbbPerPop',
    'Нападения': 'assaultPerPop',
    'Кражи со взломом': 'burglaries',
    'Кражи авто': 'autoTheftPerPop',
    'Поджоги': 'arsonsPerPop'
}

option = st.selectbox(
    'Какие будем исследовать преступления?(все будет на 100 тыс человек)',
    list(names.keys()), 0)
states = df.state.unique()
colors = []
for st1 in states:
    df_st = df[df.state == st1]
    peoples = int(df_st.population.sum())
    crimes = int(df_st[[names[option]]].sum())
    colors.append(100000 * crimes/peoples)
fig = px.choropleth(locations=states, locationmode="USA-states", color=colors, scope="usa")
st.plotly_chart(fig)
