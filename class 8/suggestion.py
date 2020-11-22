# write string one by one adding newline
with open('dog.txt', 'w') as my_file:
    [ my_file.write(f'{st}\n') for st in list_of_strings ]
import csv

dict = {'Python' : '.py', 'C++' : '.cpp', 'Java' : '.java'}
w = csv.writer(open("output.csv", "w"))
for key, val in dict.items():
    w.writerow([key, val])