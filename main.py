from PyInquirer import prompt
from examples import custom_style_2
from expense import expense_questions, new_expense
import unittest


def ask_option():
    main_option = {
        "type": "list",
        "name": "main_options",
        "message": "Expense Tracker v0.1",
        "choices": ["New Expense", "Show Status", "New User"]
    }
    option = prompt(main_option)
    if (option['main_options']) == "New Expense":
        new_expense()
        ask_option()


def ask_for_tests():
    main_option = {
        "type": "list",
        "name": "test_options",
        "message": "Do you want to run the testsuit or the project ?",
        "choices": ["Testsuit", "Project"]
    }
    option = prompt(main_option)
    if(option['test_options']) == "Testsuit":
        unittest.main()
    else:
        ask_option()


def main():
    ask_for_tests()


main()
