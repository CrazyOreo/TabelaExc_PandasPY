#Estou importanto a tabela do Pandas e dando um nome para puxar mais rapido que é "pd"
import pandas as pd

#Aqui estou deixando a tabela pandas aberta no excel já
tabela_tags = pd.read_excel("C:\TAGS.xlsx")
#tabela_tags.loc[3 ,"TAGS"] = "3"

#Estou recebendo o valor para ser inserido na tabela

while True:
    variavel_adc_tabela = input("Digite o numero da tag, escreva 'sair' caso queira sair\n")
    if variavel_adc_tabela.lower() == "sair":
        break
        # Cria um DataFrame temporário com a nova linha, tentei usar o .lower(), porem foi descontinuado pelo Pandas
    nova_linha = pd.DataFrame({"TAGS": [variavel_adc_tabela]})
    
    #Concatena o novo DataFrame com a tabela original
    tabela_tags = pd.concat([tabela_tags, nova_linha], ignore_index=True)
    if 

#Este comando abaixo serve para fechar a tabela e salvar, principalmente na parte ".to_excel", o index=False não foi uma ideia minha, mas pelo o que entendi é para remover a coluna do indice no excel
tabela_tags.to_excel("C:\TAGS.xlsx", index=False)