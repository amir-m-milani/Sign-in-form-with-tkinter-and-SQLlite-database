import tkinter
from tkinter_func import add_button, add_labels, add_textbox
import sqlite3

connection: sqlite3.connect = sqlite3.connect("users.db")
cur = connection.cursor()


def edit_user(user_id: str, fName: str, lName: str, sexuality: bool, age: str, salary: str, height: str):
    errors = []
    cur.execute("SELECT id FROM users WHERE id=?", int(user_id))
    id_list: list = cur.fetchall()
    if user_id.isnumeric() and len(id_list) != 0:
        if not fName == "":
            if fName.isalpha():
                connection.sql_query(
                    f"UPDATE users SET first_name = '{fName}' WHERE id = '{int(id)}'")
            else:
                errors.append("first name should be alphabtes")
        if not lName == "":
            if lName.isalpha():
                connection.sql_query(
                    f"UPDATE users SET last_name = '{lName}' WHERE id = {int(id)}")
            else:
                errors.append("last name should be alphabets")
        if not sexuality == " ":
            connection.sql_query(
                f"UPDATE users SET sexuality = '{sexuality}' WHERE id = {int(id)}")
        else:
            errors.append("you should choose your sex")
        if not age == "":
            if age.isnumeric():
                connection.sql_query(
                    f"UPDATE users SET age = {int(age)} WHERE id = {int(id)}")
            else:
                errors.append("age must be numbers")
        if not salary == "":
            if salary.isnumeric():
                connection.sql_query(
                    f"UPDATE users SET salary = {salary} WHERE id = {int(id)}")
            else:
                errors.append("salary must be numbers")
        if not height == "":
            if height.isnumeric():
                connection.sql_query(
                    f"UPDATE users SET height = {height} WHERE id = {int(id)}")
            else:
                errors.append("height should be numbers")

    else:
        errors.append("id has not been found!")
    if len(errors) != 0:
        error_window = tkinter.Tk()
        error_window.geometry("250x250")
        error_window.title("ERRORS")
        for index, error in enumerate(errors):
            test = tkinter.Label(error_window, text=error)
            test.grid(row=index, column=0)
        error_window.mainloop()


def EditMenu():
    edit_menu = tkinter.Tk()
    edit_menu.geometry("250x300")
    edit_menu.title("Edit user")
    add_labels(edit_menu)
    # Add text boxes
    [id_person, first_name, last_name, sexuality,
        age, height, salary] = add_textbox(edit_menu, add_menu=False)
    add_button(edit_menu, "ثبت نام", lambda: edit_user(
        user_id=id_person.get(), fName=first_name.get(), lName=last_name.get(), sexuality=sexuality.get(), age=age.get(), salary=salary.get(), height=height.get()))
    edit_menu.mainloop()
