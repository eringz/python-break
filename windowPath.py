import csv
from pathlib import Path
import os

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Ron', 36])
    writer.writerow(['Eringz', 36])
    

os.startfile(Path.cwd() / 'data.csv')
    