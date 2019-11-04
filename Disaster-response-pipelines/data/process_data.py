import sys
import pandas as pd
import os
import numpy as np
from pandas.api.types import is_string_dtype
import sqlalchemy as sqla


def load_data(messages_filepath, categories_filepath):
    '''
        input: 2 file full / relative paths: messages and categories csv files.
        output: 1 dataframe with the merged data
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    df = pd.merge(messages, categories, on="id", how="left")
    return df


def clean_data(df):
    ''' 
        input: a dataframe containing messages and categories
        output: a dataframe with:
            - columns correctly named
            - values on the correct data type for purpose
            - duplicates removed

        id, message, original, genre, categories
    '''
    # First create a dataframe of the categories, keeping id
    i = df.columns.get_loc('categories')
    tempDF = df['categories'].str.split(";", expand = True)
    categs = pd.concat([df.iloc[:, :i], tempDF, df.iloc[:, i+1:]], axis=1)

    # extract column names the expanded columns
    row = categs.iloc[0:1] # pick first row to gather column names
    skip = ['id','message','original','genre']
    category_colnames = list()
    for item in row.iteritems():
        if item[0] not in skip:
            category_colnames.append(item[1][0].split("-")[0])
    categs.columns = skip + category_colnames 

    # convert to ints those new columns' values 
    for column in categs:
        if column not in skip:
            # set each value to be the last character of the string
            categs[column] = categs[column].str[-1]
            # convert column from string to numeric
            categs[column] = categs[column].astype(int)

    # remove duplicates
    df.drop_duplicates(inplace=True)
    return df

def save_data(df, database_filename):
    '''
        input: database file name
        output: none - file saved with name provided in data folder.
    '''
    engine = sqla.create_engine('sqlite:///'+database_filename)  
    df.to_sql('clasified_messages', engine, index=False, if_exists = 'replace')


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()