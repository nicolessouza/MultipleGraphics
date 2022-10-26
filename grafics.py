from asyncore import read
import altair as alt
import streamlit as st
import pandas as pd

# Carregando Hp_dataset
df = pd.read_csv('hp_dataset.csv')

st.title('Dashboard da Saga Harry Potter 🧙‍♂️')
st.write('O objetivo desse dashboard é visualizar algumas informações sobre os livros da saga Harry Potter')

# Alterando dataframe para que os índices comecem em 1
df.index = df.index + 1

df = df.reset_index()
df["index"] = df["index"].astype(str)
df["Publish Year"] = df["Publish Year"].astype(int)

# renomeando uma coluna do dataframe
df = df.rename(columns={'index': 'Book'})

# criando coluna nova no dataframe com valores de 1 a 7
df['Hours Audio'] = [9.5, 11, 13, 22.25, 30.25, 21.5, 24]

bar1 = alt.Chart(df).mark_bar().encode(
    x= 'Book',
    y='Copies Sold WorldWide',
    color='Book'
).properties(
    width=alt.Step(50),
    title = "Vendas de Livros no Mundo"
)
# st.altair_chart(bar, use_container_width=True)
bar2 = alt.Chart(df).mark_bar().encode(
    x= 'Book',
    y='Copies Sold in UK',
    color='Book'
).properties(
    width=alt.Step(50),
    title = "Vendas de Livros no Reino Unido"
)

st.altair_chart(bar1 | bar2)

# Gráfico de linha com a quantidade de prêmios
line = alt.Chart(df).mark_line(
    size = 4
).encode(
    x= alt.X('Publish Year', scale=alt.Scale(domain=(1995, 2010))),
    y='Total Awards Won',
).properties(
    width=alt.Step(50),
    title = "Prêmios por livro"
)


#gráfico de dispersão com a quantidade de páginas e o o tempo do áudiobook
scatter = alt.Chart(df).mark_circle(
    size = 100
).encode(
    x='Hours Audio',
    y= 'Pages',
    color='Book'
).properties(
    width=alt.Step(50),
    title = "Tempo do áudiobook por número de páginas"
)
st.altair_chart(line | scatter)

st.write('A nossa base de dados pode ser observada abaixo')
st.write(df)

#Imprimindo coluna do Dataframe 
# st.write(df['Book'])