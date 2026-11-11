import csv
import random
from datetime import datetime
import os

# Constantes dos arquivos
ARQ_TAREFAS = "tarefas.csv"
ARQ_MISSOES = "missoes.csv"
ARQ_PONTUACAO = "pontuacao.csv"

# Dados em memória
tarefas = []
missoes_geradas = []
pontuacao_total = 0

missoes_disponiveis = [
    "Beber 2L de água",
    "Estudar 30 minutos",
    "Organizar a mesa de estudos",
    "Fazer uma pausa de 5 minutos",
    "Escrever 3 metas para hoje",
    "Ler 10 páginas de um livro"
]

def validar_horario(horario):
    try:
        datetime.strptime(horario, "%H:%M")
        return True
    except ValueError:
        return False

def validar_prioridade(prioridade):
    return prioridade in ["baixa", "média", "alta"]

def carregar_dados():
    global tarefas, missoes_geradas, pontuacao_total

    if os.path.exists(ARQ_TAREFAS):
        with open(ARQ_TAREFAS, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            tarefas = [
                {"nome": row["nome"], "horario": row["horario"], "prioridade": row["prioridade"], "concluida": row["concluida"] == "True"}
                for row in reader
            ]

    if os.path.exists(ARQ_MISSOES):
        with open(ARQ_MISSOES, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            missoes_geradas = [
                {"descricao": row["descricao"], "pontuacao": int(row["pontuacao"]), "concluida": row["concluida"] == "True"}
                for row in reader
            ]

    if os.path.exists(ARQ_PONTUACAO):
        with open(ARQ_PONTUACAO, encoding='utf-8') as f:
            pontuacao_total = int(f.read().strip())

def salvar_dados():
    with open(ARQ_TAREFAS, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "horario", "prioridade", "concluida"])
        writer.writeheader()
        writer.writerows(tarefas)

    with open(ARQ_MISSOES, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["descricao", "pontuacao", "concluida"])
        writer.writeheader()
        writer.writerows(missoes_geradas)

    with open(ARQ_PONTUACAO, "w", encoding='utf-8') as f:
        f.write(str(pontuacao_total))

def cadastrar_tarefa():
    nome = input("Nome da tarefa: ").strip()

    while True:
        horario = input("Horário (HH:MM): ").strip()
        if not validar_horario(horario):
            print("❌ Horário inválido. Tente novamente.")
            continue
        conflito = next((t for t in tarefas if t["horario"] == horario and not t["concluida"]), None)
        if conflito:
            print("⚠️ Já existe uma tarefa não concluída nesse horário!")
            continue
        break

    while True:
        prioridade = input("Prioridade (baixa/média/alta): ").strip().lower()
        if validar_prioridade(prioridade):
            break
        print("❌ Prioridade inválida. Tente novamente.")

    tarefas.append({"nome": nome, "horario": horario, "prioridade": prioridade, "concluida": False})
    salvar_dados()
    print("✅ Tarefa cadastrada!")

def visualizar_rotina():
    if not tarefas:
        print("📭 Nenhuma tarefa cadastrada.")
        return
    print("\n📅 ROTINA DO DIA:")
    for t in sorted(tarefas, key=lambda x: x["horario"]):
        status = "✅" if t["concluida"] else "⏳"
        print(f"[{status}] {t['horario']} - {t['nome']} ({t['prioridade']})")

    if missoes_geradas:
        print("\n🎯 MISSÕES DO DIA:")
        for m in missoes_geradas:
            status = "✅" if m["concluida"] else "⏳"
            print(f"[{status}] {m['descricao']} (+{m['pontuacao']} pts)")

def gerar_missao():
    if len(missoes_geradas) >= len(missoes_disponiveis):
        print("✔️ Todas as missões já foram geradas.")
        return

    while True:
        desc = random.choice(missoes_disponiveis)
        if desc not in [m["descricao"] for m in missoes_geradas]:
            nova = {"descricao": desc, "pontuacao": 10, "concluida": False}
            missoes_geradas.append(nova)
            salvar_dados()
            print(f"🎯 Missão gerada: {desc}")
            break

def marcar_concluida():
    global pontuacao_total
    print("\n1 - Marcar tarefa\n2 - Marcar missão")
    escolha = input("Escolha: ").strip()

    if escolha == "1":
        if not tarefas:
            print("❌ Nenhuma tarefa cadastrada.")
            return
        for i, t in enumerate(tarefas):
            status = "✅" if t["concluida"] else "⏳"
            print(f"{i+1} - [{status}] {t['nome']}")

        while True:
            entrada = input("Número da tarefa (ou 'cancelar'): ").strip()
            if entrada.lower() == "cancelar":
                return
            if entrada.isdigit():
                i = int(entrada) - 1
                if 0 <= i < len(tarefas):
                    if not tarefas[i]["concluida"]:
                        tarefas[i]["concluida"] = True
                        pontuacao_total += 10
                        salvar_dados()
                        print("✅ Tarefa concluída!")
                    else:
                        print("⚠️ Já estava concluída.")
                    return
            print("❌ Entrada inválida. Tente novamente.")

    elif escolha == "2":
        if not missoes_geradas:
            print("❌ Nenhuma missão gerada.")
            return
        for i, m in enumerate(missoes_geradas):
            status = "✅" if m["concluida"] else "⏳"
            print(f"{i+1} - [{status}] {m['descricao']}")

        while True:
            entrada = input("Número da missão (ou 'cancelar'): ").strip()
            if entrada.lower() == "cancelar":
                return
            if entrada.isdigit():
                i = int(entrada) - 1
                if 0 <= i < len(missoes_geradas):
                    if not missoes_geradas[i]["concluida"]:
                        missoes_geradas[i]["concluida"] = True
                        pontuacao_total += missoes_geradas[i]["pontuacao"]
                        salvar_dados()
                        print("✅ Missão concluída!")
                    else:
                        print("⚠️ Já estava concluída.")
                    return
            print("❌ Entrada inválida. Tente novamente.")
    else:
        print("❌ Opção inválida.")

def ver_pontuacao():
    print(f"🏆 Pontuação total: {pontuacao_total} pontos")

def resetar_dia():
    global tarefas, missoes_geradas
    confirmacao = input("⚠️ Tem certeza que deseja apagar todas as tarefas e missões? (s/n): ").strip().lower()
    if confirmacao == 's':
        tarefas = []
        missoes_geradas = []
        salvar_dados()
        print("🔄 Dia resetado com sucesso!")
    else:
        print("❌ Operação cancelada.")

def menu():
    carregar_dados()
    while True:
        print("\n📌 MENU ROTINA+")
        print("1 - Cadastrar tarefa")
        print("2 - Visualizar rotina")
        print("3 - Gerar missão do dia")
        print("4 - Marcar tarefa/missão como concluída")
        print("5 - Ver pontuação")
        print("6 - Resetar dia")
        print("7 - Sair")

        op = input("Escolha uma opção: ").strip()
        if op == "1":
            cadastrar_tarefa()
        elif op == "2":
            visualizar_rotina()
        elif op == "3":
            gerar_missao()
        elif op == "4":
            marcar_concluida()
        elif op == "5":
            ver_pontuacao()
        elif op == "6":
            resetar_dia()
        elif op == "7":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida!")

menu()