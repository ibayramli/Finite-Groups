# %%
import math 
import numpy as np
import pandas as pd
from .euclidean_algo import gcd

def find_coprimes(integer):
    """
    Inputs: integer to find coprimes to

    Outputs: a numpy array of numbers {1, 2, ... } coprime to integer
    """
    all_numbers = np.arange(1, integer + 1)
    gcd_checker = lambda x: gcd(x, integer) == 1
    vectorized_gcd_checker = np.vectorize(gcd_checker)
    coprimes = all_numbers[vectorized_gcd_checker(all_numbers)]

    return coprimes

def multiplication_table(coprimes, integer):
    """
    Inputs: an integer and a numpy array of coprimes to that integer

    Outputs: multiplication table for the Group Z_integer
    """
    coprimes_df = pd.DataFrame(pd.Series(coprimes))
    coprimes_table = coprimes_df.dot(coprimes_df.T)%integer
    coprimes_table.columns = coprimes
    coprimes_table.index = coprimes

    return coprimes_table

def compute_orders(coprimes, integer):
    """
    Inputs: an integer and a numpy array of coprimes to that integer

    Outputs: orders of elements in the Group Z_integer
    """
    coprimes_df = pd.DataFrame(pd.Series(coprimes))
    coprimes_df.columns = ["order"]
    coprimes_df.index = coprimes
    for coprime in coprimes:
        for i in range(integer):
            if coprime**(i+1)%integer == 1:
                coprimes_df.loc[coprime, "order"] = i+1
                break
    return coprimes_df

def compute_order_ocurrence(coprimes_order_df):
    """
    Inputs: an Pandas df containing elements of the Group Z_integer and their orders

    Outputs: a Pandas df containing orders of the Group Z_integer and number of group elements of that order
    """
    ocurrence_table = pd.DataFrame(coprimes_order_df.iloc[:,0].value_counts())
    ocurrence_table.columns = ["ocurrence"]
    
    return ocurrence_table
