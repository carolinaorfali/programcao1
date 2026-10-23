#escrever um programa que aceita entradas do ultilizador 
#adicionando a uma listata ate o ultilizador escrever "end"
#quando o ultilizador escreve "end", o profgrama apresenta a lista de ecra, sem o "end"
cores = ""
attempt = 0
tentativas= []

while(cores != 'end'):
    cores = input(f"Me fale cores primarias: -->")
    attempt += 1
    tentativas.append(cores)
    if ( cores== 'end'):
        print(f'desitiu ao fim de {attempt} tentativas')
else:
    for tentativa in tentativas:
        print(tentativa)
