# -*- coding: utf-8 -*-
from fork import fork_service

__author__ = 'kelvin Guerrero'


def crear_maesria(param_programa):

    #Parametros para la creación de una Maestria
    BASE_PATH_MASTER_CREATE = "http://localhost:8000/map/api/master/"
    headers_master_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    data = {
              'name': param_programa
           }
    rta = fork_service.llamada_post(BASE_PATH_MASTER_CREATE, headers_master_create, data)
    return rta


def dar_maestria( pnombre ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_MASTER = "http://localhost:8000/map/api/master/?operation=5&master_name=param_nombre"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_MASTER = BASE_PATH_MASTER.replace("param_nombre", pnombre)

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_MASTER, headers_master)
    return rta_buscar_estudiante


def dar_pensum_maestria( pid_maestria ):
    #Parametros para la llamada del pensum de una maestría
    BASE_PATH_MASTER = "http://localhost:8000/map/api/master/id_maestria/?operation=1"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_MASTER = BASE_PATH_MASTER.replace("id_maestria", str(pid_maestria))

    rta_pensum = fork_service.llamada_get(BASE_PATH_MASTER, headers_master)
    return rta_pensum


def run(*args):
    print args[0]
    crear_maesria(args[0])