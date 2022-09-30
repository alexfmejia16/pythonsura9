import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')

datosCaucasia=tablaMunicipios[tablaMunicipios["Ciudad"]=="Caucasia"]
print(datosCaucasia)