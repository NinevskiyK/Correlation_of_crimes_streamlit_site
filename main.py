import streamlit as st
import configparser

config = configparser.ConfigParser()
config.read("config.ini")


st.header('Жмякай на подсайты слева и наслаждайся красотой streamlit')