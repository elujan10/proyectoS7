#Importacion de las librerias
import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv") # leer los datos

st.header('Venta de vehiculos')
st.write('Aplicación en construcción')


hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer") # crear un histograma           
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



disp_button = st.button('Construir Grafico de Dispersion')# crear un segundo botón

if disp_button: # al hacer clic en el segundo botón
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data,x="odometer", y='price')# crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
 