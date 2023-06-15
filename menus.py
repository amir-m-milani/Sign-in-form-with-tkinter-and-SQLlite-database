import tkinter


# Add
def open_add_menu():
    add_menu = tkinter.Tk()
    add_menu.geometry("250x300")
    add_menu.title("Add user")
    add_labels(add_menu)
    add_text_box(add_menu)
    add_button(add_menu, "ثبت نام", "1")
    add_menu.mainloop()


def edit_add_menu():
    edit_menu = tkinter.Tk()
    edit_menu.geometry("250x300")
    edit_menu.title("Edit user")
    add_labels(edit_menu)
    add_text_box(edit_menu)
    add_button(edit_menu, "ویرایش", lambda: print('hello world'))
    edit_menu.mainloop()


def add_labels(menu: tkinter.Tk) -> None:
    id_person = tkinter.Label(menu, text="شناسه:")
    first_name = tkinter.Label(menu, text="نام")
    last_name = tkinter.Label(menu, text="نام خانوادگی:")
    sexual = tkinter.StringVar(menu)
    man = tkinter.Radiobutton(menu, text="مرد", value="1")
    woman = tkinter.Radiobutton(menu, text="زن", value="0")
    sexual = tkinter.Label(menu, text="جنسیت")
    age = tkinter.Label(menu, text="سن")
    weight = tkinter.Label(menu, text="وزن")
    salary = tkinter.Label(menu, text="درآمد")
    # gird
    id_person.grid(row=0, column=0)
    first_name.grid(row=1, column=0)
    last_name.grid(row=2, column=0)
    sexual.grid(row=3, column=0)
    man.grid(row=3, column=1)
    woman.grid(row=3, column=2)
    age.grid(row=4, column=0)
    weight.grid(row=5, column=0)
    salary.grid(row=6, column=0)


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


def add_button(menu: tkinter.Tk, title: str, function) -> None:
    submit_btn = tkinter.Button(menu, text=title, command=function)
    submit_btn.grid(row=7, column=0, columnspan=2)
