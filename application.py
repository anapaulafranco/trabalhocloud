# coding=utf-8
import sys
from flask import Flask
import tweepy
import time
import json

application = Flask(__name__)


# print(phrase_to_search);

consumer_key = 'hopVGo63q2B1HFw1eGy8h23nZ'
consumer_secret = 'mpgx75J0UFhCd5c9GSS0VmShoUAc2IIt9RF0goXrn1KXcFWLe6'
access_token = '344908066-rdePMLqxhXMcv932bottLSZnJ3ALDJgbl6UhyHZK'
access_token_secret = 'dMwqHfUPFarhLJBbTLavRbpNBqCEA34YTX2dv5F0eJjb6'

g = []

 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
 

@application.route("/")
def hello():
    BRAZIL_WOE_ID = 23424768
    brazil_trends = api.trends_place(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazil_trends, indent=1))
    tt = []
    for trend in trends[0]["trends"]:
        tt.append("<br>"+trend["name"])

    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada reload da pagina</p>"+ '\n'.join(tt)


if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0', debug=True)
