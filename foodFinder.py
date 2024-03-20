
# now.dining.cornell.edu/api/1.0/dining/eateries.json
#get api data using json, read
import json #json like minecraft 
import requests
import datetime


# get the data from the API
url = "https://now.dining.cornell.edu/api/1.0/dining/eateries.json"
response = requests.get(url)
data = response.json() 
top = data.keys()

#all of these foods are objectively good (down arrow )👇 add more but not too much more 
goodfood = ['pulled pork', 'smoked gouda', 'steak', 'pierogi', 'chicken parm']

#make a class for each food item with its name, eatery, and date
class FoodItem:
    def __init__(self, name, eatery, date): #innit m8
        self.name = name
        self.eatery = eatery
        self.date = date

    def __str__(self):
        return self.name + " at " + self.eatery + " on " + self.date

    def __repr__(self): #i have no idea what this method does copilot wrote it and says it's for debugging
        return self.name + " at " + self.eatery + " on " + self.date #i think it's for debugging but i'm not sure

def get_goodfood(goodfood, data): #find good food near me at any time 
    togo = [] #not the country
    for eatery in data["data"]["eateries"]: #variable names are FUCKED 
        for hours in eatery["operatingHours"]:
            for meal in hours["events"]:
                for item in meal["menu"]:
                    for dish in item["items"]:
                        for food in goodfood: #fan would be proud of the nesting 
                            if food in dish["item"].lower():
                                togo.append(FoodItem(dish["item"], eatery["name"], hours['date']))
    return togo

def gftoday(goodfood, data,date=datetime.datetime.now()): #good food today 
    # has not worked in getting me a gf on any day
    gflist = get_goodfood(goodfood, data)
    dategf = [] #i wish
    for item in gflist:
        if item.date == date:
            dategf.append(item) #I was an oop hater but then i saw the way 
    return dategf

#find what's open now 
def opennow(data,timestamp=datetime.datetime.now().timestamp()):
    open = []
    for eatery in data["data"]["eateries"]:
        for hours in eatery["operatingHours"]:
                for event in hours["events"]:
                    if event['startTimestamp'] < timestamp and timestamp < event['endTimestamp']: #better than MATLAB
                        open.append(eatery["name"])
    return open #having only worked on this after 2 am, I've never seen this work before 

#some example code‽ 

# today = datetime.date.today().strftime("%Y-%m-%d")
# print(goodfood())
# print("Good food today is:", gftoday(today, goodfood, data))
# print(opennow(data))
# print(opennow(data, 1710766800))

def menu(): #another win for the robots 
    print("1. Good food all times ")
    print("2. Good food today")
    print("3. Open now")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        food = get_goodfood(goodfood, data)
        for item in food:
            print(item)
    elif choice == '2':
        print(gftoday(goodfood, data))
    elif choice == '3':
        print(opennow(data))
    elif choice == '4':
        exit()
    else:
        print("Invalid choice. Please choose again.")
        menu() #actually most cretive use of code ever what the fuck 

menu() #does a thing 
