import requests
import pandas as pd

#Cargar lista de palabras clave:
kwDF = pd.read_csv('frases.csv', header=None, names=['keyword']) # archivo sin encabezado
frases=[]
frases=kwDF['keyword'].tolist() #Colocar frases en una lista
data=[]#Lista que serà utilizada para presentaciòn de datos en DataFrame

#Realizar la predicciòn 
for mensaje in frases:
    r = requests.get("http://127.0.0.1:8080/prediccion/'%s'" % {mensaje}) #Hacer Request (Debe estàr corriendo flask)
    data.append(f' {mensaje}'+"," f' {r.json()['prediction']}')           #Guardar resultado en lista 
        
#Transformacion a Dataframe
header = ['Frase','Prediccion']
predic = pd.DataFrame([x.split(',') for x in data[0:] if x], columns=header)   
print(predic)