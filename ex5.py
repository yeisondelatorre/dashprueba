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
