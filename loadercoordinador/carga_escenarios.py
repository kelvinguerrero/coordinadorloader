# coding=utf-8
__author__ = 'kelvin'

from loadercoordinador import maestrias, curso, profesores, seccion
from util import validar_datos
import local_settings
import csv
import json


def carga_escenario(p_numero_escenario):
    maestria = 'MAESTRIA EN ARQUITECTURAS TI'
    print 'creación de ' + maestria

    rta_dar_maestria = maestrias.dar_maestria(maestria)
    s_code_dar_maestria = rta_dar_maestria.status_code

    if rta_dar_maestria != None:
        if s_code_dar_maestria == 500:
            print 'No se encontro la maestría: ' + maestria

            rta_crear = maestrias.crear_maesria(maestria)

            if rta_crear == 500:
                print "Error en la creacion de la maestria" + maestria
            elif rta_crear == 200:
                print('Se creó la maestria:')
                print rta_crear.text
                print
        else:
            print('Ya existe la maestría')

    carga_cursos_base(p_numero_escenario)
    carga_secciones_base(p_numero_escenario)


def carga_cursos_base(p_numero_escenario):

    maestria = 'MAESTRIA EN ARQUITECTURAS TI'
    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_escenario.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_secciones_base(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_escenario.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            v_profesor = profesores.dar_profesor(p_code=row["TEACHER"])
            v_curso = curso.dar_curso(p_code=row["COURSE"])
            rta = seccion.crear_seccion(
                crn=row["CRN"],
                name=row["NAME"],
                semester=row["SEMESTER"],
                year=row["YEAR"],
                id_teacher=validar_datos.validar_datos_seccion_profesor(v_profesor),
                id_course=validar_datos.validar_datos_seccion_seccion(v_curso),
                status=row["STATUS"]
            )
            seccion.agregar_capacidad_seccion(row["CRN"], row["CAPACITY"])
            print(rta.text)