import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv/vereador_cg_2024.csv')

df.set_index('Posição', inplace=True)

#print(df.head())

data = df.loc[:, ['Nome', 'Votos']]

exp = [0.1 if i != 0 else 0.3 for i in range(len(data))]

plt.pie(data.iloc[:, 1], labels=data.iloc[:, 0], explode=exp, autopct='%.2f%%', startangle=85)

plt.show()

plt.bar(data.iloc[:, 0], data.iloc[:, 1], color='orange')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()