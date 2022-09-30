import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosTamesis=tablaMunicipios[tablaMunicipios["Ciudad"]=="Tamesis"]
print(datosTamesis)