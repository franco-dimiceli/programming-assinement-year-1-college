#
#
# ## importing custom tkinter ##
#
import customtkinter
import tkinter as tk
from tkinter import messagebox
#
class my_gui():

##        ##------------------------------------------------------------------------------------------------------------

    ## functions ##

## switching navigation frame functions ##

    def switch_to_events_menu_frame(self):

        self.event_menu_frame_navigation.pack(fill="x", )

        self.navigation_button_frame.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()

    def switch_to_start_menu_frame(self):

        self.navigation_button_frame.pack(fill="x", )

        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()

    def switch_to_edit_teams_and_individuals_frame(self):

        self.teams_and_individuals_frame_navigation.pack(fill="x", )

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()

    def switch_to_display_scoreboard_frame(self):

        self.display_scoreboard_frame_navigation.pack(fill="x", )

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()

    def close_the_program(self):

        if self.msg.askyesno(title="Exit?", message="Are you sure you want to leave?", ):

            self.root.destroy()

    def __init__(self):

    ## initialising the GUI ##

        self.root = customtkinter.CTk()

        self.root.title("scoring system")

        self.root.geometry("900x800")

    ## gets rid of the close, minimise and maximize options at the top 1 = get rid, 0 = its still there ##

        self.root.overrideredirect(0)

        self.msg = messagebox

        customtkinter.set_appearance_mode("dark")

        customtkinter.set_default_color_theme("blue")

    ## frames ##

##        ##------------------------------------------------------------------------------------------------------------

    ## start menu navigation buttons ##

        self.navigation_button_frame = customtkinter.CTkFrame(self.root, fg_color="#026592")

        self.navigation_button_frame.columnconfigure(0, weight=1, )
        self.navigation_button_frame.columnconfigure(1, weight=1, )
        self.navigation_button_frame.columnconfigure(2, weight=1, )
        self.navigation_button_frame.columnconfigure(3, weight=1, )
        self.navigation_button_frame.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nDisplay scoreboard\n", font=("roboto", 20), height=0, command=self.switch_to_display_scoreboard_frame, hover_color="#02557a").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E,)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nEdit teams and individuals\n", font=("roboto", 20), height=0, command=self.switch_to_edit_teams_and_individuals_frame, hover_color="#02557a").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nStart menu\n", font=("roboto", 20), height=0, command=self.switch_to_start_menu_frame, fg_color="#02557a", hover_color="#02557a").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nEdit events\n", font=("roboto", 20), height=0, command=self.switch_to_events_menu_frame, hover_color="#02557a").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nClose program\n", font=("roboto", 20), height=0, command=self.close_the_program, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

        self.navigation_button_frame.pack(fill="x", )

##        ##------------------------------------------------------------------------------------------------------------

    ## start menu content ##

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu navigation ##

        self.event_menu_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#026592")

        self.event_menu_frame_navigation.columnconfigure(0, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(1, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(2, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(3, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nDisplay scoreboard\n", font=("roboto", 20), height=0, command=self.switch_to_display_scoreboard_frame, hover_color="#02557a").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit teams and individuals\n", font=("roboto", 20), height=2, hover_color="#02557a").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nStart menu\n", font=("roboto", 20), height=0, command=self.switch_to_start_menu_frame, hover_color="#02557a").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit events\n", font=("roboto", 20), height=0, command=self.switch_to_events_menu_frame, fg_color="#02557a", hover_color="#02557a").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.back_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nBack\n", font=("roboto", 20), height=0, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E)

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu content ##

##        ##------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals navigation ##

        self.teams_and_individuals_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#026592")

        self.teams_and_individuals_frame_navigation.columnconfigure(0, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(1, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(2, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(3, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nDisplay scoreboard\n", font=("roboto", 20), height=0, command=self.switch_to_display_scoreboard_frame, hover_color="#02557a").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nEdit teams and individuals\n", font=("roboto", 20), height=0, command=self.switch_to_edit_teams_and_individuals_frame, fg_color="#02557a", hover_color="#02557a").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nStart menu\n", font=("roboto", 20), height=0, command=self.switch_to_start_menu_frame, hover_color="#02557a").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nEdit events\n", font=("roboto", 20), height=0, command=self.switch_to_events_menu_frame, hover_color="#02557a").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.back_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nBack\n", font=("roboto", 20), height=0, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E)

##        ##------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals content ##

##        ##------------------------------------------------------------------------------------------------------------

    ## display scoreboard navigation ##

        self.display_scoreboard_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#026592")

        self.display_scoreboard_frame_navigation.columnconfigure(0, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(1, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(2, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(3, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nDisplay scoreboard\n", font=("roboto", 20), height=0, command=self.switch_to_display_scoreboard_frame, fg_color="#02557a", hover_color="#02557a").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nEdit teams and individuals\n", font=("roboto", 20), height=0, command=self.switch_to_edit_teams_and_individuals_frame, hover_color="#02557a").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nStart menu\n", font=("roboto", 20), height=0, command=self.switch_to_start_menu_frame, hover_color="#02557a").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nEdit events\n", font=("roboto", 20), height=0, command=self.switch_to_events_menu_frame, hover_color="#02557a").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.back_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nBack\n", font=("roboto", 20), height=0, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E)

##        ##------------------------------------------------------------------------------------------------------------

    ## display scoreboard content ##

##        ##------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

my_gui()
