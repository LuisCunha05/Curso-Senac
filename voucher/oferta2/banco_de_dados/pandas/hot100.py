import pandas as pd
import matplotlib.pyplot as plt

#https://www.kaggle.com/datasets/camnugent/california-housing-prices

df = pd.read_csv('csv/housing.csv')

print(df.loc[-10:])