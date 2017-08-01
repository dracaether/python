######################################################################################################################################
#                                                                                                                                    #
# this activity is intended only for students who were able to attend the makeup class in the laboratory session dated 31 July 2017. #
# despite not being a part of it, this is my attempt at solving this problem.                                                        #
#                                                                                                                                    #
#######################################################################################################################Erin Casseapey#

## define the values
c = 11800
p = 18500
t = 28750
sss = 150
pagibig = 100

## ask for input
name=input("Please enter the employee's name: ")
print("\t[1] Contractual")
print("\t[2] Probationary")
print("\t[3] Tenured")
status=input("What employment status?: ")

# conditions
if status == '1':
    print("Gross salary =",c)
    days=int(input("Enter the days for extra load: "))
    spd=c/23
    c2=c+(spd*days)
    print("Gross salary =",c2)
    sssc=c2-sss
    pic=c2-pagibig
    wt=c2*0.12
    print("Deductions:")
    print("\tSSS =",sssc)
    print("\tPagibig =",pic)
    print("\tWithholding tax =",wt)
    days_abs=int(input("Enter the number of days absent: "))
    if days_abs == 0:
        sssc=c2-sss
        pic=c2-pagibig
        wt=c2*0.12
        print("Deductions:")
        print("\tSSS =",sssc)
        print("\tPagibig =",pic)
        print("\tWithholding tax =",wt)
        net_salary=c2
        print("The net salary of",name,"with status\nContractual is:",net_salary)
    else:
        c2=c+((spd*days)/days_abs)
        sssc=c2-sss
        pic=c2-pagibig
        wt=c2*0.12
        print("Deductions:")
        print("\tSSS =",sssc)
        print("\tPagibig =",pic)
        print("\tWithholding tax =",wt)
        net_salary=c2
        print("The net salary of",name,"with status\nContractual is:",net_salary)
    
elif status == '2':
    print("Gross salary =",p)
    days=int(input("Enter the days for extra load: "))
    spd=p/23
    p2=p+(spd*days)
    print("Gross salary =",p2)
    sssp=p2-sss
    pip=p2-pagibig
    wt=p2*0.12
    print("Deductions:")
    print("\tSSS =",sssp)
    print("\tPagibig =",pip)
    print("\tWithholding tax =",wt)
    days_abs=int(input("Enter the number of days absent: "))
    if days_abs == 0:
        sssp=p2-sss
        pip=p2-pagibig
        wt=p2*0.12
        print("Deductions:")
        print("\tSSS =",sssp)
        print("\tPagibig =",pip)
        print("\tWithholding tax =",wt)
        net_salary=p2
        print("The net salary of",name,"with status\nProbationary is:",net_salary)
    else:
        p2=p+((spd*days)/days_abs)
        sssp=p2-sss
        pip=p2-pagibig
        wt=p2*0.12
        print("Deductions:")
        print("\tSSS =",sssp)
        print("\tPagibig =",pip)
        print("\tWithholding tax =",wt)
        net_salary=p2
        print("The net salary of",name,"with status\nProbationary is:",net_salary) 
    
elif status == '3':
    print("Gross salary =",t)
    days=int(input("Enter the days for extra load: "))
    spd=t/23
    t2=t+(spd*days)
    print("Gross salary =",t2)
    ssst=t2-sss
    pit=t2-pagibig
    wt=t2*0.12
    print("Deductions:")
    print("\tSSS =",ssst)
    print("\tPagibig =",pit)
    print("\tWithholding tax =",wt)
    days_abs=int(input("Enter the number of days absent: "))
    if days_abs == 0:
        ssst=t2-sss
        pit=t2-pagibig
        wt=t2*0.12
        print("Deductions:")
        print("\tSSS =",ssst)
        print("\tPagibig =",pit)
        print("\tWithholding tax =",wt)
        net_salary=t2
        print("The net salary of",name,"with status\nTenured is:",net_salary)
    else:
        t2=t+((spd*days)/days_abs)
        ssst=t2-sss
        pit=t2-pagibig
        wt=t2*0.12
        print("Deductions:")
        print("\tSSS =",ssst)
        print("\tPagibig =",pit)
        print("\tWithholding tax =",wt)
        net_salary=t2
        print("The net salary of",name,"with status\nTenured is:",net_salary)

else:
    print("Invalid input.")
    exit()
