work_hours=[int(x) for x in input('enter the hours').split()]
wages=int(input('enter hourly wage'))
total=sum(work_hours)
salary=total*wages
print('salary is',salary)