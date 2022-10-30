# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20210409
# Student Name: Y.V.A.Amarasinghe
# Date: 12/5/2021

# Assumptions...
# student and staff members are two persons.
# Student can process only one prediction at on time.
# imported time function to run program smoothly and to act as real program.
# imported date time function to write, at what time,day that data processed and added to the text file.
# if user entered invalid number or out of range value, program ask  if user want to add another data or exit.



import time
import datetime

progresscount = []
trailercount = []
retrivercount = []
excludedcount = []
excludedcount1 = 0
trailercount1 =0
progresscount1=0
retrivercount1=0

#All user defined functions from here

def predictions(Pass_Mark, Fail_Mark):
    """this function make predictions for each students"""
    #use globle, because these variable use in out of the function
    global excludedcount1
    global trailercount1
    global progresscount1
    global retrivercount1
    if Fail_Mark in [80, 100, 120]:
        print("Exclude","\n")
        excludedcount1+=1

    elif Pass_Mark ==100:
        print("Progress (module trailer)","\n")
        trailercount1+=1

    elif Pass_Mark==120:
        print("Progress","\n")
        progresscount1+=1
    else:
        print("Module retriever","\n")
        retrivercount1+=1

def predict_using_list(passmark, defermark, Failmark):

    """This function make predictions for each students using list methods """
    progressonList = []
    progressonList.append(passmark)
    progressonList.append(defermark)
    progressonList.append(Failmark)


    if progressonList[2] in [80,100,120]:
        print("Exclude","\n")
        excludedcount.append([passmark, defermark, Failmark])

    elif progressonList[0] ==100:
        print("Progress (module trailer)","\n")
        trailercount.append([passmark, defermark, Failmark])


    elif progressonList[0]==120:
        print("Progress","\n")
        progresscount.append([passmark, defermark, Failmark])

    else:
        print("Module retriever","\n")
        retrivercount.append([passmark, defermark, Failmark])




def Range_Check(credit):
    """This function check the range valid or not after user input numbers"""
    if credit in (0,20,40,60,80,100,120):
        return True
    else:
        print(credit,"Out of range")
        return False

def Horizontal_histogram(process_count, trailer_count, retriever_count, exclude_count):

    """This function process a horizontal histogram using predicted Data"""

    print("-"*50)
    print("Horizontal Histogram")
    print(f"progress {process_count}    :","*" * process_count)
    print(f"Trailer  {trailer_count}    :","*" * trailer_count)
    print(f"Retriever  {retriever_count}  :","*" * retriever_count)
    print(f"Excluded {exclude_count}    :","*" * exclude_count)

    print(process_count + trailer_count + retriever_count + exclude_count, "Outcomes in Total")
    print("-"*50)

def Vertical_histogram(process_count, trailer_count, retriever_count, exclude_count):

    """This function process a Vertical histogram using predicted Data"""

    Processed_count = []
    starList = []
    for count in (process_count, trailer_count, retriever_count, exclude_count):
        Processed_count.append(count)
    Maximum_value = max(Processed_count)

    for count in Processed_count:
        if count <= Maximum_value:
            Star_make = ("*" * count + " " * (Maximum_value - count))
            starList.append(Star_make)
    print("Vertical Histogram")
    print("-"*50)
    print(f" progress{process_count}", f"Trailer{trailer_count}", f"Retriever{retriever_count}", f"Excluded{exclude_count} ")
    for count in range(Maximum_value):
        for Star in starList:
            print("\t"+Star[count] + "  ", end="")
        print()
    print(sum(Processed_count),"outcomes is total")
    print("-"*50)

def Predic_List_Print(predicList, predictype):

    """This function print print all predicted Data"""

    for Predicdata in predicList:
        print(predictype + "\t", end="")
        print(f"{str(Predicdata[0]):>3},   {str(Predicdata[1]):>3},   {str(Predicdata[2]):>3}")



