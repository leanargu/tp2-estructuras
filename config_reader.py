try:
    from ConfigParser import ConfigParser
except ImportError:
    # Python 3
    from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")



# ##### imprimir las secciones
# sections = config.sections()
# print("%d secciones:" % len(sections))  # Cantidad de secciones
# # Imprimimos cada una de ellas
# for section in config.sections():
#     print(section)
# ###################################
#
# ### trae un valor especifico de seccion / clave
# get_url = config.get("clarin", "lo_ultimo")
# print(get_url)
# ###############################################
#
# #### imprime todos los items por x seccion
# for item in config.items("clarin"):
#     print("clave: " + item[0], "valor: " + item[1])
# ###############################################

#### imprime todos los items de todas las secciones

for section in config.sections():
    if section != "default":
        print("\n[%s]" % section)
        url_base = config.get(section,"url_base")
        for item in config.items(section):
            if item[1] != url_base:
                print(url_base + item[1])
##################################################
