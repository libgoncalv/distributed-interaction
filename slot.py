import paho.mqtt.client as mqtt
import pickle
import time
import threading
import requests
import json



PERIODE = 1*60
data = {}


def meteo():
    while True:
        time.sleep(PERIODE)
        key = "938880fa9e4b14b4fed503bed6ae6958"
        api_url = "https://api.openweathermap.org/data/2.5/weather?q=Toulouse&units=metric&appid=%s" % key
        response = requests.get(api_url)
        data = {"description" : response.json()['weather'][0]['description'], "temp" : response.json()['main']['temp'], \
                    "humidity" : response.json()['main']['humidity'], "wind_speed" : response.json()['wind']['speed']}
        print(data)
        print()

        with open('meteo.ser', 'wb') as f:
            pickle.dump(json.dumps(data), f, protocol=2)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc)+"\n")
    client.subscribe("/UPSSITECH/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    with open('%s.ser' % (msg.topic.split("/")[-1]), 'wb') as f:
        pickle.dump(msg.payload, f, protocol=2)
    print(msg.topic+" ")
    print(msg.payload)
    print()


t = threading.Thread(target=meteo)
t.start()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.publish("/UPSSITECH", "service on")

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
