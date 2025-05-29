# 🚗 vehicle-data-visualization

## 📋 Descripción del Proyecto

**DATA VIEWER** es una aplicación web interactiva diseñada para visualizar y analizar datos de vehículos en venta. Esta herramienta permite a los usuarios explorar diversas características de los vehículos disponibles, facilitando la toma de decisiones informadas.

## ⚙️ Funcionalidades

- 📊 **Histograma de Kilometraje**: Muestra la distribución del kilometraje de los vehículos.
- 📉 **Diagrama de Dispersión**: Representa la relación entre el kilometraje y el precio de los vehículos.
- 📋 **Tabla de Información de Vehículos**: Presenta una tabla con detalles de vehículos como año, precio, kilometraje y otras características relevantes. Esta tabla muestra los vehículos de fabricantes que tienen más de 1000 anuncios (ads); sin embargo, presenta una casilla de verificación, que al seleccionarla, incluye también a los vehículos que pertenecen a fabricantes con menos de 1000 anuncios (ads).
- 📊 **Diagrama de Barras**: Muestra la cantidad de vehículos por fabricante (manufacturer). Es un diagrama de barras apiladas donde cada barra tiene diferentes colores que representan la cantidad de modelos de vehículos de cada fabricante.
- 📈 **Histograma Dinámico de Año de Vehículos**: Permite visualizar la distribución de los años de los vehículos, filtrados según la condición del vehículo. En un mismo diagrama se muestran 6 histogramas de los años de vehículos por condición.
- 🔍 **Comparación de Distribución de Precios entre Fabricantes**: Muestra en un mismo diagrama dos histogramas de precios de dos diferentes fabricantes, que se pueden seleccionar mediante menús desplegables. También hay una casilla de verificación que, al seleccionarla, normaliza el histograma (es decir, transforma las frecuencias absolutas en proporciones o porcentajes).

## 🚀 Cómo Usar

1. Ingresar al siguiente enlace https://my-project-sprint6-r6o8.onrender.com
2. Utilizar los botones para generar los diferentes gráficos y tablas.
3. Filtrar la información según las necesidades del usuario.


## 📦 Requisitos

- `pandas`
- `plotly`
- `streamlit`

## 💻 Instalación

1. Clona este repositorio, clic en este enlace https://github.com/CECIJU15/my_project_sprint6.git para acceder al repositorio.
2. Instala las dependencias necesarias usando `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `streamlit run app.py`.

## 👤 Autor

**Cecilia Juliana Ruiz Carhuamaca**  
Estudiante de análisis de datos en TripleTen  