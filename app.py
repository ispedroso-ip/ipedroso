import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Círculo Unitário Pro", layout="wide")

# Título
st.title("🎡 Círculo Unitário Interativo")

# Controle de Ângulo
angulo_graus = st.slider("Arraste para girar o ângulo α", 0.0, 360.0, 45.0, step=0.1)
angulo_rad = np.deg2rad(angulo_graus)
x_val = np.cos(angulo_rad)
y_val = np.sin(angulo_rad)

# --- Criando o Gráfico ---
fig = go.Figure()

# 1. Círculo Unitário de fundo
t = np.linspace(0, 2*np.pi, 200)
fig.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', line=dict(color='white', width=1), hoverinfo='skip'))

# 2. Eixos Cartesianos
fig.add_shape(type="line", x0=-1.5, y0=0, x1=1.5, y1=0, line=dict(color="gray", width=1))
fig.add_shape(type="line", x0=0, y0=-1.5, x1=0, y1=1.5, line=dict(color="gray", width=1))

# 3. O RAIO (A linha que liga o centro ao ponto)
fig.add_trace(go.Scatter(
    x=[0, x_val], 
    y=[0, y_val], 
    mode='lines+markers', 
    line=dict(color='white', width=3),
    marker=dict(size=[0, 10], color='white'), # Esconde o marcador no (0,0)
    hoverinfo='skip'
))

# 4. ARCO AMARELO
if angulo_graus > 0:
    arc_t = np.linspace(0, angulo_rad, 50)
    fig.add_trace(go.Scatter(x=0.2 * np.cos(arc_t), y=0.2 * np.sin(arc_t), mode='lines', line=dict(color='yellow', width=4), hoverinfo='skip'))

# 5. PROJEÇÕES COLORIDAS NOS EIXOS
fig.add_trace(go.Scatter(x=[0, x_val], y=[0, 0], mode='lines', line=dict(color='skyblue', width=6), name='cos α'))
fig.add_trace(go.Scatter(x=[0, 0], y=[0, y_val], mode='lines', line=dict(color='tomato', width=6), name='sen α'))
# Linhas pontilhadas de conexão
fig.add_trace(go.Scatter(x=[x_val, x_val], y=[0, y_val], mode='lines', line=dict(color='gray', dash='dot', width=1), hoverinfo='skip'))
fig.add_trace(go.Scatter(x=[0, x_val], y=[y_val, y_val], mode='lines', line=dict(color='gray', dash='dot', width=1), hoverinfo='skip'))

# 6. PONTO VERDE COM JANELA DE DADOS (Hover)
fig.add_trace(go.Scatter(
    x=[x_val], y=[y_val], 
    mode='markers', 
    marker=dict(size=15, color='springgreen', line=dict(width=2, color='white')),
    hovertemplate=f"<b>Ângulo:</b> {angulo_graus:.1f}°<br><b>x (cos):</b> {x_val:.4f}<br><b>y (sen):</b> {y_val:.4f}<extra></extra>"
))

# Layout
fig.update_layout(
    template="plotly_dark",
    width=None, height=600,
    xaxis=dict(range=[-1.3, 1.3], zeroline=False, scaleanchor="y", scaleratio=1, fixedrange=True),
    yaxis=dict(range=[-1.3, 1.3], zeroline=False, fixedrange=True),
    showlegend=False,
    hovermode='closest'
)

# Exibição
col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.subheader("📊 Tabela de Valores")
    st.write(f"**Graus:** {angulo_graus:.1f}°")
    st.write(f"**Cosseno (x):** {x_val:.4f}")
    st.write(f"**Seno (y):** {y_val:.4f}")
