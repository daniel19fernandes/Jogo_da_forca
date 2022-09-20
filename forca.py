
import random





def jogo_for():

#Sequência de execução do código:
    mensagem_abertura()
    palavra_chave = carrega_palavra_sec()



#Variáveis do laço
    num_letras_pc = 8
    enforcou = False
    acertou = False
    letras_certas = ["_" for letra in palavra_chave]
    erros = 0

    print(letras_certas)


    while(not enforcou and not acertou):

            chute = pede_chute()


            if(chute in palavra_chave):
                marca_chute_correto(chute, letras_certas, palavra_chave)
            else:
                erros = erros + 1

                if(chute not in palavra_chave):
                    print("Essa letra não existe na palavra. Resta apenas {} chance(s)".format(num_letras_pc))
                    num_letras_pc = num_letras_pc - 1

            enforcou = erros == 8
            acertou = "_" not in letras_certas

            print(letras_certas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_chave)


    print("Fim de jogo!")




 # ORGANIZAÇÃO DOS CÓDIGOS # Se der erro, tentar inverter a ordem... o última será o primeiro e assim por diante #



# Mensagem de abertura

def mensagem_abertura():
    print("********************************")
    print("******** JOGO DA FORCA *********")
    print("********************************")



# Carregando a palavra secreta

def carrega_palavra_sec():
    arquivo = open("palavras_ex.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero_aleat = random.randrange(0, len(palavras))
    palavra_chave = palavras[numero_aleat]
    return palavra_chave


# Imputando o chute do usuário
def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip()
    chute = chute.lower()
    return chute

# Laço que retorna se a letra chutada estiver correta ou não
def marca_chute_correto(chute, letras_certas, palavra_chave):
    index = 0
    for letra in palavra_chave:
        if (chute == letra):
            letras_certas[index] = letra
        index = index + 1



# Mensagem vencedor e perdedor

def imprime_mensagem_vencedor():
    print("Muito bem! Parabéns!")

def imprime_mensagem_perdedor(palavra_chave):
    print("Você foi enforcado! A palavra certa é: {} !".format(palavra_chave))

##Comando responsável por fazer o sistema rodar nesse arquivo e no arquivo "Tabela_de_Jogos"
if(__name__ == "__main__"):
    jogo_for()
