import streamlit as st
from datetime import datetime, timedelta
import locale


locale.setlocale(locale.LC_TIME, 'pt_BR.utf-8')

data_atual = datetime.now()
mes_passado = datetime(data_atual.year, data_atual.month, 1) - timedelta(days=1)


numero_do_mes = mes_passado.month


mes_only = mes_passado.strftime('%B').capitalize()
nome_mes_formatado = mes_passado.strftime('%B de %Y').capitalize()

logo_img = "logo2.jpg"
st.markdown("<h2 style='color: gray; font-size: 3em;'>Arquivos Mercadeli</h2>", unsafe_allow_html=True)
st.image(logo_img,use_column_width=True)
st.markdown(f"<h1 style='color: gray; font-size: 1.5em;'>{nome_mes_formatado}</h1>", unsafe_allow_html=True)


nome_arquivo = f"{numero_do_mes}{mes_only.upper()}.rar"

caminho_arquivo_rar = f"F:/CONTADOR/2024/{nome_arquivo}"


def ler_arquivo_rar(caminho):
    with open(caminho, 'rb') as arquivo_rar:
        conteudo_rar = arquivo_rar.read()
    return conteudo_rar


def download_arquivo_rar():
    conteudo_rar = ler_arquivo_rar(caminho_arquivo_rar)
    return conteudo_rar


st.download_button(
    label="Baixar Arquivo RAR",
    data=download_arquivo_rar(),
    file_name=nome_arquivo,
    key='download_button_rar'
)
