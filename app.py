import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Grafica de Barras')

poke_data = pd.read_csv('Pokemon.csv') #leo el database
hist_botton =st.button('Construir Histograma') #creo el boto para el histograma



if hist_botton: # al haer clic al boton
    #escribir un mensaje
    st.write('Crea un histograma para el tipo primario de los Pokemon')
    
    #crear u nhistograma
    fig_1 = px.histogram(poke_data, x='Type1')

    #mostra el grafico plotly interactibo
    st.plotly_chart(fig_1, use_container_width=True)

#grafico de dispercion
st.title('Grafico de dispercion')

#lista de tipos
tlist = ['Grass', 'Fire', 'Water', 'Bug', 'Normal', 'Poison', 'Electric', 'Ground', 'Fairy', 'Fighting', 'Psychic', 'Rock', 'Ghost', 'Ice', 'Dragon', 'Dark', 'Steel', 'Flying']

#lista de estadisticas
elist = ['HP', 'Attack', 'Defense', 'Sp.Atk', 'Sp.Def', 'Speed', 'Total']

#multiselect de paramatros para la grafica de dispercion
tipos = st.multiselect('Selecciona tipo', tlist, default='Grass') 
valx = st.selectbox('seleciona una estaditica', elist, index=0)
valy = st.selectbox('Seleciona otra estadistica', elist, index=1)

if tipos:
    valor_t = poke_data[poke_data['Type1'].isin(tipos)]
else:
    valor_t = poke_data


fig_2 = px.scatter(valor_t, x=valx, y=valy)
st.plotly_chart(fig_2, use_container_width=True)