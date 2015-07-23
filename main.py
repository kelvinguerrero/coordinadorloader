# -*- coding: utf-8 -*-
__author__ = 'kelvin'
import argparse
from loadercoordinador import estudiantes, profesores, datos_base, carga_escenarios


def main(**kwargs):
    if kwargs['load'] == "estudiantes":
        if len(kwargs['ofile']) > 0:
            print("Se cargo el archivo ingresado")
            estudiantes.cargar_estudiantes(kwargs['ofile'])
        else:
            print("Cargando archivos de estudiantes")
            estudiantes.cargar_estudiantes_general( )
    elif kwargs['load'] == "graduados":
        estudiantes.cargar_graduados( )
    elif kwargs['load'] == "profesores":
        profesores.cargar_profesores_general()
    elif kwargs['load'] == "base":
        datos_base.carga_mati()
    elif kwargs['load'] == "escenario":
        if len(kwargs['numero']) > 0:
            print("Cargando datos para el escenario")
            carga_escenarios.carga_escenario(kwargs['numero'])
        else:
            print("se debe digitar el numero del escenario")
            print("Ejemplo: -l escenario -e 2")
            print("En este caso estamos cargando los el escenario numero 2")
    elif kwargs['create'] > 0:
        print("Creando el escenario" + kwargs['create'])
        carga_escenarios.crear_escenario(kwargs['create'])
    else:
        print("No existe el comando l-"+kwargs['load'])

#Metodo que permite hacer el cargue de informacion a la plataforma
# Formas de cargue:
# Estudiantes: python main.py -l estudiantes
# Profesores: python main.py -l profesores
# Estudiantes graduados: python main.py -l graduados
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--create', default='', type=str, help='Type of load to do.')
    parser.add_argument('-l', '--load', default='', type=str, help='Type of load to do.')
    parser.add_argument('-f', '--ofile', default='', type=str, help='File to load.')
    parser.add_argument('-e', '--numero', default='', type=str, help='File to load.')
    args = parser.parse_args()
    print(args)
    main(**vars(args))