#Esau Gangadin
#October 29, 2015
#This program is intended to speed up patient satisfaction within the hospital
#I am working for.

#Mid and Final project

#This will being the main function

def main():
    
    endProgram = "no"
    while endProgram == "no":
        patientInformation = getInfo()
        patientBirth = getDob
        currentDate = getCurrent
        varAge = (currentYear, patientYear)
        patientAge (varAge, birthDay, birthMonth, currentMonth, currentDay)
        patientAllergies()
        printData (patientName, patientGender, patientAddress, patientZip, patientState, patientSocial, patientPhone, patientEmergency, patientVisit, patientEmployment, patientInsurance, patientAge, patientAllergies)
        

        endProgram = raw_input ("Do you want to input another patient? (enter yes or no):")

#This function will get the the patient information
def getInfo():
    patientName = input ("Enter the patient name (First name then last name):")
    patientGender = input ("Male or female?")
    patientAddress = input ("Where does the patient live?")
    patientZip = input ("What is the zip")
    patientState = input("Enter the state")
    patientSocial = input("Enter the patient social")
    patientPhone = input("Enter patient home phone number")
    patientEmergency = input ("Enter patient in case of emergency contact")
    patientVisit = input ("Reason for visit?")
    patientEmployment = input ("Please enter patient place of employment")
    patientInsurance = input ("What is the patient insuance?")
    return patientInfo

#This function will get the patient DOB information
def getDob():
    patientDay = input ("Enter in the day the patient was born")
    patientMonth = input ("Enter the patient birth month")
    patientYear = input ("Enter in the year the patient was born")
    return patientBirth

#This function will gather the current date
def getCurrent():
    currentDay = input ("What today date (only day):")
    currentMonth = input ("What is the month of today:")
    currentYear = input ("what year is it")
    return currentDate

#This function will calc the varAge
def varAge(currentYear, birthYear):
    varAge = currentYear - birthYear
    return varAge


#This function will calc the Patient Age
def patientAge(varAge, birthDay, birthMonth, currentMonth, currentDay):
    if birthMonth == currentMonth or birthDay <= currentDay:
        patientAge = varAge - 1
    if birthMonth == currentMonth or birthDay >= currentDay:
        patientAge = varAge
    if birthMonth <= currentMonth:
        patientAge = varAge
    if birthMonth > currentMonth:
        patientAge = varAge - 1
    return patientAge

#This function will get all patient information
def patientAllergies():
    #This is the line for creating variable that will control number of allergies they can enter
    count = 0

    #This will create the while loop
    while count < 10: #This ensures that up to 10 allergies can be entered
        print "Please enter if patient has any allergies(If there is no allergies left please put NA)"
        next = raw_input (">")

        #This is not from this weeks chapter, I researched on how to do a little more with while and if statements.
        if len(next) > 0 and next.isalpha():

            #len(next) > 0 is used to check whether you've entered any input or not. If lenth is 0, the origram will ask for input again
            #next.isaplha() utilizes a built-in python function, isalpha() is to make sure that the user can only enter alphabets
            #patientAllergies.append(next) uses .append() which is the default python function for adding items to a list
            
            patientAllergies.append (next)
            count = count + 1
        else:
            print "I am sorry that is a incorrect entry"
    return patientAllergies

#This will print all data in the correct order that needs to be printed
def printInfo (patientName, patientGender, patientAddress, patientZip, patientState, patientSocial, patientPhone, patientEmergency, patientVisit, patientEmployment, patientInsurance, patientAge, patientAllergies):
    print "The patient name is", patientName, "who is ", patientAge, "years old"
    print "The patient social number is: ", patientSocial, " and is ", patientGender
    print "The patient address is ", patientAddress, "from ", patientState, "with the zip ", patientZip
    print "The patient phone number is ", patientPhone, " and the emergency contact phone number is ", patientEmergency
    print "The patient place of employment is ", patientEmployment, "and uses ", patientInsurance, "insurance"
    print "The allergies the patient have are ", patientAllergies

main()
