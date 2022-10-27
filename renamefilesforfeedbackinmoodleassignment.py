from csv import reader
import os
import re
 # available in Python 2.5 and newer

#input file path and name 
#grading worksheet
path1='1/';
#files to be renamed
path2='2/';
liste1=[]#ids used as part of the name of the files to be uploaded
liste2=[]#namen
liste3=[]#matrikelnummer
zahl=0;
filename="table.csv";
datei=path1+filename;
files = os.listdir(path2);
#read table
with open(datei) as csvfile:
    readCSV = reader(csvfile);
    for row in (readCSV):
        matrikel=row[2];
        ids=row[0];
        nam=row[1];

   
        if  matrikel =="":
            # use Participant in English or Word according to the language the moodle course is set to.
            
            print ("no ID for "+nam+"\n");
        else:
            
            ids=ids.replace('Teilnehmer/in','');
            liste1.append(ids);
            liste2.append(nam);
            liste3.append(matrikel);
		
			
for file in (files):
    zahl=0;
    #match to id number / nach Matrikel
    
    for item in liste3:
      
        if re.search(item, file):
            
            newname=liste2[zahl]+"_"+liste1[zahl]+"_assignsubmission_file_"+str(zahl)+".pdf";
            
            os.rename(os.path.join(path2, file), os.path.join(path2, newname))
            break
        zahl+=1
            
