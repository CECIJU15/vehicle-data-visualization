# my_project_sprint6
Proyecto del sprint 6
# DATA VIEWER

## Descripción del Proyecto

DATA VIEWER es una aplicación web interactiva diseñada para visualizar y analizar datos de vehículos en venta. Esta herramienta permite a los usuarios explorar diversas características de los vehículos disponibles, facilitando la toma de decisiones informadas.

## Funcionalidades

- **Histograma de Kilometraje**: Muestra la distribución del kilometraje de los vehículos.
- **Diagrama de Dispersión**: Representa la relación entre el kilometraje y el precio de los vehículos.
- **Tabla de Información de Vehículos**: Presenta una tabla con detalles de vehículos como año, precio, kilometraje y otras características relevantes, esta tabla muestra los vehículos de fabricantes que tiene más de 1000 anuncios (ads), sin embargo, presenta una casilla de verifiación, si la seleccionas, la tabla incluirá también a los vehículos que pertenecen a fabricantes que tienen menos de 1000 anunicos (ads). 
- **Diagrama de Barras**: Muestra la cantidad de vehículos por fabricante (manufacturer), es una diagrama de barras apiladas, cada barra muestra diferentes colores que representa la cantidad de los modelos de vehículos de cada fabricante.
- **Histograma Dinámico de Año de vehículos**: Permite visualizar la distribución de los años de los vehículos, estan filtrados según la condición del vehículo, es decir, se muestran el un mismo diagrama 6 histrogramas de los años de vehículos por condición de vehículo.
- **Comparación de distribución de precios entre fabricantes**: Muestra en un mismo diagrama dos histogramas de precios de dos diferentes fabricantes, se puede seleccionar los fabricantes mediantes botones de menús desplegables. Tambien hay una casilla de verificación, si se selecciona la casilla se normaliza el histograma. Cuando normalizas un histograma, en lugar de mostrar las frecuencias absolutas (es decir, el número de observaciones en cada intervalo), transformas esas frecuencias en proporciones o porcentajes. Esto se hace dividiendo la frecuencia de cada intervalo entre el total de observaciones. 

## Cómo Usar

1. Ingresar al siguiente enlace https://my-project-sprint6-r6o8.onrender.com
2. Utilizar los botones para generar los diferentes gráficos y tablas.
3. Filtrar la información según las necesidades del usuario.

## Requisitos

- `pandas`
- `plotly`
- `streamlit`

## Instalación

1. Clona este repositorio, clic en este enlace https://github.com/CECIJU15/my_project_sprint6.git para acceder al repositorio.
2. Instala las dependencias necesarias usando `pip install -r requirements.txt`.
3. Ejecuta la aplicación con `streamlit run app.py`.