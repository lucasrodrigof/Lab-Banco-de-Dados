import requests
url = 'https://pokeapi.co/api/v2/ability/battle-armor'
dados = requests.get(url).json()

for x in dados ['effect_entries']:
    if x ['language']['name']== 'en':
        print(x['short_effect'])

for x in dados['pokemon']:
    print (x['pokemon']['name'])
