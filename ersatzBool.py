#Boolean system thing. Im experimenting with it
#oct/22/2023 08:19
import pandas as pd 

data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}


def get_number():
    while True:
        try:
            user_number = int(input("Input district number: "))
            return user_number
        except ValueError:
            print("Bruh do it again. Use an integer.")

user_number = get_number()

color_map = pd.DataFrame(data)

#Full List
print("~~~~~~~~~~~~~~~~~~~~~~")
print("FULL LIST")
print(color_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("BOOLEAN SERIES")

#Checks if number is equal to any item in the list through a boolean
boolean_map = color_map['District'] == user_number
print(boolean_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("DISTRICT CHECKER")

#use the boolean map
district_info = color_map[boolean_map]
district_color = district_info['Color'].values[0]
district_number = district_info['District'].values[0]

def display_info():
    print(f"Your inputted number is : {user_number}")
    print(f"Your District color is : {district_color}")

display_info()
print("~~~~~~~~~~~~~~~~~~~~~~")
print(f"Your inputted number {user_number} corresponds to District Number {district_number}")
print(district_info)
