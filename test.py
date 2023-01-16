from functions import *
import os

path = "./Data"
# obtain all files in "./Data" . They must be all .csv containing operator's prices
files_names = os.listdir(path)

# Number of operators (files)
n_operators = len(files_names)

# I Create a list of dataframes, one for each operator
df_list = read_files(path,files_names)

#### TEST ENTIRE PROGRAM

# Test a number without a corresponding prefix
no_prefix_number = "68123456789"
best_operator, best_price = find_best(df_list, n_operators, no_prefix_number)
assert (best_operator==None and best_price==None) , "not matching prefix test not passed"

# Test a number with a partially corresponding prefix
partially_match_number = "45555555"
best_operator, best_price = find_best(df_list, n_operators, partially_match_number)
assert (best_operator==None and best_price==None) , "partially matching prefix test not passed"

# Test a prefix that belongs only to "Test_A"
test_A_number = "2685555"
best_operator, best_price = find_best(df_list, n_operators, test_A_number)
assert (best_operator==0 and best_price==5.1) , "test_A test not passed"

# Test a prefix that belongs only to "Test_B"
test_B_number = "4455555"
best_operator, best_price = find_best(df_list, n_operators, test_B_number)
assert (best_operator==1 and best_price==0.5) , "test_B test not passed"

# Test a prefix that belongs to both
test_both_0_number = "4673555"
best_operator, best_price = find_best(df_list, n_operators, test_both_0_number)
assert (best_operator==0 and best_price==0.9) , "test_both_0 test not passed"

# Test a prefix that belongs to both
test_both_1_number = "46732555"
best_operator, best_price = find_best(df_list, n_operators, test_both_1_number)
assert (best_operator==1 and best_price==1) , "test_both_1 test not passed"

print("all test passed!")