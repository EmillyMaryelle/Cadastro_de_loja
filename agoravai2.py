#Emilly Maryelle Xavier Pereira Numero de matricula 519378
login= []
prints = []
endereço = []
clientes = []
usuario1= []

def menu() :
   option = int(input('''
          "  ** Armazem São Francisco ****"
          *                                                      *"
          "[1]  Cadastrar cliente                                *"
          "[2]  Adicionar endereço a um cadrasto exitente        *"
          "[3]  Dados do cliente                                 *"
          "[4]  Lista de Clientes cadastrados                    *"
          "[0]  Encerrar                                         *"
          *                                                      *"
          ******* 
           '''))

   return option


def cadastro() :
    nome_usuario = str(input('Digite o nome do usuario: '))
    login = str(input('Digite o login do usuario: '))
    newDict = {c[any(login)]: c for c in clientes}
    while login in newDict:
           print ("Login ja existente, Tente novamente")
           return menu
    senha =str(input('Digite a senha do usuario: '))
    email =str(input('Digite o e-mail do usuario: '))
    nascimento = str(input('Digite a data de nascimento: ex: mmnnoo'))
    celular = str(input('Digite o número de celular:    sem alfanumericos, apenas numeros '))
    endereço = str(input('Digite a rua: '))
    n = str(input('Digite o número: '))
    complemento =str(input('Digite o complemento com numero: '))
    bairro = str(input('Digite o bairro: '))
    cidade= str(input('Digite a cidade: '))
    cep = str(input('Digite o cep: '))
    ref = str(input('Digite um ponto de referencia se houver: '))
    clientes_dados = (nome_usuario,login, senha, email, nascimento, celular, endereço, n, complemento, bairro, cidade, cep, ref)
    clientes.append(clientes_dados)
    print(clientes)
    print('Otimo!, estamos com todos os dados e o seu cliente esta cadrastado. Obrigada(o)!')
   
def lista() :
    print1 = str(input("Digita o login do cliente:"))
    for cliente in clientes:
     if(print1 == cliente[1]):
        print(f'''
      Nome: {cliente[0]}
      login: {cliente[1]}
      senha: {cliente[2]}
      email: {cliente[3]}
      nascimento: {cliente[4]}
      celular: {cliente[5]}
      endereço: {cliente[6]}
      número: {cliente[7]}
      complemento: {cliente[8]}
      bairro: {cliente[9]}
      cidade: {cliente[10]}
      cep: {cliente[11]}
      ref:{cliente[12]}''')
     else:
          print('Cliente não Cadrastado, se deseja cadrastar, retorne ao menu e clique na opçao 1.')
                  

   
def adcionar():
   adcionando =str(input("Informe o Login: "))
   for cliente in clientes:
     if( adcionando == cliente[1]):
      endereço2 = input('Digite a rua: ')
      n2 = input('Digite o número: ')
      complemento2 = input('Digite o complemento: ')
      bairro2 = input('Digite o bairro: ')
      cidade2= input('Digite a cidade: ')
      cep2 = input('Digite o cep: ')
      ref2 = input('Digite um ponto de referência: ')
      usuario1_dados3= ( endereço2, n2, complemento2, bairro2, cidade2, cep2, ref2)
      usuario1.append(usuario1_dados3)
      print(usuario1_dados3)
      print('endereço do cliente cadastrado')
     else:
           print('Cliente não Cadrastado, se deseja cadrastar, retorne ao menu e clique na opçao 1.')
    
def cadrastados():
  for cliente in clientes:
   print(f'''
      Nome: {cliente[0]}
      login: {cliente[1]}''')
      
     

def programa() :

    while True:
        option = menu()
        if option == 1 :
            cadastro()
        if option == 2 :
            adcionar()
        if option == 3 :
            lista()
        if option == 4 :
            cadrastados()
        if option == 0 :
           break

programa()