import urllib.request
import json

def resultado_filmes(tipo):
    if tipo == 'Populares':
        url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13'
    elif tipo == 'Animação':
        url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=3ddc9b92db4de6c6559569c67bd88a13'
    elif tipo == '2010':
        url = 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average&api_key=3ddc9b92db4de6c6559569c67bd88a13'

    response = urllib.request.urlopen(url)

    dados = response.read()

    dados_json = json.loads(dados)
    return dados_json['results']
