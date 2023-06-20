import tkinter
from tkinter_func import add_button, add_labels, clear_textbox, add_textbox
import sqlite3

connection: sqlite3.connect = sqlite3.connect("users.db")
cur: sqlite3.Cursor = connection.cursor()


def add_user(user_id: tkinter.Entry, fName: tkinter.Entry, lName: tkinter.Entry, sexuality: tkinter.Entry, age: tkinter.Entry, salary: tkinter.Entry, weight: tkinter.Entry):
    # check all the problems
    errors = []
    test = errors.append(
        "ID should be numbers") if not user_id.get().isnumeric() else None
    test = errors.append(
        "Change your name.should be alphabet") if not fName.get().isalpha() else None
    test = errors.append(
        "Change your last name should be alphabet") if not lName.get().isalpha() else None
    test = errors.append(
        "age must be numbers") if not age.get().isnumeric() else None
    test = errors.append(
        "salary must be numbers!") if not salary.get().isnumeric() else None
    test = errors.append(
        "weight should be numbers") if not weight.get().isnumeric() else None
    del test
    # Check if all the text box are ok
    if len(errors) == 0:
        try:
            cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?)", [int(user_id.get()), fName.get(
            ), lName.get(), sexuality.get(), int(age.get()), salary.get(), float(weight.get())])
            connection.commit()
            for tesxbox in [user_id, fName, lName, age, salary, weight]:
                clear_textbox(tesxbox)
        except sqlite3.IntegrityError:
            error_window = tkinter.Tk()
            error_window.geometry("250x250")
            error_window.title("ERRORS")
            test = tkinter.Label(error_window, text="This ID has been taken")
            test.pack()
            error_window.mainloop()
    else:
        error_window = tkinter.Tk()
        error_window.geometry("250x250")
        error_window.title("ERRORS")
        for index, error in enumerate(errors):
            test = tkinter.Label(error_window, text=error)
            test.grid(row=index, column=0)
        error_window.mainloop()


def AddMenu():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(id INT PRIMARY KEY UNIQUE,first_name TEXT,last_name TEXT,sexuality BLOB,age INT,salary TEXT,weight NUMERIC)")
    connection.commit()
    add_menu = tkinter.Tk()
    add_menu.geometry("250x300")
    add_menu.title("Add user")
    add_labels(add_menu)
    # Add all the text box
    [id_person, first_name, last_name, sexuality,
        age, weight, salary] = add_textbox(add_menu, True)
    add_button(add_menu, "ثبت نام", lambda: add_user(user_id=id_person, fName=first_name,
               lName=last_name, sexuality=sexuality, age=age, salary=salary, weight=weight))
    add_menu.mainloop()
    connection.close()
