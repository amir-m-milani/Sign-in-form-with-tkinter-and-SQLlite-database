import tkinter
from add import AddMenu
from edit import EditMenu

# Main window
main_menu = tkinter.Tk()
main_menu.geometry("150x150")
main_menu.title("Main Menu")
# Main Buttons
add_btn = tkinter.Button(main_menu, text="Add",
                         width=20, command=AddMenu)
add_btn.grid(row=0, column=0)
edit_btn = tkinter.Button(main_menu, text="Edit",
                          width=20, command=EditMenu)
edit_btn.grid(row=1, column=0)


if __name__ == "__main__":
    main_menu.mainloop()
