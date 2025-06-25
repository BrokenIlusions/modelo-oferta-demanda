
import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="Modelo Oferta y Demanda - Interactivo", layout="centered")
st.title("📊 Modelo Interactivo de Oferta y Demanda")

# Inputs base
st.sidebar.header("📌 Parámetros iniciales")

# Pendientes fijas
m_d = -1.0
m_o = 1.0

# Interceptos base
b_d_base = st.sidebar.slider("Intercepto base Demanda (b_d)", 0.0, 100.0, 50.0)
b_o_base = st.sidebar.slider("Intercepto base Oferta (b_o)", 0.0, 50.0, 10.0)

# Desplazamientos
st.sidebar.header("🛠️ Desplazamiento de curvas")

desp_d = st.sidebar.slider("Desplazamiento Demanda (→ positiva, ← negativa)", -30.0, 30.0, 0.0)
desp_o = st.sidebar.slider("Desplazamiento Oferta (→ positiva, ← negativa)", -30.0, 30.0, 0.0)

# Nuevo intercepto con desplazamiento
b_d = b_d_base + desp_d
b_o = b_o_base + desp_o

# Rango de cantidades
Q = np.linspace(0, 100, 100)

# Ecuaciones
D = m_d * Q + b_d
O = m_o * Q + b_o

# Punto de equilibrio
try:
    q_eq = (b_d - b_o) / (m_o - m_d)
    p_eq = m_d * q_eq + b_d
    eq_text = f"🔵 Punto de Equilibrio: Q = {q_eq:.2f}, P = {p_eq:.2f}"
except ZeroDivisionError:
    q_eq, p_eq = None, None
    eq_text = "⚠️ No hay equilibrio (pendientes paralelas)"

# Gráfico interactivo
fig = go.Figure()

# Curvas actualizadas
fig.add_trace(go.Scatter(x=Q, y=D, mode='lines', name='Demanda Desplazada', line=dict(color='red')))
fig.add_trace(go.Scatter(x=Q, y=O, mode='lines', name='Oferta Desplazada', line=dict(color='green')))

# Punto de equilibrio
if q_eq and 0 <= q_eq <= 100:
    fig.add_trace(go.Scatter(x=[q_eq], y=[p_eq], mode='markers+text',
                             name='Equilibrio', marker=dict(size=10, color='blue'),
                             text=[f'({q_eq:.1f}, {p_eq:.1f})'], textposition="top center"))

fig.update_layout(title="Curvas de Oferta y Demanda con Desplazamiento",
                  xaxis_title="Cantidad (Q)", yaxis_title="Precio (P)",
                  legend=dict(x=0.02, y=0.98))

st.plotly_chart(fig)
st.success(eq_text)
