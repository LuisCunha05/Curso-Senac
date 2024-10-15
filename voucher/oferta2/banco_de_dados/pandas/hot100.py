import pandas as pd
import matplotlib.pyplot as plt

#https://www.kaggle.com/datasets/camnugent/california-housing-prices

df = pd.read_csv('csv/housing.csv')

near_200k = df.query('ocean_proximity == "NEAR BAY" & median_house_value >= 200000.0').sort_values('median_house_value')

#print(near_200k.sort_values('housing_median_age'))
count_near200 = near_200k.housing_median_age.value_counts()
#opa.sort()
#print(*opa.items())

valQ = {}
valQ.update(count_near200.items())


#Exibe grafico de barras
plt.subplot(3,2,1)
plt.bar([str(key) for key in valQ.keys()], valQ.values(), color='orange')
plt.title('Idade das Casas com avalição maior que 200K proximas a orla')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()


inland_200k = df.query('ocean_proximity == "INLAND" & median_house_value >= 200000.0').sort_values('median_house_value')
count_land200 = inland_200k.housing_median_age.value_counts()

valQ = {}
valQ.update(count_land200.items())


#Exibe grafico de barras
plt.subplot(3,2,2)
plt.bar([str(key) for key in valQ.keys()], valQ.values(), color='orange')
plt.title('Idade das Casas com avalição maior que 200K longe da orla')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()


rooms = df.loc[:, ['population', 'housing_median_age']].sort_values('housing_median_age')
plt.subplot(3,2,3)
plt.scatter(rooms.iloc[:, 1], rooms.iloc[:, 0], color='orange')
plt.title('População por idade das casas')
plt.tight_layout()


income = df.loc[:, ['housing_median_age', 'median_income']].sort_values('housing_median_age')
plt.subplot(3,2,4)
plt.scatter(income.iloc[:, 0], income.iloc[:, 1], color='orange')
plt.title('Renda por idade das casas')
plt.tight_layout()


#BAY vs INLAND
bay = df.query('ocean_proximity == "NEAR BAY" & housing_median_age <= 20')
land = df.query('ocean_proximity != "NEAR BAY" & housing_median_age <= 20')

pop_bay = bay.loc[:, ['population']]
pop_land = land.loc[:, ['population']]


bay_l = list(pop_bay.iloc[:, 0].astype(float))
land_l = list(pop_land.iloc[:, 0].astype(float))

data = [(sum(bay_l)), sum(land_l)]
#print(data)

plt.subplot(3,2,5)
plt.pie(data, autopct='%.2f%%', labels=['BAY', 'INLAND'], rotatelabels=True)
plt.title('Divisão da População em terra e Prox. a Orla nos ultimos 20 anos')
plt.tight_layout()
plt.show()
