# -*- coding: utf-8 -*-
__author__ = 'kelvin Guerrero'
import os

#Maestrias
MATI = 'Maestrías en Arquitecturas de Tecnologías de Información'
MBC = 'Maestría en biología computacional'
MBIT = 'Maestría en tecnologías de Información para el Negocio'
MESI = 'Maestría en Seguridad de la Información'
MISIS = 'Maestría en Ingeniería de Sistemas y Computación'
MISO = 'Maestría en Ingenieria de Software'
LENG = 'Lenguajes'


base_proyect_path = os.getcwd()
path_student = base_proyect_path+"/data/student/"
path_student_graduated = base_proyect_path+"/data/student_graduated/"
path_teacher_graduated = base_proyect_path+"/data/teacher/"

path_base_escenario = base_proyect_path+"/data/num_escenario/base/"
path_base_cursos_base = base_proyect_path+"/data/num_escenario/base/cursos/"
path_base_secciones_base = base_proyect_path+"/data/num_escenario/base/secciones/"
path_student_escenario = base_proyect_path+"/data/num_escenario"

scrumdo_username=""
scrumdo_password=""
scrumdo_host="http://www.scrumdo.com"

public_key = ""
secret_key = ""

test_link_key = ""
# substitute your server URL Here
SERVER_URL = "http://testlink.net/testlink/lib/api/xmlrpc.php"

# Write data protection
write_example=False
# Information
write_organization_slug=""
write_project_slug=""
