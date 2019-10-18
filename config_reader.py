import recolector
try:
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser
from pathlib import Path
config = ConfigParser()
config.read("config.ini")



#### imprime todos los items de todas las secciones
def imprimir_secciones():
    lista_de_secciones = []

    for section in config.sections():

        if section != "default":
            url_base = config.get(section,"url_base")
            for item in config.items(section):
                print(item)
                path = "noticias" + "/" + section + "/" + item[0] + "/"
                if item[1] != url_base:
                    print(path)
                    crear_carpetas_xml("noticias",section,item[0],path)
                    # item[1] corresponde a la url de cada seccion,
                    # indicamos que sea distinto a la urlbase para que no se agregue a la lista
                    if item[1] != url_base and len(item[0]) < 3:
                        recolector.print_xml(path + item[0], url_base + item[1])
                    else :
                        print(item[1][-3:])
                        if item[1] != url_base and item[1][-3:] != "xml":
                            recolector.print_xml(path + item[0], url_base + item[1])


    #return lista_de_secciones
##################################################
#crea los directorios de manera recursiva, si ya estan creados no hace nada
#prepara la ruta del archivo y lo guarda en la carpeta
def crear_carpetas_xml(carpeta_1,carpeta_2,carpeta_3,ruta):
    Path(carpeta_1,carpeta_2,carpeta_3).mkdir(parents=True, exist_ok=True)


imprimir_secciones()


