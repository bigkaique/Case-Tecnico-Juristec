

import pandas as pd

# Simulação de dados obtidos de um processo judicial com o que voces me passaram tentei fazer algo simples 
#  nao uso muito pandas mas tentei fazer algo que fosse mais ou menos o que voces me passaram, espero que seja isso mesmo, se tiver algo errado me avisam que e algo que tenho interrece em aplende e me apronfunda mais.
dados_obtidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

# Construir o DataFrame
df = pd.DataFrame(dados_obtidos)

# Eliminar linhas com id vazio
df = df.dropna(subset=['id_processo'])

# Uniformizar o status
df['status'] = df['status'].str.capitalize()

# Simplificar valor_causa
df['valor_causa'] = df['valor_causa'].str.replace('R$', '')
df['valor_causa'] = df['valor_causa'].str.replace('.', '')
df['valor_causa'] = df['valor_causa'].str.replace(',', '.')

# Transformar em número
df['valor_causa'] = pd.to_numeric(df['valor_causa'], errors='coerce')

print(df)
