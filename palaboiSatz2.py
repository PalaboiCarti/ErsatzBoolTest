# palaboiSatz v2.0
# oct/22/2023 13:01
# Fully operational, added comments for your dumb ahh
import pandas as pd 

# Data set
data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}
# Base variables
user_number = None
color_map = pd.DataFrame(data)

# Luh calm functions
def get_name():
    while True:
        name = input("⌨ Name: ")
        if all(char.isalpha() or char.isspace() or char in "., " for char in name):
            return name
        else:
            print("Error: Invalid credentials. Please try again.")
            print("---------------------")

def get_age():
    while True:
        try:
            age = int(input("⌨ Age: "))
            return age
        except ValueError:
            print("Invalid input")
            print("---------------------")

def get_number():
    while True:
        try:
            global user_number
            user_number = int(input("⌨ District number: "))
            if 1 <= user_number <= 9:
                return user_number 
            else:
                print("Select an integer between 1-9 bruh.")
        except ValueError:
            print("Use an integer, dumbass.")
      
# Display that shit
def display_info():
    print("》》》》》》》》》》》》 PLEASE ENTER YOUR USER INFORMATION BELOW 《《《《《《《《《《《《")
    name = get_name()
    age = get_age()
    # Call this to change the global var user_number
    get_number()

    # Check if user_number is in the data
    boolean_map = color_map['District'] == user_number

    # Variable translations n shit
    district_info = color_map[boolean_map]
    district_number = district_info['District'].values[0]
    district_color = district_info['Color'].values[0]
    
    def get_curfew_schedule(age, district_color):
        if not district_info.empty:
            # Luh calm variables
            day = None
            curfew_start = None
            curfew_end = None

            # Luh calm ifelse
            if age > 60 or age < 18:
                if district_color == 'blue':
                    day = "Mon/Thu/Fri"
                elif district_color == 'red':
                    day = "Wed/Sat/Mon"
                elif district_color == 'green':
                    day = "Tue/Fri/Sat"
                curfew_start, curfew_end = "10PM", "5AM"
            else:
                if district_color == 'blue':
                    day = "Mon/Wed"
                elif district_color == 'red':
                    day = "Thu/Fri"
                elif district_color == 'green':
                    day = "Tue/Sat"
                curfew_start, curfew_end = "6AM", "9PM" 

            # Luh calm return values from Luh calm ifelse
            return day, f"{curfew_start}-{curfew_end}"
        else:
            print("No information found for District number:", user_number)
    
    # Set values returned from get_curfew_schedule
    day, curfew_schedule = get_curfew_schedule(age, district_color) 

    # Display the outpput
    print("》》》》》》》》》》》》》》》》 HERE IS YOUR CURFEW SCHEDULE 《《《《《《《《《《《《《《《《")
    print("")
    print(f"☞ Name: {name}")
    print(f"☞ Age: {age}")
    print(f"☞ District {district_number}, {district_color}")
    print(f"☞ Curfew Schedule: {day}, {curfew_schedule}, Sun 9PM - 6PM")
    print("")
    print("》》》》》》》》》》》》》》》》》》》 PLEASE STAY SAFE! 《《《《《《《《《《《《《《《《《《《《")

# Display that ho
display_info()
