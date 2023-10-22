#Boolean system thing. Im experimenting with it
#oct/20/2023 17:57
import pandas as pd 

data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}


def get_number():
    while True:
        try:
            district_number = int(input("Number: "))
            return district_number
        except ValueError:
            print("Bruh do it again. Use an integer.")

district_number = get_number()

color_map = pd.DataFrame(data)

#Full List
print("~~~~~~~~~~~~~~~~~~~~~~")
print("FULL LIST")
print(color_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("BOOLEAN SERIES")

#Checks if number is equal to any item in the list through a boolean
boolean_map = color_map['District'] == district_number
print(boolean_map)

print("~~~~~~~~~~~~~~~~~~~~~~")
print("DISTRICT CHECKER")

#use the boolean map
print(f"Your inputted number is : {district_number}")

district_info = color_map[boolean_map]
district_color = district_info['Color'].values[0]
print(f"Your District color is : {district_color}")

print(district_info)
