import streamlit as st
from streamlit_option_menu import option_menu
from apps import DespXVotos, gastosReceitasVotos, candidatos, municipios  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")


# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": candidatos.app, "title": "Candidatos", "icon": "people"},
    {"func": DespXVotos.app, "title": "Votos e Correlações", "icon": "file-bar-graph"},
    {"func": municipios.app, "title": "Votos e Municipios", "icon": "map"},
    {"func": gastosReceitasVotos.app, "title": "Receitas e Despesas", "icon": "file-bar-graph"}
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Eleições 2018",
        options=titles,
        icons=icons,
        menu_icon="menu-button-fill",
        default_index=default_index,
    )

    st.sidebar.title("Sobre")
    st.sidebar.info(
        """
        Esse [aplicativo](https://share.streamlit.io/gabrielhxg/eleicoes_streamlit) foi criado por [Gabriel Hxg](https://gabrielhxg.carrd.co/) 
        como forma de apresentação do projeto de ciência de dados 'Eleições 2018'. 
        
        Dados Fonte: [Prestação de contas eleitorais](https://dadosabertos.tse.jus.br/dataset/prestacao-de-contas-eleitorais-2018/resource/0ecf7548-55c6-4080-b989-50b0eeb790bf), [Resultados da votação](https://dadosabertos.tse.jus.br/dataset/resultados-2018/resource/459d3040-12a2-4b59-9d90-31bec1e3e40d)
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
