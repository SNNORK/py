menu= ' '
:[1] - Cadastrar novo usuario
:[2] - Excluir usuario
:[3] - Exibir todos ({})

...:[0] - Sair
 whith open('usuario.dat','r' as arquivo:
 for linha in arquivo:
 if len(linha.strip()))>0: usuario.append(linha.strip())

opcao=''
usuarios = []
while opcao != '0' :
os.system('clear') or None 
Print(menu.format(Len(usuarios)))
opcao= input('Digite a opcao desejada: ')
         if opcao=='1' : usuarios.append(input('Nome:'))
         if opcao=='2' : usuarios.remove(input('Nome:'))
         if opcao=='3' :
         usuarios.sort ()
       for u in usuarios: 
         print(u.strip())
        input(' ')
 whith    open('usuario.dat','w') as arquivo:
    usuario.sort(
for usuarios in usuarios:
   arquivo.write('\n'+usuario.strip())