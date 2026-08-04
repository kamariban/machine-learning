import pandas as pd
import re

file_csv = "/Users/kamari/Documents/project_info/employees.csv"
file_txt = "/Users/kamari/Documents/project_info/employees.txt"

try:
    csv = pd.read_csv(file_csv)

except Exception as e:
    print(f"Error: {e}")


employee_df = pd.DataFrame(csv)

with open(file_txt, mode="r") as my_file:
    txt = my_file.read()

### csv df exercises

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

def department_count(df):
    return df["JOB_ID"].value_counts().to_dict()

#print(employee_df.head(10))
#print(employee_df.dtypes)

### txt exercises
#print(txt)
#count
def count(text):
    #without strip counts empty space line as a line.
    sentence_counter = len([line for line in text.splitlines() if line.strip()])
    character_counter = len(text)
    word_counter  = len(text.split(" "))

    return word_counter, sentence_counter, character_counter


def longest_word(text):
    words = text.split()
    sort = sorted(words, key=len)
    return sort[-1]


def top_10(text):
    words = text.split(" ")
    freq = {}
    clean_words = [re.sub(r"[^\w\s]", "", text) for text in words]
    for x in clean_words:
        freq[x] = clean_words.count(x)
    sort = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

    return list(sort.items())[:10]

print(top_10(txt))
#print(txt.split())



