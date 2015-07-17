# -*- coding: utf-8 -*-
from fork import fork_service
from loadercoordinador import maestrias
import json
__author__ = 'kelvin Guerrero Avila'


def dar_seccion_crn( p_crn ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_seccion = "http://localhost:8000/map/api/section/crn_seccion/?operation=6"
    headers_course = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    BASE_PATH_seccion = BASE_PATH_seccion.replace("crn_seccion", str(p_crn))

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_seccion = fork_service.llamada_get(BASE_PATH_seccion, headers_course)
    return rta_buscar_seccion

def crear_seccion(crn,name,semester,year,status,id_teacher,id_course):

    #Parametros para la creación de una Maestria
    BASE_PATH_SECTION_CREATE = "http://localhost:8000/map/api/section/"
    headers_section_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    data = {
              "crn":crn,
              "name":name,
              "semester":semester,
              "year":year,
              "status":status,
              "teacher":id_teacher,
              "course":id_course
           }
    rta = fork_service.llamada_post(BASE_PATH_SECTION_CREATE, headers_section_create, data)
    return rta


def agregar_capacidad_seccion(prm_crn_seccion, capacidad):
    #Parametros para la creación de una Maestria
    BASE_PATH_SECTION_CAPACIDAD = "http://localhost:8000/map/api/section/crn_seccion/"
    headers_section_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_SECTION_CAPACIDAD = BASE_PATH_SECTION_CAPACIDAD.replace("crn_seccion", prm_crn_seccion)

    data = {
              "operation":5,
              "jsoncapacidad":capacidad
           }
    rta = fork_service.llamada_post(BASE_PATH_SECTION_CAPACIDAD, headers_section_create, data)
    return rta