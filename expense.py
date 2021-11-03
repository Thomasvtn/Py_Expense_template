from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type": "input",
        "name": "amount",
        "message": "New Expense - Amount: ",
    },
    {
        "type": "input",
        "name": "label",
        "message": "New Expense - Label: ",
    },
    {
        "type": "input",
        "name": "spender",
        "message": "New Expense - Spender: ",
    },

]


def new_expense(*args):
    f = open('csv/expense_report.csv', 'a+')
    writer = csv.writer(f)

    infos = prompt(expense_questions)
    writer.writerow([infos['amount'], infos['label'], infos['spender']])
    print("Expense Added !")

    f.close()

    return True
