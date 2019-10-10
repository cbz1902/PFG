#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy, os
import datetime
from credencial import credenciales

#objeto que contiene las claves de acceso
miCredencial = credenciales()

# API de tweetpy para coger datos de twitter
auth = tweepy.OAuthHandler(miCredencial.get_consumer_key(), miCredencial.get_consumer_secret())
auth.set_access_token(miCredencial.get_access_token(), miCredencial.get_access_token_secret())
api = tweepy.API(auth)

# Obtiene lo que se quiere buscar
print('El siguiente script permite ingresar un termino de busqueda y buscarlo en Twitter, pueden ser hashtags\n')
terBusqueda = (input('Ingrese el termino de busqueda :\n'))
terBusqueda.encode('UTF-8')

# Se obtiene el place_id del Paraguay
places = api.geo_search(query="PARAGUAY")
place_id = places[0].id
SearchQuery = 'place:'+place_id+' '+terBusqueda

try:
    # Crea el set de tweets dependiendo de lo que se busco
    sQuery = tweepy.Cursor(api.search, q= SearchQuery, show_user=True, lang = 'es').items(10)
    # Comprobacion de si ya existe ese archivo
    datasetName = terBusqueda.replace(" ", "-")  # Remplaza un espacio por un guion de ser necesario

    #Itero los resultados de la busqueda y creo los datos correspondientes
    for tweet in sQuery:
        terBusqueda = terBusqueda.replace(" ", "-")  # Remplaza un espacio por un guion de ser necesario
        print(tweet.text)


except tweepy.TweepError:
    print('You have an error on your auth, please check your keys')
