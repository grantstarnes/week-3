import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...

# Exercise 1: Fibonacci Sequence Function
# Write a recursive function to compute the nth Fibonacci number in the series

def fibonacci(n):
    ''' This function is responsible for returning the nth Fibonacci number in the series based on the input n.
        For example, if we were to call fib(3), the function would return 2. The function would first check if
        n is equal to 0 or 1, and if not, it essentially skips to the else statement, which returns the the sum of
        the two previous Fibonacci numbers, which are calculated by calling the function recursively with n-1 and n-2.
        So, in this example, the return statement would end up being fib(2) + fib(1), which is 1 + 1 = 2. Fib(2) holds 
        the value of 1 because it is calculated as fib(1) + fib(0), which is 1 + 0 = 1. Fib(1) is 1 because of the base case.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Exercise 2: Integer to Binary Conversion
# Write a recursive function to convert an integer to its binary representation

def to_binary(n):
    '''
    This function is responsible for converting an integer n to its binary representation as a string.
    The function first checks if n is less than 2, in which case it simply returns the string representation 
    of n (either '0' or '1'). If n is 2 or greater, the function calls itself recursively with the integer floor division
    of n by 2 (n // 2) and concatenates the result with the string representation of the remainder (modulus) when n is divided by 2 (n % 2).
    This effectively builds the binary representation from the most significant bit to the least significant bit.
    '''
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

# Exercise 3: Bellevue Almshouse Data Analysis

# Extracting the data

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

# 3.1: Return a list of all columns sorted by the least missing values to most missing values

def task_1():
    '''
    This function returns a list of column names sorted by the least missing values to most missing values (NaN values).
    It first takes the data in the gender column and cleans it up, replacing any '?' or invalid entries ('h', 'g') with NaN 
    in order to get an accurate count of missing values, and makes sure gender is simply 'm', 'f', or NaN. It then sums the 
    number of NaN values in each column using the isna() method followed by sum(). The resulting series of NaN counts is then
    sorted in ascending order using sort_values(). Finally, the function returns a list of the column names sorted by the number of missing values.
    '''

    df_bellevue['gender'] = df_bellevue['gender'].replace('?', np.nan).replace('h', np.nan).replace('g', np.nan)
    nan_count = df_bellevue.isna().sum()
    nan_sorted = nan_count.sort_values()
    return nan_sorted.index.tolist()

# 3.2: Return a dataframe for each year in the dataset with total number of entries for each year

def task_2():
    '''
    This function returns a dataframe that contains the total number of admissions for the disease 'recent emigrant' for each year in the dataset.
    It first converts the 'date_in' column to datetime format using pd.to_datetime(). Then, it extracts the year from the 'date_in' column and creates a new column called 'year'.
    Next, it filters the dataframe to include only rows where the 'disease' column is equal to 'recent emigrant'.
    Finally, it groups the filtered dataframe by the 'year' column, counts the number of entries for each year using size(), and renames the resulting column to 'total_admissions'.
    The function returns the resulting dataframe with two columns: 'year' and 'total_admissions'.
    '''

    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'])
    df_bellevue['year'] = df_bellevue['date_in'].dt.year

    yearly_admissions = df_bellevue.groupby('year').size().reset_index(name='total_admissions')

    return yearly_admissions

# 3.3: Return a series with the index as gender and the values as the average age for the indexed gender

def task_3():
    '''
    This function returns a pandas Series with the index as gender and the values as the average age for each gender.
    It groups the dataframe by the gender column and calculates the mean age for each, which is then rounded to two decimal places for clarity.
    '''

    return df_bellevue.groupby('gender')['age'].mean().round(2)

# 3.4: Return a list of the 5 most common professions in order of prevalence (most common first)

def task_4():
    '''
    This function returns a list of the 5 most common professions in the dataset, ordered from most to least prevalent.
    It uses the value_counts() method on the 'profession' column to count the occurrences of each profession, then selects 
    the top 5 using head(), and finally extracts the index (profession names only) and converts it to a list. We could use
    head(5) instead of head() since the default is 5, but I wanted to be explicit.
    '''

    top_professions = df_bellevue['profession'].value_counts().head().index.tolist()
    return top_professions
