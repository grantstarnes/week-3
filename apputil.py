import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...

# Exercise 1: Fibonacci Sequence Function
# Write a recursive function to compute the nth Fibonacci number in the series

def fib(n):
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
    return fib(n - 1) + fib(n - 2)

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

def task_i():
    df_bellevue['gender'] = df_bellevue['gender'].replace('?', np.nan).replace('h', np.nan).replace('g', np.nan)
    nan_count = df_bellevue.isna().sum()
    nan_sorted = nan_count.sort_values()
    return nan_sorted.index.tolist()

# 3.2: Return a dataframe for each year in the dataset with total number of entries for each year

def task_ii():
    df_bellevue['date_in'] = pd.to_datetime(df_bellevue['date_in'])
    df_bellevue['year'] = df_bellevue['date_in'].dt.year

    recent_emigrant = df_bellevue[df_bellevue['disease'] == 'recent emigrant']

    yearly_admissions = recent_emigrant.groupby('year', as_index=False).size().rename(columns={'size': 'total_admissions'})

    return yearly_admissions

# 3.3: Return a series with the index as gender and the values as the average age for the indexed gender

def task_iii():
    return df_bellevue.groupby('gender')['age'].mean().round(2)

# 3.4: Return a list of the 5 most common professions in order of prevalence (most common first)

def task_iv():
    top_professions = df_bellevue['profession'].value_counts().head().index.tolist()
    return top_professions
