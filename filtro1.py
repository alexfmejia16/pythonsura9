import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosAndes=tablaMunicipios[tablaMunicipios["Ciudad"]=="Andes"]
print(datosAndes)

'''archivoHTML=datosBarbosa.to_html()
archivoTEXTO=open("datosBarbosa.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()'''

