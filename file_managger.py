'''
file_managger es el encargado de gestionar, y crear las carpetas
'''
import os
import config_reader as cr

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/noticias/"


def crear_carpeta_medios():
    """
    crea las carpetas segun todos los medios en el archivo config.ini
    """
    medios = cr.get_medios()
    for medio in medios:
        directorio = ROOT_DIR + medio
        try:
            os.makedirs(directorio, exist_ok=True)
        except OSError:
            print("La creación del directorio %s falló" % directorio)
        else:
            print("Se ha creado el directorio: %s " % directorio)


def crear_carpetas_secciones():
    """
    crea las carpetas detro de su medio correspondiente
    :return:
    """
    medios = cr.get_medios()

    for medio in medios:
        secciones = cr.get_secciones_por_medio(medio)
        for seccion in secciones:
            directorio = ROOT_DIR + medio + "/" + seccion
            try:
                os.mkdir(directorio)
            except OSError:
                print("La creación del directorio %s falló" % directorio)
            else:
                print("Se ha creado el directorio: %s " % directorio)

def crear_archivo_xml():
    """
    crea los archivos xml para cada seccion
    :return:
    """
    medios = cr.get_medios()
    for medio in medios:
        secciones = cr.get_secciones_por_medio(medio)
        for seccion in secciones:
            xml_path = get_path_xml(medio, seccion)
            f = open(xml_path, "w+")
            f.close()

def crear_archivos():
    """
    invoca la creacion de carpetas y archivos xml
    :return:
    """
    crear_carpeta_medios()
    crear_carpetas_secciones()
    crear_archivo_xml()


def get_path_xml(medio, seccion):
    xml_path = ROOT_DIR + medio + "/" + seccion + "/" + seccion + ".xml"

    return xml_path


if __name__ == '__main__':
    get_path_xml('clarin', 'deportes')
