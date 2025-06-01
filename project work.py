#Starting with my project
#School Management



import mysql.connector as sqltor
db_password = input("Enter your MySQL password:")
myconn = sqltor.connect(host = 'localhost',user = 'root',passwd = "{}".format(db_password))
mycur = myconn.cursor(buffered = True)
mycur.execute('Use project')
mycur.execute('Create table if not exists Basic_info_student(Admission_No int Primary key,Name varchar(50) Not null, Class varchar(8), DOB varchar(20), Gender varchar(14),Email varchar(40), Address varchar(50),Contact_no bigint)')




#Student's information
def studentinfo():
    try:
        Admn = int(input('Enter the admission number of student:'))
        Name = input('Enter the name of student:')
        Class = input('Enter the class(along with section):')
        DOB = input('Enter date of birth:')
        Gender = input('Enter the gender of student:')
        Email = input('Enter email id:')
        Address = input('Enter address of student:')
        Cont = int(input('Enter contact number of student:'))
        mycur.execute("insert into Basic_info_student values({},'{}','{}','{}','{}','{}','{}',{})".format(Admn,Name,Class,DOB,Gender,Email,Address,Cont))
        myconn.commit()
        print('Data added successfully')
    except:
        print('Error!,Try again')
#studentinfo()




    
#Updating Student's data
def updatestudent():
    try:
        print('Parameters to update:\n1.Name\n2.Class\n3.DOB\n4.Gender\n5.Email\n6.Address\n7.Contact number')
        Admn = int(input('Enter admission number of student:'))
        ch = int(input('Enter your choice:'))
        
        if ch==1:
            Name = input('Enter new name:')
            mycur.execute("Update Basic_info_student set Name = '{}' where Admission_No = {}".format(Name,Admn))
            myconn.commit()
        elif ch==2:
            Class = input('Enter new class:')
            mycur.execute("Update Basic_info_student set Class = '{}' where Admission_No = {}".format(Class,Admn))
            myconn.commit()
        elif ch==3:
            DOB = input('Enter correct date of birth:')
            mycur.execute("Update Basic_info_student set DOB = '{}' where Admission_No = {}".format(DOB,Admn))
            myconn.commit()
        elif ch==4:
            Gender = input('Enter the gender(correct) of student:')
            mycur.execute("Update Basic_info_student set Gender = '{}' where Admission_No = {}".format(Gender,Admn))
            myconn.commit()
        elif ch==5:
            Email = input('Enter the correct Email:')
            mycur.execute("Update Basic_info_student set Email = '{}' where Admission_No = {}".format(Email,Admn))
            myconn.commit()
        elif ch==6:
            Address = input('Enter correct Address:')
            mycur.execute("Update Basic_info_student set Address = '{}' where Admission_No = {}".format(Address,Admn))
            myconn.commit()
        elif ch == 7:
            Contact = int(input('Enter correct phone number:'))
            mycur.execute("Update Basic_info_student set Contact_No = {} where Admission_No = {}".format(Contact,Admn))
            myconn.commit()
        else:
            print('Wrong choice! Try again')
    except:
        print('Error!,Try again')

#updatestudent()





#Guardian's information table creation
mycur.execute('Create table if not exists Guardian_info(Admno_of_ward int,Name_of_ward varchar(40) NOT NULL,Father_name varchar(40) NOT NULL,Mother_name varchar(40) NOT NULL, Father_occupation varchar(20),Mother_occupation varchar(40))')
def Guardianinfo():
    try:
        mycur.execute('Select Admission_No from Basic_info_student')
        Admn = int(input('Enter the admission number of existing student:'))
        for i in mycur:
            if Admn in i:
                print('Student found! You may proceed')
                Nm = input('Enter the name of student:')
                Fname = input("Enter father's name:")
                Mname = input("Enter mother's name:")
                Focc = input("Enter father's occupation:")
                Mocc = input("Enter mother's occupation:")
                mycur.execute("insert into Guardian_info values({},'{}','{}','{}','{}','{}')".format(Admn,Nm,Fname,Mname,Focc,Mocc))
                myconn.commit()
    except:
        print('Error, Try again!')
        #Some beautiful finishing required here toooooo
#Guardianinfo()



