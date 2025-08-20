employees = {}

def generate_slip(emp_id ,employees):
    emp = employees[emp_id]
    print("---- Employee Salary Slip ----")
    print(f"Employee ID: {emp_id}")
    print(f"Employee Name: {emp['name']}")
    print(f"Basic Salary: {emp['basic']}")
    print(f"Allowances: {emp['allowances']}")
    print(f"Deduction: {emp['deductions']}")

    net_salary = emp["basic"] + emp["allowances"] - emp["deductions"]
    print(f"Net Salary: {net_salary}")

while True:
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    basic_salary = float(input("Enter employee basic salary: "))
    allowances = float(input("Enter allowances: "))
    deductions = float(input("Enter deductions: "))
    
    employees[emp_id] = {
        "name" : name,
        "basic" : basic_salary,
        "allowances" : allowances,
        "deductions" : deductions
    }

    generate_slip(emp_id, employees)

    choice = input("Want to exit? ")
    if choice.lower() == "yes":
        break

