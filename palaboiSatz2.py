# palaboiSatz v2.0
# oct/22/2023 10:34
# Initial commit 
import pandas as pd 

# Data set.
data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}

# Initialize user_number
user_number = None

color_map = pd.DataFrame(data)

# Put your functions here.
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
            global user_number
            user_number = int(input("Input district number: "))
            if 1 <= user_number <= 9:
                return user_number 
            else:
                print("Select an integer between 1-9 bruh.")
        except ValueError:
            print("Use an integer, dumbass.")
            
# Display that shit
def display_info():
    name = get_name()
    
    # Call get_number to set the user_number
    get_number()
    
    # Check if user_number is in the data
    boolean_map = color_map['District'] == user_number
    district_info = color_map[boolean_map]
    
    if not district_info.empty:
        district_color = district_info['Color'].values[0]
        district_number = district_info['District'].values[0]
        
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("DISTRICT CHECKER")
        print(f"☞ Name: {name}")
        print(f"☞ District number : {district_number}")
        print(f"☞ District Color : {district_color}")
    else:
        print("No information found for District number:", user_number)

# Main function
display_info()
