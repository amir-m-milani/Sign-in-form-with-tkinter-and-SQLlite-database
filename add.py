import tkinter
from tkinter_func import add_button, add_labels, clear_textbox
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
    add_button(add_menu, "ثبت نام", lambda: add_user(user_id=id_person, fName=first_name,
               lName=last_name, sexuality=sexuality, age=age, salary=salary, weight=weight))
    add_menu.mainloop()
    connection.close()
