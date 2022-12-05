import streamlit as st
import pandas as pd
import plotly.express as px
from main import config

df = pd.read_csv(config['Dataset']['df_path'])

st.title('Плохие ли иностранцы?')
st.header('Тут мы поисследуем зависит ли количество иностранцев от кол-ва плохих штук?')


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

trendline = st.checkbox('Показать линию тренда?')

trend = {'trendline': None}

if trendline:
    trend = {'trendline': "ols"}

st.header('Зависимость преступлений от количества людей, которые плохо говорят по английски')
fig1 = px.scatter(df, y=names[option], x='PctNotSpeakEnglWell',
                  **trend, labels={names[option]: option + ' на 100 тысяч', 'PctNotSpeakEnglWell': 'Кол-во плохо знающих англ(в процентах)'})
st.plotly_chart(fig1)

st.header('Зависимость преступлений от количества людей, которые родились в другой стране')
fig2 = px.scatter(df, y=names[option], x='PctForeignBorn',
                  **trend, labels={names[option]: option + ' на 100 тысяч', 'y': 'Кол-во родившихся зарубежом(в процентах)'})
st.plotly_chart(fig2)

st.header('Зависимость преступлений от количества людей, которые иммигрировали')
names2 = {
    'раньше 5 лет назад': 'PctRecentImmig',
    '5-8 лет назад': 'PctRecImmig5',
    '8-10 лет назад': 'PctRecImmig8',
    'более 10 лет назад': 'PctRecImmig10',
}
radio = st.radio(
    'Выбери когда иммигрировали!',
    list(names2.keys()),
)

fig3 = px.scatter(df, x=names2[radio], y=names[option], **trend,
                  labels={names2[radio]: radio + ' в процентах', names[option]: option + ' на 100 тысяч'})
st.plotly_chart(fig3)


st.markdown('Если долго смотреть, то можно увидеть, что на некоторых графиках линия тренда отрицательная(Изнасилования)! Удивительно...')
