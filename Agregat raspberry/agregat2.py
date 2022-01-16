import paho.mqtt.client as mqtt
import time
from pigpio_dht import DHT22
import json
from statistics import mean


SLOT = "UPSSITECH"
AGREGAT = "bureau19"

PERIODE = 1*60
GPIO = 4

config = {"nombre" : 2, "type" : ['temperature_celcius', 'humidite_pourcent'], \
            "localisation" : ["Sur la table", "Sur la table"], "moyenne" : [0.0, 0.0]}




client = mqtt.Client()
client.connect("192.168.1.46", 1883, 60)

sensor = DHT22(GPIO)

result = sensor.read()
while(not result['valid']):
    result = sensor.read()
moy_temp = [result['temp_c']]*10
moy_hum = [result['humidity']]*10

while True:
    time.sleep(PERIODE)
    result = sensor.read()
    while(not result['valid']):
        result = sensor.read()
    print(result)

    moy_temp = moy_temp[1:] + [result['temp_c']]
    moy_hum = moy_hum[1:] + [result['humidity']]
    config["moyenne"] = [mean(moy_temp), mean(moy_hum)]

    client.publish("/%s/%s" % (SLOT, AGREGAT), json.dumps(config))