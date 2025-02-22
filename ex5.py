import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns


data = {
    'Volumen de Producción': [1000, 500, 1500, 800, 1200, 900, 1100, 650, 1400, 2000],
    'Técnica de Cultivo': ['Riego por goteo', 'Tradicional', 'Riego por goteo', 'Sist. Hidropónico', 
                           'Tradicional', 'Sist. Hidropónico', 'Riego por goteo', 'Tradicional', 
                           'Riego por goteo', 'Sist. Hidropónico'],
    'Campesino Asociado': ['Juan Pérez', 'María López', 'Carlos García', 'Ana Ruiz', 
                           'Luis Hernández', 'Elena Díaz', 'José Martínez', 'Sofía Torres', 
                           'Miguel Sánchez', 'Laura Fernández'],
    'Género': ['Masculino', 'Femenino', 'Masculino', 'Femenino', 'Masculino', 
               'Femenino', 'Masculino', 'Femenino', 'Masculino', 'Femenino'],
    'Edad': [45, 38, 50, 32, 41, 29, 54, 27, 36, 41],
    'Año': [2021, 2021, 2022, 2022, 2023, 2023, 2022, 2023, 2021, 2021]  # Año de producción
}

# Crear el DataFrame
df = pd.DataFrame(data)


# Streamlit App Title
st.title("📊 DAsh Agrícola")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select año:", int(df["Año"].min()), int(df["Año"].max()), int(df["Año"].min()))

# Filter data based on the selected year
filtered_df = df[df["Año"] == selected_year]

# Create three different plots
# 1. Scatter plot - Volumen de Producción vs Edad
fig1 = px.scatter(filtered_df, x="Edad", y="Volumen de Producción", color="Técnica de Cultivo", 
                  size="Volumen de Producción", title="Volumen de Producción vs Edad")

# 2. Bar chart - Volumen de Producción por Técnica de Cultivo
fig2 = px.bar(filtered_df, x="Técnica de Cultivo", y="Volumen de Producción", color="Técnica de Cultivo", 
              title="Volumen de Producción por Técnica de Cultivo")

# 3. Line chart - Volumen de Producción por Año
fig3 = px.line(filtered_df.groupby("Año").sum().reset_index(), x="Año", y="Volumen de Producción", 
               title="Volumen de Producción por Año")

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)
