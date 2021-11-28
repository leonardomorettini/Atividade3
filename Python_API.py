# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 16:51:23 2021

@author: Leopardo
"""

import pandas as pd
import requests
#Biblioteca para criar os gráficos
import matplotlib.pyplot as plt
#URL base de dados do governo
url = 'https://dados.antt.gov.br/dataset/a133da64-1e03-4832-909d-e1eb835eec2e/resource/d46bbb49-95f3-44b0-bb9a-0ce095746bbe/download/investimentos.json'
#passando a URL e recebendo um Json
resp = requests.get(url).json()
df = pd.json_normalize(resp["investimentos"])
data_frame= pd.read_json(url)
print(df)
print(type(df))
#to numeric
df["valor"] = pd.to_numeric(df["valor"])
#Maiores investimentos
df2= df.groupby(['concessionaria','ano','valor'])['valor'].max().sort_values(ascending = False).head(2)
print(df2)
#Maiores velhos
df3= df.groupby(['concessionaria','ano','valor'])['ano'].min().sort_values(ascending = False).head(2)
print(df3)

# valor medio investido por concessionaria
fig, ax = plt.subplots(figsize=(40,7))
df.groupby('concessionaria').mean().plot.barh()