import pandas
import numpy
from copy import copy

def add_full_name(path_to_csv, path_to_new_csv):
    #Assume you will be reading in a csv file with the same columns that the
    #Lahman baseball data set has -- most importantly, there are columns
    #called 'nameFirst' and 'nameLast'.
    #1) Write a function that reads a csv
    #located at "path_to_csv" into a pandas dataframe and adds a new column
    #called 'nameFull' with a player's full name.
    #
    #For example:
    #   for Hank Aaron, nameFull would be 'Hank Aaron', 
	#
	#2) Write the data in the pandas dataFrame to a new csv file located at
	#path_to_new_csv

    #WRITE YOUR CODE HERE
    data = pandas.read_csv(path_to_csv)
    data['nameFull'] = data['nameFirst'] + ' ' + data['nameLast']
    #import pdb; pdb.set_trace()
    
    
    data.to_csv(path_to_new_csv)



def imputation(filename):
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this: 
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    # 
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv(filename)
    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))
    #average_weight = numpy.mean(baseball['weight'])
    #import pdb; pdb.set_trace()
    #baseball['weight'].fillna)
    
    #YOUR CODE GOES HERE

    return baseball


if __name__ == "__main__":
    # For local use only
    # If you are running this on your own machine add the path to the
    # Lahman baseball csv and a path for the new csv.
    path_to_csv = "Master.csv"
    #path_to_new_csv = "NewMaster.csv"
    #print add_full_name(path_to_csv, path_to_new_csv)
    print imputation(path_to_csv)
    