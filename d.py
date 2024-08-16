import requests
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
dados = requests.get(url).json()
for d in dados['dados']:
    if d['siglaPartido'] == 'PL' and d ['siglaUf'] == 'SP':
        arquivo = d['nome'] + '.jpg'
        print (arquivo)
        f = open(arquivo, 'wb')
        foto = requests.get(d['urlFoto']).content
        f.write(foto)
        f.close()
