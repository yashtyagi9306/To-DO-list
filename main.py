#Todo list
main={}
n=[]

def ename():
    u_name=input("Enter name: ")
    main[u_name]=""
    n.append(u_name)
    adm=len(n)

def etask(n):
    i=len(n)
    z=n[i-1]
    l=[]
    y="Y"
    while y=="Y":
        t=input("Add a task: ")
        l.append(t)
        y=input("Press Y to add another task: ")
        y=y.upper()      
        main[z]=l

def sname(main):
    x=main.keys()
    j=1
    for i in x:
        print(j,"-",i)
        j+=1
        
def atask(l):
    t=input("Add a task: ")
    l.append(t)

while True:
    w=int(input("Main Menu: \n1. Create To-do list\n2. Use To-do list\n3. Remove To-do list\n4. Quit\n"))

    if (w==1):
        #creating a to-do list
        ename()
        etask(n)

    elif (w==2):
        while True:
            print("Choice: ")
            x=int(input("1. Add task\n2. Remove task\n3. Mark as completed\n4. View task list\n5. Go back to main menu\n "))
            
            if (x==1):
                sname(main)
                p=int(input("In which candidate's list you want to add task?\nEnter serial number:  "))
                key = list(main.keys())[p-1]
                value=main[key]
                for a in value:
                    print(a)
                t=input("Add a task: ")
                value.append(t)
                for a in value:
                    print(a)
            
            elif (x==2):
                sname(main)
                p=int(input("From which candidate's list you want to remove task?\nEnter serial number: "))
                key = list(main.keys())[p-1]
                value=main[key]
                for a in value:
                    print(a)
                
                e=int(input("Enter task number: "))
                x=value[e-1]
                value.remove(x)
                for a in value:
                    print(a)

            elif (x==3):
                sname(main)
                p=int(input("Which candidate's list? "))
                key = list(main.keys())[p-1]
                value=main[key]
                for a in value:
                    print(a)
                z=int(input("Enter task number of the completed task: "))
                x=value[z-1]
                x=x+"✅"
                value[z-1]=x 
                for a in value:
                    print(a)
            elif (x==4):
                sname(main)
                p=int(input("Which candidate's list you want to see? "))
                key = list(main.keys())[p-1]
                value=main[key]
                for a in value:
                    print(a)
            else:
                break
        
    elif (w==3):
        sname(main)
        p=int(input("Which candidate's list you want to delete? "))
        key = list(main.keys())[p-1]
        del main[key]
    elif(w is not 1 or 2 or 3 or 4):
        print("Enter a valid number from 1 to 4")
    else:
        print("************End of program*****************")
        break
