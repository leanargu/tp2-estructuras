'''
file_managger es el encargado de gestionar, y crear las carpetas
'''
import os


def crear_archivo_xml():
    pass


def crear_carpeta_medios():
    pass


def crear_carpeta_secciones():
    pass


def crear_archivo():
    directorio = "/Users/diego/test/"

    try:
        os.stat(directorio)
    except:
        os.mkdir(directorio)
