import requests
total = 0
for pag in range(1, 46):
    print (f'Página {pag}...')
    url = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2023&ordem=ASC&pagina={pag}&itens=15'
    resp = requests.get(url).json()

    for x in resp['dados']:
        total = total + x['valorLiquido']
        

print (f'R$ Total = {total:.2f}')
