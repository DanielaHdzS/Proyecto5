import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv(
    'vehicles_us.csv')  # leer los datos

st.header('Aplicacion Proyecto Sprint 5')

build_histogram = st.checkbox('Construir histograma')  # crear un botón

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox(
    'Construir grafico de dispersion')  # crear un botón

if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
