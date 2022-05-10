import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

def app():
    st.title("Exploração | Dados principais")
    st.subheader(' ')


    ########### Set data ##########
    full = pd.read_csv('CandidatosFull.csv')
    main_df = full.drop(columns=(['Unnamed: 0','NR_CANDIDATO']))
    full = full.drop(columns=(['Unnamed: 0','NR_CANDIDATO','NM_PARTIDO']))

    ########## First viz ##########
    # Votes, gasto and receita
    RecXDesp = main_df[['Gasto_Candidato','TotalReceita_Candidato']]#,'NM_PARTIDO','DS_CARGO']]

    st.subheader('Receitas, Despesas e Total de Votos')
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown("""**Estudo considerando 2963 Candidatos**""")

    st.write('''Os gráficos abaixo demonstram as relações entre os valores de **Receita|Despesa** x **Total de Votos** de cada candidato.''') 
    st.write('Considere explorar a escala Log em cada eixo para a padronização das métricas.')
    st.markdown('---')

    col1, col2, col3 = st.columns((2,2,1))
    logx = col1.radio('Escala Log | eixo x',('Sim', 'Não'),0)
    logy = col2.radio('Escala Log | eixo y',('Sim', 'Não'),0)
    
    

    for col in RecXDesp.columns:
        fig = px.scatter(main_df, 
                        x = RecXDesp[col], 
                        y=main_df['Votos recebidos'],
                        trendline="ols", 
                        log_x=(logx=='Sim'),
                        log_y=(logy=='Sim'),
                        color_discrete_sequence=px.colors.qualitative.Set1, 
                        template="plotly_dark")
        fig.update_layout(xaxis_title=col)
        # Plot!
        st.plotly_chart(fig, use_container_width=True)

    ## Corr metrics ###
    dXv = main_df[['Gasto_Candidato','Votos recebidos','TotalReceita_Candidato']].corr()
    
    valued=round(dXv.iloc[1][0],5)
    valuer=round(dXv.iloc[1][-1],5)

    col1.metric(label="Correlação Despesas X Votos", value=valued)
    col2.metric(label="Correlaçãoas Receitas X Votos", value=valuer,delta_color="blue")


    


   

    
