import os
import csv

#print("Directorio actual", os.getcwd())

with open("./world_population.csv") as file:
    reader = csv.reader(file)
    print(list(reader))