import requests
import json
import Adafruit_DHT as dht
import time
import threading
from threading import Timer

url = 'http://api.figs.noedominguez.com:9000/v1/measurement_event/'

def hello():
    try:
        h,t = dht.read_retry(dht.DHT22, 4)

        payloadT = {"measurement_id": 2, "magnitude": t, "created_at": ""} #Temperature
        payloadH = {"measurement_id": 3, "magnitude": h, "created_at": ""} #Humidity
        headers = {'Content-type': 'application/json'}

        myResponseT = requests.post(url, data=json.dumps(payloadT), headers=headers)  #for temperature
        myResponseH = requests.post(url, data=json.dumps(payloadH), headers=headers) #for humidity

        print("\n")
        print myResponseT.content
        print myResponseH.content
        if(not myResponseT.ok or not myResponseH.ok):
            print "There was an error"
            jData = json.loads(myResponseT.content and myResponseH.content)
            #threading.Timer(60.0, hello).start

        # If response code is not ok (200), print the resulting http error code with description
        myResponseT.raise_for_status()
        myResponseH.raise_for_status()
    except:
        pass

while True:
        hello()
        time.sleep(60)
