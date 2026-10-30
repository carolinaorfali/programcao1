m1={'ID':1,'nome':'brilhozinho nos olhozinho'}
m2={'ID':2, 'nome':'palpite'}

print(m1,m2)

print(f"ID: {m1['ID']}")
print(f"Nome: {m1['nome']}")
print(f"ID: {m2['ID']}")
print(f"Nome: {m2['nome']}")

#print(m1.keys())
m1['estilo']='pop portugues'
m2['estilo']='MPB'
musicas=[m1,m2]
#musica.append(m1)
#musica.append(m2)

print(musicas)

for musica in musicas:
  #print(musica)
  print(f"ID: {musica['ID']}")
  print(f"Nome: {musica['nome']}")

musicas.append({'ID':3,'nome':'welcome to the jungle'})
musicas[2]['estilo']='rock'
for musica in musicas:
  #print(musica)
  print(f"ID: {musica['ID']}")
  print(f"Nome: {musica['nome']}")
  print(f"estilo: {musica['estilo']}")

for musica in musicas:
    if musica['estilo'] == 'rock':
     for chave,valor in musica.items():
        print (f'{chave}:{valor}')
