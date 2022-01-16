from flask import Flask
import pickle
from glob import glob
import json


api = Flask(__name__)

@api.route('/UPSSITECH', methods=['GET'])
def get_UPSSITECH():
  to_return = []
  for file in glob("./*.ser"):
    with open(file, 'rb') as f:
      to_return.append(pickle.load(f))
  return json.dumps(str(to_return))

@api.route('/UPSSITECH/foyer', methods=['GET'])
def get_UPSSITECH_foyer():
  with open("foyer.ser", 'rb') as f:
    data = pickle.load(f)
  return json.dumps(str(data))

@api.route('/UPSSITECH/bureau19', methods=['GET'])
def get_UPSSITECH_bureau19():
  with open("bureau19.ser", 'rb') as f:
    data = pickle.load(f)
  return json.dumps(str(data))

@api.route('/UPSSITECH/meteo', methods=['GET'])
def get_UPSSITECH_meteo():
  with open("meteo.ser", 'rb') as f:
    data = pickle.load(f)
  return json.dumps(str(data))

if __name__ == '__main__':
    api.run(host="192.168.1.46") 