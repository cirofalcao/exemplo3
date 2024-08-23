# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Exibir tarefas")
    print("4. Sair")

# Função para adicionar tarefa
def adicionar_tarefa(lista):
    tarefa = input("Digite a tarefa: ")
    lista.append(tarefa)
    print("Tarefa adicionada.")

# Função para remover tarefa
def remover_tarefa(lista):
    tarefa = input("Digite a tarefa para remover: ")
    if tarefa in lista:
        lista.remove(tarefa)
        print("Tarefa removida.")
    else:
        print("Tarefa não encontrada.")

# Função para exibir tarefas
def exibir_tarefas(lista):
    if lista:
        print("\nTarefas:")
        for tarefa in lista:
            print(f"- {tarefa}")
    else:
        print("Nenhuma tarefa na lista.")

# Programa principal
tarefas = []

while True:
    exibir_menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        adicionar_tarefa(tarefas)
    elif escolha == '2':
        remover_tarefa(tarefas)
    elif escolha == '3':
        exibir_tarefas(tarefas)
    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")