# -*- coding: utf-8 -*-
import Lib.GetOldTweets.got3 as g

def capturar_old_tweets():
    tweetsCriteria = g.manager.TweetCriteria()
    tweetsCriteria.setQuerySearch("@Asuncionmuni OR @Ferreiromario1")
    tweetsCriteria.setSince("2017-09-01")
    tweetsCriteria.setUntil("2018-02-28")
    tweetsCriteria.setMaxTweets(100)
    tweet_history = g.manager.TweetManager.getTweets(tweetsCriteria)
    print(tweet_history)

capturar_old_tweets()
