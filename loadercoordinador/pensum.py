# -*- coding: utf-8 -*-
from fork import fork_service

__author__ = 'kelvin Guerrero'


def crear_pensum(param_master_id,param_programa):

    #Parametros para la creación de un pensum de para un programa
    BASE_PATH_MASTER_CREATE = "http://localhost:8000/map/api/pensum/"
    headers_master_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    data = {
              'name': param_programa,
              'active': True,
              'master_id': param_master_id
           }
    rta = fork_service.llamada_post(BASE_PATH_MASTER_CREATE, headers_master_create, data)
    return rta


def dar_pensum( pnombre ):
    #Parametros para la llamada de un pensum
    BASE_PATH_MASTER = "http://localhost:8000/map/api/master/?operation=5&master_name=param_nombre"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_MASTER = BASE_PATH_MASTER.replace("param_nombre", pnombre)

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_MASTER, headers_master)
    return rta_buscar_estudiante


def dar_pensum_maestria( pnombre_maestria ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_MASTER = "http://localhost:8000/map/api/master/?operation=5&master_name=param_nombre"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #BASE_PATH_MASTER = BASE_PATH_MASTER.replace("param_nombre", pnombre)

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_MASTER, headers_master)
    return rta_buscar_estudiante

def run(*args):
    print args[0]
    crear_maesria(args[0])