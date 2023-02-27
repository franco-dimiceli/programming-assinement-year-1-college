## importing tkinter ##

import tkinter as tk

from tkinter import messagebox

## initialising the gui ##

root = tk.Tk()

root.title("scoring system")

root.geometry("900x800")


## functions ##

def warning_box():

    if messagebox.askyesno(title="Quit", message="are you sure"):

        root.destroy()


# def warning_box_close_program():

## navigation buttons ##

navigation_button_frame = tk.Frame(root, )

navigation_button_frame.columnconfigure(0, weight=1, )
navigation_button_frame.columnconfigure(1, weight=1, )
navigation_button_frame.columnconfigure(2, weight=1, )
navigation_button_frame.columnconfigure(3, weight=1, )

display_scoreboard_button = tk.Button(navigation_button_frame, text="display scoreboard", font=("", 18), height=2, )
display_scoreboard_button.grid(row=0, column=0, sticky=tk.W + tk.E)

edit_teams_and_individuals_button = tk.Button(navigation_button_frame, text="edit teams and individuals", font=("", 18),
                                              height=2, )
edit_teams_and_individuals_button.grid(row=0, column=1, sticky=tk.W + tk.E)

start_menu_button = tk.Button(navigation_button_frame, text="start menu", font=("", 18), height=2, )
start_menu_button.grid(row=0, column=2, sticky=tk.W + tk.E)

close_program_button = tk.Button(navigation_button_frame, text="close program", font=("", 18), height=2, )
close_program_button.grid(row=0, column=3, sticky=tk.W + tk.E)

root.protocol("WM_DELETE_WINDOW", warning_box())

navigation_button_frame.pack(fill="x", )

## edit events menu ##

root.mainloop()
