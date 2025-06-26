
import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="Modelo Estático de Oferta y Demanda", layout="centered")
st.title("📉 Modelo Estático de Oferta y Demanda")

# Pendientes y interceptos fijos
m_d = -1.0  # pendiente demanda
b_d = 50.0  # intercepto demanda

m_o = 1.0   # pendiente oferta
b_o = 10.0  # intercepto oferta

# Rango de cantidades
Q = np.linspace(0, 100, 100)

# Cálculo de curvas
D = m_d * Q + b_d
O = m_o * Q + b_o

# Cálculo de punto de equilibrio
q_eq = (b_d - b_o) / (m_o - m_d)
p_eq = m_d * q_eq + b_d

# Gráfico
fig = go.Figure()

# Curvas fijas
fig.add_trace(go.Scatter(x=Q, y=D, mode='lines', name='Demanda', line=dict(color='red')))
fig.add_trace(go.Scatter(x=Q, y=O, mode='lines', name='Oferta', line=dict(color='green')))

# Punto de equilibrio
fig.add_trace(go.Scatter(x=[q_eq], y=[p_eq], mode='markers+text',
                         name='Equilibrio', marker=dict(size=10, color='blue'),
                         text=[f'({q_eq:.1f}, {p_eq:.1f})'], textposition="top center"))

# Configuración del gráfico
fig.update_layout(title="Curvas de Oferta y Demanda (Situación Actual)",
                  xaxis_title="Cantidad (Q)",
                  yaxis_title="Precio (P)",
                  legend=dict(x=0.02, y=0.98))

# Mostrar gráfico
st.plotly_chart(fig)
st.success(f"🔵 Punto de Equilibrio: Q = {q_eq:.2f}, P = {p_eq:.2f}")
