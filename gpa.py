


import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect(r"C:\Users\91739\Desktop\work\basic\work 1\1.db")
cursor = conn.cursor()

print("----------------------------------------------------------------------------")
print("----CGPA CALCULATOR FOR THIRD SEMESTER----")
print("----------------------------------------------------------------------------")
nn = int(input("1: FIND CGPA FOR THE STUDENTS \n 2: SURVEY OF THE CGPA \n\n ENTER THE CHOICE :::"))
print("if ypu get 'U' in any subject means cgpa score can't be calculated\n")

print("----------------------------------------------------------------------------")


#asssuming the subject credit points as default

m3 = 4
dbms = 3
coa = 3
oop = 3
ds = 4
dbms_lab = 2
oop_lab = 2
if nn==1:
    n = int(input("entr the number of student to calculate cgpa :"))
    print("***************************************************")
    print("\n----GRADE-----")
    print("\n ---(O :: 10)--- \n --(A+:: 9) --- \n ---(A :: 8) --- \n --(B+:: 7) --- \n ---(B:: 6) --- \n --(C+:: 5) ---")
    print("***************************************************")
    for i in range(n):
        name = input("enter the name:")
        reg = int(input("enter the register number :"))
        print("***************************************************************")
        print("--enter the opiton based on the grade you obtained---")
        print("\n*************************************************************\n")
        math = int(input("---mathematical fountation and computer science --- :"))
        DBMS = int(input("---database management system -- :"))
        COA = int(input("---computer organization architecture-- :"))
        OOP = int(input("---object oriented progrsmming--  :"))
        DS = int(input("---digital system --:"))
        DBMS_LAB = int(input("--DBMS LAB --:"))
        OOP_LAB = int(input("---OOP LAB-- :"))
        print("***************************************************************")

    # using lambda function

    # lamda function for m3

        step1 = lambda ma:m3 * ma
        s1 = step1(math)
    
    #lambda function for dbms
        step2 = lambda db:dbms * db
        s2 = step2(DBMS)

    #lambda function for coa
        step3 = lambda co:coa *co
        s3 = step3(COA)

    #lambda function for oop
        step4 = lambda oo:oop *oo
        s4 = step4(OOP)  

    #lambda function for ds
        step5 = lambda d:ds *d
        s5 = step5(DS)  

    #lambda function for dbmslab
        step6 = lambda dl:dbms_lab * dl
        s6 = step6(DBMS_LAB)

    #lambda function for ooplab
        step7 = lambda ol:oop_lab * ol 
        s7 = step7(OOP_LAB)

        print("++++++++++++++++++++++++++++++++++++++")

        cgpa =(s1+s2+s3+s4+s5+s6+s7)/21

        print("---CGPA:",cgpa,"---")

        print("---------------------------------------")
    

        sql = "insert into users (reg,name,mark) values(?,?,?);"

        cursor.execute(sql,(reg,name,cgpa))

        conn.commit()
        print('DATA ADDED TO THE DATABASE ')
    

if nn==2:

  sq1 = "select reg from users;"

  cursor.execute(sq1)

  reg1= cursor.fetchall()

  conn.commit()

  sq2 ="select mark from users;"
  cursor.execute(sq2)

  mark1 = cursor.fetchall()

  conn.commit()


  print('SURVEY OF CGPA REPRESENT IN GRAPH')

  figure = plt.figure()
  axes = figure.add_subplot(1,1,1)
  axes.stem(reg1,mark1)
  plt.show()



if nn==3:
    mark2=[]
    mark2.append (mark1)
    print(mark2)
