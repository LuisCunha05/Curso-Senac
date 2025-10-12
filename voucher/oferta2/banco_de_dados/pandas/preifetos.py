import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox


def generate_graphics_from_csv(path: str):
    df = pd.read_csv(path)

    df.set_index('Posição', inplace=True)

    data = df.loc[:, ['Nome', 'Votos']]

    exp = [0.05 if i != 0 else 0.2 for i in range(len(data))]

    #Exibe grafico de pizza
    plt.pie(data.iloc[:, 1], labels=data.iloc[:, 0], explode=exp, autopct='%.2f%%', startangle=85, rotatelabels=True)
    plt.tight_layout()
    plt.show()

    #Exibe grafico de barras
    plt.bar(data.iloc[:, 0], data.iloc[:, 1], color='orange')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':

    generate_graphics_from_csv('csv/cg_prefeitos.csv')

    if(messagebox.askyesno('Exibir para Dourados?', 'Deseja exibir os gráficos a cidade de Dourados?')):
        generate_graphics_from_csv('csv/du_prefeitos.csv')
    
    if(messagebox.askyesno('Exibir para Três lagos?', 'Deseja exibir os gráficos a cidade de Três lagos?')):
        generate_graphics_from_csv('csv/tl_prefeitos.csv')
    
    if(messagebox.askyesno('Exibir para Corumbá?', 'Deseja exibir os gráficos a cidade de Corumbá?')):
        generate_graphics_from_csv('csv/cu_prefeitos.csv')
    
    if(messagebox.askyesno('Exibir para Ponta Porã?', 'Deseja exibir os gráficos a cidade de Ponta Porã?')):
        generate_graphics_from_csv('csv/pp_prefeitos.csv')
