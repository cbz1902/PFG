#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""************************************SE IMPORTAN LAS LIBRERIAS A UTILIZAR********************************************************************************"""
import GetOldTweets3 as g
import re
import csv
from trabajar_archivos import escribir_txt

"""*********************************************DEFINICIONES DE VARIABLES A SER UTILIZADAS*****************************************************************"""
term_busq = '@Telefuturo OR @AsuncionMuni OR @sntcanal9 OR @Ferreiromario1 OR @msaludpy OR @Ops_Paraguay OR @lanacionpy OR @diariocronicapy OR @SenepaParaguay OR @mambiente_py OR @ABCDigital OR #alertacontraelmosquito' #Termino de busqueda
			
exp_reg = '.lluvia.|inund.|.crecid.|.agua.|.servida.|.desag.|.llueve.|.raudal.|.basura.|.recicla.|.desecho.|.vertedero.|.escombro.|.dengue.|.mosquito.|.aedes.|.criadero.|.minga.|.fumiga.|.repelen.|.espiral|.mosquitero.' #expresion regular por medio del cual se filtra los tweets
tweetsCriteria = g.manager.TweetCriteria() #objeto para capturar el tweets
tweets_filtrado = 0
"""*********************************************************************************************************************************************************"""

def capturar_old_tweets_mes(fecha_inicio, fecha_fin,term):
    """FUNCION QUE CAPTURA LOS TWEETS EN BASE AL TERMINO QUE RECIBE, DEVUELVE UNA LISTA CON TODOS LOS TWEETS CAPTURADOS,
    ESTA CONFIGURADO PARA CAPTURAR 6000 TWEETS
    @fecha_inicio : fecha para comenzar la captura
    @fecha_fin: fecha a finalizar la captura
    @term: termino de busquea de los tweets
    """
    print("########### CAPTURANDO TWEETS ###########")
    tweetsCriteria.setQuerySearch(term)
    tweetsCriteria.setSince(fecha_inicio)
    tweetsCriteria.setUntil(fecha_fin)
    tweetsCriteria.setMaxTweets(500000000)
    tweet_history = g.manager.TweetManager.getTweets(tweetsCriteria)
    return tweet_history

def filtrar_tweets(tweets):
    """FUNCIONQ QUE FILTRA LOS TWEETS QUEE NECESARIOS EN BASE A LA EXPRESION REGULAR
    @tweets: Tweets que fueron capturados
    """
    global tweets_filtrado
    lista = []
    for i in range(0,len(tweets)):        
        if re.match(exp_reg, str(tweets[i].text),flags=re.IGNORECASE) != None:
            lista.append(str(tweets[i].text)+'\n')
            tweets_filtrado +=1
    return lista

if __name__ == "__main__":    
    old_tweets = capturar_old_tweets_mes("2017-09-01","2018-03-30",term_busq)
    escribir_txt('data/tweets_capturados.txt',filtrar_tweets(old_tweets))
    print("########### "+str(tweets_filtrado)+" FILTRADOS ###########")
    print("########### TXT CREADO CON EXITO ###########")