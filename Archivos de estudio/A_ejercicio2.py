#Archivos CSV 
import csv


with open ('Archivo_preuba.csv') as file:
    reader = csv.reader(file)
    
for row in reader:
    print()
    
        