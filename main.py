import pandas as pd
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt


def main():
    print('BEM-VINDO A O FIFINHA-GRAFO\n')
    print('CARREGANDO O GRAFO...')
    G = nx.read_gml('grafoCompleto.gml')
    print('GRAFO CARREGADO!\n\n')
    print('OBS: PARA SAIR DIGITE exit')
    print('Digite o nome de dois jogadores que não atuaram juntos durante a carreira: ')
    jogador1 = 'null'
    while(jogador1 != 'exit'):
        jogador1 = input('Digite o nome do primeiro jogador: ')
        if(jogador1 != 'exit'):
            if(G.has_node(jogador1)):
                print('JOGADOR ENCONTRADO NO GRAFO!')
                jogador2 = input('Digite o nome do segundo jogador: ')
                if(jogador2 != 'exit'):
                    if(G.has_node(jogador2)):
                        print('JOGADOR ENCONTRADO NO GRAFO!\n')
                        caminhoMinimo(jogador1, jogador2, G)

                    else:
                        print('JOGADOR NÃO ENCONTRADO, POR FAVOR, VERIFICA SE O NOME ESTÁ CORRETO')
            else:
                print('JOGADOR NÃO ENCONTRADO, POR FAVOR, VERIFICA SE O NOME ESTÁ CORRETO')

def caminhoMinimo(player1, player2, grafo):
    try:
        caminho = nx.shortest_path(grafo, player1, player2)
        print('A distância mínima é ', len(caminho)-1)
        print('A LIGAÇÃO ENCONTRADA ENTRE OS JOGADORES FOI: \n')
        for node in caminho:
            print(node,'\n')
        print('\n')
    except:
        print('OS JOGADORES NÃO POSSUEM NENHUMA LIGAÇÃO\n')

main()