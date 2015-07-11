# coding=utf-8
__author__ = 'kelvin'

from faker import Factory
from loadercoordinador import maestrias, curso, profesores, seccion, estudiantes
from util import validar_datos
import local_settings
import csv
import json
import random


def carga_escenario(p_numero_escenario):


    carga_cursos_base(p_numero_escenario)
    # carga_secciones_base(p_numero_escenario)
    # carga_estudiantes_base(p_numero_escenario)
    # carga_estudiantes(p_numero_escenario)
    # export_csv_estudiantes()


def carga_estudiantes(p_numero_escenario):
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_escenario.replace("num_escenario",path_num_escenario)
    estudiantes.cargar_estudiantes(path_escenario+'estudiantes.csv')


def carga_cursos_base(p_numero_escenario):
    carga_cursos_mati(p_numero_escenario)
    carga_cursos_mbc(p_numero_escenario)
    carga_cursos_mbit(p_numero_escenario)
    carga_cursos_mesi(p_numero_escenario)
    carga_cursos_misis(p_numero_escenario)
    carga_cursos_miso(p_numero_escenario)


def carga_cursos_mati(p_numero_escenario):
    maestria = 'Maestrías en Arquitecturas de Tecnologías de Información'


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


    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_mati.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_cursos_mbc(p_numero_escenario):
    maestria = 'Maestría en biología computacional'


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

    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_mbc.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_cursos_mbit(p_numero_escenario):
    maestria = 'Maestría en tecnologías de Información para el Negocio'

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



    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_mbit.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_cursos_mesi(p_numero_escenario):
    maestria = 'Maestría en Seguridad de la Información'

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


    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_mesi.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_cursos_misis(p_numero_escenario):
    maestria = 'Maestría en Ingeniería de Sistemas y Computación'

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


    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_misis.csv", 'rb') as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=delimiter)
        for row in reader:

            validar_datos.analisis_datos_curso(prm_maestria= maestria)

            obj_maestria = maestrias.dar_maestria(maestria)
            json_maestria = json.loads(obj_maestria.text)

            obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
            json_pensum = json.loads(obj_pensum.text)
            rta = curso.crear_curso(row['NAME'], row['CODE'], row['CREDITS'], row['SUMMER'], json_pensum[0]["id"])
            print(rta.text)


def carga_cursos_miso(p_numero_escenario):
    maestria = 'Maestría en Ingenieria de Software'


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

    print 'creación de ' + maestria

    print "Cargando cursos escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_cursos_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "cursos_base_miso.csv", 'rb') as csvfile:
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


def carga_estudiantes_base(p_numero_escenario):
    maestria = 'MAESTRIA EN ARQUITECTURAS TI'
    fake = Factory.create()
    for x in range(0, 200):
        es_last_name = fake.lastName()
        es_name = fake.firstName()
        es_email = fake.email()
        es_code = random.randint(199000000,201599999)
        add_student(code=es_code,email=es_email,lastname=es_last_name,name=es_name,master=maestria)


#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def add_student(code, email, lastname, name, master):
    estudiantes.crear_estudiantes(master, code, lastname, name, email, 1)


def export_csv_estudiantes():
    estudaintes_dic = estudiantes.dar_estudiantes()
    estudaintes_mod = estudaintes_dic.text.replace("code","CARNET")
    estudaintes_mod = estudaintes_mod.replace("lastname","APELLIDOS")
    estudaintes_mod = estudaintes_mod.replace("name","NOMBRES")
    list_est = json.loads(estudaintes_mod)

    with open('data/escenario1/estudiantes.csv', 'wb') as f:  # Just use 'w' mode in 3.x
        fieldnames = ['CARNET', 'NOMBRES', 'APELLIDOS', 'email', 'master']
        w = csv.DictWriter(f,fieldnames=fieldnames, delimiter=' ')
        encabezados = True
        for es in list_est:
            tmp =es["master"]
            es["master"] = tmp["NOMBRES"]
            del es["id"]
            del es["student_status"]
            if encabezados:
                w.writeheader()
                encabezados = False
            w.writerow(es)