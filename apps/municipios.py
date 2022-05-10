import streamlit as st
import pandas as pd
import plotly.express as px


def app():
    st.title("Votos por Município")

    logx = st.radio('Escala Log',('Sim', 'Não'),1)
    votsMuns = pd.read_csv('votXmun_cand.csv')

## Style | RegPlot
    fig = px.scatter(votsMuns, 
                        x='NM_MUNICIPIO', 
                        y='Total_Votos',
                        color = 'DS_CARGO',
                        log_y=(logx=='Sim'),
                        color_discrete_sequence=px.colors.qualitative.Safe, 
                        template="plotly_dark")
    # Plot 
    st.subheader('Scatter plot ')
    st.write('Municípios votantes X número de votos | **por candidato**')

    st.plotly_chart(fig, use_container_width=True)



    ## Style | 2D KDE 
    
    fig = px.histogram(votsMuns,
                       x='NM_MUNICIPIO', 
                       y='Total_Votos',
                       color = 'DS_CARGO',
                       log_y=(logx=='Sim'),
                       marginal="violin",
                       hover_data=votsMuns.columns)
    st.subheader('Histograma')
    st.write('Distribuição de número de municípios votantes em cada candidato | Por Cargo')
    st.plotly_chart(fig, use_container_width=True)

