import recolector
import xml_helper as xml

try:
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser

'''
config_reader se encarga de leer el archivo config.ini donde se encuentran la informacion
para armar los links RSS y la configuracion correspondiente a las llamadas de los request
'''
config = ConfigParser()
config.read("config.ini")


def get_medios():
    """
    :return: retorna una lista con los medios que hay en el archivo config.ini
    """

    lista_medios = []
    sections = config.sections()
    for medio in sections:
        if medio != "default":
            lista_medios.append(medio)

    return lista_medios


def get_secciones_por_medio(medio):
    """
    :param medio: es el medio de comunicacion al cual se le va a consultar sus secciones
    :return: retorna una lista con las secciones que tiene cada medio de comunicación
    """
    lista_secciones = []
    medio = config.items(medio)
    for seccion in medio:
        if seccion[0] != "url_base":
            lista_secciones.append(seccion[0])

    return lista_secciones


def get_todas_secciones():
    """
    :return: retorna una lista con todas las secciones de todos los medios existentes en el archivo config.ini
    """
    lista_secciones = []
    medios = get_medios()

    for medio in medios:
        secciones = get_secciones_por_medio(medio)
        for seccion in secciones:
            lista_secciones.append(seccion)

    return lista_secciones


def get_default():
    default = {}


def get_link(medio_comunicacion, seccion):
    """
    :param medio_comunicacion:
    :param seccion:
    :return: url completa (url base + el path del rss)
    """
    url_base = config.get(medio_comunicacion, "url_base")
    path_rss = config.get(medio_comunicacion, seccion)

    url = url_base + path_rss

    return url


def get_all_links_rss():
    """
    :return: retorno una lista con todos los links completos de los rss.
    """

    lista_url = []
    medios = get_medios()

    for medio in medios:
        secciones = get_secciones_por_medio(medio)
        for seccion in secciones:
            url = get_link(medio, seccion)
            lista_url.append(url)

    return lista_url


if __name__ == '__main__':
    print(get_all_links_rss())
