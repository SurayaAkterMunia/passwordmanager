import os
print("Welcome to password Manager")
print(" Chosse any opption below")
op=input("Do you have any master password? yes/ no \n ")
op=op.lower()
i=0
def masterp():
    mpwd = input("Password: \n")
    s=" "
    with open('masterpass.txt','r') as f:
        for line in f.readlines():
            s=line
        if len(s) == len(mpwd):
            mainmenu()
        else:
            for i in range (0,3):
                print( "Invalid Password !! Please try again !!")
                mpwd = input("Password: \n")
                if len(mpwd)== len(s):
                    mainmenu()           
def addmasterp():
     mpwd = input(" Enter a Master Password: \n")
     with open('masterpass.txt','a') as f:
         f.write(mpwd)
def search():
    un=input("Enter Your name \n")
    s=" "
    with open('pass.txt','r') as f:
        for line in f.readlines():
            s=line
        if un in s:
            print(line)
    print("Back To Main Menu")
    print("1. Main Menu \n", "2.Exit")
    o=int(input("Please Enter an Opption: \n "))
    if o ==1:
        mainmenu()
    if o==2:
        exit(0)
          
def add():
    n=input(" Enter Your Name: \n")
    
    with open('pass.txt','a+') as f:
        f.write(n + ": ")
    a= int(input("Enter how many account do you want enter: \n "))
    for i in range (0,a):
        an = input("Account Name: \n")
        pwd = input("Password: \n")
        f= open('pass.txt','a')
        f.write(an + ": " + pwd + "|" )
    if a==a:
        f.write("\n")
        f.close()
    print("Back To Main Menu")
    print("1. Main Menu \n", "2.Exit")
    o=int(input("Please Enter an Opption: \n "))
    if o ==1:
        mainmenu()
    if o==2:
        exit(0)
def view():
     with open('pass.txt','r') as f:
        for line in f.readlines():
            print(line)
        print("Back To Main Menu")
        print("1. Main Menu \n", "2.Exit")
        o=int(input("Please Enter an Opption: \n "))
        if o ==1:
            mainmenu()
        if o==2:
            exit(0)
def modify():
      up=input("Enter record You want to modify : \n")
      f1=open("temp.txt","w")
      with open('pass.txt','r') as f:
          s=' '
          for line in f.readlines():
              s=line
              l=s.split()
              if len(s)>0:
                  if len(l[0]) != up:
                      f1.write(s)
      with open('temp.txt','w') as f1:
          n=input(" Enter Your Name: \n")
          f1.write(n + ": ")
          a= int(input("Enter how many account do you want enter: \n "))
          for i in range (0,a):
              an = input("Account Name: \n")
              pwd = input("Password: \n")
              f1.write(an + ": " + pwd + "|" )
      f1=open("temp.txt","a")
      if a==a:
        f1.write("\n")
        f1.close()
      os.remove("pass.txt")
      os.rename("temp.txt","pass.txt")           
      print("Back To Main Menu")
      print("1. Main Menu \n", "2.Exit")
      o=int(input("Please Enter an Opption: \n "))
      if o ==1:
          mainmenu()
      if o==2:
          exit(0)     
def delete():
    dl=input("Enter record You want to delete : \n")
    with open('pass.txt','r') as f:
        s=' '
        for line in f.readlines():
            s=line
            l=s.split()
    with open('temp.txt','w') as f1:
        if len(s)>0:
            if len(l[0]) != dl:
                f1.write(s)
    os.remove("pass.txt")
    os.rename("temp.txt","pass.txt")
    print("Your Record havebeen deleted")
    print("Back To Main Menu")
    print("1. Main Menu \n", "2.Exit")
    o=int(input("Please Enter an Opption: \n "))
    if o ==1:
        mainmenu()
    if o==2:
        exit(0)
def mainmenu():
    print("1. To view all the pass word : view  \n" "2. Add new Password : add \n" "3. Delete password : delete \n" "4. Modify Password : modify \n""5.To Search : search \n","6.Exit:exit")
    op= input(" Please Enter a Mode \n ")
    if op=="search":
       search()
    if op=="add":
        add()
    if op=="delete":
        delete()
    if op=="modify":
        modify()
    if op=="view":
        view()
    if op=="exit":
        exit(0)
if op == "yes":
    masterp()
if op == "no":
    addmasterp()
