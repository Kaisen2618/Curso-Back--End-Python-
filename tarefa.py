#inicializar a lista de tarefas vazia

lista_de_tarefas = {}
          
#função para adicionar uma tarefa á lista                                                               

def adicionarTarefa(tarefa):
 lista_de_tarefas.append(tarefa)

#função para remover uma tarefa da lista

def remover_tarefa(indice):
    
    if 0 <= indice < len:

          del  lista_de_tarefas[indice]
    else:
          print("indice inválido. tarefa removida")
          
#função para listar todas as tarefas da lista        

def listar_tarefa():
    
    print("Lista de Tarefas")
    
if lista_de_tarefas:
        for indice, tarefa in enumerate(lista_de_tarefas):
            print("{indice}: {tarefa}")
        else:
            print("A lista de tarefa está vazia")
    
    #loop prinipal do processo
    
while True:
    
     print("opções")
     print("1, adicionar tarefa")
     print("2, remover tarefa")
     print("3, listar tarefa")
     print("4, Sair")
    
     escolha = input("escolha uma opção (1/2/3/4)")
    
     if escolha == "1":
        
        nova_tarefa = input("digite uma nova tarefa")
        adicionarTarefa(nova_tarefa)
    
     elif escolha == "2":
         
        indice_remove = int(input("Digite o indice de tarefa a ser removido"))
        remover_tarefa(indice_remove)
        
     elif escolha == "3":
         
         listar_tarefa()
         
     elif escolha == "4":
         print("programa encerrado")
         
            
         
         
        