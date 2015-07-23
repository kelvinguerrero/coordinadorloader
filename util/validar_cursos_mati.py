# coding=utf-8
__author__ = 'kelvin'
import local_settings


#Metodo que valida las reglas de los cursos de MATI
#Este metodo es basado en los datos puestos en las reglas de negocio del archivo local_settings
def validar_curso_mati(prm_creditos, prm_ingles, codigo_curso):
    json_datos = local_settings.cursos_reglas_mati
    if codigo_curso in json_datos.keys():
        for key in json_datos:
            if key == codigo_curso:
                if prm_creditos >= json_datos[key]['creditos']:
                    if json_datos[key]['ingles']:
                        if prm_ingles:
                            return True
                        else:
                            return False
                    else:
                        return True
                    return True
        return False

    else:
        return True
