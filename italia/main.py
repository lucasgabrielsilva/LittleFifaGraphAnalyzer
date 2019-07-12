import pandas as pd
import networkx as nx
import json


G = nx.read_gml('grafo.gml')

print('lendo elencos')
dataset1 = pd.read_csv('./2004.csv')
dataset2 = pd.read_csv('./2005.csv')
dataset3 = pd.read_csv('./2006.csv')
dataset4 = pd.read_csv('./2007.csv')
dataset5 = pd.read_csv('./2008.csv')
dataset6 = pd.read_csv('./2009.csv')
dataset7 = pd.read_csv('./2010.csv')
dataset8 = pd.read_csv('./2011.csv')
dataset9 = pd.read_csv('./2012.csv')
dataset10 = pd.read_csv('./2013.csv')
dataset11 = pd.read_csv('./2014.csv')
dataset12 = pd.read_csv('./2015.csv')
dataset13 = pd.read_csv('./2016.csv')
dataset14 = pd.read_csv('./2017.csv')
dataset15 = pd.read_csv('./2018.csv')

print('Construindo grafo')

flag1 = False
flag2 = False

for index, row in dataset1.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset1.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())


print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset2.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset2.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())


print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset3.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset3.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset4.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset4.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset5.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset5.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")


flag1 = False
flag2 = False

for index, row in dataset6.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset6.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset7.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset7.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset8.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset8.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())


print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset9.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset9.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")


flag1 = False
flag2 = False

for index, row in dataset10.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset10.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset11.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset11.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset12.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset12.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())


print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset13.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset13.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset14.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset14.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())


print("-------------------------------------começo------------------------------------------")

flag1 = False
flag2 = False

for index, row in dataset15.iterrows():
    nome = row['player_name']
    clube = row['club_name']
    temporada = row['year']
    dataNascimento = row['date_of_birth']
    date = str(dataNascimento)
    
    if not (G.has_node(nome)):
        G.add_node(nome, nascimento = date)
        flag1 = True
    else:
        data = G.nodes[nome]['nascimento']
        if(data == dataNascimento):
            flag1 = True
        else:
            flag1 = False
    if(flag1):
        for indice, coluna in dataset15.iterrows():
            nome1 = coluna['player_name']
            clube1 = coluna['club_name']
            temporada1 = coluna['year']
            dataNascimento1 = coluna['date_of_birth']
            date1 = str(dataNascimento1)

            if not (G.has_node(nome1)):
                G.add_node(nome1, nascimento = date1)
                flag2 = True
            else:
                data1 = G.nodes[nome1]['nascimento']
                if(data1 == dataNascimento1):
                    flag2 = True
                else:
                    flag2 = False
            if(flag2):
                if(temporada1 == temporada):
                    if((nome1 != nome) and (clube == clube1)):
                        G.add_edge(nome, nome1, color='black', weight=1)
    print('index: ', index, '  --  arestas: ', G.number_of_edges())

nx.write_gml(G, 'grafo1.gml')
print('termino, grafo gerado')

