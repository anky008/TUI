import os

def startupMessage():
    print ("\t\t\t Hi this is my TUI project")
    os.system('''echo "'date +%T'"\b\b\b\b'''
    print ("\t\t\t -------------------------")

# choice 5
def createFolder():
    print ("Enter the folder name:",end="")
    folderName=input()
    os.system('mkdir {0}'.format(folderName))
    print ("Successfully created!")


# choice 6
def setupWebServer():
    os.system('var=$(rpm -q subl)')
    x=os.system('echo $var ')
    if (x==0):
        os.system(''' setenforce 0
        yum install httpd;
        systemctl start httpd;
        systemctl enable httpd''')


def main():
    os.system('clear')
    startupMessage()
    comeOut=False
    while (1):
        print ("""List of commands available
                1) See the Date
                2) See the Calender
                3) Create a new user
                4) Create a new file
                5) create a new directory
                6) Setup web server
                7) Exit """)

        print ("Enter your choice:",end="")
        choice=input()
        
        try:
            choice=int (choice)
        except ValueError:
            print ("Please Enter Valid Choice")
            continue

        if (choice==1):
            os.system('date')

        elif (choice==2):
            os.system('cal')

        elif (choice==3):
            print ("Enter the user name:",end="")
            userName=input()
            os.system("useradd {}".format(userName))
            os.system("passwd {}".format(userName))

        elif (choice==4):
            print ("in construction")

        elif (choice==5):
            createFolder()

        elif (choice==6):
            setupWebServer()
        
        elif(choice==7):
            break
            comeOut=True

        else:
            print ("please enter  a valid choice")
        
    if (comeOut==True):
            exit()

main()
    
