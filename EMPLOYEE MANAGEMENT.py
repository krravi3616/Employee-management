print('\n')
print('     |||***Welcome to Employee Management App***|||')
print('     ==============================================')
print('\n')
def start ():
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print('press - 1 - to start')
    print('press - 2 - to Exit from program')
    print('@@@@@@@@@@@@@@@@@@@@@@')
    print('\n')
    while 8==8:
            v=int(input('enter your choice :'))
            print('\n')
            if v==1:
                employee()
            elif v==2:
                
                print('thank you for using PYTHON application ')
                exit()
            else:
                
                print('sorry, wrong input given, please try again')

def employee ():
        print('*EMPLOYEE MANAGEMENT pannel*')
        print('####################################################')
        print('press - 1 - to Insert Employee Details')
        print('press - 2 - to list to employee details')
        print('press - 3 - to search Employee by Employee - ID')
        print('press - 4 - to search Employee Details on bassic-salary')
        print('press - 5 - to Delete Employee Details')
        print('press - 6 - to show Employee Management Pannel Menu')
        print('press - 7 - to back')
        print('press - 8 - to Exit from Program')
        print('####################################################')
        print('*-\n')
        while 10==10:
                 a=int(input('enter your choice :'))
                 print('\n')
                 if a==1:
                         insert()
                 elif a==2:
                        show()
                 elif a==3:
                        search()
                 elif a==4:
                        salary()
                 elif a==5:
                        delete()
                 elif a==6:
                        employee()
                 elif a==7:
                        start()
                 elif a==8:
                        print('    |||***Thank you for using python application***|||')
                        print('    ==================================================')
                        exit()
                 else:
                        print('SORRY, Wrong input given, please Try again..')
z=[]

def insert():
         print('please insert employee details')
         print('------------------------------')
         print('\n')
         empid=int(input('enter employee-ID :'))
         name=input('enter employee-name:')
         designation=input('Enter employee-Designation :')
         salary=int(input('enter employee-salary :'))
         dob=input('enter employee-DOB :')
         doj=input('enter employee-DOJ :')
         z.append([empid,name,designation,salary,dob,doj])
def show ():
        for x in range(len(z)):
                print('employee details')
                print('----------------')
                print('Employee-ID :',z[x][0])
                print('Employee-Name :',z[x][1])
                print('Employee-Designation :',z[x][2])
                print('Employee-Salary :',z[x][3])
                print('Employee-Date-of-Birth :',z[x][4])
                print('Employee-Date-of-Joining :',z[x][5])

def search ():
    s=int(input('Enter Emp-ID:'))
    for x in range(len(z)):
        if s==z[x][0]:
            print('Employee Details for the Emp-ID:',s)
            print('---------------------------------')
            print('Employee-ID :',z[x][0])
            print('Employee-Name :',z[x][1])
            print('Employee-Designation :',z[x][2])
            print('Employee-Salary :',z[x][3])
            print('Employee-Date-of-Birth :',z[x][4])
            print('Employee-Date-of-Joining :',z[x][5])

def salary():
    s1=int(input('Enter 1st salary range :'))
    s2=int(input('Enter 2nd salary range :'))
    for x in range(len(z)):
        if z[x][3]>=s1 and z[x][3]<=s2:
            print('Employee Details between Salary Range :',s1,'-',s2)
            print('---------------------------------------------------')
            print('Employee ID :',z[x][0])
            print('Employee-Name :',z[x][1])
            print('Employee-Designation :',z[x][2])
            print('Employee-Salary :',z[x][3])
            print('Employee-Date-of-Birth :',z[x][4])
            print('Employee-Date-of-Joining :',z[x][5])

def delete():
    d=int(input('Enter Emp-ID:'))
    for x in range(len(z)):
        if d==z[x][0]:
            print('Employee Details for the Emp-ID :',d)
            print('Employee-ID :',z[x][0])
            print('Employee-Name :',z[x][1])
            print('Employee-Designation :',z[x][2])
            print('Employee-Salary :',z[x][3])
            print('Employee-Date-of-Birth :',z[x][4])
            dd=input('Do you really want to delete[y/n] :')
            if dd=='y' or dd=='y':
                del z[x]
                print('Employee Details Deleted Successfully')
            else:
                print('Deletion Aborated')

     break

start()
employee()
                
                    

















            



















            
                
                
                















         
                              
                
                        

















        
        
