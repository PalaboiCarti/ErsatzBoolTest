#Boolean system thing. Im experimenting with it
#oct/22/2023 08:19
import pandas as pd 

# Data set.
data = {
    'District': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Color': ['blue', 'red', 'blue', 'red', 'blue', 'red', 'green', 'green', 'green']
}

# Put your functions here.
def get_number():
    while True:
        try:
            user_number = int(input("Input district number: "))
            if 1 <= user_number <= 9:
                return user_number
            else:
                print("Select an integer between 1-9 bruh.")
        except ValueError:
            print("Use an integer, dumbass.")

user_number = get_number()

# Data frame out of data set from earlier.
color_map = pd.DataFrame(data)

# Full List
def full_list():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("FULL LIST")
    print(color_map)

# Checks if number is equal to any item in the list through a boolean.
boolean_map = color_map['District'] == user_number

def boolean_series():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("BOOLEAN SERIES")
    print(boolean_map)

# Display corresponding values through the boolean map. 
# Whatever number of an item in the dataframe corresponds to your inputted number, it will display the data of said item. 
# Basta kaya mo na yan.
district_info = color_map[boolean_map]
district_color = district_info['Color'].values[0]
district_number = district_info['District'].values[0]

# Display that shit
def display_info():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("DISTRICT CHECKER")
    print(f"Your inputted number is : {user_number}")
    print(f"Your District color is : {district_color}")

# Main function
def main():
    full_list()
    boolean_series()
    display_info()
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Your inputted number \"{user_number}\" corresponds to District Number {district_number}")
    print(district_info)

main()