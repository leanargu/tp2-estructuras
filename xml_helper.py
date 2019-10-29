import requests
import config_reader
from xml.dom import minidom
import file_managger as fm
from xml.etree import cElementTree as ET
"""
Esta clase se encarga de hacer las operaciones referidas a los archivos xml.
"""

def write_xml(path_xml, noticias):
    """
    La noticia se debera escribir unicamente si la mismo no se encuentra repetida, por lo cual
    se le deberá paras una lista de noticias
    :param path_xml:
    :param noticias:
    :return:
    """
    #try:
        #if archivo not emtpy:
            #append item
        #else:
            #save_all_response
    #except:
    archivo = open(path_xml, "a", encoding="utf-8")
    archivo.write(noticias)

def borrar_noticia():
    """
    se encarga de borrar una noticia del xml que trae el response
    :return:
    """
def noticia_repetida(path_xml, noticia):
    noticias_obtenidas = get_noticias(path_xml)


    for titulos_fechas_noticia in get_titulos_fechas(noticias_obtenidas):
        titulo_noticia_guardada = titulos_fechas_noticia[0]
        titulo_noticia_nueva = noticia.find('title').text
        fecha_noticia_guardada = titulos_fechas_noticia[1]
        fecha_noticia_nueva = noticia.find('pubDate').text
        if titulo_noticia_nueva == titulo_noticia_guardada or fecha_noticia_guardada == fecha_noticia_nueva:
            return True
    return False

def read_xml(archivo):
    pass

def get_noticias(xml_path):

    tree = ET.parse(xml_path)
    root = tree.getroot()
    channel = root.find('channel')
    noticias = channel.findall('item')

    return noticias

def get_titulos_fechas(noticias):
    """
    :param noticias: recibe una lista de noticias las cuales analizara su contenido
    :return: retorna una lista de tuplas que contendran el titulo y la fecha de cada noticia
    """
    for noticia in noticias:
        titulo = noticia.find('title').text
        fecha = noticia.find('pubDate').text
        yield titulo, fecha



# if __name__ == '__main__':
#     for noticia in get_noticias("/home/agonzalez/tp2-estructuras/noticias/clarin/deportes/deportes.xml"):
#         noticia.