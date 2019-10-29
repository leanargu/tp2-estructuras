import requests
import config_reader as cr
import xml_helper as xml
import file_managger as fm
from xml.etree import cElementTree as ET

'''
El recolector es el encargado de obtener los los resultados de los request (xml)
y colocarlos en el archivo correspondiente.
'''


def get_noticias(url):
    """
    :param url: link del RSS
    :return: retornará el response del url en formato xml y con codificación UTF-8
    """
    response = requests.get(url).content.decode('utf-8')
    return response

def guardar_noticia(medio, seccion):
    """
    :param medio:
    :param seccion:
    :return: guarda las noticias filtrandolas por lo requerido
    """
    path_xml = fm.get_path_xml(medio, seccion)
    url = cr.get_link(medio, seccion)
    noticias_get = get_noticias(url)

    tree = ET.ElementTree(ET.fromstring(noticias_get))
    root = tree.getroot()
    channel = root.find('channel')
    noticias = channel.findall('item')


    for noticia in noticias:
        if not xml.noticia_repetida(path_xml, noticia):
            root.remove(root.find('item'))
        xml.write_xml(path_xml, noticias)




def guardar_todas_las_noticias():
    medios = cr.get_medios()

    for medio in medios:
        secciones = cr.get_secciones_por_medio(medio)
        for seccion in secciones:
            guardar_noticia(medio, seccion)


if __name__ == '__main__':
    fm.crear_archivos()
    guardar_todas_las_noticias()
