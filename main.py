from functions import *
import os

path = "./Data"
# obtain all files in "./Data" . They must be all .csv containing operator's prices
files_names = os.listdir(path)

# Number of operators (files)
n_operators = len(files_names)

# I Create a list of dataframes, one for each operator
df_list = read_files(path,files_names)

# Receive the phone number as keyboard input
phone_number = input("Insert the phone number : ")

best_operator, best_price = find_best(df_list, n_operators, phone_number)

if best_price == None:
    print("No plan found for any operator for the given number")
else:
    print("operator file : ",files_names[best_operator]," with price : ",best_price)