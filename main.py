import datetime
from art import *


tprint('Welcome to Vaccine\nRagistration Form',font='small')

next1 = datetime.date.today() + datetime.timedelta(days=1)
next2 = datetime.date.today() + datetime.timedelta(days=2)
next3 = datetime.date.today() + datetime.timedelta(days=3)

def bookvcc(name=1,password=1,email=1,nv=1,n=1,next=1,num2=1,toto = 1):
                                            t5 = True
                                            while t5 == True:
                                                cunovac = str(int(nv)-1)
                                                t5,t4,t3,t1 = False,False,False,False
                                                with open('data.txt','r') as data:
                                                    lines = data.readlines()
                                                    lines2 = []
                                                    for sub in lines:
                                                        lines2.append(sub.replace("\n", ""))
                                                    lines3 = lines2[op3].split(',')
                                                    del lines3[n]
                                                    lines3.insert(n,cunovac)
                                                    lines4 = ','.join(str(i) for i in lines3)+'\n'
                                                    lines.remove(lines[op3])
                                                    lines.insert(op3,lines4)
                                                with open('data.txt','w') as data:
                                                    data.writelines(lines)
                                                with open('data2.txt','r') as data2:
                                                    lines = data2.readlines()
                                                    needlines = lines[:-1]
                                                    lastline = needlines[-1]
                                                    lastline2 = []
                                                    for sub in lastline:
                                                        lastline2.append(sub.replace("\n", ""))
                                                    realneedlines = needlines[:-1]
                                                    for i in lastline2:
                                                        realneedlines.append(i)
                                                try:
                                                    if toto == 2:
                                                        name = logname
                                                        password = logpass
                                                        email = email2
                                                        phnum = phnum2
                                                        with open('data2.txt','r') as data2:
                                                            lines = data2.readlines()
                                                            del lines[ind2]
                                                            realneedlines = lines
                                                except Exception as e:
                                                    pass
                                                if toto == 1:
                                                    with open('data2.txt','w') as data2:
                                                        data2.writelines(realneedlines)
                                                    with open('data2.txt','a') as data2:
                                                        data2.writelines(f'\n{name},{password},{email},r,True,{next},{num2}')
                                                elif toto == 2:
                                                    with open('data2.txt','w') as data2:
                                                        data2.writelines(realneedlines)
                                                    with open('data2.txt','a') as data2:
                                                        data2.writelines(f'{name},{password},{email},r,True,{next},{num2}')     
                                                 
def book(name,password,email,to=1,num2=1,res = 0):
                                                    global op3
                                                    try:
                                                        with open('data.txt') as data:
                                                            lines = data.readlines()
                                                            lines2 = []
                                                            for sub in lines:
                                                                lines2.append(sub.replace("\n", ""))
                                                            hnames = []
                                                            for i in lines2:
                                                                hnames.append(i.split(',')[0])
                                                            unames = []
                                                            for i in lines2:
                                                                unames.append(i.split(',')[1])
                                                            pnames = []
                                                            for i in lines2:
                                                                pnames.append(i.split(',')[2])
                                                            n1vs = []
                                                            for i in lines2:
                                                                n1vs.append(i.split(',')[3])
                                                            n2vs = []
                                                            for i in lines2:
                                                                n2vs.append(i.split(',')[4])
                                                            n3vs = []
                                                            for i in lines2:
                                                                n3vs.append(i.split(',')[5])
                                                        
                                                        op3 = int(input('Choose Hospital: '))
                                                        num2 = op3
                                                        if 33 == 3:
                                                            print(f'no hospital on {op3} try again')
                                                        else:
                                                            n1v = n1vs[op3]
                                                            n2v = n2vs[op3]
                                                            n3v = n3vs[op3]
                                                            print(f'{next1} | {next2} | {next3} ')
                                                            print(f'    {n1v}           {n2v}            {n3v}          ')
                                                            print(f'(1 for) booking in {next1}\n(2 for) booking in {next2}\n(3 for) booking in {next3}\nselect date: ')
                                                            t14 = True
                                                            while t14 == True:
                                                                try:
                                                                    op5 = int(input())
                                                                    if op5 == 1:
                                                                        if to == 2:
                                                                            bookvcc(name,password,email,n1v,3,next1,num2,toto = 2)
                                                                            t14 = False
                                                                        else:
                                                                            bookvcc(name,password,email,n1v,3,next1,num2,toto = 1)
                                                                            t14 = False
                                                                    elif op5 == 2:
                                                                        if to == 2:
                                                                            bookvcc(name,password,email,n2v,4,next2,num2,toto = 2)
                                                                            t14 = False
                                                                        else:
                                                                            bookvcc(name,password,email,n2v,4,next2,num2,toto = 1)
                                                                    elif op5 == 3:
                                                                        if to == 2:
                                                                            bookvcc(name,password,email,n3v,5,next3,num2,toto = 2)
                                                                            t14 = False
                                                                        else:
                                                                            bookvcc(name,password,email,n3v,5,next3,num2,toto = 1)
                                                                            t14 = False 
                                                                    else:
                                                                        print('not a valid input')
                                                                except Exception as e:
                                                                    print('not a valid input')
                                                                    print(e)
                                                            print('Vaccine Succesfully Booked')
                                                    except Exception as e:
                                                        print('not a valid option')
                                                        print(e)
                                                    if res == 0:
                                                        pass
                                                    else:
                                                        pass    

