import os
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
#Limpando o terminal 
os.system('clear')

saldo =0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
saque = 0
deposito = 0

while True:
    opcao = input(menu)

    if opcao == "d" or opcao =="D":
        #Limpando o terminal 
        os.system('clear')
        print("Deposito")
        deposito = float(input("Digite o valor que deseja depositar "))
        if deposito > 0:
            
            print(f"O valor de R$ {deposito}, foi depositado com sucesso")
            print (f"Seu saldo é de R$ {saldo+deposito}")
            extrato +="\n"
            extrato += f"  Saldo antes -------------------- R$ {saldo:.2f}\n"     
            saldo   += deposito      
            extrato += f"  Deposito realizado no valor de - R$ {deposito:.2f}\n"
            extrato += f"  Saldo depois ------------------- R$ {saldo:.2f}\n"         
        else:
            #Limpando o terminal 
            os.system('clear')
            print("Verifique o valor que deseja depoistar")
    elif opcao =="s" or opcao =="S":
        #Limpando o terminal 
        os.system('clear')
        print("Saque")
        #print(f"Número de saques {numero_saque}")
        if numero_saque < LIMITE_SAQUES:
            saque = float(input("Informe o valor que deseja sacar"))
            if(saque > saldo):
                #Limpando o terminal 
                os.system('clear')
                print(f"Valor solicitado é maior do que saldo R$ {saldo} em conta")
            elif saque > limite:
                #Limpando o terminal 
                os.system('clear')
                print(f"Valor R${saque:.2f} solicitado é maior do que o limite R$ {limite:.2f} por saque")
            else:
                #Limpando o terminal 
                os.system('clear')
                print(f"Saque realizado com sucesso, seu saldo em conta é de R$ {saldo - saque:.2f}")
                numero_saque = numero_saque+1
                extrato +="\n"
                extrato += f"  Saldo  antes ------------------- R$ {saldo:.2f}\n"     
                saldo   -= saque       
                extrato += f"  Saque  realizado no valor de --- R$ {saque:.2f}\n"
                extrato += f"  Saldo  depois ------------------ R$ {saldo:.2f}\n" 
        else:
            #Limpando o terminal 
            os.system('clear')
            print("Você já sacou 3 vezes hoje, aguarde 24 horas para novos saque")    
    elif opcao == "e" or opcao =="E":
        #Limpando o terminal 
        os.system('clear')
        print("Extrato")
       
        for numero in range(0,int(50)):
            print("_",end="")
        print()
        bem_vindo="Seja bem-vindo(a)"
        bem_vindo = bem_vindo.center(50)
        print(bem_vindo.upper(),end="| \n")
        for numero in range(0,int(50)):
            print("_",end="")
                
        print(f"\nSeu saldo atual é de  -------------------- R$ {saldo:.2f}")
        print (extrato)
    elif opcao == "q" or opcao =="Q":
        #Limpando o terminal 
        os.system('clear')
        print("Saiu do sistema, obrigado por utilizar nossos serviços")
        break
    else:
        #Limpando o terminal 
        os.system('clear')
        print("Operação inválida, por favor selecione novamente a operação desejada.")
