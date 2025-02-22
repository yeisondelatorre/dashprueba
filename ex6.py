# example 6
# Cargar el dataset de mpg de Seaborn
df = sns.load_dataset('mpg')

# Asegúrate de que los datos no tengan valores nulos
df = df.dropna()


# Streamlit App Title
st.title("📊 Dashboard de Análisis de Autos")

# Crear un filtro en el sidebar para seleccionar el año del modelo (model_year)
selected_year = st.sidebar.slider("Selecciona un año de modelo:", int(df["model_year"].min()), int(df["model_year"].max()), int(df["model_year"].min()))

# Filtrar los datos según el año seleccionado
filtered_df = df[df["model_year"] == selected_year]

# Gráfico 1: Relación entre el peso y las millas por galón, coloreado por origen
fig1 = px.scatter(filtered_df, x="weight", y="mpg", color="origin", 
                  size="horsepower", title="Relación entre Peso y MPG (Color por Origen)")

# Gráfico 2: Promedio de MPG por número de cilindros
# Seleccionar solo columnas numéricas antes de aplicar el promedio
fig2 = px.bar(df.groupby("cylinders").agg({"mpg": "mean"}).reset_index(), x="cylinders", y="mpg", 
              title="Promedio de MPG por Número de Cilindros")

# Gráfico 3: Evolución de la Potencia y Aceleración a lo largo de los años de modelo
# Seleccionar solo columnas numéricas antes de aplicar el promedio
fig3 = px.line(df.groupby("model_year").agg({"horsepower": "mean", "acceleration": "mean"}).reset_index(), 
               x="model_year", y=["horsepower", "acceleration"], 
               title="Evolución de Potencia y Aceleración por Año de Modelo")

# Layout - Usando Tabs para mostrar los diferentes gráficos
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)