while True:
    try:
        print('------------------------------\n\n(1 for) Enter as User\n(2 for) Exit.\n\n------------------------------\n')
        enter = int(input())

        if enter == 1:
            global logname
            global logpass
            global ind2
            global email2
            global phnum2
            t6 = True
            while t6 == True:
                print('(1 for) Loging In\n(2 for) Registering\n(3 for) Exiting')
                op = int(input())
                try:
                    if op == 1:
                        t15 = True
                        while t15==True:
                            try:
                                logname = input('Enter your loging username: ')
                                with open('data2.txt','r') as data2:
                                    lines = data2.readlines()
                                    lines2 = []
                                    for sub in lines:
                                        lines2.append(sub.replace("\n", ""))
                                    names = []
                                    for i in lines2:
                                        names.append(i.split(',')[0])
                                    if logname in names:
                                        ind2 = names.index(logname)
                                        t15 = False
                                    else:
                                        print('not a valid username')
                            except Exception as e:
                                print('not a valid username')
                            t16 = True
                            while t16 == True:
                                try:
                                    logpass = input('Enter your login password: ')
                                    with open('data2.txt','r') as data2:
                                        lines = data2.readlines()
                                        lines2 = []
                                        for sub in lines:
                                            lines2.append(sub.replace("\n", ""))
                                        passwords = []
                                        for i in lines2:
                                            passwords.append(i.split(',')[1])
                                        emails2 = []
                                        for i in lines2:
                                            emails2.append(i.split(',')[2])
                                        email2 = emails2[ind2]
                                        phnums2 = []
                                        for i in lines2:
                                            phnums2.append(i.split(',')[3])
                                        phnum2 = phnums2[ind2]
                                        records2 = []
                                        for i in lines2:
                                            records2.append(i.split(',')[4])
                                        reallogpass = passwords[ind2]
                                        if logpass == reallogpass:
                                            print('You are loged in')
                                            print('(1 for) Booking vaccine\n(2 for) Seeing your booking date\n(3 for) exit')
                                            t17 = True
                                            while t17 == True:
                                                try:
                                                    logop = int(input())
                                                    if logop == 1:
                                                        if records2[ind2] == 'True':
                                                            print('already booked can not book again')
                                                            t17 = False
                                                        else:
                                                            with open('data.txt') as data:
                                                                lines = data.readlines()
                                                                lines2 = []
                                                                for sub in lines:
                                                                    lines2.append(sub.replace("\n", ""))
                                                                hos = []
                                                                for i in lines2:
                                                                    hos.append(i.split(',')[0])
                                                                print('All hospitals available are: ')
                                                                for i,j in enumerate(hos):
                                                                    print(f'({i} for) {j}')
                                                            book(logname,logpass,email2,to=2)
                                                            t17 = False
                                                    elif logop == 2:
                                                        with open('data2.txt') as data2:
                                                                lines = data2.readlines()
                                                                lines2 = []
                                                                for sub in lines:
                                                                    lines2.append(sub.replace("\n", ""))
                                                                names = [i.split(',')[0] for i in lines2]
                                                                ind3 = names.index(logname)
                                                                datas2 = [i.split(',')[5] for i in lines2]
                                                                date4 = datas2[ind3]
                                                                print(f'\nYour date of vaccination is {date4}\n')
                                                                t17 == False
                                                                t16 = False
                                                                t12 = False
                                                                t8 = False
                                                                t7 = False
                                                                t6 = False
                                                    elif logop == 3:
                                                        t17 == False
                                                        t16 = False
                                                        t12 = False
                                                        t8 = False
                                                        t7 = False
                                                        t6 = False
                                                    else:
                                                       print('not a valid option try 1 or 2') 
                                                except Exception as e:
                                                    print('not a valid option try 1 or 2')
                                                    print(e)
                                            t16 = False
                                        else:
                                            print('wrong password for the username')
                                except Exception as e:
                                    print('not a valid password for the username')

                    elif op == 2:
                        t7 = True
                        while t7 == True:
                            t8 = True
                            while t8 == True:
                                try:
                                    name = str(input('Enter Your name(Atleast 2 word and no number): '))
                                    if len(name) < 2:
                                        print('Not a valid name (too small)')
                                    else:
                                        t8 = False
                                except Exception as e:
                                    print('Not a valid name you have use number in it')
                            t9 = True
                            while t9 == True:
                                try:
                                    password = input('Enter Your password(Atleast 5 word): ')
                                    if len(password) < 5:
                                        print('Not a valid password (too small)')
                                    else:
                                        t9 = False
                                except Exception as e:
                                    print('Not a valid password')
                            t10 = True
                            while t10 == True:
                                try:
                                    email = input('Enter Your email: ')
                                    if len(email) < 5 or '@' not in email:
                                        print('Not a valid email')
                                    else:
                                        with open('data2.txt','a') as data2:
                                            data2.writelines(f'\n{name},{password},{email},r,False,none,none')
                                            t10 = False
                                except Exception as e:
                                    print('Not a valid email')
                            t12 = True
                            while t12 == True:
                                try:
                                    op2 = int(input('(1 for) Booking Vaccine\n(2 for) Exit'))
                                    if op2 == 1:
                                            with open('data.txt') as data:
                                                lines = data.readlines()
                                                lines2 = []
                                                for sub in lines:
                                                    lines2.append(sub.replace("\n", ""))
                                                hos = []
                                                for i in lines2:
                                                    hos.append(i.split(',')[0])
                                                print('All hospitals available are: ')
                                                for i,j in enumerate(hos):
                                                    print(f'({i} for) {j}')
                                                lahosind = i
                                            t13 = True
                                            while t13 == True:
                                                book(name,password,email,to=1)
                                                t13,t12,t8,t7,t6 = False,False,False,False,False
                                    elif op2 == 2:
                                        t12,t8,t7,t6 = False,False,False,False
                                    else:
                                        print('not a valid option try 1 or 2')
                                except Exception as e:
                                    print('not a valid option try 1 or 2')
                                t7 = False
                                t6 = False
                    elif op== 3:
                        t6 = False
                    else:
                        print('Not a Valid input try 1, 2 or 3')
                except Exception as e:
                    print('Not a Valid input try 1, 2 or 3')

        elif enter == 2:
            quit()
        else:
            print('Sorry its a wrong input try 1 , 2 or 3 ')
    except Exception as e:
        print('Sorry its a wrong input try 1 , 2 or 3 ')