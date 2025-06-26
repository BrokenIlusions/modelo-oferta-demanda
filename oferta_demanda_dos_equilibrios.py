
import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="Oferta y Demanda con Dos Equilibrios", layout="centered")
st.title("📊 Modelo con Oferta Desplazable y Equilibrios Comparativos")

# Parámetros fijos
m_d = -1.0  # pendiente demanda
b_d = 50.0  # intercepto demanda

m_o = 1.0   # pendiente oferta
b_o_base = 10.0  # intercepto base oferta

# Cálculo del equilibrio original
q_eq_base = (b_d - b_o_base) / (m_o - m_d)
p_eq_base = m_d * q_eq_base + b_d

# Desplazamiento de oferta
st.sidebar.header("🛠️ Desplazamiento de Oferta")
desp_o = st.sidebar.slider("Desplazamiento de Oferta (→ positiva, ← negativa)", -30.0, 30.0, 0.0)
b_o_nueva = b_o_base + desp_o  # nuevo intercepto de oferta

# Rango de cantidades
Q = np.linspace(0, 100, 100)

# Cálculo de curvas
D = m_d * Q + b_d
O_base = m_o * Q + b_o_base
O_nueva = m_o * Q + b_o_nueva

# Cálculo del nuevo equilibrio
q_eq_nuevo = (b_d - b_o_nueva) / (m_o - m_d)
p_eq_nuevo = m_d * q_eq_nuevo + b_d

# Gráfico
fig = go.Figure()

# Curvas
fig.add_trace(go.Scatter(x=Q, y=D, mode='lines', name='Demanda Fija', line=dict(color='red')))
fig.add_trace(go.Scatter(x=Q, y=O_base, mode='lines', name='Oferta Original', line=dict(color='green', dash='dot')))
fig.add_trace(go.Scatter(x=Q, y=O_nueva, mode='lines', name='Oferta Desplazada', line=dict(color='green')))

# Punto de equilibrio original
fig.add_trace(go.Scatter(x=[q_eq_base], y=[p_eq_base], mode='markers+text',
                         name='Equilibrio Inicial', marker=dict(size=10, color='blue'),
                         text=[f'Base: ({q_eq_base:.1f}, {p_eq_base:.1f})'], textposition="top center"))

# Nuevo punto de equilibrio
fig.add_trace(go.Scatter(x=[q_eq_nuevo], y=[p_eq_nuevo], mode='markers+text',
                         name='Nuevo Equilibrio', marker=dict(size=10, color='orange'),
                         text=[f'Nuevo: ({q_eq_nuevo:.1f}, {p_eq_nuevo:.1f})'], textposition="bottom center"))

# Layout
fig.update_layout(title="Curva de Demanda Fija con Oferta Desplazable y Dos Equilibrios",
                  xaxis_title="Cantidad (Q)", yaxis_title="Precio (P)",
                  legend=dict(x=0.01, y=0.99))

# Mostrar
st.plotly_chart(fig)
st.success(f"🔵 Equilibrio Inicial: Q = {q_eq_base:.2f}, P = {p_eq_base:.2f}")
st.info(f"🟠 Nuevo Equilibrio: Q = {q_eq_nuevo:.2f}, P = {p_eq_nuevo:.2f}")
