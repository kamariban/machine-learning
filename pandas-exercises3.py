import pandas as pd

file_csv = "/Users/kamari/Documents/project_info/employees.csv"

class EmployeeDatabase:
    def __init__(self, csv):
        self.csv = csv
        self.data = None

    def load_data(self, info):
        self.data = pd.read_csv(self.csv)
        return self.data


    def show_all(self, info):
        df = self.data[["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME",]]
        return df

    def highest_salary(self,info):
        highest = self.data.sort_values(by= "SALARY", ascending=False)
        return highest.iloc[0]

    def average_salary(self,info):
        counter = 0
        total = 0
        for x in self.data["SALARY"]:
            total += x
            counter += 1
        return f"Average Salary: {total / counter}"

        #return self.data["SALARY"].mean()

    def department_count(self,info):
        data = self.load_data(info)
        return dict(data["DEPARTMENT_ID"].value_counts())


    def find_employee(self, name):
        name = self.data[self.data["FIRST_NAME"] == name]
        return name

test = EmployeeDatabase(file_csv)
print(test.load_data(file_csv))

#print(test.load_data(file_csv))
col = test.load_data(file_csv)
#print(list(col))

print(test.find_employee("Pat"))


