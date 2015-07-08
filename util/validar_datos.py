# coding=utf-8
__author__ = 'kelvin'
import json
from loadercoordinador import maestrias, pensum


def validar_datos_seccion_profesor(p_v_profesor):
    print("PROFESOR")
    print(p_v_profesor.text)
    print(p_v_profesor.status_code)
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


def analisis_datos_curso(prm_maestria):
    obj_maestria = maestrias.dar_maestria(prm_maestria)
    code_dar_maestria = obj_maestria.status_code

    if obj_maestria != None:
                if code_dar_maestria == 500:
                    print 'No se encontro la maestría: ' + prm_maestria
                    rta_crear = maestrias.crear_maesria(prm_maestria)

                    if rta_crear == 500:
                        print "Error en la creacion de la maestria" + prm_maestria

                    elif rta_crear == 200:
                        print('Se creó la maestria:')
                        print rta_crear.text
                        print
                        obj_maestria = maestrias.dar_maestria(prm_maestria)
    json_maestria = json.loads(obj_maestria.text)

    obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
    code_dar_pensum = obj_pensum.status_code

    if obj_pensum != None:
        if code_dar_pensum == 500:
            print 'No se encontro un pensum de la maestria'

            rta_crear = pensum.crear_pensum(json_maestria["id"],json_maestria["name"]+" pensum")
            rta_crear_code= rta_crear.status_code
            if rta_crear_code == 500:
                print "Error en la creacion del pensum" + json_maestria["name"]+" pensum"

            elif rta_crear_code == 200:
                print('Se creó el pensum:')
                print rta_crear.text
                print
                obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
    json_pensum = json.loads(obj_pensum.text)
    print( json_pensum )
    print( json_maestria )