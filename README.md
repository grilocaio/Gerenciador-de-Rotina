# 📅 Gerenciador de Rotina (Rotina+ & QuestPlanner)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/CLI-Terminal_App-222222?style=for-the-badge&logo=gnometerminal&logoColor=white" alt="CLI" />
  <img src="https://img.shields.io/badge/Persistência-CSV-16A34A?style=for-the-badge" alt="CSV" />
</p>

> Sistema de linha de comando (CLI) desenvolvido em **Python** que combina **planejamento de rotina diária** com **gamificação por missões e pontuação**, projetado para estimular a produtividade e o cumprimento de metas diárias sem conflitos de horário.

---

## 📌 Funcionalidades Principais

- **📋 Cadastro de Tarefas com Detecção de Conflitos**:
  - Validação de formato de horário (`HH:MM`) e níveis de prioridade (`baixa`, `média`, `alta` ou escala `1–3`).
  - Verificação automática de sobreposição de horários, impedindo que duas tarefas pendentes ocupem o mesmo intervalo.
- **🎯 Gerador de Missões Diárias Gamificadas**:
  - Sorteio dinâmico de missões saudáveis e produtivas sem repetição no mesmo dia (ex.: *Beber 2L de água*, *Estudar 30 minutos*, *Organizar a mesa de estudos*, *Ler 10 páginas de um livro*).
- **🏆 Sistema de Pontuação (XP)**:
  - Ao concluir tarefas da rotina ou missões diárias, o usuário acumula pontos proporcionais à prioridade da atividade.
- **💾 Persistência Automática em Arquivos CSV**:
  - Todas as tarefas (`tarefas.csv`), missões geradas (`missoes.csv`) e pontuação acumulada (`pontuacao.csv`) são salvas e recarregadas automaticamente entre sessões.

---

## 📂 Estrutura do Repositório

```text
Gerenciador-de-Rotina/
├── main.py              # Versão completa (Rotina+) com persistência automática em CSV
├── quest_planner.py     # Protótipo QuestPlanner com cálculo de duração (timedelta) e conflito de intervalos
└── README.md            # Documentação do sistema
```

---

## 🚀 Como Executar

### Pré-requisitos
- **Python 3.8+** instalado (utiliza apenas bibliotecas nativas: `csv`, `datetime`, `random`, `os`).

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/grilocaio/Gerenciador-de-Rotina.git

# 2. Acesse a pasta do projeto
cd Gerenciador-de-Rotina

# 3. Execute o sistema principal (com salvamento em CSV)
python main.py

# Ou execute o protótipo de intervalos de tempo (QuestPlanner)
python quest_planner.py
```

---

## 🖥️ Exemplo de Uso no Terminal

```text
📋 MENU ROTINA+
1 - Cadastrar tarefa
2 - Visualizar rotina
3 - Gerar missão do dia
4 - Marcar tarefa/missão como concluída
5 - Ver pontuação
6 - Sair

📅 ROTINA DO DIA:
[✅] 07:30 - Exercícios (média)
[⏳] 09:00 - Reunião com equipe (alta)
[⏳] 10:30 - Estudar Python (alta)

🎯 MISSÕES DO DIA:
[✅] Beber 2L de água (+10 pts)
[⏳] Ler 10 páginas de um livro (+10 pts)
```

---

## 👨‍💻 Autor

Desenvolvido por **Caio Grilo**  
- GitHub: [@grilocaio](https://github.com/grilocaio)
- LinkedIn: [Caio Grilo](https://www.linkedin.com/in/caio-grilo/)
