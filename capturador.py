#!/usr/bin/python
# -*- coding: utf-8 -*-

import GetOldTweets3 as g
import  re

def capturar_old_tweets():
    tweetsCriteria = g.manager.TweetCriteria()
    tweetsCriteria.setQuerySearch("@AsuncionMuni OR @ferreiromario1 OR @msaludpy")
    tweetsCriteria.setSince("2017-09-01")
    tweetsCriteria.setUntil("2018-03-30")
    tweetsCriteria.setMaxTweets(200)
    tweet_history = g.manager.TweetManager.getTweets(tweetsCriteria)
    filtrar_tweets(tweet_history)

def buscar(patrones, texto):
    list = []
    for patron in patrones:
        print(re.match(patron, texto))
    return list

def filtrar_tweets(tweets):

    exp_agua = ['lluvia*','inundacion*','crecida*','agua*','servida*','desag*','llueve','raudal*']
    exp_basura = ['basura*','recicla*','desecho','toxico','vertedero*','escombro*']
    exp_dengue = ['dengue','mosquito','aedes','criadero*','minga*','fumiga*']
    exp_proteccion = ['repelen*','espiral','mosquiter*']

    for i in range(0,len(tweets)):
        try:
            print(str(tweets[i].text))
        except:
            pass
            

capturar_old_tweets()
