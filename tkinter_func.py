import tkinter


def add_labels(menu: tkinter.Tk) -> None:
    id_person = tkinter.Label(menu, text="شناسه:")
    first_name = tkinter.Label(menu, text="نام")
    last_name = tkinter.Label(menu, text="نام خانوادگی:")
    sexual = tkinter.Label(menu, text="جنسیت")
    age = tkinter.Label(menu, text="سن")
    weight = tkinter.Label(menu, text="وزن")
    salary = tkinter.Label(menu, text="درآمد")
    # gird
    id_person.grid(row=0, column=0)
    first_name.grid(row=1, column=0)
    last_name.grid(row=2, column=0)
    sexual.grid(row=3, column=0)
    age.grid(row=4, column=0)
    weight.grid(row=5, column=0)
    salary.grid(row=6, column=0)


def add_button(menu: tkinter.Tk, title: str, function) -> None:
    submit_btn = tkinter.Button(menu, text=title, command=function)
    submit_btn.grid(row=7, column=0, columnspan=2)


def clear_textbox(textbox: tkinter.Entry):
    textbox.delete(0, tkinter.END)
