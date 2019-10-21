import recolector
try:
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser
from pathlib import Path

'''
config_reader se encarga de leer el archivo config.ini donde se encuentran la informacion
para armar los links RSS y la configuracion correspondiente a las llamadas de los request
'''
config = ConfigParser()
config.read("config.ini")



# ### imprime todos los items de todas las secciones
# def imprimir_secciones():
#     lista_de_secciones = []
#
#     for section in config.sections():
#
#         if section != "default":
#             url_base = config.get(section,"url_base")
#             for item in config.items(section):
#                 print(item)
#                 path = "noticias" + "/" + section + "/" + item[0] + "/"
#                 if item[1] != url_base:
#                     print(path)
#                     crear_carpetas_xml("noticias",section,item[0],path)
#                     # item[1] corresponde a la url de cada seccion,
#                     # indicamos que sea distinto a la urlbase para que no se agregue a la lista
#                     if item[1] != url_base and len(item[0]) < 3:
#                         recolector.print_xml(path + item[0], url_base + item[1])
#                     else :
#                         print(item[1][-3:])
#                         if item[1] != url_base and item[1][-3:] != "xml":
#                             recolector.print_xml(path + item[0], url_base + item[1])


    #return lista_de_secciones
##################################################
#crea los directorios de manera recursiva, si ya estan creados no hace nada
#prepara la ruta del archivo y lo guarda en la carpeta
# def crear_carpetas_xml(carpeta_1,carpeta_2,carpeta_3,ruta):
#     Path(carpeta_1,carpeta_2,carpeta_3).mkdir(parents=True, exist_ok=True)

########################################################################################################

def get_medios():
    '''
    :return: retorna una lista con los medios que hay en el archivo config.ini
    '''

    lista_medios = []
    sections = config.sections()
    for medio in sections:
        if medio != "default":
            lista_medios.append(medio)

    return lista_medios

def get_secciones_por_medio(medio):
    '''
    :param medio: es el medio de comunicacion al cual se le va a consultar sus secciones
    :return: retorna una lista con las secciones que tiene cada medio de comunicación
    '''

    lista_secciones = []
    medio = config.items(medio)
    for seccion in medio:
        if seccion[0] != "url_base":
            lista_secciones.append(seccion[0])

    return lista_secciones

def get_todas_secciones():
    '''
    :return: retorna una lista con todas las secciones de todos los medios existentes en el archivo config.ini
    '''
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
    '''

    :param medio_comunicacion:
    :param seccion:
    :return:
    '''


def get_all_links_rss():
    '''
    :return: retorno una lista con todos los links completos de los rss.
    '''

    lista_url = []
    sections = config.sections()

    for medio in sections:
        if medio != 'default':
            url_base = config.get(medio, "url_base")

            medio_comunicacion = config.items(medio)

            for seccion in medio_comunicacion:
                rss_path = seccion[1]

                if rss_path != url_base:
                    url = url_base + rss_path
                    lista_url.append(url)
    return lista_url


if __name__ == '__main__':
    get_all_links_rss()
