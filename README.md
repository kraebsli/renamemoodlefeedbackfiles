# renamemoodlefeedbackfiles
Rename moodle feedback files for bulk upload in moodle assigment

Rename moodle feedback files for bulk upload in moodle assigment (if students did not use assignment for uploading). This is a python script which does the renaming of feedback files to bulk upload in moodle assignment. The source files, e.g. files to rename, should have an identifier, student name or student id, which can be used to match the files.

For renaming a reference file is used. This you get if you download the grading worksheet from the assignment. 

From this file the first three columns are needed:
column 1: identifier: the identifier is constructed with participant + the identifier
column 2: full name
column 3: id number (Matrikelnummer)


The Worksheet should be called tabelle.csv.

The line  ids=ids.replace('Teilnehmer/in',''); should be adapted according to the language settings of your moodle course, e.g. Participant in english.

The script analyzes the grading worksheet and puts the contents of the three columns in three different lists.

Then it goes through the files to be renamed and looks if the file name contains the id number. If this is the case the file is renamed following the pattern the moodle assignment requires: 
fullname_identifier_assignsubmission_file_filename

