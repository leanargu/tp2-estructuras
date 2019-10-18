import requests
import config_reader

def print_xml(nombre_archivo,url):
    archivo = open(nombre_archivo + ".xml", "a")
    response = requests.get(url).content.decode('utf-8')
    archivo.write(response)

def imprimir_todo():
    for url in config_reader.imprimir_secciones():
        print_xml(url)