def Loop_program():

    """ this function work if user wants to enter another data set"""

    while True:
        print("Would you like to enter another set of data?")
        repeatbutton = input("Enter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if repeatbutton == "y":
            return True
        elif repeatbutton == "q":
            break
        else:
            print("You enterd wrong index please enter it again.....\n")
            continue
    return False



passlist =[]
def DataGathering(student,process):
    """This function gather Data from user and loop if user made mistake while appending data to the program"""


    def processManage(process):

        """This function select which process type,(using list or normal variable form) the specific data to process
        process1=processing using prediction function
        processList=processing using prediction_using_list function"""

        if process == "process1":
            predictions(Mark_list[0], Mark_list[2])
        elif process == "processList":
            predict_using_list(Mark_list[0], Mark_list[1], Mark_list[2])
        else:
            print("wrong process input")




    if  (student =="A" or student=="B"):
        Mark_list =list()
        W_Condition = True
        while W_Condition == True:
            try:
                for catogory in ("pass", "defer", "fail"):

                    Marks = int(input(f"Please enter your credit at {catogory}: "))
                    if Range_Check(Marks) == True:
                        Mark_list.append(Marks)
                        if len(Mark_list) == 3:
                            if sum(Mark_list) == 120:
                                processManage(process)
                                Mark_list.clear()
                                if student=="B":
                                    if Loop_program() == False:
                                        W_Condition = False
                                        break

                                    else:
                                        W_Condition = True
                                        break

                                elif student=="A":
                                    W_Condition = False
                                    break



                            else:
                                print("Total Incorrect")
                                Mark_list.clear()
                                if Loop_program() == False:
                                    W_Condition = False
                                    break
                                else:
                                    W_Condition = True
                                    break
                        else:
                            continue
                    else:
                        Mark_list.clear()
                        if Loop_program() == False:
                            W_Condition = False
                            break

                        else:
                            W_Condition = True
                            break

            except ValueError:
                print("Integer Required")
                Mark_list.clear()
                if Loop_program() == False:
                    break
                else:
                    continue
    else:
        print("you entered Wrong index")






def Select_staff_OR_Student():
    """This function select, user is staff member or student """

    studentorstaff = input("if you are a student press (A),Staff memeber Press (B): ")
    studentorstaff = studentorstaff.upper().strip(" ")
    DataGathering(studentorstaff,"process1")
    if studentorstaff=="B":
        return "B"
    else:
        return "A"



def FileHandle():

    """This function check about file handling"""
    allProcessedData = [progresscount, trailercount, retrivercount, excludedcount]
    ProcessType = ["progress-", "trailer -", "retrive -", "exclude -"]


    def fileWrite():
        data_time=datetime.datetime.now()
        file.write(f"\nprogression outcome data predicted on {data_time.strftime('%x  '  '  %X')}\n")
        for type,data in zip(ProcessType,allProcessedData):
            for x in data:
                file.write(type +" ")
                file.write(f"{str(x[0]):>3},   {str(x[1]):>3},   {str(x[2]):>3},\n")
                file.flush()
        file.close()
        #Referance for zip funtion
        #"www.w3schools.com"
        #https://www.w3schools.com/python/python_datetime.asp

        #reference for the data and time
        #"www.w3schools.com"
        #https://www.w3schools.com/python/python_datetime.asp



    try:
        file = open("UniversityPredictions.txt", "a")
        fileWrite()
    except FileExistsError:
        print("File Handle error found")



def ReadFiles():

    """this function read all predicted data from text file"""

    try:
        file = open("UniversityPredictions.txt", "r")
        print("Retrieving all data from file....\n")
        time.sleep(3)
        print(file.read())


    except:
        print("File Handling Error found!")




def Start_Print_Statment():
    print("-" * 100)
    print("\t\t\t", "*" * 10, "UNIVERSITY STUDENT'S PROGRESS PREDICTION PROGRAM", "*" * 10)
    print("-" * 100)
    print(""" PROGRAM MENU:
     Part 1(Main Part)                :  PRESS 'A'
     Part 2(Vertical Histrogram)      :  PRESS 'B'
     Part 3(List printing)            :  PRESS 'C'
     Part 4(File writing and reading) :  PRESS 'D'
     Part 5(all in one)               :  PRESS 'E'
        """)
def Menu():
        menuIndex = input("Select one from menu:")
        menuIndex = menuIndex.upper().strip(" ")
        if menuIndex == "A":
            print("Are you a student or Staff member?")
            if Select_staff_OR_Student() == "B":
                Horizontal_histogram(progresscount1, trailercount1, retrivercount1, excludedcount1)



        elif menuIndex == "B":
            print("you are using Staff mode...\n")
            DataGathering("B", "process1")
            Vertical_histogram(progresscount1, trailercount1, retrivercount1, excludedcount1)

        elif menuIndex == "C":
            print("you are using Staff mode...\n")
            DataGathering("B", "processList")
            Horizontal_histogram(len(progresscount), len(trailercount), len(retrivercount), len(excludedcount))
            Vertical_histogram(len(progresscount), len(trailercount), len(retrivercount), len(excludedcount))
            Predic_List_Print(progresscount, "Progress-")
            Predic_List_Print(trailercount, "Trailer -")
            Predic_List_Print(retrivercount, "Retrive -")
            Predic_List_Print(excludedcount, "Exclude -")

        elif menuIndex == "D":
            print("you are using Staff mode...\n")
            DataGathering("B", "processList")
            FileHandle()
            print("Data stored into the file Successfully....\n")
            ReadFiles()


            
        elif menuIndex =="E":
            print("you are using Staff mode...\n")
            DataGathering("B", "processList")
            Horizontal_histogram(len(progresscount), len(trailercount), len(retrivercount), len(excludedcount))
            Vertical_histogram(len(progresscount), len(trailercount), len(retrivercount), len(excludedcount))
            Predic_List_Print(progresscount, "Progress-")
            Predic_List_Print(trailercount, "Trailer -")
            Predic_List_Print(retrivercount, "Retrive -")
            Predic_List_Print(excludedcount, "Exclude -")
            FileHandle()
            print("Data stored into the file Successfully....\n")
            ReadFiles()

            
        else:
            print(f"""You entered wrong Menu Index 
            Program is Terminating...""")
            time.sleep(2)
            print("Please Enter correct index next time")


#program runs from here

try:
    Start_Print_Statment()
    Menu()
except:
    print("Program error")
