# aylat

# This program will calculate and display different aspects of a user's payroll

# Define constants
OT_MULTIPLIER = 1.5
DEDUCTION_PERCENTAGE = 0.2

# Prompt user to input information
EmployeeName = input('Enter the employees full name: ')
RegHours = float(input('Enter the number of regular hours worked by the employee: '))
OvertimeHours = float(input('Enter the number of overtime hours worked by the employee: '))
PayRate = float(input('Enter the hourly pay for the the employee: '))

# Perform payroll calculations based on user input
RegPay = RegHours * PayRate
OvertimePay = OvertimeHours * PayRate * OT_MULTIPLIER
GrossPay = RegPay + OvertimePay
Deductions = GrossPay * DEDUCTION_PERCENTAGE
NetPay = GrossPay - Deductions

# Display and format the output to the user
print('\n')
print('Employee Name:\t\t', EmployeeName)
print('Regular Hours Worked:\t', format(RegHours, '.2f'))
print('Overtime Hours Worked:\t', format(OvertimeHours, '.2f'))
print('Hourly Pay Rate:\t$', format(PayRate, ',.2f'), sep='')
print('\n')
print('Regular Pay:\t\t$', format(RegPay, ',.2f'), sep='')
print('Overtime Pay:\t\t$', format(OvertimePay, ',.2f'), sep='')
print('Gross Pay:\t\t$', format(GrossPay, ',.2f'), sep='')
print('Deductions:\t\t$', format(Deductions, ',.2f'), sep='')
print('Net Pay:\t\t$', format(NetPay, ',.2f'), sep='')