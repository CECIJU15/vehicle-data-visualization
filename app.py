import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.title("DATA VIEWER")

st.subheader("Vehicle list")

car_data['model_year'] = car_data['model_year'].apply(lambda x: int(x) if pd.notna(x) else pd.NA)

# Convertir a tipo Int64 de pandas
car_data['model_year'] = car_data['model_year'].astype('Int64')

car_data['manufacturer'] = car_data['model'].str.split(' ').str[0]  # Extrae el fabricante del modelo

# Contar anuncios por fabricante
manufacturer_counts = car_data['manufacturer'].value_counts()

# Filtrar los fabricantes con mas de 1000 anuncios
more_than_1000_ads = manufacturer_counts[manufacturer_counts > 1000]

# Extraer la lista de fabricantes
manufacturers_list = more_than_1000_ads.index.tolist()

filtered_by_manufacturer = car_data[car_data['manufacturer'].isin(manufacturers_list)]

filtered_by_manufacturer.reset_index(drop=True, inplace=True)

show_full_data = st.checkbox("Include manufacturers with less than 1000 ads")

if show_full_data:
    st.write(car_data)  # Mostrar el DataFrame completo
else:
    st.write(filtered_by_manufacturer)  # Mostrar el DataFrame filtrado

st.subheader("Vehicle type by manufacturer")

type_counts = car_data.groupby(['manufacturer', 'type'])['type'].size().reset_index(name='count')

fig = px.bar(
    type_counts,
    x='manufacturer',
    y='count',
    color='type',
    labels={'count': 'Count', 'manufacturer': 'Manufacturer'},
    text='count',
    color_discrete_sequence=px.colors.qualitative.Vivid
)

# Ajustar la presentación
fig.update_traces(texttemplate='%{text}', textposition='inside')
fig.update_layout(barmode='stack')

# Mostrar el gráfico
st.plotly_chart(fig)

st.subheader("Histogram of condition vs model_year")

fig1 = px.histogram(
    car_data,
    x='model_year',
    color='condition',
    barmode='overlay',
    labels={'model_year': 'Model year'}
    
)

st.plotly_chart(fig1) 

st.subheader("Compare price distribution between manufacturers")

# Obtener los valores únicos de la columna 'manufacturer'
opciones = car_data['manufacturer'].unique()
opciones = sorted(opciones)

# Crear un menú desplegable con una clave única
seleccion1 = st.selectbox("Select manufacturer 1:", opciones, key="fabricante1")


# Crear un menú desplegable con otra clave única
seleccion2 = st.selectbox("Select manufacturer 2:", opciones, key="fabricante2")

# Filtrar los datos según los fabricantes seleccionados
filtered_data = car_data[car_data['manufacturer'].isin([seleccion1, seleccion2])]

# Crear el histograma
price_distribution_fig = px.histogram(
    filtered_data,
    x='price',
    color='manufacturer',
    labels={'price': 'Price', 'manufacturer': 'Manufacturer'},
    barmode='overlay',
    nbins=30,  # Puedes ajustar el número de bins según sea necesario
    color_discrete_sequence=['#800080', '#ff7f0e']
)

# Ajustar la presentación
price_distribution_fig.update_traces(opacity=0.85)  # Ajustar la opacidad para ver las superposiciones

# Mostrar el gráfico
# st.plotly_chart(price_distribution_fig)

price_distribution_fig_norm = px.histogram(
    filtered_data,
    x='price',
    color='manufacturer',
    labels={'price': 'Price', 'manufacturer': 'Manufacturer'},
    barmode='overlay',
    histnorm='percent',  # Normalizar para mostrar porcentajes
    nbins=30,
    color_discrete_sequence=['#800080', '#ff7f0e']
)

# Ajustar la presentación
price_distribution_fig_norm.update_traces(opacity=0.85)

# Mostrar el gráfico
# st.plotly_chart(price_distribution_fig_norm)

show_full_data_1 = st.checkbox("Normalize histogram")

if show_full_data_1:
    st.plotly_chart(price_distribution_fig_norm)
else:
    st.plotly_chart(price_distribution_fig)