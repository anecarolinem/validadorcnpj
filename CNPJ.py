import re  # tirar os pontos do cnpj

regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(CNPJ):
    CNPJ = so_numeros(CNPJ)

    try: #não aceitar letras
        if segue_sequencia(CNPJ):
            return False
    except:
        return False

    try: # se tiver erro, não continuar o programa
        novo_cnpj= calcula_digito(CNPJ=CNPJ, digito=1)
        novo_cnpj = calcula_digito(CNPJ=novo_cnpj, digito=2)
    except Exception as e:
        return False

    if novo_cnpj == CNPJ:
        return True
    else:
        return False

def calcula_digito(CNPJ, digito):
    if digito == 1:
        regressivoss= regressivos[1:]
        novo_cnpj = CNPJ[:-2]
    elif digito == 2:
        regressivoss= regressivos
        novo_cnpj = CNPJ
    else:
        return None

    total = 0
    for indice, regressivo in enumerate(regressivoss):
        total +=int (CNPJ[indice]) * regressivo

    digito = 11 - (total % 11)
    digito= digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

def segue_sequencia(CNPJ): #verificar se não é um CNPJ com com números repetidos
    sequencia = CNPJ[0] * len(CNPJ)
    if sequencia == CNPJ:
         return True
    else:
         return False


def so_numeros(CNPJ):
    return re.sub(r'[^0-9]', '', CNPJ)
