import pandas as pd

#print(pd.__version__)

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

#print(df.head()) printa começo

#print(df.info()) mostra tipo de dados das colunas

#print(df.set_index('PassengerId'))
df.set_index('PassengerId', inplace=True) # muda qual id utiliza
#print(df.set_index('Name'))

#print(df.values)

#print(df.loc[[1,2], ['Name', 'Sex', 'Age']]) formata a exibição de um pedaço das colunas

#print(df.loc[10:20])

#print(df.loc[10:20:2])

#print(df.loc[:25, ['Name', 'Sex', 'Age']])

#print(df.query('Age > 20').head())

#print(df.query('Age > 20 & Sex=="male"').head())

#print(df.query('Age > 40 | Sex=="male"').head())
#df.loc[:250]
#new_df = df.dropna() # Remove valores vazios

#new_df = df.copy()
#new_df['Cabin'].fillna('F4', inplace=True)
#print(new_df.loc[:100])
#new_df.dropna(inplace=True)
#print(new_df.loc[:100])

#df.to_csv('dataset.cvs', sep=',', index=False, encoding='utf-8-sig')


#---------criança----------
#child = df.query('Age < 10 & Survived==1')
#print(child.count())
#child.to_csv('criancas.cvs', sep=',', index=False, encoding='utf-8-sig')

#---------mulheres----------
#mulheres = df.query('Sex=="female" & Survived==1')
#print(mulheres[:])
#mulheres.to_csv('mulheres.cvs', sep=',', index=False, encoding='utf-8-sig')

#---------homens----------
#homens = df.query('Sex=="male" & Survived==1')
#print(homens[:])
#homens.to_csv('homens.cvs', sep=',', index=False, encoding='utf-8-sig')

#---------homens----------
#idoso = df.query('Age > 50 & Survived==1')
#print(idoso[:])
#idoso.to_csv('idoso.cvs', sep=',', index=False, encoding='utf-8-sig')

#---------crianca menina----------
#menina = df.query('Age < 12 & Sex=="female" & Survived==1')
#print(menina[:])
#menina.to_csv('menina.cvs', sep=',', index=False, encoding='utf-8-sig')