#Updating Guardian's data
def UpdateGuardian():
    try:
        Admn = int(input('Enter the admission number of student:'))
        print("Parameters to change:\n1.Father's name\n2.Mother's name\n3.Father's occupation\n4.Mother's occupation")
        ch = int(input('Enter your choice:'))        
        if ch ==1:
            Fn = input("Enter father's name(corrected)")
            mycur.execute("Update Guardian_info set Father_name = '{}' where Admno_of_ward = {}".format(Fn,Admn))
            myconn.commit()
        elif ch==2:
            Mn = input("Enter mother's name(corrected):")
            mycur.execute("Update Guardian_info set Mother_name = '{}' where Admno_of_ward = {}".format(Mn,Admn))
            myconn.commit()
        elif ch==3:
            Fo = input("Enter father's occupation:")
            mycur.execute("Update Guardian_info set Father_occupation = '{}' where Admno_of_ward = {}".format(Fo,Admn))
            myconn.commit()
        elif ch==4:
            Mo = input("Enter mother's occupation:")
            mycur.execute("Update Guardian_info set Mother_occupation = '{}' where Admno_of_ward = {}".format(Mo,Admn))
            myconn.commit()
        else:
            print('Wrong choice! Try again')
        print('Value submitted in wrong format, try again!')
    except:
        print('Error! Try again')




#Creating Teacher's information table
mycur.execute('create table if not exists Teacher_info(Teacher_ID int Primary Key,Name_of_Teacher varchar(40) NOT NULL,Mastered_subject varchar(25),Date_of_joining varchar(30),Teaching_experience int,Salary int)')
def Teacherinfo():
    try:
        ID = int(input('Enter teacher id:'))
        Name = input("Enter teacher's name:")
        Sub = input("Enter the subject in which the teacher is proficient:")
        DOJ = input('Enter date of joining:')
        Exp = int(input('Enter teaching experience:'))
        Salary = int(input('Enter salary:'))
        mycur.execute("insert into Teacher_info values({},'{}','{}','{}',{},{})".format(ID,Name,Sub,DOJ,Exp,Salary))
        myconn.commit()
        print('Data added successfully')
    except:
        print('Error!Try again')
#Teacherinfo()



#Update Teacher's data
def updateteacher():
    try:
        ID = int(input('Enter teacher id:'))
        mycur.execute('Select Teacher_ID from Teacher_info')
        for i in mycur:
            if ID in i:
                print('Teacher found! You may proceed')
                print('Parameters to update:\n1. Name\n2. Mastered subject\n3. Date of joining\n4. Teaching experience\n5. Salary')
                ch = int(input('Enter your choice:'))
                if ch ==1:
                    name = input('Enter the name(corrected):')
                    mycur.execute("Update Teacher_ID set Name_of_Teacher = '{}' where Teacher_ID = {}".format(name,ID))
                    myconn.commit()
                elif ch == 2:
                    sub = input('Enter the mastered subject(updated):')
                    mycur.execute("Update Teacher_ID set Mastered_subject = '{}' where Teacher_ID = {}".format(sub,ID))
                    myconn.commit()
                elif ch==3:
                    doj = input('Enter date of joining:')
                    mycur.execute("Update Teacher_ID set Date_of_joining = '{}' where Teacher_ID = {}".format(doj,ID))
                    myconn.commit()
                elif ch ==4:
                    exp = int(input('Enter teaching experience:'))
                    mycur.execute("Update Teacher_ID set Teaching_experience = '{}' where Teacher_ID = {}".format(exp,ID))
                    myconn.commit()
                elif ch==5:
                    salary = int(input('Enter updated salary:'))
                    mycur.execute("Update Teacher_ID set Salary = {} where Teacher_ID = {}".format(salary,ID))
                    myconn.commit()
                else:
                    print('Invalid choice')
    except:
        print('Error!,Try again')
                
            



mycur.execute('Create table if not exists TC_info(Admission_No int Primary key,Name varchar(50) Not null, Current_class varchar(8), DOB varchar(20), Gender varchar(14),Email varchar(40), Address varchar(50),Contact_no bigint,Date_of_omission varchar(30),Session_year varchar(15))')
#TC related issue
def tclist():
    try:
        Admn = int(input('Enter the admission number of student whose TC is to be made:'))
        mycur.execute('Select Admission_No from basic_info_student')
        delta = mycur.fetchall()
        for i in delta:
            if Admn in i:
                print('Student found! You may proceed')
                mycur.execute('select * from basic_info_student where Admission_No = {}'.format(Admn))
                L = []
                for k in mycur:
                    for g in k:
                        L.append(g)   #List of data of student whose Transfer Certificate is to be made
                Admn = L[0]
                Name = L[1]
                Class = L[2]
                DOB = L[3]
                Gender = L[4]
                Email = L[5]
                Address = L[6]
                Contact = L[7]
                DOO = input('Enter the date of omission of student from school:')
                SYear = input('Enter session year:')
                mycur.execute('Delete from basic_info_student where Admission_No = {}'.format(Admn))
                myconn.commit()
                mycur.execute("insert into TC_info values({},'{}','{}','{}','{}','{}','{}',{},'{}','{}')".format(Admn,Name,Class,DOB,Gender,Email,Address,Contact,DOO,SYear))
                myconn.commit()
                print('Changes made successfully')
    except:
        print('Error!, try again')
            

