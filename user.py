from PyInquirer import prompt
user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New User - Name:",
    }
]


def add_user():
    infos = prompt(user_questions)
    print("User Added !")
    return True
