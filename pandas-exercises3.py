import pandas as pd

file_csv = "/Users/kamari/Documents/project_info/employees.csv"

class EmployeeDatabase:
    def __init__(self, csv):
        self.csv = csv
        self.data = None

    def load_data(self, info):
        self.data = pd.read_csv(self.csv)
        return self.data

    def show_all(self):
        df = self.data[["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME",]]
        print(df)

    def highest_salary(self):
        highest = self.data.sort_values(by= "SALARY", ascending=False)
        return highest.iloc[0]

    def lowest_salary(self):
        highest = self.data.sort_values(by="SALARY", ascending=True)
        return highest.iloc[0]

    def average_salary(self):
        counter = 0
        total = 0
        for x in self.data["SALARY"]:
            total += x
            counter += 1
        return f"Average Salary: {total / counter}"

        #return self.data["SALARY"].mean()

    def department_count(self):
        return dict(self.data["DEPARTMENT_ID"].value_counts())


    def find_employee(self, first_name=None, last_name=None, eid=None):
        if first_name is not None:
            return self.data[self.data["FIRST_NAME"] == first_name]
        elif last_name is not None:
            return self.data[self.data["LAST_NAME"] == last_name]
        elif eid is not None:
            return self.data[self.data["EMPLOYEE_ID"] == eid]
        return None

    def department_report(self, d_id):
        report = self.data[self.data["DEPARTMENT_ID"] == d_id]
        d_num = len(report)
        avg = report["SALARY"].mean().round()
        sort = report["SALARY"].sort_values(ascending=False)
        high = sort.iloc[0]

        return (report,
                f" Department: {d_id}" ,
                f" Employees: {d_num}" ,
                f" Average Salary: {avg}" ,
                f" Highest Salary: {high}")



test = EmployeeDatabase(file_csv)
test.load_data(file_csv)
#test.show_all()
print(test.department_report(100))




