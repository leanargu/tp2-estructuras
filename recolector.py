import requests
import config_reader

'''
El recolector es el encargado de obtener los los resultados de los request (xml)
y colocarlos en el archivo correspondiente.
'''

def print_xml(nombre_archivo,url):
    archivo = open(nombre_archivo + ".xml", "a")
    response = requests.get(url).content.decode('utf-8')
    archivo.write(response)

def imprimir_todo():
    for url in config_reader.imprimir_secciones():
        print_xml(url)












