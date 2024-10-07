import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('csv/nba_seasons.csv')

df.rename(columns={'Unnamed: 0':'player_id'}, inplace=True )
df.set_index('player_id', inplace=True)
print(df.head())

player_height = df.loc[0:11145, ['player_height']]
player_weight = df.loc[0:11145, ['player_weight']]
age = df.loc[0:11145, ['age']]

print(age['age'][:])
salt = []
for index in range(len(player_weight)):
    weight = player_weight.iloc[index, 0]
    player_age = age.iloc[index, 0]
    salt.append(weight * 1_000_000 * (player_age / 10) )


#x = np.array(player_weight)
#y = np.array(player_height)


#print(player_height)
#print(player_weight)

plt.xlabel(u'Peso')
plt.ylabel(u'Altura')
plt.title('NBA players: Peso x Altura')

#coef = np.polyfit(player_weight,player_height,1)
#poly1d_fn = np.poly1d(coef) 
# poly1d_fn is now a function which takes in x and returns an estimate for y
#plt.scatter(player_weight, player_height, color='purple')
plt.scatter(player_weight, salt)

#a = (10, 20, 30, 15, 24, 5, 19)
#exp = (0.1, 0.1, 0.1, 0.4, 0.1,0.1, 0.1)
#labels = ('a','b','c','d','e','f','g')
#
#plt.pie(a, explode=exp, labels=labels, autopct='%.2f%%', shadow=True)

plt.show()




#---------criança----------
#child = df.query('Age < 10 & Survived==1')
#print(child.count())
#child.to_csv('criancas.cvs', sep=',', index=False, encoding='utf-8-sig')