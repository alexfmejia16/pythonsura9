import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosYarumal=tablaMunicipios[tablaMunicipios["Ciudad"]=="Yarumal"]
print(datosYarumal)