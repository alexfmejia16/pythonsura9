import pandas as pd

tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados.to_string())


# filtro 1 quiero obtener todos los datos de los analistas 1
tablaAnalista1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)

archivoHTML=tablaAnalista1.to_html()
archivoTEXTO=open("datosanalistas1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

tablaAnalista2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalista2.to_html()
archivoTEXTO=open("datosanalistas2.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()