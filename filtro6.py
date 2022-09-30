import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosMedellin=tablaMunicipios[tablaMunicipios["Ciudad"]=="Medellín"]
datosordenados=datosMedellin.sort_values(by="Arboles")


print(datosordenados)