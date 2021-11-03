from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name:",
    }
]


# f = open('csv/expense_report.csv', 'a+')
#     writer = csv.writer(f)

#     infos = prompt(expense_questions)
#     writer.writerow([infos['amount'], infos['label'], infos['spender']])
#     print("Expense Added !")

#     f.close()

def add_user():
    f = open('csv/users.csv', 'a+')
    writer = csv.writer(f)

    infos = prompt(user_questions)
    writer.writerow([infos['name']])
    print("User Added !")

    f.close()
    return True
