__author__ = 'kelvin Guerrero'
# coding=utf-8

import sys
import requests
import json


def llamada_post(pbase_path, pheaders, pdata):
    s = requests.Session()
    s.verify = False
    jsondata = json.dumps(pdata)
    try:
        r = requests.post(pbase_path, headers=pheaders, data=jsondata)
        return r
    except Exception as e:
        message ="Error no existe conexión con Coordinador"
        sys.exit(message)


def llamada_get(pbase_path, pheaders):
    s = requests.Session()
    s.verify = False
    try:
        r = requests.get(pbase_path, headers=pheaders)
        return r
    except Exception as e:
        message ="Error no existe conexión con Coordinador"
        sys.exit(message)


def llamada_put(pbase_path, pheaders, pdata):
    s = requests.Session()
    s.verify = False
    try:
        r = requests.put(pbase_path, headers=pheaders, data=pdata)
        return r
    except Exception as e:
        message ="Error no existe conexión con Coordinador"
        sys.exit(message)
