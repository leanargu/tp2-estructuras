import requests
import config_reader

def write_xml(path_xml, noticia):
    archivo = open(path_xml, "a")
    archivo.write(noticia)

def read_xml(archivo):
    pass
