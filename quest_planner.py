import datetime

# Estruturas de dados principais
tarefas = []
missoes = []
pontuacao_total = 0

def adicionar_tarefa(nome, horario_inicio, duracao, prioridade):
    global tarefas, missoes
    
    # Verificar conflito de horário
    nova_tarefa = {
        'nome': nome,
        'horario_inicio': horario_inicio,
        'duracao': duracao,
        'prioridade': prioridade,
        'concluida': False
    }
    
    for tarefa in tarefas:
        if verificar_conflito(tarefa, nova_tarefa):
            print(f"Conflito de horário com: {tarefa['nome']}")
            return False
            
    tarefas.append(nova_tarefa)
    
    # Criar missão associada
    nova_missao = {
        'tarefa': len(tarefas) - 1,  # índice da tarefa
        'pontuacao': prioridade * 10
    }
    missoes.append(nova_missao)
    
    return True

def verificar_conflito(tarefa1, tarefa2):
    fim1 = tarefa1['horario_inicio'] + datetime.timedelta(minutes=tarefa1['duracao'])
    fim2 = tarefa2['horario_inicio'] + datetime.timedelta(minutes=tarefa2['duracao'])
    
    return not (fim1 <= tarefa2['horario_inicio'] or fim2 <= tarefa1['horario_inicio'])

def marcar_concluida(indice):
    global tarefas, pontuacao_total
    
    if 0 <= indice < len(tarefas):
        tarefas[indice]['concluida'] = True
        pontuacao_total += missoes[indice]['pontuacao']
        return True
    return False

def visualizar_dia():
    print("\n--- Tarefas do Dia ---")
    for i, tarefa in enumerate(sorted(tarefas, key=lambda x: x['horario_inicio'])):
        status = "✓" if tarefa['concluida'] else " "
        hora_fim = tarefa['horario_inicio'] + datetime.timedelta(minutes=tarefa['duracao'])
        print(f"{i+1}. [{status}] {tarefa['horario_inicio'].strftime('%H:%M')}-{hora_fim.strftime('%H:%M')} | {tarefa['nome']} (Prioridade: {tarefa['prioridade']})")

def visualizar_missoes():
    print("\n--- Missões Diárias ---")
    for i, missao in enumerate(missoes):
        tarefa = tarefas[missao['tarefa']]
        status = "✓" if tarefa['concluida'] else " "
        print(f"{i+1}. [{status}] {tarefa['nome']} - {missao['pontuacao']} pontos")
    
    print(f"\nPontuação Total: {pontuacao_total}")

# Função para popular com dados de exemplo
def popular_exemplos():
    adicionar_tarefa("Reunião com equipe", datetime.datetime(2023, 1, 1, 9, 0), 60, 2)
    adicionar_tarefa("Estudar Python", datetime.datetime(2023, 1, 1, 10, 30), 90, 3)
    adicionar_tarefa("Almoço", datetime.datetime(2023, 1, 1, 12, 30), 60, 1)
    adicionar_tarefa("Beber água", datetime.datetime(2023, 1, 1, 11, 0), 5, 1)
    adicionar_tarefa("Exercícios", datetime.datetime(2023, 1, 1, 7, 30), 30, 2)

# Menu interativo
def menu():
    while True:
        print("\n=== QuestPlanner ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas do Dia")
        print("3. Visualizar Missões")
        print("4. Marcar Tarefa como Concluída")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome da tarefa: ")
            hora = input("Horário de início (HH:MM): ")
            duracao = int(input("Duração (minutos): "))
            prioridade = int(input("Prioridade (1-3): "))
            
            try:
                hora_partes = list(map(int, hora.split(':')))
                horario = datetime.datetime(2023, 1, 1, hora_partes[0], hora_partes[1])
                adicionar_tarefa(nome, horario, duracao, prioridade)
                print("Tarefa adicionada com sucesso!")
            except:
                print("Formato inválido! Use HH:MM")
                
        elif opcao == "2":
            visualizar_dia()
            
        elif opcao == "3":
            visualizar_missoes()
            
        elif opcao == "4":
            visualizar_dia()
            try:
                indice = int(input("Número da tarefa a marcar como concluída: ")) - 1
                if marcar_concluida(indice):
                    print("Tarefa marcada como concluída!")
                else:
                    print("Índice inválido!")
            except:
                print("Digite um número válido!")
                
        elif opcao == "5":
            print("Saindo do QuestPlanner...")
            break
            
        else:
            print("Opção inválida!")

# Execução principal
if __name__ == "__main__":
    print("=== Protótipo QuestPlanner ===")
    print("Um combinado de Planejador de Rotina e Gerador de Missões")
    
    # Popular com alguns exemplos
    popular_exemplos()
    
    # Iniciar menu interativo
    menu()