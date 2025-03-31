import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv") # leer los datos

st.header('Venta de vehiculos')
st.write('Aplicación en construcción.')


hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")            
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



disp_button = st.button('Construir Grafico de Dispersion')

if disp_button:
    st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de coches')
    fig = px.scatter(car_data,x="odometer")
    st.plotly_chart(fig, use_container_width=True)
