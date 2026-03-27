requirements:
pandas

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
