import csv
import array
import pandas
import numpy as np

con = []
q =input("Enter your registration number.")



with open('/content/result_TVE.csv','rt')as f:
    data = csv.reader(f)
    for row in data:
        con.append(row)
#for t in range(50,700):
    #for i in con[t]:
      #ir=[]
      #ir.append(i[6:8])




for i in range(60,847):

     for t in con[i]:
       ir = []
       ir.append(t[0:10])

       if(ir[0]==q):
           x=i
           for t in con[x]:
               ip = []
               iw =[]
               ib =[]
               ic =[]
               id =[]
               ig =[]
               ih =[]
               ij =[]
               ip.append(t[6:8])
               iw.append(t[16:18])
               ib.append(t[26:30])
               ic.append(t[36:40])
               id.append(t[46:50])
               ig.append(t[56:60])
               ih.append(t[66:70])
               ij.append(t[76:80])

           p = ip[0]
           w = iw[0]
           b = ib[0]
           c = ic[0]
           d = id[0]
           g = ig[0]
           h = ih[0]
           j = ij[0]

for a in p:
    if(a.isalpha()):
        grade1=a

for a in w:
    if (a.isalpha()):
        grade2 = a
for a in b:
    if (a.isalpha()):
        grade3 = a
for a in c:
    if (a.isalpha()):
        grade4 = a
for a in d:
    if (a.isalpha()):
        grade5 = a
for a in g:
    if (a.isalpha()):
        grade6 = a
for a in h:
    if (a.isalpha()):
        grade7 = a

for a in j:
    if (a.isalpha()):
        grade8 = a


lis = np.array([4,4,3,3,1,1,1,4])
lis2 =[grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8]

if(grade1=='O'):
    g1=10
if(grade1=='A'):
    g1=8.75
if(grade1=='B'):
    g1=7.5
if(grade1=='C'):
    g1=6
if(grade1=='P'):
    g1=5
if(grade1=='F'):
    g1=0



if(grade2=='O'):
    g2=10
if(grade2=='A'):
    g2=8.75
if(grade2=='B'):
    g2=7.5
if(grade2=='C'):
    g2=6
if(grade2=='P'):
    g2=5
if(grade2=='F'):
    g2=0



if(grade3=='O'):
    g3=10
if(grade3=='A'):
    g3=8.75
if(grade3=='B'):
    g3=7.5
if(grade3=='C'):
    g3=6
if(grade3=='P'):
    g3=5
if(grade3=='F'):
    g3=0


if(grade4=='O'):
    g4=10
if(grade4=='A'):
    g4=8.75
if(grade4=='B'):
    g4=7.5
if(grade4=='C'):
    g4=6
if(grade4=='P'):
    g4=5
if(grade4=='F'):
    g4=0


if(grade5=='O'):
    g5=10
if(grade5=='A'):
    g1=8.75
if(grade5=='B'):
    g5=7.5
if(grade5=='C'):
    g5=6
if(grade5=='P'):
    g5=5
if(grade5=='F'):
    g5=0


if(grade6=='O'):
    g6=10
if(grade6=='A'):
    g6=8.75
if(grade6=='B'):
    g6=7.5
if(grade6=='C'):
    g6=6
if(grade6=='P'):
    g6=5
if(grade6=='F'):
    g6=0


if(grade7=='O'):
    g7=10
if(grade7=='A'):
    g7=8.75
if(grade7=='B'):
    g7=7.5
if(grade7=='C'):
    g7=6
if(grade7=='P'):
    g7=5
if(grade7=='F'):
    g7=0


if(grade8=='O'):
    g8=10
if(grade8=='A'):
    g8=8.75
if(grade8=='B'):
    g8=7.5
if(grade8=='C'):
    g8=6
if(grade8=='P'):
    g8=5
if(grade8=='F'):
    g8=0

lis3=[g1,g2,g3,g4,g5,g6,g7,g8]
ar = np.asarray(lis3)
newar = ar*lis
s =sum(newar)


gpa=(s/210)*10
print(gpa)
