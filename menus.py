import tkinter
from SQLConnect import *


# Add User
def add_user(id: str, fName: str, lName: str, sexuality: bool, age: str, salary: str, weight: str):
    connection = SQLConnect("users")
    # check all the problems
    errors = []
    if not id.isnumeric():
        errors.append("ID should be numbers")
    if not fName.isalpha():
        errors.append("Change your name.should be alphabet")
    if not lName.isalpha():
        errors.append("Change your last name.should be alphabet")
    if not age.isnumeric():
        errors.append("age must be numbers")
    if not salary.isnumeric():
        errors.append("salary must be numbers!")
    if not weight.isnumeric():
        errors.append("weight should be numbers")
    if len(errors) == 0:
        try:
            connection.sql_query(
                f"INSERT INTO users VALUES({int(id)},'{fName}','{lName}','{sexuality}',{int(age)},'{salary}',{float(weight)})")
            print("your user has been add!")
        except sqlite3.IntegrityError:
            print("Your id isnot Unique")
    else:
        error_window = tkinter.Tk()
        error_window.geometry("250x250")
        error_window.title("ERRORS")
        for index, error in enumerate(errors):
            test = tkinter.Label(error_window, text=error)
            test.grid(row=index, column=0)
        error_window.mainloop()


def edit_user(id: str, fName: str, lName: str, sexuality: bool, age: str, salary: str, weight: str):
    connection = SQLConnect("users")
    errors = []
    id_list: list = connection.select_query(
        f"SELECT id FROM users WHERE id={int(id)}")
    if id.isnumeric() and int(id) == id_list[0][0]:
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

# Add window


def open_add_menu():
    connection = SQLConnect("users")
    connection.sql_query(
        "CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY UNIQUE,first_name TEXT,last_name TEXT,sexuality BLOB,age INT,salary TEXT,weight NUMERIC)")
    add_menu = tkinter.Tk()
    add_menu.geometry("250x300")
    add_menu.title("Add user")
    add_labels(add_menu)
    # add_text_box(add_menu)
    id_person = tkinter.Entry(add_menu, width=20)
    first_name = tkinter.Entry(add_menu, width=20)
    last_name = tkinter.Entry(add_menu, width=20)
    age = tkinter.Entry(add_menu, width=20)
    weight = tkinter.Entry(add_menu, width=20)
    salary = tkinter.Entry(add_menu, width=20)
    # gird
    id_person.grid(row=0, column=1, columnspan=2)
    first_name.grid(row=1, column=1, columnspan=2)
    last_name.grid(row=2, column=1, columnspan=2)
    age.grid(row=4, column=1, columnspan=2)
    weight.grid(row=5, column=1, columnspan=2)
    salary.grid(row=6, column=1, columnspan=2)
    #####################
    sexuality = tkinter.StringVar(add_menu)
    sexuality.set("1")
    man = tkinter.Radiobutton(add_menu, text="مرد",
                              variable=sexuality, value="1")
    woman = tkinter.Radiobutton(
        add_menu, text="زن", variable=sexuality, value="0")
    man.grid(row=3, column=1)
    woman.grid(row=3, column=2)
    #####################
    add_button(add_menu, "ثبت نام", lambda: add_user(id=id_person.get(), fName=first_name.get(
    ), lName=last_name.get(), sexuality=sexuality.get(), age=age.get(), salary=salary.get(), weight=weight.get()))

    add_menu.mainloop()
    connection.close()


def edit_add_menu():
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
    add_button(edit_menu, "ثبت نام", lambda: edit_user(id=id_person.get(), fName=first_name.get(
    ), lName=last_name.get(), sexuality=sexuality.get(), age=age.get(), salary=salary.get(), weight=weight.get()))
    edit_menu.mainloop()


def add_labels(menu: tkinter.Tk) -> None:
    id_person = tkinter.Label(menu, text="شناسه:")
    first_name = tkinter.Label(menu, text="نام")
    last_name = tkinter.Label(menu, text="نام خانوادگی:")
    # sexual = tkinter.StringVar(menu)
    # man = tkinter.Radiobutton(menu, text="مرد", value="1")
    # woman = tkinter.Radiobutton(menu, text="زن", value="0")
    sexual = tkinter.Label(menu, text="جنسیت")
    age = tkinter.Label(menu, text="سن")
    weight = tkinter.Label(menu, text="وزن")
    salary = tkinter.Label(menu, text="درآمد")
    # gird
    id_person.grid(row=0, column=0)
    first_name.grid(row=1, column=0)
    last_name.grid(row=2, column=0)
    sexual.grid(row=3, column=0)
    # man.grid(row=3, column=1)
    # woman.grid(row=3, column=2)
    age.grid(row=4, column=0)
    weight.grid(row=5, column=0)
    salary.grid(row=6, column=0)


"""
def add_text_box(menu: tkinter.Tk) -> None:
    id_person = tkinter.Entry(menu, width=20)
    first_name = tkinter.Entry(menu, width=20)
    last_name = tkinter.Entry(menu, width=20)
    age = tkinter.Entry(menu, width=20)
    weight = tkinter.Entry(menu, width=20)
    salary = tkinter.Entry(menu, width=20)
    # gird
    id_person.grid(row=0, column=1, columnspan=2)
    first_name.grid(row=1, column=1, columnspan=2)
    last_name.grid(row=2, column=1, columnspan=2)
    age.grid(row=4, column=1, columnspan=2)
    weight.grid(row=5, column=1, columnspan=2)
    salary.grid(row=6, column=1, columnspan=2)
"""


def add_button(menu: tkinter.Tk, title: str, function) -> None:
    submit_btn = tkinter.Button(menu, text=title, command=function)
    submit_btn.grid(row=7, column=0, columnspan=2)
