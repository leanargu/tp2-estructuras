import requests
from bs4 import BeautifulSoup
import config_reader

def print_xml(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    print(soup.prettify())

def imprimir_todo():
    for seccion in config_reader.imprimir_secciones():
        print_xml(seccion)

imprimir_todo()