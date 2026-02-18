import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Salud 3º ESO", page_icon="🏥")

# Título y Descripción
st.title("Calculadora de Rebajas🏷️📉")
st.markdown("Holas, introduce tus datos")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("Precio Original", min_value=0, max_value=500, value=50)
descuento_porcentaje = st.sidebar.slider("Porcentaje de la Rebaja", 0, 100, 50)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
   
    # Fórmula Matemática: Peso entre altura al cuadrado
    rebaja = precio * (1 - descuento_porcentaje / 100)
   
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
   
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu Precio Final es:", value=f"{rebaja:.2f}")
        st.markdown(''':grey[Te Ahorras:]''')
        st.write(f"{precio*descuento_porcentaje/100:.2f}")
       
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if descuento_porcentaje >= 50:
            st.warning("🤑 Demasiado Barato")        
    # Extra: Mostrar la fórmula usada (LaTeX)
    st.write("---")
    st.info("Fórmula utilizada:")
    st.latex(r''' Rebaja = \frac{precio * porcentaje}{100} ''')

