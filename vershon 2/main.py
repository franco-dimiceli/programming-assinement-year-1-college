
## importing custom tkinter and message box ##

import customtkinter
# import tkinter as tk
from tkinter import messagebox
class my_gui:

##        ##------------------------------------------------------------------------------------------------------------

    ## functions ##

## frame for edit events ##

    def edit_events_content_frame(self, label_text, ):

        self.edit_events_main_frame = customtkinter.CTkFrame(self.new_frame, )

        self.edit_events_main_frame.rowconfigure(0, weight=1)
        self.edit_events_main_frame.rowconfigure(1, weight=1)
        self.edit_events_main_frame.rowconfigure(2, weight=1)
        self.edit_events_main_frame.columnconfigure(0, weight=1)

        self.event_label = customtkinter.CTkLabel(self.edit_events_main_frame, text=label_text, font=("roboto", 18)).grid(row=0, pady=10, padx=30, )

        self.event_entry = customtkinter.CTkEntry(self.edit_events_main_frame, width=500).grid(row=1, pady=10, )

        return self.edit_events_main_frame

    def edit_events_content_frame_func(self):

        self.edit_events_content_frame("Event 1").place(x=50, y=25)
        self.edit_events_content_frame("Event 2").place(x=50, y=150)
        self.edit_events_content_frame("Event 3").place(x=50, y=275)
        self.edit_events_content_frame("Event 4").place(x=50, y=400)
        self.edit_events_content_frame("Event 5").place(x=50, y=525)

##      ##--------------------------------------------------------------------------------------------------------------

## edit teams and individuals navigation frame ##

    def event_1_to_5_buttons_frame(self, label_text, command):

        self.events_1_to_5_main_frame = customtkinter.CTkFrame(self.frame_for_event_bottons, )

##      ##--------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals frame ##

    def edit_teams_content_frame(self, label_text, ):

        self.edit_teams_main_frame = customtkinter.CTkFrame(self.editing_teams_frame, )

        self.edit_teams_main_frame.columnconfigure(0, weight=1)
        self.edit_teams_main_frame.columnconfigure(1, weight=1)
        self.edit_teams_main_frame.rowconfigure(0, weight=1)
        self.edit_teams_main_frame.rowconfigure(1, weight=1)
        self.edit_teams_main_frame.rowconfigure(2, weight=1)
        self.edit_teams_main_frame.rowconfigure(3, weight=1)
        self.edit_teams_main_frame.rowconfigure(4, weight=1)
        self.edit_teams_main_frame.rowconfigure(5, weight=1)
        self.edit_teams_main_frame.rowconfigure(6, weight=1)

        self.place_label = customtkinter.CTkLabel(self.edit_teams_main_frame, text=label_text, font=("roboto", 18), ).grid(column=0, row=0, pady=10)

        self.team_entry = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter team name", font=("roboto", 16), height=35, ).grid(column=0, row=1, pady=10, padx=10, )

        self.individual_text_box_1 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 1", font=("roboto", 14), width=150, height=35, ).grid(column=1, row=2, pady=10, padx=10)
        self.individual_text_box_2 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 2", font=("roboto", 14), width=150, height=35, ).grid(column=1, row=3, pady=10, padx=10)
        self.individual_text_box_3 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 3", font=("roboto", 14), width=150, height=35, ).grid(column=1, row=4, pady=10, padx=10)
        self.individual_text_box_4 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 4", font=("roboto", 14), width=150, height=35, ).grid(column=1, row=5, pady=10, padx=10)
        self.individual_text_box_5 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 5", font=("roboto", 14), width=150, height=35, ).grid(column=1, row=6, pady=10, padx=10)

        return self.edit_teams_main_frame

    def edit_teams_content_frame_func(self):

        self.edit_teams_content_frame("1st place").place(x=50, y=25)
        self.edit_teams_content_frame("3rd place").place(x=50, y=415)
        self.edit_teams_content_frame("2nd place").place(x=500, y=25)
        self.edit_teams_content_frame("4th place").place(x=500, y=415)

##      ##--------------------------------------------------------------------------------------------------------------


