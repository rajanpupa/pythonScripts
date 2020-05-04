import pandas as pd

# define dataframe from two series
data = {
    'cars' : [5, 4, 1, 7], # series 
    'boats' : [2,6, 0, 2]  # series
}

# assining indices to rows specific dataframe elements
vehicles = pd.DataFrame(data, index= ['Peter', 'Sara', 'Ali', 'John'])

# getting information about the data
print(vehicles.info())

# indexing certain element in the frame
print(vehicles.loc['Ali'])

# see first rows in dataframe
print(vehicles.head())

