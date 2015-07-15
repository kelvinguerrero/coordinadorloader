# -*- coding: utf-8 -*-
from util import folder
from loadercoordinador import maestrias
from fork import fork_service
import csv
import json
import local_settings

__author__ = 'kelvin Guerrero'


#Metodo encargado en la creación de un estudiante
def servicio_crear_estudiante( pdata ):
    #Parametros para la llamada de la creación de un estudiante
    BASE_PATH = 'http://localhost:8000/map/api/student/'
    headers = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    rta = fork_service.llamada_post(BASE_PATH, headers, pdata)
    s_code_creacion = rta.status_code

    if s_code_creacion == 500:
        json_rta = json.loads(rta.text)
        return json_rta['mensaje']
    elif s_code_creacion == 200:
        json_rta = json.loads(rta.text)
        return json_rta


def crear_estudiantes(pprograma, pcodigo , papellido, pnombre, pemail, pstatus):
     #Parametros para la llamada de la llamada de un estudiante
    BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", str(pcodigo))

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
    s_code = rta_buscar_estudiante.status_code
    if s_code == 500:
        json_rta = json.loads(rta_buscar_estudiante.text)['mensaje']
        if json_rta == 'No existe el estudiante':

            rta_dar_maestria = maestrias.dar_maestria(pprograma)
            s_code_dar_maestria = rta_dar_maestria.status_code

            if rta_dar_maestria != None:
                if s_code_dar_maestria == 500:
                    print 'No se encontro la maestría: ' + pprograma

                    rta_crear = maestrias.crear_maesria(pprograma)

                    if rta_crear == 500:
                        print "Error en la creacion de la maestria" + pprograma
                    elif rta_crear == 200:
                        print('Se creó la maestria:')
                        print rta_crear.text
                        print

                elif s_code_dar_maestria == 200:
                    decode_dar_maestria = rta_dar_maestria.text
                    json_maestria = json.loads(decode_dar_maestria)
                    master_id=json_maestria["id"]
                    data = {
                        'lastname': papellido,
                        'code': pcodigo,
                        'email': pemail,
                        'name': pnombre,
                        'student_status': pstatus,
                        'master_id': master_id
                    }
                    rta = servicio_crear_estudiante( data )
                    print rta
                else:
                    print "Error en el estudiante" + pcodigo
            else:
                print "Error en la busqueda de la maestría: " + pcodigo

    else:
        print "Estudiante ya existe: " + pcodigo


def cargar_estudiantes( parchivo ):
    print parchivo
    delimiter = '	'
    with open( local_settings.path_student + parchivo, 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            crear_estudiantes(row['PROGRAMA'], row['CARNET'] , row['APELLIDOS'], row['NOMBRES'], row['EMAIL'], 1)


def cargar_estudiantes_escenario( parchivo ):
    print parchivo
    delimiter = ';'
    with open( parchivo, 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        print('Cargando estudiantes')
        for row in reader:
            crear_estudiantes(row['master'], row['CARNET'] , row['APELLIDOS'], row['NOMBRES'], row['email'], 1)
        print('Estudiantes cargados')


def cargar_estudiantes_graduados(parchivo):

    #Parametros para la llamada de un estudiante
    headers_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Parametros para actualizar los datos de un estudiante
    BASE_PATH_EDIT_STUDENT = "http://localhost:8000/map/api/student/codigo_student"
    headers_edit_student = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    delimiter = '	'
    with open(local_settings.path_student_graduated + parchivo, 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:
            BASE_PATH_STUDENT = "http://localhost:8000/map/api/student/codigo_student/?operation=6"

            pprograma = row["PROGRAMA"]
            papellido = row['APELLIDOS']
            pcodigo = row['CARNET']
            pnombre = row['NOMBRES']
            pstatus = 3
            BASE_PATH_STUDENT = BASE_PATH_STUDENT.replace("codigo_student", row['CARNET'])

            rta_buscar_estudiante = fork_service.llamada_get(BASE_PATH_STUDENT, headers_student)
            s_code = rta_buscar_estudiante.status_code

            if s_code == 500:

                rta_dar_maestria = maestrias.dar_maestria(pprograma)
                s_code_dar_maestria = rta_dar_maestria.status_code

                if rta_dar_maestria != None:
                    if s_code_dar_maestria == 500:
                        print 'No se encontro la maestría: ' + pprograma

                        rta_crear = maestrias.crear_maesria(pprograma)

                        if rta_crear == 500:
                            print "Error en la creacion de la maestria" + pprograma
                        elif rta_crear == 200:
                            print('Se creó la maestria:')
                            print rta_crear.text
                            print

                    elif s_code_dar_maestria == 200:
                        decode_dar_maestria = rta_dar_maestria.text
                        json_maestria = json.loads(decode_dar_maestria)
                        master_id=json_maestria["id"]
                        data = {
                            'lastname': papellido,
                            'code': pcodigo,
                            'name': pnombre,
                            'student_status': pstatus,
                            'master_id': master_id
                        }
                        rta = servicio_crear_estudiante( data )
                        print rta
                    else:
                        print "Error en el estudiante" + pcodigo
                else:
                    print "Error en la busqueda de la maestría: " + pcodigo

            else:
                json_id_estudiante = json.loads(rta_buscar_estudiante.text)['id']

                BASE_PATH_EDIT_STUDENT = BASE_PATH_EDIT_STUDENT.replace("codigo_student", str(json_id_estudiante))
                data_edit = {
                    'student_status': 3
                }
                print(BASE_PATH_EDIT_STUDENT)
                print(data_edit)
                rta = fork_service.llamada_put(BASE_PATH_EDIT_STUDENT, headers_edit_student, data_edit)
                print "Estudiante ya existe: " + pcodigo
                print "Se actualiza el estado a graduado"
                print(rta.text)


def cargar_estudiantes_general( ):
    archivos = folder.listar_archivos( local_settings.path_student )
    for ruta in archivos:
        cargar_estudiantes(ruta)


def cargar_graduados():
    archivos = folder.listar_archivos( local_settings.path_student_graduated )
    for ruta in archivos:
        cargar_estudiantes_graduados(ruta)


def dar_estudiantes( ):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_MASTER = "http://localhost:8000/map/api/student"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_estudiantes = fork_service.llamada_get(BASE_PATH_MASTER, headers_master)
    return rta_estudiantes


def verificar_existe_curso(codigo_curso, id_estudiante):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_COURSE = "http://localhost:8000/map/api/student/id_estudiante/?operation=5&code_curso=num_codigo_curso"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }
    BASE_PATH_COURSE = BASE_PATH_COURSE.replace("id_estudiante", str(id_estudiante))
    BASE_PATH_COURSE = BASE_PATH_COURSE.replace("num_codigo_curso", str(codigo_curso))


    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_estudiantes = fork_service.llamada_get(BASE_PATH_COURSE, headers_master)
    return rta_estudiantes


def agregar_curso_aprobado(prm_id_estudiante, prm_id_seccion):
    #Parametros para la llamada de la llamada de una maestría
    BASE_PATH_COURSE = "http://localhost:8000/map/api/subject/"
    headers_master = {
        'API-KEY': '123',
        'Authorization': 'Token ef3859d862f572ad532fceb04536e948da1d5270'
    }

    data = {
                "grade": 3,
                "student_status": True,
                "student": prm_id_estudiante,
                "section": prm_id_seccion
            }

    #Se llama al servicio de llamada de estudiante para verificar si este existe
    rta_registro = fork_service.llamada_post(BASE_PATH_COURSE, headers_master, data)
    return rta_registro