import csv
# import person
# import WUF



''' CSV FORMAT
EXPOSURE_ID, PERSON, EXPOSURE_DATE, EXPOSURE_TIME, 
OR: STUDENT_ID, STUDENT_NAME, EXPOSURE_DATE, EXPOSURE_LOCATION'''


''' JSON FORMAT
    {
        Student_ID:
        Student_Name:
        Exposure: [
                [Monday, [Gym, Library], [Greg]],
                [Tuesday, [Bank], [Tom]]
        ]
    }
'''

'''General function to get input making sure it is of a specific type'''
def inputType(prompt, inputType, is_list = False):
    responseList = []
    while True:
        response = input(prompt)
        if response == "that's it": break
        try:
            resp = inputType(response)
            if is_list:
                responseList.append(resp)
            else:
                return resp
        except BaseException:
            print("This is not " + inputType + " data")
    return responseList


def getUserInput(person):
    # function should ask user where they went - not sure about granularity yet; example specifies particular buildings
    lastVisited = []
    while True:
        response = input("Where do you remember visiting the last week? ")
        if response == "that's it":
            break
        lastVisited.append(response)

        print(lastVisited)

    
    dayExposed = input("What day did you become exposed? ")
    # unless we do some fancy NLP stuffS, the format will most likely be like: 7-9; 1-3; etc.
    
    othersExposedCount = 0
    othersExposed = []
    while True:
        response = input("Who do you remember was with you? ")
        othersExposedCount += 1
        if response == "that's it":
            break
        othersExposed.append(response)

    if len(othersExposed) > 0:
        getSecondaryContact(othersExposed)
    personList = [person,dayExposed,lastVisited, othersExposed]
    
    database.append(personList)

def getSecondaryContact(othersExposed):
    #Function for calling all of the secondary contacts
    for person in othersExposed:
        print("The following questions are for", person, ":")
        getUserInput(person)
        
def writer():
    #Writes into the Json File
    header = ["NAME","DAY EXPOSED", "LOCATION", "PEOPLE CONTACTED"]
    file = open('tracing.json', 'w')

    for x in database:
        dictionary ={
        "NAME" : x[0],
        "DAY EXPOSED" : x[1],
        "LOCATIONS" : x[2],
        "PEOPLE CONTACTED" :x[3]}
        json_object = json.dumps(dictionary, indent = 4)
        file.write(json_object)
    file.close()
                
        
    

person = input("What is your name? ")

getUserInput(person)
writer()
