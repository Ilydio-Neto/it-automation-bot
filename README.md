# it-automation-bot
Bot de automação para tarefas de TI corporativa como:  criação de usuários, reset de senha, monitoramento e geração de relatórios.
Como rodar:
cd app

# Criar usuário
python main.py --create-user maria maria@email.com

# Resetar senha
python main.py --reset-password maria

# Monitorar serviços
python main.py --monitor

# Gerar relatório
python main.py --report ../data/users_report.csv