## switching navigation frame functions ##
    def switch_to_events_menu_frame(self):

        self.event_menu_frame_navigation.pack(fill="x", )
        self.edit_events_content_frame_func()
        self.new_frame.place(x=100, y=100)

        self.navigation_button_frame.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()
        self.edit_teams_and_individuals_content_frame.pack_forget()
        self.display_scoreboard_content_frame.pack_forget()

    def switch_to_start_menu_frame(self):

        self.navigation_button_frame.pack(fill="x", )

        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()
        self.edit_teams_and_individuals_content_frame.pack_forget()
        self.display_scoreboard_content_frame.pack_forget()
        self.new_frame.place_forget()

    def switch_to_edit_teams_and_individuals_frame(self):

        self.teams_and_individuals_frame_navigation.pack(fill="x", )
        self.edit_teams_and_individuals_content_frame.pack(pady=80)

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()
        self.display_scoreboard_content_frame.pack_forget()
        self.new_frame.place_forget()

    def switch_to_display_scoreboard_frame(self):

        self.display_scoreboard_frame_navigation.pack(fill="x", )
        self.display_scoreboard_content_frame.pack(pady=80)

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.edit_teams_and_individuals_content_frame.pack_forget()
        self.new_frame.place_forget()

    def switch_to_edit_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_teams_content_frame_func()

        self.edit_teams_and_individuals_content_frame.pack_forget()

    def close_the_program(self):

        if self.msg.askyesno(title="Exit?", message="Are you sure you want to leave?", ):

            self.root.destroy()

##      ##--------------------------------------------------------------------------------------------------------------

    def __init__(self):

    ## initialising the GUI ##

        self.root = customtkinter.CTk()

        self.root.title("scoring system")

        self.root.geometry("1300x1000")

    ## gets rid of the close, minimise and maximize options at the top 1 = get rid, 0 = its still there ##

        self.root.overrideredirect(True)

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

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit teams and individuals\n", font=("roboto", 20), height=2, command=self.switch_to_edit_teams_and_individuals_frame, hover_color="#02557a").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nStart menu\n", font=("roboto", 20), height=0, command=self.switch_to_start_menu_frame, hover_color="#02557a").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit events\n", font=("roboto", 20), height=0, command=self.switch_to_events_menu_frame, fg_color="#02557a", hover_color="#02557a").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nClose program\n", font=("roboto", 20), height=0, command=self.close_the_program, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu content ##

        self.new_frame = customtkinter.CTkFrame(self.root, width=600, height=650, )

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

        self.close_program_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nClose program\n", font=("roboto", 20), height=0, command=self.close_the_program, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals content ##

        self.edit_teams_and_individuals_content_frame = customtkinter.CTkFrame(self.root, fg_color="#262626", height=400, width=400)

        self.edit_teams_and_individuals_content_frame.columnconfigure(0, weight=0, )
        self.edit_teams_and_individuals_content_frame.columnconfigure(1, weight=0, )

        self.edit_individuals_button = customtkinter.CTkButton(self.edit_teams_and_individuals_content_frame, text="Edit individuals", font=("roboto", 20), height=600, width=400, hover_color="#02557a").grid(row=0, column=0, padx=100, pady=50)

        self.edit_teams_button = customtkinter.CTkButton(self.edit_teams_and_individuals_content_frame, text="Edit teams", font=("roboto", 20), height=600, width=400, hover_color="#02557a", command=self.switch_to_edit_teams_menu).grid(row=0, column=1, padx=100, pady=50)

        self.editing_teams_frame = customtkinter.CTkFrame(self.root, width=850, height=800, )

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

        self.close_program_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nClose program\n", font=("roboto", 20), height=0, command=self.close_the_program, hover_color="#02557a").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

    ## display scoreboard content ##

        self.display_scoreboard_content_frame = customtkinter.CTkFrame(self.root, fg_color="#262626", height=400, width=400)

        self.display_scoreboard_content_frame.columnconfigure(0, weight=0, )
        self.display_scoreboard_content_frame.columnconfigure(1, weight=0, )

        self.edit_individuals_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Edit individuals", font=("roboto", 20), height=600, width=400, hover_color="#02557a").grid(row=0, column=0, padx=100, pady=50)

        self.edit_teams_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Edit teams", font=("roboto", 20), height=600, width=400, hover_color="#02557a").grid(row=0, column=1, padx=100, pady=50)

##        ##------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

my_gui()
