# coding=utf-8
__author__ = 'kelvin'

from faker import Factory
from loadercoordinador import maestrias, curso, profesores, seccion, estudiantes, pensum
from util import validar_datos,validar_cursos_mati
import local_settings
import csv
import json
import random


#Metodo para crear estudiantes ramdom
# carga_estudiantes_base(p_numero_escenario)
#export_csv_estudiantes()
def crear_escenario(p_numero_escenario):
    carga_cursos_base(p_numero_escenario)
    carga_secciones_base(p_numero_escenario)
    generar_estudiantes_base_random(p_numero_escenario)
    exportar_estudiantes_csv(p_numero_escenario)
    carga_cursos_estudiantes(p_numero_escenario)
    exportar_estudiantes_csv(p_numero_escenario)


def carga_escenario(p_numero_escenario):
    carga_cursos_base(p_numero_escenario)
    carga_secciones_base(p_numero_escenario)
    carga_estudiantes(p_numero_escenario)


def carga_estudiantes_sin_secciones(p_numero_escenario):
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_student_escenario.replace("num_escenario",path_num_escenario)
    estudiantes.cargar_estudiantes_escenario_sin_secciones(path_escenario+'/estudiantes.csv')


def carga_estudiantes(p_numero_escenario):
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_student_escenario.replace("num_escenario",path_num_escenario)
    estudiantes.cargar_estudiantes_escenario(path_escenario+'/estudiantes.csv')


def carga_cursos_base(p_numero_escenario):
    carga_cursos_mati(p_numero_escenario)
    carga_cursos_mbc(p_numero_escenario)
    carga_cursos_mbit(p_numero_escenario)
    carga_cursos_mesi(p_numero_escenario)
    carga_cursos_misis(p_numero_escenario)
    carga_cursos_miso(p_numero_escenario)
    carga_cursos_lenguajes(p_numero_escenario)


def carga_cursos_mati(p_numero_escenario):
    maestria = local_settings.MATI

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
    maestria = local_settings.MBC

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
    maestria = local_settings.MBIT

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
    maestria = local_settings.MESI

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
    maestria = local_settings.MISIS

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
    maestria = local_settings.MISO


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


def carga_cursos_lenguajes(p_numero_escenario):
    maestria = local_settings.LENG

    rta_dar_maestria = maestrias.dar_maestria(maestria)
    s_code_dar_maestria = rta_dar_maestria.status_code

    if rta_dar_maestria != None:
        if s_code_dar_maestria == 500:
            print 'No se encontro el curso: ' + maestria

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
    with open( path_escenario + "cursos_base_lenguajes.csv", 'rb') as csvfile:
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
    carga_secciones_mati(p_numero_escenario)
    carga_secciones_mbc(p_numero_escenario)
    carga_secciones_mbit(p_numero_escenario)
    carga_secciones_mesi(p_numero_escenario)
    carga_secciones_misis(p_numero_escenario)
    carga_secciones_miso(p_numero_escenario)
    carga_secciones_lenguajes(p_numero_escenario)


def carga_secciones_mati(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_mati.csv", 'rb') as csvfile:
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


def carga_secciones_mbc(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_mbc.csv", 'rb') as csvfile:
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


def carga_secciones_mbit(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_mbit.csv", 'rb') as csvfile:
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


def carga_secciones_mesi(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_mesi.csv", 'rb') as csvfile:
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


def carga_secciones_misis(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_misis.csv", 'rb') as csvfile:
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


def carga_secciones_miso(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_miso.csv", 'rb') as csvfile:
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


def carga_secciones_lenguajes(p_numero_escenario):
    print "Cargando secciones escenario "+ p_numero_escenario
    delimiter = '	'
    path_num_escenario = "escenario"+p_numero_escenario
    path_escenario = local_settings.path_base_secciones_base.replace("num_escenario",path_num_escenario)
    with open( path_escenario + "secciones_base_lenguajes.csv", 'rb') as csvfile:
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


#Metodo encargado de crear un estudiante
# params: code => codigo del estudiante, email => email del estudiante, lastname => apellido del estudiante,
#         name => Nombre del estudiante, master
def add_student(code, email, lastname, name, master):
    estudiantes.crear_estudiantes(master, code, lastname, name, email, 1)


def carga_cursos_estudiantes(p_numero_escenario):
    rta = estudiantes.dar_estudiantes()
    list_estudiante = json.loads(rta.text)
    print ("Creando Cursos")
    for estudiante in list_estudiante:
        print ".",
        print "."
        curso_uno = False
        numero = 0
        ingles = False
        creditos = 0
        while not curso_uno:
            pensum_mati = pensum.dar_pensum_maestria(local_settings.MATI)
            json_p_mati = json.loads(pensum_mati.text)
            curso_obj = dar_curso_random(json_p_mati["id"])
            rta = estudiantes.verificar_existe_curso(curso_obj["id"],estudiante["id"])
            if rta.status_code == 500:
                rta_validacion = validar_cursos_mati.validar_curso_mati(creditos,ingles,curso_obj['code'])
                if rta_validacion:
                    secciones_curso = curso.dar_seccion_curso(curso_obj["id"])
                    list_secciones = json.loads(secciones_curso.text)
                    estudiantes.agregar_curso_aprobado(list_secciones[0]["id"],estudiante["id"])
                    numero = numero + 1
                    creditos = creditos + curso_obj['credits']
            if numero == 7:
                curso_uno = True
    print("Cursos Creados Correctamente")


def dar_curso_random(id_pensum):
    cursos = pensum.dar_cursos_pensum(id_pensum)
    list_cursos = json.loads(cursos.text)
    numero = random.randint(0, list_cursos.__len__()-1)
    return list_cursos[numero]


#def export_csv_cursos_estudiantes()
def exportar_estudiantes_csv(numEscenario):
    estudaintes_dic = estudiantes.dar_estudiantes()
    estudaintes_mod = estudaintes_dic.text.replace("code","CARNET")
    estudaintes_mod = estudaintes_mod.replace("lastname","APELLIDOS")
    estudaintes_mod = estudaintes_mod.replace("name","NOMBRES")
    list_est = json.loads(estudaintes_mod)

    with open('data/escenario'+str(numEscenario)+'/estudiantes.csv', 'wb') as f:  # Just use 'w' mode in 3.x
        fieldnames = ['CARNET', 'NOMBRES', 'APELLIDOS', 'email', 'master','SECCIONES']
        w = csv.DictWriter(f, delimiter=';',fieldnames=fieldnames,
                           quoting=csv.QUOTE_NONE)
        encabezados = True
        for es in list_est:
            tmp =es["master"]
            es["master"] = tmp["NOMBRES"]
            sec = estudiantes.dar_secciones_estudiantes(es["id"])
            obj_seccion = json.loads(sec.text)
            lista_secciones = list()
            for r in obj_seccion:
                lista_secciones.append(r["section"]["crn"])
            del es["id"]
            del es["student_status"]
            es["SECCIONES"] = lista_secciones
            if encabezados:
                w.writeheader()
                encabezados = False
            es['master'] = es['master'].encode('utf8')
            w.writerow(es)


def generar_estudiantes_base_random(p_numero_escenario):
    maestria = 'MAESTRIA EN ARQUITECTURAS TI'
    fake = Factory.create()
    for x in range(0, 200):
        es_last_name = fake.lastName()
        es_name = fake.firstName()
        es_email = fake.email()
        es_code = random.randint(199000000,201599999)
        add_student(code=es_code,email=es_email,lastname=es_last_name,name=es_name,master=maestria)
