import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config('HENRIQUE - ECOP06','https://unifei.edu.br/wp-content/themes/twentytwelve-child/img/cabecalho/logo-unifei-oficial.png')


st.title('pagina demo ecop06')

esportes = pd.read_csv('https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv')

st.dataframe(esportes)