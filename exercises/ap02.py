import sys 
sys.stdout.reconfigure(encoding="utf-8")
# comentario 
'''
comentario de varias linhas 
'''
nome = 'Carolina Orfali'
print("olá "+ nome)
print(f"Olá {nome},\nBem-vinda! ")

#receber dados de utilizador 
disciplina = input(f"Olá {nome}, escreve o nome de uma disciplina:")
print(f"Olá {nome},\nBem-vinda a {disciplina}! ")

print("nome é do tipo: " + type (nome).__name__)

