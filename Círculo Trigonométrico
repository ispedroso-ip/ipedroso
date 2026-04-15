import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Configuração da página
st.set_page_config(page_title="Círculo Unitário", layout="wide")

st.title("🎡 Círculo Unitário Interativo")

# Sidebar para controle (opcional, já que o gráfico é interativo)
angulo_graus = st.sidebar.slider("Ajuste o ângulo (α)", 0.0, 360.0, 45.0)
angulo_rad = np.deg2rad(angulo_graus)

# Cálculos
x = np.cos(angulo_rad)
y = np.sin(angulo_rad)

# Função para formatar radianos em texto
def format_rad(rad):
    pi_frac = rad / np.pi
    if np.isclose(pi_frac, 0): return "0"
    if np.isclose(pi_frac, 0.5): return "π/2"
    if np.isclose(pi_frac, 1.0): return "π"
    if np.isclose(pi_frac, 1.5): return "3π/2"
    if np.isclose(pi_frac, 2.0): return "2π"
    return f"{pi_frac:.2f}π"

# --- Criação do Gráfico com Plotly ---
fig = go.Figure()

# 1. O Círculo
t = np.linspace(0, 2*np.pi, 100)
fig.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', name='Círculo', line=dict(color='white')))

# 2. Eixos X e Y
fig.add_shape(type="line", x0=-1.5, y0=0, x1=1.5, y1=0, line=dict(color="gray", width=1))
fig.add_shape(type="line", x0=0, y0=-1.5, x1=0, y1=1.5, line=dict(color="gray", width=1))

# 3. Projeções (Seno e Cosseno)
fig.add_trace(go.Scatter(x=[x, x], y=[0, y], mode='lines', line=dict(color='red', dash='dash'), name='Seno'))
fig.add_trace(go.Scatter(x=[0, x], y=[y, y], mode='lines', line=dict(color='blue', dash='dash'), name='Cosseno'))

# 4. Raio e Ponto
fig.add_trace(go.Scatter(x=[0, x], y=[0, y], mode='lines+markers', name='Raio', marker=dict(size=10, color='green')))

# Configurações de layout do gráfico
fig.update_layout(
    width=600, height=600,
    xaxis=dict(range=[-1.2, 1.2], zeroline=False),
    yaxis=dict(range=[-1.2, 1.2], zeroline=False),
    showlegend=False,
    template="plotly_dark"
)

# Layout em Colunas (Gráfico à esquerda, Tabela à direita)
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Tabela de Valores")
    st.markdown(f"""
    | Grandeza | Valor |
    | :--- | :--- |
    | **α (graus)** | {angulo_graus:.1f}° |
    | **α (rad)** | {format_rad(angulo_rad)} |
    | **x = cos α** | `{x:.4f}` |
    | **y = sen α** | `{y:.4f}` |
    """)
