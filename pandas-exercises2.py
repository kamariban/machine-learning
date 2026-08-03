import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

file_csv = "/Users/kamari/Documents/project_info/employees.csv"
file_txt = "/Users/kamari/Documents/project_info/employees.txt"

try:
    csv = pd.read_csv(file_csv)

except Exception as e:
    print(f"Error: {e}")


employee_df = pd.DataFrame(csv)

with open(file_txt, mode="r") as my_file:
    txt = my_file.read()

##exercises

def employee_count(df):
    return df["EMPLOYEE_ID"].count()

#print(employee_count(employee_df))

def average_salary(df):
    return df["SALARY"].mean()


def highest_in_the_room(df):
    high = df["SALARY"].max()
    return df[df["SALARY"] == high]

def find_employee(df, name):
    return df[df["FIRST_NAME"] == name]

print(find_employee(employee_df,"William"))

#print(employee_df.head(10))
#print(employee_df.dtypes)





