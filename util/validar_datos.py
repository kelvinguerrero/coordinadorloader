__author__ = 'kelvin'
import json


def validar_datos_seccion_profesor(p_v_profesor):
    respuesta = None
    if p_v_profesor.status_code == 200:
        json_profesor = json.loads(p_v_profesor.text)
        respuesta = json_profesor["id"]
    return respuesta


def validar_datos_seccion_seccion(p_v_curso):
    respuesta = None
    if p_v_curso.status_code == 200:
        json_curso = json.loads(p_v_curso.text)
        respuesta = json_curso["id"]
    return respuesta