from numpy import full
import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Candidatos e suas campanhas")

    st.markdown(
        """
    **Estudo considerando 2963 Candidatos**
    """
    )

    ########### Set data ##########
    full = pd.read_csv('candidatosFull.csv')
    full = full.drop(columns=(['Unnamed: 0','NR_CANDIDATO','NM_PARTIDO']))


    ########## Define querying functions##### #####
    # Select Cargo
    cargosList = list(set(full.DS_CARGO))
    cargosList.remove('Vice-governador')
    cargos     = st.multiselect('Selecione o Cargo',cargosList, cargosList[0] )
    cargString = ''.join([(carg + '|') for carg in cargos])[:-1]

    # Select candidatos
    candList   = full[full.DS_CARGO.str.contains(cargString)].Candidato.to_list()
    candidatos = st.multiselect('Selecione o Candidato',candList, candList[5:8])
    
    def detalhesCandidato(candidatos):
        candString   = ''.join([(name + '|') for name in candidatos])[:-1]
        candFiltered = full[full.Candidato.str.contains(candString)]
        candFiltered = candFiltered.set_index('Candidato')
        candFiltered = candFiltered.drop(columns=(['DS_CARGO','Gasto_Candidato','Votos recebidos']))
        return candFiltered

    df = detalhesCandidato(candidatos)

    # Separate 
    dfCols = list(df.columns.values)
    despesas = df[dfCols[:38]]
    receitas = df[dfCols[38:-1]]
    
    ##### Visualização ########
    ## Style | Bar Plot
    st.subheader('Receita por Candidatos')
    fig1 = px.bar(receitas, 
                color_discrete_sequence=px.colors.qualitative.Set1, 
                template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

    ## Style | Bar Plot
    st.subheader('Despesas por Candidatos')
    fig2 = px.bar(despesas, 
                color_discrete_sequence=px.colors.qualitative.T10, 
                template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

    
