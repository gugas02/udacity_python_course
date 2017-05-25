# importa a biblioteca que trata funções do sistema
import os
# variavel que diz o caminho da pasta de arquivo
path = "C:/Users/elisabete/Documents/udacity_python_course/aula2/prank"
# armazena o nome dos arquivos em uma lista
file_list = os.listdir(path)
print(file_list)
# salva o diretorio atual
save_dir = os.getcwd()
# muda o diretorio atual para o diretorio dos arquivos a ser renomeado
os.chdir(path)
# for para iterar em todos os elementos da lista
for file_name in file_list:
    print("Verificando/renomeando o arquivo "+file_name)
    # função que renomeia os arquivos de uma determinada pasta.
    # a função str.translate() consegue retirar caracteres indesejados de uma determinada string, no caso ela verifica
    # se na string existe algum numero decimal, caso exista ela retira ele
    #maketrans cria a tabela necessaria para .translate funcionar
    os.rename(file_name, file_name.translate(str.maketrans("","", "0123456789")))
# retorna para o diretorio inicial do preograma
os.chdir(path)