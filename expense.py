from os import name, read
from PyInquirer import prompt
import csv

from prompt_toolkit.shortcuts import print_tokens


def spender_list(answers):
    f = open('csv/users.csv')
    reader = csv.reader(f)
    name_list = list(reader)

    f.close()

    res = []

    for row in name_list:
        res.append(row[0])

    return res


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
        "type": "list",
        "name": "spender",
        "message": "New Expense - Spender: ",
        "choices": spender_list
    }

]


def new_expense(*args):
    f = open('csv/expense_report.csv', 'a+')
    writer = csv.writer(f)

    infos = prompt(expense_questions)

    writer.writerow([infos['amount'], infos['label'], infos['spender']])

    print("Expense Added !")

    f.close()

    return True
