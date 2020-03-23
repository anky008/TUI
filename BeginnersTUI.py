import os

def startupMessage():
     os.system('tput setaf 1')
     print ("\t\t\t Hi this is my TUI project")
     os.system('tput setaf 7')
     print ("\t\t\t -------------------------")


def createFileHelper(directory=None):

    if (directory!=None):
        os.chdir(directory)

    currWorkingDir=os.getcwd()
    print ("Enter the name of file with extension:",end="")
    fileName=input()
    os.system("touch {}".format(fileName))
    print ("File created succesfully")
    os.system("gedit {}".format(fileName))
    print ("Do you want to create more files ? :",end="")
    ifMoreFiles=input()
    ifMoreFiles=ifMoreFiles.lower()
    
    os.chdir(currWorkingDir)
    if (ifMoreFiles=="yes" or ifMoreFiles=="y"):
        createFile(directory)
    else:
        return


# choice 4 - helps tp navigate to a folder
def navigateToFolder(directoryName):

    currWorkingDir=os.getcwd()
    list1=[x for x in directoryName.strip().split(" ")]

    for index in range(len(list1)):
        x=os.system("ls {} | grep {}".format(currWorkingDir,list1[index]))
    
        if (x!=0):
            print ("The folder {} dosen't exist:".format(list1[index]))
            print ("Do you want to create {}?: ".format(list1[index]),end="")
            ifCreateFolder=input().strip().lower()
            if (ifCreateFolder=="yes" or ifCreateFolder=="y"):
                createFolderHelper(list1[index],currWorkingDir)

            else:
                return currWorkingDir

        currWorkingDir=currWorkingDir + "/" + list1[index]
        os.chdir(currWorkingDir)

    return currWorkingDir



# choice 5 -> takes the path and crates the file  
def createFile():
    print ("Do you want to create file here ? :",end="")
    CreateFileHere=input().lower()
    if (CreateFileHere == "yes" or CreateFileHere=="y"):
        createFileHelper()

    else:
        print ("Enter the path where you want to create file in space seperated way:",end="")
        userPath=input()
        updatedPath=navigateToFolder(userPath)
        createFileHelper(updatedPath)


def createFolderHelper(folderName=None,path=None):

    if (path == None):
        path=os.getcwd()

    if (folderName == None):
        print ("Enter the folder name:",end="")
        folderName=input()

    os.system('mkdir {0}'.format(folderName))
    print ("Successfully created!")


# choice 6 -> creates a folder 
def createFolder():
    print ("Do you want to create folder here? :",end="")
    createFolderHere=input().lower()
    if (createFolderHere=="yes" or createFolderHere=="y"):
        createFolderHelper()

    else: 
        print ('''Enter path where you want to create folder in space seperated way:''',end="")
        userPath=input().strip()
        updatedPath=navigateToFolder(userPath)
        createFolderHelper(updatedPath)


# choice 7 -> setup httpd 
def setupWebServer():
    os.system("sudo setenforce 0")
    os.system("yum install httpd")
    os.system("systemctl start httpd")
    os.system("systemctl enable httpd")

    currWorkingDir=os.getcwd()

    print ("Do you want to add web pages:",end="")
    createPages=input()
    createPages=createPages.lower()
    if (createPages=="false" or createPages=="f"):
         return

    print ("Enter your web pages here")
    os.chdir("/var/www/html")
    print ("now create files here")
    createFile("/var/www/html")
    os.chdir(currWorkingDir)



def main():
    os.system('clear')
    startupMessage()
    comeOut=False
    while (1):
        print ("""List of commands available
                1) See the Date
                2) See the Calender 
                3) Create a new user
                4) Go to a folder
                5) Create a new file
                6) create a new directory
                7) Setup web server
                8) See the current working folder
                9) See the contents of the current working folder 
                10) Exit """)

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
            print ("Enter the path in space seperated sequential order:",end="")
            userPath=input().strip()
            navigateToFolder(userPath)


        elif (choice==5):
            createFile()
            
        elif (choice==6):
            createFolder()

        elif (choice==7):
            setupWebServer()

        elif (choice==8):
            os.getcwd()

        elif (choice==9):
            os.system("ls")
        
        elif (choice==10):
            comeOut=True
            break

        else:
            print ("please enter  a valid choice")
        
    if (comeOut==True):
        exit()

main()
