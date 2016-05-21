# -*- coding: cp1252 -*-
from twython import Twython, TwythonStreamer
import time
import json
        
class MyStreamer(TwythonStreamer):
    def __init__(self,APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET):
        TwythonStreamer.__init__(self,APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        self.f = open('doentes.json','a')
        
    def on_success(self, data):
        if 'text' in data:
            try:
                json.dump(data,self.f)
                self.f.write('\n')
            except KeyboardInterrupt:
                self.disconnect()

    def on_error(self, status_code, data):
        print status_code
        time.sleep(1200)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

APP_KEY = '3fAqfDiUqgd0W1x0pVUgw'
APP_SECRET = 'glYybjUNfBj6KmtCLhUDYJH2sURkTisZTJ89iVHQ'

twitter = Twython(APP_KEY, APP_SECRET)

auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = '30722040-x5MDlxbfrjytx9nT5M7OMozCsyPb6Qvst6aCTaYO3' #auth['oauth_token']
OAUTH_TOKEN_SECRET = 'zrAJgsAonwThRbKZEsAGtnrlvJuZOxV8QxgIz5monrtS3' #auth['oauth_token_secret']

stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#stream.statuses.filter(track="#doente,#gripado,#gripada,#virose,#gripe,#diarreia,#vomito,#febre",location='-73.817,-33.733,-28.850,16.800')
stream.statuses.filter(locations='-46.5,-24,-46.2,-23.9')
