#palaboiSatz v3.0 lol
#oct/22/2023 20:04
# Fully operational. Will add comments soon hindi ngayon kasi tinatamad pa ko, kaya mo na yan.
import pandas as pd 

# Data set.
data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}
color_map = pd.DataFrame(data)

def get_name():
    while True:
        name = input("⌨ Name: ")
        if all(char.isalpha() or char.isspace() or char in "., " for char in name):
            return name
        else:
            print("Error: Invalid credentials. Please try again.")
            print("---------------------")
            
def get_number():
    while True:
        try:
            user_number = int(input("⌨ District Number: "))
            if 1 <= user_number <= 9:
                return user_number
            else:
                print("Select an integer between 1-9 bruh.")
        except ValueError:
            print("Use an integer, dumbass.")

def get_age():
    while True:
        try:
            age = int(input("⌨ Age: "))
            return age
        except ValueError:
            print("Invalid input")
            print("---------------------")

def district_checker(number):
    district_number = number
    bool_res = color_map['District'] == district_number
    district_info = color_map[bool_res]
    district_number = district_info['District'].values[0]
    district_color = district_info['Color'].values[0]
    return district_number, district_color, 

def get_schedule(age, district_color):
    age = age
    dcolor = district_color
    day = None
    curfew_start = None
    curfew_end = None
    if age > 60 or age < 18:
        if dcolor == "blue":
            day = "Mon/Thu/Fri"
        elif dcolor == "red":
            day = "Wed/Sat/Mon"
        elif dcolor == "green":
            day = "Tue/Fri/Sat"
        else :
            print("Invalid credentials")
        curfew_start, curfew_end = "10PM", "5AM"
    else: 
        if dcolor == "blue":
            day = "Mon/Wed"
        elif dcolor == "red":
            day = "Thur/Fri"
        elif dcolor == "green":
            day = "Tue/Sat"
        else: 
            print("Invalid credentials")
        curfew_start, curfew_end = "6AM", "9PM" 
    return day, f"{curfew_start}-{curfew_end}"
        
def main():
    print("》》》》》》》》》》》》 PLEASE ENTER YOUR USER INFORMATION BELOW 《《《《《《《《《《《《")
    name = get_name()
    user_number = get_number()
    age = get_age()
    district_number, district_color = district_checker(user_number)
    days, curfew_schedule = get_schedule(age, district_color)
    print("》》》》》》》》》》》》》》》》 HERE IS YOUR CURFEW SCHEDULE 《《《《《《《《《《《《《《《《")
    print("")
    print(f"☞ Name: {name}")
    print(f"☞ District {district_number}: {district_color}")
    print(f"☞ Curfew Schedule : {days}, {curfew_schedule}")
    print(f"☞ Sunday Curfew : 21:00 - 9:00")
    print("")
    print("》》》》》》》》》》》》》》》》》》》 PLEASE STAY SAFE! 《《《《《《《《《《《《《《《《《《《《")

main()