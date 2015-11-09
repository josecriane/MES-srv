from MES_srv.settings import GCM_APIKEY
from rest_framework.renderers import JSONRenderer

import unirest

url = 'https://gcm-http.googleapis.com/gcm/send'
headers =  { "Content-Type":"application/json", "Authorization":"key=" + GCM_APIKEY }

class Message():
    def __init__(self, to=[], data=None):
        self.to = to
        self.data = data

    def send_message(self):
        params = {'to':self.to, 'data': self.data}
        params = JSONRenderer().render(params)
        print params
        unirest.post(url, headers=headers, params=params, callback=self.callback)
    
    def callback(self, response):
        print "code: " + str(response.code)
        print "headers: " + str(response.headers)
        print "body: " + str(response.body)
        print "raw_body: " + str(response.raw_body)
