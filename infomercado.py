import requests as req
import pandas as pd
import plotly.express as px
# import streamlit as st


host = 'https://dadosabertos.ccee.org.br'
api = '/api/3/action/'
conjunto = 'geracao_horaria_fonte_submercado'
limite = 10000
lista_datasets = []
lista_dados = []
conjunto = req.get(host+api+f'package_show?id={conjunto}').json()
resources = conjunto['result']['resources']

for resource in resources:
    print(resource['id'])
    req_next = req.get(host+api+f'datastore_search?resource_id={resource["id"]}&offset=0&limit={limite}').json()
    lista_datasets.append(req_next['result']['records'])
    while (req_next['result']['offset'] + req_next['result']['limit']) < req_next['result']['total']:
        req_next= req.get(host+req_next['result']['_links']['next']).json()
        lista_datasets.append(req_next['result']['records'])

for d in lista_datasets:
    df = pd.DataFrame(d)
    lista_dados.append(df)

ghfs = pd.concat(lista_dados)


