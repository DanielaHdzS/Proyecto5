import streamlit as st
import pandas as pd
import plotly_express as px
from PIL import Image

car_data = pd.read_csv(
    'vehicles_us.csv')  # leer los datos

st.set_page_config(page_title='Proyecto 5 - Vehiculos',
                   page_icon='🤓', layout='wide')
# intro
with st.container():
    st.header('Sprint 5 📚')
    st.title('Aplicacion Web - Proyecto')
    st.write('Proyecto basado en una base de datos de vehiculos 🚗')
    st.write('Elaborado por Daniela Hernandez 👩 para el bootcamp de Tripleten')
    st.write(""" Se tienen dos opciones para que gracias a la base de datos podemos obtener:
             \n     a. Podemos construir un histograma 
             \n     b. Se puede construir un grafico de dispersion\n
             Tu decides👀 """)


build_histogram = st.checkbox('Construir histograma 📊')  # crear un botón

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox(
    'Construir grafico de dispersion 📈')  # crear un botón

if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
