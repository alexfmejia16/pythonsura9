import csv
import pandas as pd

tabla=pd.read.csv('./Siembras.csv')

#tabla de estadisticas 
tablaEstadisticas=tabla.describe()


#solo obtener medias de la tabla estadisticas (solo 1 fila)

tablaMedias=tablaEstadisticas.loc[['mean']]

#solo obtener los datos de una columna. 
tablaMediasAboles=tablaMedias["Arboles"].to_frame()