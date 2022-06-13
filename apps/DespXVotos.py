import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np



def app():
    st.title("Visualização de Correlação")

    st.markdown(
        """
    **Estudo de correlações**
    """
    )

    # Set data
    full = pd.read_csv('DespesasXVotos.csv')
    full = full.drop(columns=('Unnamed: 0'))

    # Set Colunas
    int_cols = full.select_dtypes(exclude='object').columns.to_list()
    cols = st.multiselect('Selecione as despesas',int_cols,int_cols[:5])

    
    col1, col2, col3 = st.columns((3,1,1))
    # Set std
    Oh = col1.slider('Range limite | Controle de outliers', 0.0, 4.0, 4.0)
    logx = col2.radio('Escala Log | eixo x',('Sim', 'Não'),1)
    logy = col3.radio('Escala Log | eixo y',('Sim', 'Não'),0)
    st.subheader('______________')
    st.subheader('Correlações')

    def regger(full,cols,Oh):

        for coluna in cols:

            # define cleaned df
            noOut_df = full[[coluna,'Votos recebidos']]
            noOut_df_log = np.log(noOut_df)

            # Set mean
            noOut_df_mean = noOut_df[coluna].mean()
            # Set standard deviation
            noOut_df_std = noOut_df[coluna].std()
            # Set range
            rang = noOut_df_mean+(Oh*noOut_df_std)

            # Set df with no outliers
            noOut_df = noOut_df[noOut_df[coluna]<rang]

            ## Style | RegPlot
            fig = px.scatter(noOut_df, 
                            x=coluna, 
                            y='Votos recebidos',
                            log_x=(logx=='Sim'),
                            log_y=(logy=='Sim'),
                            trendline="ols",
                            color_discrete_sequence=px.colors.qualitative.Set1, 
                            template="plotly_dark")

            # Correlation metric
            if (logx=='Sim') and (logy=='Sim'):
                value =round(noOut_df_log.corr(), 4)
            else:
                value =round(noOut_df.corr(), 4)
            
            st.metric(label=f'Correlação entre Voto e {coluna}', value=value.iloc[0][1])

            # Plot 
            st.plotly_chart(fig, use_container_width=True)
            
    regger(full,cols,Oh)

    
    






