import tkinter
from tkinter_func import add_button, add_labels
import sqlite3

connection: sqlite3.connect = sqlite3.connect("users.db")
cur = connection.cursor()


def edit_user(user_id: str, fName: str, lName: str, sexuality: bool, age: str, salary: str, weight: str):
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
        if not weight == "":
            if weight.isnumeric():
                connection.sql_query(
                    f"UPDATE users SET weight = {weight} WHERE id = {int(id)}")
            else:
                errors.append("weight should be numbers")

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

    # add_text_box(add_menu)
    id_person = tkinter.Entry(edit_menu, width=20)
    first_name = tkinter.Entry(edit_menu, width=20)
    last_name = tkinter.Entry(edit_menu, width=20)
    age = tkinter.Entry(edit_menu, width=20)
    weight = tkinter.Entry(edit_menu, width=20)
    salary = tkinter.Entry(edit_menu, width=20)
    # gird
    id_person.grid(row=0, column=1, columnspan=2)
    first_name.grid(row=1, column=1, columnspan=2)
    last_name.grid(row=2, column=1, columnspan=2)
    age.grid(row=4, column=1, columnspan=2)
    weight.grid(row=5, column=1, columnspan=2)
    salary.grid(row=6, column=1, columnspan=2)
    #####################
    sexuality = tkinter.StringVar(edit_menu)
    sexuality.set(" ")
    man = tkinter.Radiobutton(edit_menu, text="مرد",
                              variable=sexuality, value="1")
    woman = tkinter.Radiobutton(
        edit_menu, text="زن", variable=sexuality, value="0")
    man.grid(row=3, column=1)
    woman.grid(row=3, column=2)
    #####################
    add_button(edit_menu, "ثبت نام", lambda: edit_user(
        user_id=id_person.get(), fName=first_name.get(), lName=last_name.get(), sexuality=sexuality.get(), age=age.get(), salary=salary.get(), weight=weight.get()))
    edit_menu.mainloop()