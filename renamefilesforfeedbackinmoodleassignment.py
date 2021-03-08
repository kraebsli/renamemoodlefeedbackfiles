from csv import reader
import os
import re
 # available in Python 2.5 and newer

# input file path and name 
#bewertungstabelle
path1='C:\\Users/........../1/';
#dateien
path2='C:\\Users/............../2/';
liste1=[]#ids
liste2=[]#namen
liste3=[]#matrikelnummer
zahl=0;
filename="tabelle.csv";
datei=path1+filename;
files = os.listdir(path2);
#bewertungstabelle auslesen
with open(datei) as csvfile:
    readCSV = reader(csvfile);
    for row in (readCSV):
        ids=row[0];
        ids=ids.replace('Teilnehmer/in','');
        liste1.append(ids);
        nam=row[1];
        liste2.append(nam);
        matrikel=row[2];
        liste3.append(matrikel);
		
#dateien umbenennen			
for file in (files):
    zahl=0;
    #match nach Name, kann aber mit matrikelnummer abgeglichen werden
    for item in liste2:
        
        if re.match(item, file):
       
            newname=liste2[zahl]+"_"+liste1[zahl]+"_assignsubmission_file_"+str(zahl)+".pdf";
            
            os.rename(os.path.join(path, file), os.path.join(path, newname))
        zahl+=1
