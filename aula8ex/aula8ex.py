#Os exercicios estao separados por funcao, no ex4 estava tentando utilizar replace mas nao estava funcionando
#Entao achei este metodo fillna() realizar esta tarefa

import pandas as pd

def ex1():
    df = pd.read_excel('best-selling game consoles.xlsx')
    print(df)
    
    
def ex2():
    df = pd.read_excel('best-selling game consoles.xlsx')
    sub = df["Console Name"].str.replace("NES","Nintendinho").str.upper()
    print(sub)


def ex3():
    df = pd.read_excel('best-selling game consoles.xlsx')
    filtro = df["Released Year"] > 2010
    df_filtrado = df[filtro]
    print(df_filtrado)

    
def ex4():
    df = pd.read_excel('best-selling game consoles.xlsx')
    df.describe()
    df.info()
    df.fillna('missing')


def ex5():
    df = pd.read_excel('best-selling game consoles.xlsx')
    filtro = ((df["Discontinuation Year"] - df["Released Year"] < 2) & (df["Discontinuation Year"] - df["Released Year"] > 0))
    df_filtrado = df[filtro]
    print(df_filtrado)

    
ex1()
ex2()
ex3()
ex4()  
ex5()