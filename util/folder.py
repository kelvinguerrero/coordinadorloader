from os import listdir
from os.path import isfile, join
__author__ = 'kelvin'


def listar_archivos(path):
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    return onlyfiles

