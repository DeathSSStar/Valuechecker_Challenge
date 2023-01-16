import pandas as pd
import numpy as np


def read__csv(file):
    """
    This is a pd.read_csv() with declared column names
    and with prefix read as string

    file : "path/filename"
    """
    df = pd.read_csv(file, names=["prefix","price"],header=None,dtype={"prefix":"str"})
    return df


def read_files(path, files_names):
    """
    This function creates a list that will contain all the dataframes 
    that are read from the folder in path

    path : is the folder in which all the .csv are stored
    files_names : list that contains all the files name in folder path
    """
    files_list = []

    for name in files_names:
        files_list.append(read__csv(path+"/"+name))
    return files_list


def find_price(df,phone_number):
    """
    This function finds the price for an operator for the phone number inputted.

    df : Dataframe of the operator
    phone_number : inputted phone number
    """
    prefix = df["prefix"]
    # I have to initialize ind = None to correctely obtain a KeyError that 
    # will be catched by the try-except in find_best() function
    ind = None

    for i in range(len(phone_number)):
        # condition contains a Boolean series with all the prefixes that start with the
        # same first number as the phone number
        condition = prefix.str.startswith(phone_number[:i+1])

        # stop condition. checks if all boolean values are false.
        # this happens when no prefix matches the first i digits of phone_number
        if (~condition).all():
            break
        
        # Update prefix series. This way I significantly reduce the dimension of the series.
        prefix = prefix.loc[condition]
        
        # obtain a list of indices with prefix matching initial part of phone number
        index = prefix[prefix==phone_number[:i+1]].index
        if len(index)==1:
            ind = index[0]

    price = df["price"][ind]
    return price


def find_best(df_list, n_operator, phone_number):
    """
    This function obtain the best price among all the operator for the inputted phone number

    df_list : list that contains each operators dataframe
    n_operator : number of operators
    phone_number : inputted phone number
    """

    # This  loop creates a list containing the best price for each operator
    prices = []
    for operator in range(n_operator):

        # This try-except is used for the case when an operator does not 
        # provide a plan for such number, i.e. no prefix match are found
        # The KeyError is obtained when ind is None
        try:
            prices.append(find_price(df_list[operator],phone_number))
        except KeyError:
            # I need to append a NaN to keep the correct operator numeration
            prices.append(np.NaN)

    # Check the best operator
    try:
        # np.nanargmin is a np.argmin that ignores NaNs
        best_operator = np.nanargmin(prices)
        best_price = prices[best_operator]

    # np.nanargmin raises a ValueError when there are only NaNs
    # i.e. there's no plan for this number for any operator    
    except ValueError:
        return None,None

    return best_operator,best_price