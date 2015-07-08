__author__ = 'kelvin Guerrero'
# coding=utf-8
import json
from loadercoordinador import maestrias, curso, pensum, seccion, profesores
from util import validar_datos


def analisis_datos_curso(prm_id, prm_cursosMati, prm_maestria):
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


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MATI
def carga_mati():

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


    print "carga de cursos de MATI"


    cursosMati = {
        "ARTI4101": {"name": "Gerencia de Proyectos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4102": {"name": "Comunicación Efectiva para Arquitectos", "credits": 4, "summer": False},
        "ARTI4103": {"name": "Arquitectura de Negocios y Estrategia de TI", "credits": 4, "summer": False},
        "ARTI4104": {"name": "Fundamentos para Arquitectos", "credits": 4, "summer": False},
        "ARTI4201": {"name": "Arquitectura de Solución", "credits": 4, "summer": False},
        "ARTI4202": {"name": "Arquitectura de Información", "credits": 4, "summer": False},
        "ARTI4203": {"name": "Arquitectura de Infraestructura de TI", "credits": 4, "summer": False},
        "ARTI4204": {"name": "Arquitectura de Seguridad", "credits": 4, "summer": False},
        "ARTI4205": {"name": "Arquitectura de Procesos de Negocio", "credits": 4, "summer": False},
        "ARTI4301": {"name": "Proyecto final", "credits": 4, "summer": False},
        "ARTI4106": {"name": "Arquitectura Empresarial", "credits": 4, "summer": False}
    }

    for codigo in cursosMati:
        analisis_datos_curso(codigo, cursosMati, maestria)

        obj_maestria = maestrias.dar_maestria(maestria)
        json_maestria = json.loads(obj_maestria.text)

        obj_pensum = maestrias.dar_pensum_maestria(json_maestria["id"])
        json_pensum = json.loads(obj_pensum.text)
        rta = curso.crear_curso(cursosMati[codigo]["name"], codigo, cursosMati[codigo]["credits"], cursosMati[codigo]["summer"], json_pensum[0]["id"])
        print(rta.text)
    #
    print "carga de secciones de MATI"
    seccionesMati = {
        13183: {"course": "ARTI4101", "capacity": {"MATI": 34, "pregrado": 3, "otros": 3}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        13579: {"course": "ARTI4102", "capacity": {"MATI": 32, "pregrado": 2, "otros": 6}, "name": "2", "semester": 1, "year": 2015, "teacher": 120000000, "status": 0},
        12663: {"course": "ARTI4103", "capacity": {"MATI": 40, "MBIT": 40, "MESI": 10}, "name": "1", "semester": 1, "year": 2015, "teacher": 79232014, "status": 0},
        13981: {"course": "ARTI4104", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "2", "semester": 1, "year": 2015, "teacher": 198714604, "status": 0},
        13982: {"course": "ARTI4106", "capacity": {"MATI": 60, "MBIT": 40}, "name": "1", "semester": 1, "year": 2015, "teacher": 130000000, "status": 0},
        12664: {"course": "ARTI4201", "capacity": {"MATI": 35, "otros": 5}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        12667: {"course": "ARTI4202", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 140000000, "status": 0},
        12665: {"course": "ARTI4203", "capacity": {"MATI": 20, "MESI": 20}, "name": "1", "semester": 1, "year": 2015, "teacher": 79419382, "status": 0},
        13185: {"course": "ARTI4204", "capacity": {"MATI": 32, "pregrado": 4, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 85462189, "status": 0},
        13285: {"course": "ARTI4205", "capacity": {"MATI": 34, "pregrado": 2, "otros": 4}, "name": "1", "semester": 1, "year": 2015, "teacher": 200021872, "status": 0},
        13582: {"course": "ARTI4301", "capacity": {"MATI": 99}, "name": "1", "semester": 1, "year": 2015, "teacher": 79505041, "status": 0}
    }

    for seccion_p in seccionesMati:
        v_profesor = profesores.dar_profesor(p_code=seccionesMati[seccion_p]["teacher"])
        v_curso = curso.dar_curso(p_code=seccionesMati[seccion_p]["course"])
        rta = seccion.crear_seccion(
            crn=seccion_p,
            name=seccionesMati[seccion_p]["name"],
            semester=seccionesMati[seccion_p]["semester"],
            year=seccionesMati[seccion_p]["year"],
            id_teacher= validar_datos.validar_datos_seccion_profesor(v_profesor),
            id_course=validar_datos.validar_datos_seccion_seccion(v_curso),
            status=seccionesMati[seccion_p]["status"]
        )
        print(rta.text)
            #capacity=seccionesMati[seccion_p]["capacity"],



#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MBC
def carga_mbc():
    print "carga de cursos de MBC"
    cursosMbc = {
        "1": {"name": "Bioinformática", "credits": 4, "summer": False},
        "2": {"name": "Algoritmos en Biología Computacional", "credits": 4, "summer": False},
        "3": {"name": "Fundamentos en programación para ciencias biológicas", "credits": 4, "summer": False},
        "4": {"name": "Biología Molecular Avanzada", "credits": 4, "summer": False},
        "5": {"name": "Biología Cuantitativa", "credits": 4, "summer": False},
        "6": {"name": "Procesamiento de datos biológicos", "credits": 4, "summer": False},
        "7": {"name": "Computación de alto desempeño para ciencias biológicas", "credits": 4, "summer": False},
        "8": {"name": "Computación visual para ciencias biológicas", "credits": 4, "summer": False},
        "9": {"name": "Modelamiento de redes", "credits": 4, "summer": False},
        "0": {"name": "Analisis de secuencias", "credits": 4, "summer": False},
        "10": {"name": "Biología de sistemas", "credits": 4, "summer": False},
        "11": {"name": "Biología sintética", "credits": 4, "summer": False},
        "12": {"name": "Introducción a la ingeniería de proteinas", "credits": 4, "summer": False},
        "13": {"name": "Modelamientos matemáticos en biología", "credits": 4, "summer": False}}

    for codigo in cursosMbc:
        obj_maestria = maestrias.dar_maestria(p_pensum)
        json_maestria = json.loads(obj_maestria.text)
        master_id = json_maestria["id"]

        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBC"),
            code=codigo,
            credits=cursosMbc[codigo]["credits"],
            name=cursosMbc[codigo]["name"],
            summer=cursosMbc[codigo]["summer"])


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MBIT
def carga_mbit():
    print "carga de cursos de MBIT"
    cursosMbit = {
        "MBIT4101": {"name": "Habilidades Gerenciales en TI", "credits": 4, "summer": False},
        "MBIT4201": {"name": "Emprendimiento y Negocios Electrónicos", "credits": 4, "summer": False},
        "MBIT4202": {"name": "Gobierno de TI", "credits": 4, "summer": False},
        "MBIT4203": {"name": "Business Analytics", "credits": 4, "summer": False},
        "MBIT4204": {"name": "Gestión de Servicios de TI", "credits": 4, "summer": False},
        "MBIT4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MBIT4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MBIT4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MBIT4205": {"name": "Fundamentos de Gerencia de TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])


    #Secciones de MBIT
    print "carga de secciones de MBIT"
    seccionesMesi = {
        16852: {"course": "MBIT4101", "name": "1", "capacity": {"MBIT": 40, "MESI": 10, "otros": 10}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        15804: {"course": "MBIT4101", "name": "2", "capacity": {"MBIT": 40, "MESI": 10, "otros": 10}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        13984: {"course": "MBIT4201", "name": "1", "capacity": {"MBIT": 40, "MISO": 26, "pregrado": 8, "otros": 6}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        16853: {"course": "MBIT4201", "name": "2", "capacity": {"MBIT": 40, "MISO": 26, "pregrado": 8, "otros": 6}, "semester": 1, "year": 2015, "teacher": 194814117, "status": 0},
        13985: {"course": "MBIT4202", "name": "1", "capacity": {"MBIT": 30, "MESI": 10, "otros": 5}, "semester": 1, "year": 2015, "teacher": 900000000, "status": 0},
        14598: {"course": "MBIT4203", "name": "1", "capacity": {"MBIT": 35, "otros": 5}, "semester": 1, "year": 2015, "teacher": 199617196, "status": 0},
        14599: {"course": "MBIT4204", "name": "1", "capacity": {"MBIT": 35, "otros": 5}, "semester": 1, "year": 2015, "teacher": 110000000, "status": 0},
        14600: {"course": "MBIT4205", "name": "1", "capacity": {"MBIT": 30, "MESI": 5, "otros": 5}, "semester": 1, "year": 2015, "teacher": 800000000, "status": 0},
        17118: {"course": "MBIT4301", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0},
        17119: {"course": "MBIT4302", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0},
        17120: {"course": "MBIT4303", "name": "1", "capacity": {"MBIT": 99}, "semester": 1, "year": 2015, "teacher": 0, "status": 0}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"]),
            capacity=seccionesMesi[seccion]["capacity"],
            status=seccionesMesi[seccion]["status"]
        )


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MESI
def carga_mesi():
    print "carga de cursos de MESI"
    cursosMbit = {
        "MSIN4201": {"name": "Modelos de Seguridad – Aplicaciones y Análisis de Estándares", "credits": 4,"summer": False},
        "MSIN4203": {"name": "Gerencia de CSIRTs y Manejo de Incidentes", "credits": 4, "summer": False},
        "MSIN4301": {"name": "PROYECTO FINAL", "credits": 4, "summer": False},
        "MSIN4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MSIN4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MSIN4101": {"name": "Ingeniería Criptográfica y su Aplicación en TI", "credits": 4, "summer": False}}

    for codigo in cursosMbit:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MBIT"),
            code=codigo,
            credits=cursosMbit[codigo]["credits"],
            name=cursosMbit[codigo]["name"],
            summer=cursosMbit[codigo]["summer"])

    #Secciones de MESI
    print "carga de secciones de MESI"
    seccionesMesi = {
        15850: {"course": "MSIN4101", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000005, "status": 0},
        14607: {"course": "MSIN4201", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 199427762, "status": 0},
        15851: {"course": "MSIN4203", "name": "1", "capacity": {"MESI": 33, "pregrado": 4, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000006, "status": 0},
        14609: {"course": "MSIN4302", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0},
        14608: {"course": "MSIN4301", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000007, "status": 0},
        16217: {"course": "MSIN4303", "name": "1", "capacity": {"MESI": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0}}

    for seccion in seccionesMesi:
        add_section(
            crn=seccion,
            name=seccionesMesi[seccion]["name"],
            semester=seccionesMesi[seccion]["semester"],
            year=seccionesMesi[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMesi[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMesi[seccion]["course"]),
            capacity=seccionesMesi[seccion]["capacity"],
            status=seccionesMesi[seccion]["status"]
        )


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MISIS
def carga_misis():
    print "carga de cursos de MISIS"
    cursosIsis = {
        "ISIS-4422": {"name": "Servicios móviles y redes de próxima generación", "credits": 4, "summer": False},
        "ISIS-4518": {"name": "Sistemas de Recomendación", "credits": 4, "summer": False},
        "ISIS-4820": {"name": "Ambientes interactivos 3D", "credits": 4, "summer": False},
        "ISIS-4216": {"name": "Inteligencia artificial y representación de conocimiento", "credits": 4,
                      "summer": False}}

    for codigo in cursosIsis:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosIsis[codigo]["credits"],
            name=cursosIsis[codigo]["name"],
            summer=cursosIsis[codigo]["summer"])


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MISO
def carga_miso():
    print "carga de cursos de MISO"
    cursosMiso = {
        "MISO4202": {"name": "Mejoramiento de la productividad: Automatización", "credits": 4, "summer": False},
        "MISO4204": {"name": "Fábricas de software y líneas de producto", "credits": 4, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4301": {"name": "Proyecto Integrador", "credits": 4, "summer": False},
        "MISO4302": {"name": "Tesis I", "credits": 4, "summer": False},
        "MISO4303": {"name": "Tesis II", "credits": 8, "summer": False},
        "MISO4205": {"name": "Mejoramiento de la experiencia del usuario", "credits": 4, "summer": False},
        "MISO4101": {"name": "Procesos de Desarrollo Ágiles", "credits": 4, "summer": False}}

    for codigo in cursosMiso:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_MISIS"),
            code=codigo,
            credits=cursosMiso[codigo]["credits"],
            name=cursosMiso[codigo]["name"],
            summer=cursosMiso[codigo]["summer"])

    #Secciones de MISO
    print "carga de secciones de MISO"
    seccionesMiso = {
        14446: {"course": "MISO4101", "name": "1", "capacity": {"MISO": 35, "pregrado": 3, "otros": 2}, "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        13986: {"course": "MISO4202", "name": "1", "capacity": {"MISO": 35, "pregrado": 2, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000001, "status": 0},
        14604: {"course": "MISO4204", "name": "1", "capacity": {"MISO": 35, "pregrado": 3, "otros": 2}, "semester": 1, "year": 2015, "teacher": 79505041, "status": 0},
        16210: {"course": "MISO4205", "name": "1", "capacity": {"MISO": 33, "otros": 3}, "semester": 1, "year": 2015, "teacher": 000000002, "status": 0},
        16211: {"course": "MISO4301", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000003, "status": 0},
        15251: {"course": "MISO4302", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0},
        16212: {"course": "MISO4303", "name": "1", "capacity": {"MISO": 99}, "semester": 1, "year": 2015, "teacher": 000000004, "status": 0}}

    for seccion in seccionesMiso:
        add_section(
            crn=seccion,
            name=seccionesMiso[seccion]["name"],
            semester=seccionesMiso[seccion]["semester"],
            year=seccionesMiso[seccion]["year"],
            teacher=Teacher.objects.get(code=seccionesMiso[seccion]["teacher"]),
            course=Course.objects.get(code=seccionesMiso[seccion]["course"]),
            capacity=seccionesMiso[seccion]["capacity"],
            status=seccionesMiso[seccion]["status"]
        )


#-----------------------------------------------------------------------------------------------------------------------
#Cursos de MISO
def carga_ingles():
    print "carga de curso Ingles"
    cursosMiso = {
        "LENG0001": {"name": "Ingles", "credits": 0, "summer": False}}

    for codigo in cursosMiso:
        add_course(
            pensum=Pensum.objects.get(name="Pensum_ENGLISH"),
            code=codigo,
            credits=cursosMiso[codigo]["credits"],
            name=cursosMiso[codigo]["name"],
            summer=cursosMiso[codigo]["summer"])

    #Secciones de MISO
    print "carga de secciones de Ingles"
    seccionesMiso = {
        00001: {"course": "LENG0001", "name": "1", "capacity": {"otros": 99}, "semester": 1, "year": 2015, "status": 0},
        00002: {"course": "LENG0001", "name": "1", "capacity": {"otros": 99}, "semester": 2, "year": 2015, "status": 0},
        00003: {"course": "LENG0001", "name": "1", "capacity": {"otros": 99}, "semester": 1, "year": 2014, "status": 0},
        00004: {"course": "LENG0001", "name": "1", "capacity": {"otros": 99}, "semester": 2, "year": 2014, "status": 0}
        }

    for seccion in seccionesMiso:
        add_section_no_teacher(
            crn=seccion,
            name=seccionesMiso[seccion]["name"],
            semester=seccionesMiso[seccion]["semester"],
            year=seccionesMiso[seccion]["year"],
            course=Course.objects.get(code=seccionesMiso[seccion]["course"]),
            capacity=seccionesMiso[seccion]["capacity"],
            status=seccionesMiso[seccion]["status"]
        )