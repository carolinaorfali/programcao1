import math
import random #random qualquer numero#
lmin,lmax = 1,1000
numbertoguess = random.randint(lmin,lmax)  

# guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

# print(f'valor inserido: {guess}, do tipo ({type(guess).__name__})')
# print(f'{guess.isnumeric()} ;{guess.isdecimal()}')
guess = ""
attempt = 0
tentativas= []

while (guess != numbertoguess and guess != 'end'):
    guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

    guess = guess.strip()

    try: 
        guess = int(guess)
        if (guess > numbertoguess):
            print("mais baixo")
        elif (guess < numbertoguess):
            print("mais alto")
        else:
            print("acertou")   
       
    except Exception as ex:
        if (guess != 'end'):
           print(f'O valor "{guess}" não é um número válido: {type(ex).__name__}: {ex}')
    finally:
        attempt += 1 # equivalente a attempt + 1 #
        tentativas.append(guess)
    print(f'valor inserido: {guess} á {attempt}ª tentativas')
if (guess == 'end'):
            print(f'desitiu ao fim de {attempt} tentativas')
else:
    print(f'acertou no numero {numbertoguess} em {attempt} tentativas')
    for tentativa in tentativas:
        print(tentativa)