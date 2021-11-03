from PyInquirer import prompt
import csv

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name:",
    }
]


def add_user():
    f = open('csv/users.csv', 'a+')
    writer = csv.writer(f)

    infos = prompt(user_questions)
    writer.writerow([infos['name']])
    print("User Added !")

    f.close()
    return True
