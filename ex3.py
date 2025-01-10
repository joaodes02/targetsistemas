import json

def calcular_faturamento(faturamento_diario):
    faturamento_com_dados = [f['valor'] for f in faturamento_diario if f['valor'] > 0]
    
    if not faturamento_com_dados:
        return "Não houve faturamento em nenhum dia do mês."
    
    menor_faturamento = min(faturamento_com_dados)
    maior_faturamento = max(faturamento_com_dados)
    
    media_faturamento = sum(faturamento_com_dados) / len(faturamento_com_dados)
    
    dias_superior_media = len([f for f in faturamento_com_dados if f > media_faturamento])
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_superior_media": dias_superior_media
    }

_json = 'dados.json'

with open(_json, 'r') as file:
    dados = json.load(file)

resultado = calcular_faturamento(dados)

print(f"Menor faturamento: {resultado['menor_faturamento']}")
print(f"Maior faturamento: {resultado['maior_faturamento']}")
print(f"Dias com faturamento superior à média: {resultado['dias_superior_media']}")
