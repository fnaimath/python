def expense_tracker():
    expenses = {}

    num_days = int(input('How many days are you tracking? '))

    for i in range(num_days):
        day = str(input('What day is this? '))
        expenses_day = int(input('What was the toal expenses for this day? '))
        expenses[day] = expenses_day
    

    for day, exp in expenses.items():
        print(f'{day}: {exp}, \n')

expense_tracker()