import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Círculo Unitário Pro", layout="wide")

# Título e Estilo
st.markdown("""
    <style>
    .main { background-color: #0f0f14; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎡 Círculo Unitário Interativo")

# Controle de Ângulo
col_input, col_info = st.columns([2, 1])
with col_input:
    angulo_graus = st.slider("Arraste para girar o ângulo α", 0.0, 360.0, 45.0, step=0.1)

angulo_rad = np.deg2rad(angulo_graus)
x_val = np.cos(angulo_rad)
y_val = np.sin(angulo_rad)

# --- Função para formatar radianos ---
def format_rad(rad):
    frac = rad / np.pi
    if np.isclose(frac, 0): return "0"
    common = {0.5: "π/2", 1.0: "π", 1.5: "3π/2", 2.0: "2π", 0.25: "π/4", 0.75: "3π/4"}
    for val, label in common.items():
        if np.isclose(frac, val, atol=0.01): return label
    return f"{frac:.2f}π"

# --- Criando o Gráfico ---
fig = go.Figure()

# 1. Círculo Unitário e Eixos
t = np.linspace(0, 2*np.pi, 150)
fig.add_trace(go.Scatter(x=np.cos(t), y=np.sin(t), mode='lines', line=dict(color='white', width=2), hoverinfo='skip'))
fig.add_shape(type="line", x0=-1.5, y0=0, x1=1.5, y1=0, line=dict(color="gray", width=1))
fig.add_shape(type="line", x0=0, y0=-1.5, x1=0, y1=1.5, line=dict(color="gray", width=1))

# 2. Marcadores (-1, -1/2, 1/2, 1)
marks = [-1, -0.5, 0.5, 1]
labels = ["-1", "-1/2", "1/2", "1"]
fig.add_trace(go.Scatter(x=marks, y=[0.05]*4, text=labels, mode="text", textposition="bottom center", hoverinfo='skip'))
fig.add_trace(go.Scatter(x=[0.05]*4, y=marks, text=labels, mode="text", textposition="middle right", hoverinfo='skip'))

# 3. O ARCO AMARELO (Ângulo α)
if angulo_graus > 0:
    arc_t = np.linspace(0, angulo_rad, 50)
    fig.add_trace(go.Scatter(
        x=0.2 * np.cos(arc_t), 
        y=0.2 * np.sin(arc_t), 
        mode='lines', 
        line=dict(color='yellow', width=4),
        name='Ângulo α'
    ))

# 4. Projeções (Seno e Cosseno) - Linhas Coloridas nos Eixos
fig.add_trace(go.Scatter(x=[x_val, x_val], y=[0, y_val], mode='lines', line=dict(color='white', dash='dot', width=1), hoverinfo='skip'))
fig.add_trace(go.Scatter(x=[0, x_val], y=[y_val, y_val], mode='lines', line=dict(color='white', dash='dot', width=1), hoverinfo='skip'))

fig.add_trace(go.Scatter(x=[0, x_val], y=[0, 0], mode='lines', line=dict(color='skyblue', width=6), name='cos α'))
fig.add_trace(go.Scatter(x=[0, 0], y=[0, y_val], mode='lines', line=dict(color='tomato', width=6), name='sen α'))

# 5. Ponto invisível que segue o mouse (Hover dinâmico)
# Adicionamos uma "camada" invisível sobre o círculo para capturar o mouse
fig.add_trace(go.Scatter(
    x=np.cos(t), y=np.sin(t),
    mode='lines',
    line=dict(color='rgba(0,0,0,0)'), # Invisível
    hoverinfo='x+y',
    hovertemplate="α: %{text}<br>x: %{x:.3f}<br>y: %{y:.3f}<extra></extra>",
    text=[f"{(np.degrees(i)):.1f}°" for i in t],
    showlegend=False
))

# 6. O Ponto Ativo (Ponto Verde)
fig.add_trace(go.Scatter(
    x=[x_val], y=[y_val], 
    mode='markers+text', 
    marker=dict(size=18, color='springgreen', line=dict(width=2, color='white')),
    text=[f"({x_val:.2f}, {y_val:.2f})"],
    textposition="top right",
    hoverinfo='skip'
))

# Configurações para o mouse "grudar" no gráfico
fig.update_layout(
    hovermode='closest', # Faz o hover focar no ponto mais próximo do mouse
    dragmode=False,      # Desabilita o zoom de caixa para não atrapalhar
    # ... (restante do layout igual ao anterior)
)

# Configurações de Layout (Círculo Perfeito)
fig.update_layout(
    template="plotly_dark",
    width=None, height=600,
    xaxis=dict(range=[-1.3, 1.3], zeroline=False, scaleanchor="y", scaleratio=1, fixedrange=True),
    yaxis=dict(range=[-1.3, 1.3], zeroline=False, fixedrange=True),
    margin=dict(l=10, r=10, t=10, b=10),
    showlegend=False
)

# --- Layout Final com Tabela ---
col1, col2 = st.columns([2, 1])
with col1:
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

with col2:
    st.markdown(f"""
    ### 📊 Dados do Ponto
    ---
    **Ângulo α:**
    * {angulo_graus:.1f}°
    * {format_rad(angulo_rad)}
    
    <h3 style='color:skyblue'>x = cos α: {x_val:.4f}</h3>
    <h3 style='color:tomato'>y = sen α: {y_val:.4f}</h3>
    """, unsafe_allow_html=True)
