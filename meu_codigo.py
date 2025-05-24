import pandas as pd

# Criar DataFrame
dados = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Daniela'],
    'Idade': [28, 34, 25, 40],
    'Salário': [3000, 4500, 2500, 5200]
}

df = pd.DataFrame(dados)
print("DataFrame criado:")
print(df)

# Salvar CSV
df.to_csv('dados_funcionarios.csv', index=False)

# Ler CSV
df_csv = pd.read_csv('dados_funcionarios.csv')
print("\nLendo dados salvos:")
print(df_csv)

# Filtro
print("\nSalário maior que 3000:")
print(df_csv[df_csv['Salário'] > 3000])

# Ordenar
print("\nOrdenado por idade:")
print(df_csv.sort_values(by='Idade'))

# Média
media = df_csv['Salário'].mean()
print(f"\nMédia salarial: R${media:.2f}")

# Adicionar Bônus
df_csv['Bônus'] = df_csv['Salário'] * 0.10
print("\nCom bônus:")
print(df_csv)

# Salvar novo CSV
df_csv.to_csv('dados_funcionarios_com_bonus.csv', index=False)
