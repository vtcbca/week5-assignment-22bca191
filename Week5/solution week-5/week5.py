Attribute=['sid','sname','city','contect_no']
records=[[1,'sunny patel','vyara',9856432456],
         [2,'rohit sharma','bajipura',9964789098],
         [3,'rahul soni','surat',6543789090],
         [4,'gaurav aahire','bardoli',8469546134],
         [5,'malav patel','bharuch',9312477895]]
list=[]
for i in range(5):
    no=int(input(" Enter Student ID: "))
    sname=input(" Enter Student Name: ")
    city=input(" Enter city of student: ")
    contect_no=int(input(" Enter Student Contect_no: "))
    l=[no,sname,city,contect_no]
    list.append(l)

import csv
with open('student.csv','w',newline='')as cfile:
    file=csv.writer(cfile)
    file.writerow(Attribute)
    file.writerow(records)
    file.writerows(l)


import csv
with open('student.csv','r',newline='')as read_obj:
    all_records=csv.reader(read_obj)
    for records in all_records:
        print(records)
    
