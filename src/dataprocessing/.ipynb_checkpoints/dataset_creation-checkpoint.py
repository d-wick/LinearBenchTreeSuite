####################
# Formating dataset
# -----------------
####################
# - Import csv data from the package
####################
import pandas as pd
import numpy as np

from dataprocessing.data_loader_processed import load_raw_csv

####################
# - Extract data from csv
# - Format dates as columns
# - Format products as lines
# - Print results to excel file for reference
####################
def import_data():
    # Load the CSV file
    data = load_raw_csv()
    
    # Create a column "Period" with both the Year and the Month
    data["Period"] = data["Year"].astype(str) + "-" + data["Month"].astype(str)
    # We use the datetime formatting to make sure format is consistent
    data["Period"] = pd.to_datetime(data["Period"]).dt.strftime("%Y-%m")
    
    # Create a pivot of the data to show the periods on columns and the car makers on rows
    df = pd.pivot_table(data=data,values="Quantity",index="Make",columns="Period",aggfunc='sum',fill_value=0)
    
    # Print data to Excel for reference  
    df.to_excel("LBTS_Clean_Demand.xlsx")
    return df

####################
# - Create train and test sets
# - df: historical demand
# - x_len: # of months used to make prediction
# - y_len: # of months to predict
# - y_test_len: # of months for final test
####################
def datasets(df, x_len=12, y_len=1, y_test_len=12):

    D = df.values
    periods = D.shape[1]
    
    # Training set creation: run through all the possible time windows
    loops = periods + 1 - x_len - y_len - y_test_len 
    train = []
    for col in range(loops):
        train.append(D[:,col:col+x_len+y_len])
    train = np.vstack(train)
    X_train, Y_train = np.split(train,[x_len],axis=1)
     
    # Test set creation: unseen "future" data with the demand just before
    max_col_test = periods + 1 - x_len - y_len
    test = []
    for col in range(loops,max_col_test):
        test.append(D[:,col:col+x_len+y_len])
    test = np.vstack(test)
    X_test, Y_test = np.split(test,[x_len],axis=1)
     
    # this data formatting is needed if we only predict a single period
    #  - array.ravel() makes NumPy array 1D
    if y_len == 1:
        Y_train = Y_train.ravel()
        Y_test = Y_test.ravel()
        
    return X_train, Y_train, X_test, Y_test

####################
# - Calls functions to create datasets for ml alg
####################
df = import_data()
X_train, Y_train, X_test, Y_test = datasets(df)