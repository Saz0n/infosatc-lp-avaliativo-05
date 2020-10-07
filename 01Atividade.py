contador = 0
saldo_conta = 0

import re
lista_nome=[]
lista_sobrenome=[]
lista_cpf=[]
lista_endereco= []
lista_numero=[] 
lista_senha = [] 
lista_email = []

def caracterEspecial(text):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
    if(regex.search(text) == None):
        return 1
    else:
        return 0

def cadastro():
    escolha_cadastro = 0
    
    while ( escolha_cadastro == 0):
        
        
       
        lista_nome.append(input ("Insira seu nome:"))  
        print ("O nome cadastro foi:",lista_nome[contador])
        while (len(lista_nome[contador])<3):
            print("O nome precisar ter pelo menos tres letras para ser registrado")
            del(lista_nome[contador])            
            lista_nome.append (input ("Insira seu nome novamente:")) 
            print ("O nome cadastrado foi:",lista_nome [contador])
            
        
       
        lista_sobrenome.append (input ("Insira seu sobrenome:"))  
        print ("o sobrenome cadastrado:",lista_sobrenome[contador])
        while (len(lista_sobrenome[contador])<3):
            print("O sobrenome precisar ter pelo menos tres letras para ser registrado")
            del(lista_sobrenome[contador])
            lista_sobrenome.append (input ("Insira seu sobrenome novamente:")) 
            print("Esse foi o sobrenome digitado", lista_sobrenome[contador])

              
        lista_cpf.append(input ("Insira seu cpf:"))  
        print("Esse foi o cpf digitado", lista_cpf[contador])
        
        lista_endereco.append(input("insira seu endereço:"))
        print("Esse foi o endereço digitado", lista_endereco[contador])
        
        contador2=0
        while(contador2==0):
            lista_email.append(input("Digite seu email, não se esqueca do @:"))       
            if "@" in lista_email[contador]:
                print("Esse foi o E-mail digitado:", lista_email[contador])  
                contador2=1            
            else:
                del(lista_email[contador])
        

        lista_numero.append(input("Digite seu numero para contato:"))
        print("O numero digitado foi esse:", lista_numero[contador])
        
        lista_senha.append(input("Digite sua senha, ela precisa conter caracteres especiais e numeros:"))
        contador2=caracterEspecial(lista_senha[contador])

        while (contador2 == 1):
            del(lista_senha[contador])
            lista_senha.append(input("Digite sua senha, ela precisa conter caracteres especiais e numeros:"))
            print("Senhas nessesitam de caracteres especiais e senha por favor digite sua senha novamente:")
            contador2=caracterEspecial(lista_senha[contador])
        
        contador+1 
        escolha_cadastro = int(input("Digite 0 para cadastrar mais uma pessoa e 1 não cadastrar:"))  
        
        
            


def operaçoes ():
    caixa = 1
    conta_transferencia = 0
    sacar=0
    saldo_conta= 0
    while caixa == 1:
        print("Digite 1 para depositar")
        print("Digite 2 para sacar")
        print("Digite 3 para conferir saldo")
        print("Digite 4 para transferir")
        print("Digite 5 para encerrar conta")
    
        escolha = int(input("Escolha a operação desejada:"))
    
    
        if escolha == 1:
            depositar = int(input("Digite o quanto em RS voce deseja despositar na sua conta:"))
            while depositar < 0:
                depositar = int(input("Digite o quanto em RS voce deseja despositar na sua conta apenas numeros postivos:"))
                print("Seu saldo atual é de", saldo_conta)
            else:
                saldo_conta = depositar + saldo_conta
                print("Seu saldo atual é de", saldo_conta)
    
        if escolha == 2:
            sacar = float(input("Digite o quanto em RS voce deseja sacar:"))
            while sacar > saldo_conta:
                print("Voce não possui saldo suficiente para esse saque:")
                escolha = int(input("Escolha outra operação desejada:"))
            else:
                saldo_conta = saldo_conta - sacar
                print("Seu saldo atual é de", saldo_conta)
    
        if escolha == 3:
            print("Seu saldo atual é de", saldo_conta)
    
        if escolha == 4:
            conta_transferencia = int(input("Digite o numero da conta que voce deseja tranferir:"))
            transferencia = int(input("Digite o valor da transferencia:"))
            if transferencia > saldo_conta:
                print("voce não possui saldo suficiente para essa tranferencia:")
            else:

                saldo_conta= saldo_conta - transferencia 
                conta_transferencia = conta_transferencia + transferencia 
                print("tranferencia concluida com succeso:")
                print("Seu saldo atual é de:", saldo_conta)
    
        if escolha == 5:
            print("Operação encerrada")
            caixa = 0
