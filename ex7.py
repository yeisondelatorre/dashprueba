#ejemplo 7

import streamlit as st
import plotly.express as px
import seaborn as sns

# Cargar el dataset de mpg de Seaborn
df = sns.load_dataset('mpg')

# Asegurarse de que no hay valores nulos en las columnas necesarias
df = df.dropna(subset=['mpg', 'weight', 'horsepower', 'cylinders', 'model_year', 'origin'])

# Streamlit App Title
st.title("📊 Dashboard Interactivo con Múltiples Gráficos - Análisis de Autos")

# Crear un filtro en el sidebar para seleccionar el año de modelo (model_year)
selected_year = st.sidebar.slider("Selecciona un Año de Modelo:", int(df["model_year"].min()), int(df["model_year"].max()), int(df["model_year"].min()), step=1)

# Filtrar los datos según el año seleccionado
filtered_df = df[df["model_year"] == selected_year]

# Crear tres gráficos diferentes
# Gráfico 1: Relación entre el peso y las millas por galón, coloreado por origen
fig1 = px.scatter(filtered_df, x="weight", y="mpg", color="origin", 
                  size="horsepower", title="Relación entre Peso y MPG (Color por Origen)")

# Gráfico 2: Promedio de MPG por número de cilindros
fig2 = px.bar(df.groupby("cylinders").agg({"mpg": "mean"}).reset_index(), x="cylinders", y="mpg", 
              title="Promedio de MPG por Número de Cilindros")

# Gráfico 3: Evolución de la Potencia del Motor a lo largo de los años de modelo
fig3 = px.line(df.groupby("model_year").agg({"horsepower": "mean"}).reset_index(), 
               x="model_year", y="horsepower", title="Evolución de la Potencia del Motor por Año de Modelo")

# Organizar los gráficos en un diseño de cuadrícula con dos columnas
col1, col2 = st.columns(2)  # Crear 2 columnas

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # Primer gráfico en la primera columna

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Segundo gráfico en la segunda columna

# Agregar el tercer gráfico en una fila de ancho completo abajo
st.plotly_chart(fig3, use_container_width=True)
