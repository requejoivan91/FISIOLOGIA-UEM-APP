import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Fisiología del Ejercicio UEM - Tema 1",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .block-card {
        background-color: #F3F4F6;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background-color: #EFF6FF;
        border: 1px solid #BFDBFE;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Navegación Sidebar
st.sidebar.title("🧬 Fisiología UEM")
st.sidebar.markdown("**Tema 1: Fuentes Energéticas**")

seccion = st.sidebar.radio(
    "Navegación del Temario",
    [
        "🏠 Inicio y Visión General",
        "⚡ Bloque 1: Bioenergética y Fosfágenos",
        "🍞 Bloque 2: Hidratos de Carbono",
        "🥑 Bloque 3: Lípidos y Cuerpos Cetónicos",
        "🥩 Bloque 4: Proteínas y Mix Energético",
        "🎯 Simulacro de Examen Global",
        "📊 Tabla Integradora y Guía"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Consejo de Estudio:** Revisa primero la teoría, practica con las flashcards interactivas y termina evaluándote con el quiz de cada bloque.")

# ==========================================
# SECCIÓN: INICIO
# ==========================================
if seccion == "🏠 Inicio y Visión General":
    st.markdown('<div class="main-title">Fisiología del Ejercicio I - Universidad Europea</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Portal Interactivo de Estudio: Tema 1 - Fuentes Energéticas en la Actividad Física</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Bloques Fisiológicos", "4")
    with col2:
        st.metric("Rutas Metabólicas", "8 Hauptwegen")
    with col3:
        st.metric("Materiales Didácticos", "19 Recuros")
    with col4:
        st.metric("Objetivo Examen", "10/10")

    st.markdown("### 🗺️ Arquitectura de la Asignatura")
    st.markdown("""
    Esta aplicación web organiza todo el temario oficial dividiéndolo en 4 bloques funcionales para facilitar la retención activa (*Active Recall*) y la repetición espaciada:
    
    1. **Bloque 1:** Bioenergética General, la molécula de ATP y el Sistema de Fosfágenos (ATP-PCr).
    2. **Bloque 2:** Metabolismo de los Hidratos de Carbono (Glucólisis citosólica, mitocondrial, lanzaderas de ATP y dinámica del lactato).
    3. **Bloque 3:** Metabolismo de los Lípidos (Lipólisis, carnitina, $\\beta$-oxidación, zona Fat-Max y cuerpos cetónicos).
    4. **Bloque 4:** Metabolismo Proteico (Desaminación, BCAA/leucina, ciclo Alanina-Glucosa, ciclo de las purinas y amonio).
    """)

# ==========================================
# SECCIÓN: BLOQUE 1
# ==========================================
elif seccion == "⚡ Bloque 1: Bioenergética y Fosfágenos":
    st.header("⚡ Bloque 1: Bioenergética General y Sistema de Fosfágenos")
    
    tab1, tab2, tab3 = st.tabs(["📚 Apuntes Clave", "🎴 Flashcards Interactivas", "📝 Quiz de Autoevaluación"])
    
    with tab1:
        st.markdown("""
        ### Conceptos Fundamentales
        * **ATP (Trifosfato de Adenosina):** Moneda energética celular. Su hidrólisis por la **ATPasa** produce $ADP + P_i + \\text{Energía}$.
        * **Sistema de Fosfágenos (Anaeróbico Aláctico):**
          * Enzima clave: **Creatina-cinasa (CK)**.
          * Reacción: $PCr + ADP \\rightarrow ATP + C$.
          * Duración: Esfuerzos máximos de <10 segundos.
          * Las reservas de PCr son **3 a 5 veces superiores** a las de ATP.
          * Resíntesis de PCr: Proceso aeróbico (50% en 30 s, 90% en 2 min). Contribuye al **EPOC**.
        """)
        
    with tab2:
        st.subheader("Ponte a prueba con las Flashcards")
        with st.expander("❓ ¿Cuál es la enzima responsable de la hidrólisis directa del ATP en el músculo?"):
            st.success("**Respuesta:** La **ATPasa** (miofibrilar/sarcoplásmica).")
            
        with st.expander("❓ ¿Cuánto tardan en resintetizarse las reservas de Fosfocreatina (PCr) tras un esfuerzo máximo?"):
            st.success("**Respuesta:** El 50% se resintetiza en 30 segundos y aproximadamente el 90% en 2 minutos (vía aeróbica).")

    with tab3:
        st.subheader("Quiz Rápido: Bloque 1")
        q1 = st.radio("1. ¿Qué proporción guardan las reservas intramusculares de PCr respecto a las de ATP?", 
                      ["Son iguales", "Las de PCr son de 3 a 5 veces superiores", "Las de ATP son 10 veces superiores"], key="b1_q1")
        if st.button("Comprobar Bloque 1"):
            if q1 == "Las de PCr son de 3 a 5 veces superiores":
                st.success("¡Correcto! Las reservas de PCr actúan como tampón energético inmediato.")
            else:
                st.error("Incorrecto. La respuesta correcta es que las reservas de PCr son de 3 a 5 veces superiores a las de ATP.")

# ==========================================
# SECCIÓN: BLOQUE 2
# ==========================================
elif seccion == "🍞 Bloque 2: Hidratos de Carbono":
    st.header("🍞 Bloque 2: Metabolismo de los Hidratos de Carbono")
    
    tab1, tab2, tab3 = st.tabs(["📚 Apuntes Clave", "🎴 Flashcards Interactivas", "📝 Quiz de Autoevaluación"])
    
    with tab1:
        st.markdown("""
        ### Glucólisis y Balance Energético
        * **Transportador principal:** **GLUT4** (translocado por insulina y contracción muscular).
        * **Rendimiento Citosólico:** 
          * Desde glucosa libre: **2 ATP netos**.
          * Desde glucógeno muscular: **3 ATP netos** (ahorro de 1 ATP inicial).
        * **Lanzaderas Mitocondriales:**
          * **Glicerol-3-Fosfato:** Genera 30 ATP (glucosa) o 31 ATP (glucógeno).
          * **Malato-Aspartato:** Genera 32 ATP (glucosa) o 33 ATP (glucógeno).
        * **Lactato:** No es un residuo tóxico. Transportado por **MCT4** (salida de fibras rápidas) y **MCT1** (entrada en fibras lentas/corazón para su oxidación). Reutilizado en el hígado mediante el **Ciclo de Cori**.
        """)
        
    with tab2:
        st.subheader("Flashcards Bloque 2")
        with st.expander("❓ ¿Qué transportador saca el lactato de las fibras tipo II y cuál lo capta en las tipo I?"):
            st.success("**Respuesta:** **MCT4** para la expulsión en fibras tipo II; **MCT1** para la captación y oxidación en fibras tipo I y miocardio.")

    with tab3:
        st.subheader("Quiz Rápido: Bloque 2")
        q2 = st.radio("1. ¿Cuál es el rendimiento neto total de ATP de una molécula de glucógeno mediante la lanzadera Malato-Aspartato?",
                      ["30 ATP", "32 ATP", "33 ATP"], key="b2_q1")
        if st.button("Comprobar Bloque 2"):
            if q2 == "33 ATP":
                st.success("¡Correcto! 32 ATP de base + 1 ATP extra por entrar como glucógeno.")
            else:
                st.error("Incorrecto. El valor exacto es 33 ATP.")

# ==========================================
# SECCIÓN: SIMULACRO GLOBAL
# ==========================================
elif seccion == "🎯 Simulacro de Examen Global":
    st.header("🎯 Simulacro de Examen Global - Fisiología UEM")
    st.write("Responde a estas preguntas integradoras para evaluar tu nivel general antes del examen:")
    
    score = 0
    
    p1 = st.radio("1. ¿Qué enzima limita y regula la velocidad de la lipólisis en el tejido adiposo?",
                  ["Lipoproteína Lipasa (LPL)", "Lipasa Hormonosensible (LHS)", "Carnitina Palmitoiltransferasa-1 (CPT-1)"])
    if p1 == "Lipasa Hormonosensible (LHS)":
        score += 1
        
    p2 = st.radio("2. Durante un ejercicio prolongado con depleción de glucógeno, ¿cuál es la principal fuente de amonio acumulado?",
                  ["Ciclo de las purinas (AMP-desaminasa)", "Desaminación masiva de aminoácidos (BCAA)", "Hidrólisis de fosfocreatina"])
    if p2 == "Desaminación masiva de aminoácidos (BCAA)":
        score += 1
        
    if st.button("Ver Nota Final del Simulacro"):
        st.metric("Resultado", f"{score} / 2 aciertos")
        if score == 2:
            st.balloons()
            st.success("¡Excelente! Tienes los conceptos de integración metabólica perfectamente consolidados.")
        else:
            st.warning("Repasa las áreas con fallos utilizando las guías y tarjetas por bloque.")

# ==========================================
# SECCIÓN: TABLA INTEGRADORA
# ==========================================
elif seccion == "📊 Tabla Integradora y Guía":
    st.header("📊 Tabla Comparativa de Rutas y Enzimas Clave")
    
    df_resumen = pd.DataFrame({
        "Sustrato / Vía": ["Sistema PCr", "Glucólisis Anaeróbica", "Glucólisis Aeróbica", "Beta-Oxidación", "Proteínas / BCAA"],
        "Ubicación Cellular": ["Citosol", "Citosol", "Citosol + Mitocondria", "Matriz Mitocondrial", "Mitocondria / Hígado"],
        "Enzima / Transportador Clave": ["Creatina-cinasa", "PFK-1 / MCT4", "PDH / MCT1", "LHS / CPT-1 / FATP1", "AMP-desaminasa / BCAA-aminotransferasa"],
        "Rendimiento Energético": ["1 ATP / PCr", "2-3 ATP", "30-33 ATP", "100+ ATP / Ácido Graso", "3-10% del total (prolongado)"],
        "Factor Limitante": ["Agotamiento de PCr", "Acumulación de H+ / Acidez", "Disponibilidad de O2", "Transporte por CPT-1 / Flujo sanguíneo", "Depleción de glucógeno"]
    })
    
    st.dataframe(df_resumen, use_container_width=True)
    st.caption("Tabla elaborada para el estudio del Tema 1 de Fisiología del Ejercicio I - UEM.")