cadastro()
            
def atualizacao():
    escolha_02=0
    atualização_cadastro = 0
    while (atualização_cadastro == 0):
    
    
        print("Digite 1 consultar um cliente")
        print("Digite 2 consultar lista de clientes")
        print("Digite 3 deletar um cliente")
        print("Digite 4 atualizar dados de um cliente específico")
        print("Digite 5 para encerrar")
        
        escolha_02 = int(input("escolha a operação desejada:"))
        if escolha_02 == 1:
            n_cliente= int(input("Qual o numero do cliente no cadastro:"))
            print("Nome cliente:",lista_nome[n_cliente])  
            print("Sobrenome cliente:", lista_sobrenome[n_cliente])
            print("Cpf cliente:", lista_cpf[n_cliente])
            print("E-mail do cliente:", lista_email[n_cliente])
            print("Endereço do cliente", lista_endereco[n_cliente])
            print("Numero do cliente:", lista_numero[n_cliente])
            print ("Senha do cliente",lista_senha[n_cliente])
        
        if escolha_02 ==2:
            print("Lista de clientes", lista_nome)
        
        if escolha_02 == 3:
            n_cliente_exclu = int(input("Escreva o numero do cliente que voce deseja excluir:"))
            del(lista_nome[n_cliente_exclu])
            del(lista_sobrenome[n_cliente_exclu])
            del(lista_cpf[n_cliente_exclu])
            del(lista_email[n_cliente_exclu])
            del(lista_endereco[n_cliente_exclu])
            del(lista_numero[n_cliente_exclu])
            del(lista_senha[n_cliente_exclu])
        
        if escolha_02 == 4:
            atualizar_cadastro = 0
            n_cliente=int(input("Escreva o numero de cadastro do cliente que voce deseja modficar:"))
            
            lista_nome.insert(n_cliente,(input("Insira seu nome:")))  
                
            while (len(lista_nome[n_cliente])<3):
                print("O nome precisar ter pelo menos tres letras para ser registrado")
                del(lista_nome[n_cliente])            
                lista_nome.insert(n_cliente,(input ("Insira seu nome novamente:"))) 
                    
            
        
       
            lista_sobrenome.insert(n_cliente,(input ("Insira seu sobrenome:")))  
            print ("o sobrenome cadastrado:",lista_sobrenome[n_cliente])
            while (len(lista_sobrenome[n_cliente])<3):
                print("O sobrenome precisar ter pelo menos tres letras para ser registrado")
                del(lista_sobrenome[n_cliente])
                lista_sobrenome.insert(n_cliente,(input ("Insira seu sobrenome novamente:"))) 
                print("Esse foi o sobrenome digitado", lista_sobrenome[n_cliente])

              
            lista_cpf.insert(n_cliente,(input ("Insira seu cpf:"))) 
            print("Esse foi o cpf digitado", lista_cpf[n_cliente])
        
            lista_endereco.insert(n_cliente,(input("insira seu endereço:")))
            print("Esse foi o endereço digitado", lista_endereco[n_cliente])
        
        
            contador3=0
            while(contador3==0):
                lista_email.append(input("Digite seu email, não se esqueca do @:"))       
                if "@" in lista_email[contador]:
                    print("Esse foi o E-mail digitado:", lista_email[contador])  
                    contador3=1            
                else:
                    del(lista_email[contador])
        

            lista_numero.insert(n_cliente,(input("Digite seu numero para contato:")))
            print("O numero digitado foi esse:", lista_numero[n_cliente])
        
            
            lista_senha.append(input("Digite sua senha, ela precisa conter caracteres especiais e numeros:"))
            contador2=caracterEspecial(lista_senha[contador])

            while (contador2 == 1):
                del(lista_senha[contador])
                lista_senha.append(input("Digite sua senha, ela precisa conter caracteres especiais e numeros:"))
                print("Senhas nessesitam de caracteres especiais e senha por favor digite sua senha novamente:")
                contador2=caracterEspecial(lista_senha[contador])

            atualizar_cadastro = int(input("Digite 0 para atualizar mais um cadastro e 1 não:"))

        if escolha_02 == 5:
            atualização_cadastro= atualização_cadastro + 1

atualizacao()     


            