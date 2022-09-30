import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosCaldas=tablaMunicipios[tablaMunicipios["Ciudad"]=="Caldas"]
print(datosCaldas)