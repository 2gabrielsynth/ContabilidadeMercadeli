import streamlit as st
from datetime import datetime, timedelta
import os
os.system('apt-get install -y locales')

# Configuração da localização para português do Brasil
os.system('locale-gen pt_BR.utf-8')
os.system('update-locale LANG=pt_BR.utf-8 LC_TIME=pt_BR.utf-8')

# Agora, você pode usar a biblioteca locale no seu código
import locale
locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')


locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

data_atual = datetime.now()
mes_passado = datetime(data_atual.year, data_atual.month, 1) - timedelta(days=1)


numero_do_mes = mes_passado.month


mes_only = mes_passado.strftime('%B').capitalize()
nome_mes_formatado = mes_passado.strftime('%B de %Y').capitalize()

logo_img = "imgs/logo2.jpg"
st.markdown("<h2 style='color:#BD2F3C; font-size: 3em;'>Arquivos Mercadeli</h2>", unsafe_allow_html=True)
st.image(logo_img,use_column_width=True)
st.markdown(f"<h1 style='color:#BD2F3C; font-size: 1.5em;'>{nome_mes_formatado}</h1>", unsafe_allow_html=True)


nome_arquivo = f"{numero_do_mes}{mes_only.upper()}"

caminho_arquivo_Autorizadas = "Autorizadas.rar"
caminho_arquivo_Canceladas = "Canceladas.rar"
caminho_arquivo_Devoluções = "Devoluções.rar"
caminho_arquivo_Perdas = "Perdas.rar"
caminho_arquivo_Rejeitadas = "Rejeitadas.rar"
caminho_arquivo_Relatórios = "Relatórios.rar"
caminho_arquivo_VarejoVendas = "VarejoVendas.rar"


def ler_arquivo_rar(caminho):
    with open(caminho, 'rb') as arquivo_rar:
        conteudo_rar = arquivo_rar.read()
    return conteudo_rar


def download_arquivo_Autorizadas():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Autorizadas)
    return conteudo_rar

def download_arquivo_Canceladas():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Canceladas)
    return conteudo_rar

def download_arquivo_Devoluções():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Devoluções)
    return conteudo_rar

def download_arquivo_Perdas():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Perdas)
    return conteudo_rar

def download_arquivo_Rejeitadas():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Rejeitadas)
    return conteudo_rar

def download_arquivo_Relatórios():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_Relatórios)
    return conteudo_rar

def download_arquivo_VarejoVendas():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_VarejoVendas)
    return conteudo_rar

st.markdown(f"<h1 style='color:#BD2F3C; font-size: 1.3em;'>Frente de Loja:</h1>", unsafe_allow_html=True)
st.download_button(
    label="Notas Autorizadas",
    data=download_arquivo_Autorizadas(),
    file_name="Autorizadas",
    key='download_button_rar'
)

st.download_button(
    label="Notas Canceladas",
    data=download_arquivo_Canceladas(),
    file_name="Canceladas",
    key='download_button_rar2'
)
st.download_button(
    label="Notas Rejeitadas",
    data=download_arquivo_Rejeitadas(),
    file_name="Rejeitadas",
    key='download_button_rar5'
)

st.markdown(f"<h1 style='color: gray; font-size: 1.3em;'>Varejo Fácil:</h1>", unsafe_allow_html=True)
st.download_button(
    label="Devoluções",
    data=download_arquivo_Devoluções(),
    file_name="Devoluções",
    key='download_button_rar3'
)
st.download_button(
    label="Perdas",
    data=download_arquivo_Perdas(),
    file_name="Perdas",
    key='download_button_rar4'
)

st.download_button(
    label="Relatórios",
    data=download_arquivo_Relatórios(),
    file_name="Relatórios",
    key='download_button_rar6'
)
st.download_button(
    label="Varejo Vendas",
    data=download_arquivo_VarejoVendas(),
    file_name="Varejo Vendas",
    key='download_button_rar7'
)