# No of students
def nofstudents():
    try:
        cl = input('Enter the class:')
        mycur.execute("Select count(*) from basic_info_student where class = '{}'".format(cl))
        s = mycur.fetchone()
        for i in s:
            print('No of students:',i)
    except:
        print('Error!, Try again')

#Printing details of an individual student
def detailstu():
    try:
        Admn = int(input('Enter the admission number of student:'))
        mycur.execute('Select Admission_No from basic_info_student')
        for i in mycur:
            if Admn in i:
                print('Student found')
                mycur.execute('Select * from basic_info_student where Admission_No = {}'.format(Admn))
                s = mycur.fetchone()
                print('Admission Number:',s[0])
                print('Name:',s[1])
                print('Class:',s[2])
                print('DOB:',s[3])
                print('Gender:',s[4])
                print('Email id:',s[5])
                print('Address:',s[6])
                print('Contact Number:',s[7])
    except:
        print('Error!, Try again')

#printing details of student's guardian
def detailguardian():
    try:
        Admn = int(input('Enter the admission number of student:'))
        mycur.execute('Select Admno_of_ward from guardian_info')
        for i in mycur:
            if Admn in i:
                print('Student found')
                mycur.execute('Select * from guardian_info where Admno_of_ward = {}'.format(Admn))
                s = mycur.fetchone()
                print('Admission number of student:',s[0])
                print('Name of student:',s[1])
                print("Father's name:",s[2])
                print("Mother's name:",s[3])
                print("Father's occupation:",s[4])
                print("Mother's occupation:",s[5])
    except:
        print('Error!, Try again')



#Printing teacher's details
def teacherdetail():
    try:
        ID = int(input("Enter teacher's ID:"))
        mycur.execute('select Teacher_id from teacher_info')
        for i in mycur:
            if ID in i:
                print('Teacher found')
                mycur.execute('Select * from teacher_info where teacher_id = {}'.format(ID))
                s = mycur.fetchone()
                print("Teacher's ID:",s[0])
                print('Name:',s[1])
                print('Mastered subject:',s[2])
                print('Date of joining:',s[3])
                print('Teaching experience:',s[4])
                print('Salary:',s[5])
    except:
        print('Error!,Try again')
    
while True:
    try:
        print('------------Welcome!----------------')
        print("-----******Choose the one upon which you want to bring change******-----------\nA. STUDENT \nB. GUARDIAN\
        \nC.TEACHER")
        C = input('Enter your choice (out of A,B,C):')
        if C == 'A':
            while True:
                print('----------Functions to work upon----------------\n1. Adding a student(new admission)\n2. Updating data of a student\n3. Remove a student(if in case he/she has taken TC)\
                \n4. Know the number of students in a class\n5. Know the details of a student')
                ch = int(input('Enter your choice:'))
                if ch ==1:
                    studentinfo()
                elif ch==2:
                    updatestudent()
                elif ch==3:
                    tclist()
                elif ch==4:
                    nofstudents()
                elif ch==5:
                    detailstu()
                else:
                    print('Invalid choice')
                K = input('Do you want to exit from student portal?(Y/N)')
                if K not in 'Nn':
                    break
            
                
        elif C == 'B':
            while True:
                print("-------------Functions to work upon---------------\n1. Add Guardian info\n2. Update Guardian info\n3. Printing details of a student's guardian") 
                ch = int(input('Enter your choice:'))
                if ch==1:
                    Guardianinfo()
                elif ch==2:
                    UpdateGuardian()
                elif ch==3:
                    detailguardian()
                else:
                    print('Invalid choice')
                K = input('Do you want to exit from guardian portal?(Y/N)')
                if K not in 'Nn':
                    break
                
        elif C == 'C':
            while True:
                print("-------------Functions to work upon---------------\n1. Add a teacher\n2. Update teacher info\n3. Printing details of teacher")
                ch = int(input('Enter your choice:'))
                if ch==1:
                    Teacherinfo()
                elif ch==2:
                    updateteacher()
                elif ch==3:
                    teacherdetail()
                K = input('Do you want to exit from teacher portal?(Y/N)')
                if K not in 'Nn':
                    break
        else:
            print('Invalid choice!')
        kt = input('Do you want to continue?(Y/N)')
        if kt not in 'Yy':
            break
    except:
        print('Error!, try again')
        

    
    

