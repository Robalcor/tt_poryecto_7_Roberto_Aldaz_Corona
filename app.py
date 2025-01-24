import pandas as pd
import plotly.express as px
import streamlit as st

poke_data = pd.read_csv('Pokemon.csv') #leo el database
hist_botton =st.button('Construir Histograma') #creo el boto para el histograma

if hist_botton: # al haer clic al boton
    #escribir un mensaje
    st.write('Crea un histograma para el tipo primario de los Pokemon')
    
    #crear u nhistograma
    fig_1 = px.histogram(poke_data, x='Type1')

    #mostra el grafico plotly interactibo
    st.plotly_chart(fig_1, use_container_width=True)
