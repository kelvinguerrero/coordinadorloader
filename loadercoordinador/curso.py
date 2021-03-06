# -*- coding: utf-8 -*-
from fork import fork_service
from loadercoordinador import maestrias
import json
__author__ = 'kelvin Guerrero Avila'


def crear_curso(p_nombre, p_code, p_creditos, p_vacacional, p_pensum):

    #Parametros para la creación de una Maestria
    BASE_PATH_COURSE_CREATE = "http://localhost:8000/map/api/course/"
    headers_course_create = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    data = {
              'code': p_code,
              'name': p_nombre,
              'credits': p_creditos,
              'summer': p_vacacional,
              'pensum': p_pensum
           }
    rta = fork_service.llamada_post(BASE_PATH_COURSE_CREATE, headers_course_create, data)
    return rta


def dar_curso( p_code ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_COURSE = "http://localhost:8000/map/api/course/?operation=2&code_curso=p_code_curso"
    headers_course = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_COURSE = BASE_PATH_COURSE.replace("p_code_curso", p_code)
    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_curso = fork_service.llamada_get(BASE_PATH_COURSE, headers_course)

    return rta_buscar_curso


def dar_seccion_curso(p_id_curso):
    #Parametros para la_ llamada de la llamada de una maestría
    BASE_PATH_SECCIONES_COURSE = "http://localhost:8000/map/api/course/id_curso/?operation=1"
    headers_course = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    BASE_PATH_SECCIONES_COURSE = BASE_PATH_SECCIONES_COURSE.replace("id_curso", str(p_id_curso))
    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_curso = fork_service.llamada_get(BASE_PATH_SECCIONES_COURSE, headers_course)

    return rta_buscar_curso