
## importing custom tkinter and message box ##

import customtkinter
from tkinter import messagebox
class my_gui:

##        ##------------------------------------------------------------------------------------------------------------

    ## functions ##

## frame for edit events ##

    def edit_events_content_frame(self, text_var, ):

        self.edit_events_main_frame = customtkinter.CTkFrame(self.new_frame, )

        self.edit_events_main_frame.rowconfigure(0, weight=1)
        self.edit_events_main_frame.rowconfigure(1, weight=1)
        self.edit_events_main_frame.rowconfigure(2, weight=1)
        self.edit_events_main_frame.columnconfigure(0, weight=1)

        self.event_label = customtkinter.CTkLabel(self.edit_events_main_frame, font=self.the_font_small, textvariable=text_var, ).grid(row=0, pady=10, padx=30, )

        self.event_entry = customtkinter.CTkEntry(self.edit_events_main_frame, width=500, textvariable=text_var).grid(row=1, pady=10, )

        return self.edit_events_main_frame

    def edit_events_content_frame_func(self):

        self.edit_events_content_frame(self.event_1_variable).place(x=50, y=25)
        self.edit_events_content_frame(self.event_2_variable).place(x=50, y=150)
        self.edit_events_content_frame(self.event_3_variable).place(x=50, y=275)
        self.edit_events_content_frame(self.event_4_variable).place(x=50, y=400)
        self.edit_events_content_frame(self.event_5_variable).place(x=50, y=525)

##      ##--------------------------------------------------------------------------------------------------------------

## edit teams and individuals navigation frame ##

    def event_1_to_5_buttons_frame(self,  variable_1, variable_2, variable_3, variable_4, variable_5, command_1, ):

        self.events_1_to_5_main_frame = customtkinter.CTkFrame(self.root, width=850, height=800, )

        self.event_1_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_1, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_1).grid(row=0, column=0, pady=10, padx=10)
        self.event_2_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_2, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, ).grid(row=0, column=1, pady=10, padx=10)
        self.event_3_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_3, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, ).grid(row=0, column=2, pady=10, padx=10)
        self.event_4_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_4, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, ).grid(row=0, column=3, pady=10, padx=10)
        self.event_5_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_5, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, ).grid(row=0, column=4, pady=10, padx=10)

        return self.events_1_to_5_main_frame

##      ##--------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals frame content ##

    def edit_teams_content_frame(self, label_text, variable_1, variable_2, variable_3, variable_4, variable_5):

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

        self.place_label = customtkinter.CTkLabel(self.edit_teams_main_frame, text=label_text, font=self.the_font_small, ).grid(column=0, row=0, pady=10)

        self.team_entry = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter team name", font=("roboto", 16), height=35, ).grid(column=0, row=1, pady=10, padx=10, )

        self.individual_text_box_1 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 1", font=("roboto", 14), width=150, height=35, textvariable=variable_1, ).grid(column=1, row=2, pady=10, padx=10)
        self.individual_text_box_2 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 2", font=("roboto", 14), width=150, height=35, textvariable=variable_2, ).grid(column=1, row=3, pady=10, padx=10)
        self.individual_text_box_3 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 3", font=("roboto", 14), width=150, height=35, textvariable=variable_3, ).grid(column=1, row=4, pady=10, padx=10)
        self.individual_text_box_4 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 4", font=("roboto", 14), width=150, height=35, textvariable=variable_4, ).grid(column=1, row=5, pady=10, padx=10)
        self.individual_text_box_5 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 5", font=("roboto", 14), width=150, height=35, textvariable=variable_5, ).grid(column=1, row=6, pady=10, padx=10)

        return self.edit_teams_main_frame

    def edit_teams_content_frame_func(self):

        self.edit_teams_content_frame("1st place", self.student_num_variables, self.individual_2_team_1, self.individual_3_team_1, self.individual_4_team_1, self.individual_5_team_1, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3, self.individual_2_team_3, self.individual_3_team_3, self.individual_4_team_3, self.individual_5_team_3,).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2, self.individual_2_team_2, self.individual_3_team_2, self.individual_4_team_2, self.individual_5_team_2,).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4, self.individual_2_team_4, self.individual_3_team_4, self.individual_4_team_4, self.individual_5_team_4,).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.check_student_num_input, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    ## editing individuals frame #
    # def edit_individuals_frame(self, ):
    #
    #     self.edit_individuals_event_1_1_menu = customtkinter.CTkFrame(self.edit_individuals_event_1_menu)
    #
    #     self.individual_entry_1 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=0, padx=10, pady=10, )
    #     self.first_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="1st place", font=self.the_font_small, ).grid(column=0, row=0, padx=10, pady=10, )
    #
    #     self.individual_entry_2 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=1, padx=10, pady=10, )
    #     self.second_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="2nd place", font=self.the_font_small, ).grid(column=0, row=1, padx=10, pady=10, )
    #
    #     self.individual_entry_3 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=2, padx=10, pady=10, )
    #     self.third_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="3rd place", font=self.the_font_small, ).grid(column=0, row=2, padx=10, pady=10, )
    #
    #     self.individual_entry_4 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=3, padx=10, pady=10, )
    #     self.forth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="4th place", font=self.the_font_small, ).grid(column=0, row=3, padx=10, pady=10, )
    #
    #     self.individual_entry_5 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=4, padx=10, pady=10, )
    #     self.fifth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="5th place", font=self.the_font_small, ).grid(column=0, row=4, padx=10, pady=10, )
    #
    #     self.individual_entry_6 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=5, padx=10, pady=10, )
    #     self.sixth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="6th place", font=self.the_font_small, ).grid(column=0, row=5, padx=10, pady=10, )
    #
    #     self.individual_entry_7 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=6, padx=10, pady=10, )
    #     self.seventh_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="7th place", font=self.the_font_small, ).grid(column=0, row=6, padx=10, pady=10, )
    #
    #     self.individual_entry_8 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=7, padx=10, pady=10, )
    #     self.eighth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="8th place", font=self.the_font_small, ).grid(column=0, row=7, padx=10, pady=10, )
    #
    #     self.individual_entry_9 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=8, padx=10, pady=10, )
    #     self.ninth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="9th place", font=self.the_font_small, ).grid(column=0, row=8, padx=10, pady=10, )
    #
    #     self.individual_entry_10 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, ).grid(column=1, row=9, padx=10, pady=10, )
    #     self.tenth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text="10th place", font=self.the_font_small, ).grid(column=0, row=9, padx=10, pady=10, )
    #
    #     return self.edit_individuals_event_1_1_menu
    #
    # def edit_individuals_frame_func(self):
    #
    #     self.edit_individuals_frame().pack()

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
        self.events_1_to_5_main_frame.pack_forget()
        self.editing_teams_frame.pack_forget()

    def switch_to_start_menu_frame(self):

        self.navigation_button_frame.pack(fill="x", )

        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()
        self.edit_teams_and_individuals_content_frame.pack_forget()
        self.display_scoreboard_content_frame.pack_forget()
        self.new_frame.place_forget()
        self.events_1_to_5_main_frame.pack_forget()
        self.editing_teams_frame.pack_forget()

    def switch_to_edit_teams_and_individuals_frame(self):

        self.teams_and_individuals_frame_navigation.pack(fill="x", )
        self.edit_teams_and_individuals_content_frame.pack(pady=80)

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.display_scoreboard_frame_navigation.pack_forget()
        self.display_scoreboard_content_frame.pack_forget()
        self.new_frame.place_forget()
        self.events_1_to_5_main_frame.pack_forget()
        self.editing_teams_frame.pack_forget()

    def switch_to_display_scoreboard_frame(self):

        self.display_scoreboard_frame_navigation.pack(fill="x", )
        self.display_scoreboard_content_frame.pack(pady=80)

        self.navigation_button_frame.pack_forget()
        self.event_menu_frame_navigation.pack_forget()
        self.teams_and_individuals_frame_navigation.pack_forget()
        self.edit_teams_and_individuals_content_frame.pack_forget()
        self.new_frame.place_forget()
        self.events_1_to_5_main_frame.pack_forget()
        self.editing_teams_frame.pack_forget()

    def switch_to_edit_teams_menu(self):

        self.event_1_to_5_buttons_frame(self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable, self.switch_to_event_1_frame_teams_menu).pack(pady=250)

        self.edit_teams_and_individuals_content_frame.pack_forget()

    def switch_to_event_1_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_teams_content_frame_func()

        self.events_1_to_5_main_frame.pack_forget()

    def close_the_program(self):

        if self.msg.askyesno(title="Exit?", message="Are you sure you want to leave?", ):

            self.root.destroy()

##      ##--------------------------------------------------------------------------------------------------------------

    ## data validation ##

    def check_student_num_input(self):

        self.invalid_charicters = (":", ";", "/", ",", ".", ">", "<", "?", "|", "@", "'", "#", "~", "-", "_", "=", "+", "}", "{", "[", "]", "(", ")", "¬", "`", "!", "£", "$", "%", "^", "&", "*", )

        self.charicters_counter = 0

        self.user_input = self.student_num_variables.get()

        print(self.user_input)

        for char in self.invalid_charicters:

            if char in self.user_input:
                self.charicters_counter = + 1

        if self.charicters_counter > 0:

            self.msg.showinfo(title="Error", message="cant have :, ;, /, , ., >, <, ?, |, @, ', # ~, -, _, =, +, }, {, [, ], (, ), ¬, `, !, £, $, %, ^, &, *, in the student number")

        try:

            int(self.user_input)

        except ValueError:

            self.msg.showinfo(title="Error", message="must input a student number, names and other words wont be accepted")

        if len(self.user_input) > 6:

            self.msg.showinfo(title="Error", message="cant input more the 6 numbers")

        if self.user_input == self.individual_2_team_1 or self.individual_3_team_1 or self.individual_4_team_1 or self.individual_5_team_1:

            self.msg.showinfo(title="Error", message="cant have 2 of the same student in 1 team")

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

        self.the_font = customtkinter.CTkFont(family="roboto", size=20, weight="bold")

        self.the_font_small = customtkinter.CTkFont(family="roboto", size=18, weight="bold")

    ## frames ##

##        ##------------------------------------------------------------------------------------------------------------

    ## start menu navigation buttons ##

        self.navigation_button_frame = customtkinter.CTkFrame(self.root, fg_color="#002542")

        self.navigation_button_frame.columnconfigure(0, weight=1, )
        self.navigation_button_frame.columnconfigure(1, weight=1, )
        self.navigation_button_frame.columnconfigure(2, weight=1, )
        self.navigation_button_frame.columnconfigure(3, weight=1, )
        self.navigation_button_frame.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nDisplay scoreboard\n", font=self.the_font, height=0, command=self.switch_to_display_scoreboard_frame, hover_color="#25b2a1", fg_color="#002542", ).grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E,)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nEdit teams and individuals\n", font=self.the_font, height=0, command=self.switch_to_edit_teams_and_individuals_frame, fg_color="#002542", hover_color="#25b2a1").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nStart menu\n", font=self.the_font, height=0, command=self.switch_to_start_menu_frame, fg_color="#25b2a1", hover_color="#25b2a1").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nEdit events\n", font=self.the_font, height=0, command=self.switch_to_events_menu_frame, fg_color="#002542", hover_color="#25b2a1").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.navigation_button_frame, text="\nClose program\n", font=self.the_font, height=0, command=self.close_the_program, fg_color="#002542", hover_color="#25b2a1").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

        self.navigation_button_frame.pack(fill="x", )

##        ##------------------------------------------------------------------------------------------------------------

    ## start menu content ##

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu navigation ##

        self.event_menu_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#002542")

        self.event_menu_frame_navigation.columnconfigure(0, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(1, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(2, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(3, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nDisplay scoreboard\n", font=self.the_font, height=0, command=self.switch_to_display_scoreboard_frame, hover_color="#02557a", fg_color="#002542").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit teams and individuals\n", font=self.the_font, height=2, command=self.switch_to_edit_teams_and_individuals_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nStart menu\n", font=self.the_font, height=0, command=self.switch_to_start_menu_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nEdit events\n", font=self.the_font, height=0, command=self.switch_to_events_menu_frame, fg_color="#25b2a1", hover_color="#25b2a1").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.event_menu_frame_navigation, text="\nClose program\n", font=self.the_font, height=0, command=self.close_the_program, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu content ##

        self.new_frame = customtkinter.CTkFrame(self.root, width=600, height=650, )

        ## edit events variable ##

        self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable = customtkinter.StringVar(value="Event 1"), customtkinter.StringVar(value="Event 2"), customtkinter.StringVar(value="Event 3"), customtkinter.StringVar(value="Event 4"), customtkinter.StringVar(value="Event 5")

##        ##------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals navigation ##

        self.teams_and_individuals_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#002542")

        self.teams_and_individuals_frame_navigation.columnconfigure(0, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(1, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(2, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(3, weight=1, )
        self.teams_and_individuals_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nDisplay scoreboard\n", font=self.the_font, height=0, command=self.switch_to_display_scoreboard_frame, fg_color="#002542", hover_color="#25b2a1").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nEdit teams and individuals\n", font=self.the_font, height=0, command=self.switch_to_edit_teams_and_individuals_frame, fg_color="#25b2a1", hover_color="#25b2a1").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nStart menu\n", font=self.the_font, height=0, command=self.switch_to_start_menu_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nEdit events\n", font=self.the_font, height=0, command=self.switch_to_events_menu_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.teams_and_individuals_frame_navigation, text="\nClose program\n", font=self.the_font, height=0, command=self.close_the_program, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

    ## edit teams and individuals content navigation ##

        self.edit_teams_and_individuals_content_frame = customtkinter.CTkFrame(self.root, height=400, width=400)

        self.edit_teams_and_individuals_content_frame.columnconfigure(0, weight=0, )
        self.edit_teams_and_individuals_content_frame.columnconfigure(1, weight=0, )

        self.edit_individuals_button = customtkinter.CTkButton(self.edit_teams_and_individuals_content_frame, text="Edit individuals", font=self.the_font, height=600, width=400, fg_color="#002542", hover_color="#25b2a1").grid(row=0, column=0, padx=100, pady=50)

        self.edit_teams_button = customtkinter.CTkButton(self.edit_teams_and_individuals_content_frame, text="Edit teams", font=self.the_font, height=600, width=400, hover_color="#25b2a1", fg_color="#002542", command=self.switch_to_edit_teams_menu).grid(row=0, column=1, padx=100, pady=50)

    ## edit teams menu ##

        self.editing_teams_frame = customtkinter.CTkFrame(self.root, width=900, height=900, )

    ## edit teams variables ##

        ## event 1 ##

        ## team 1 ##
        self.student_num_variables, self.individual_2_team_1, self.individual_3_team_1, self.individual_4_team_1, self.individual_5_team_1,  = customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar()

        ## team 2 ##
        self.individual_1_team_2, self.individual_2_team_2, self.individual_3_team_2, self.individual_4_team_2, self.individual_5_team_2, = customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar()

        ## team 3 ##
        self.individual_1_team_3, self.individual_2_team_3, self.individual_3_team_3, self.individual_4_team_3, self.individual_5_team_3, = customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar()

        ## team 4 ##
        self.individual_1_team_4, self.individual_2_team_4, self.individual_3_team_4, self.individual_4_team_4, self.individual_5_team_4, = customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar(), customtkinter.StringVar()

    ## edit individuals menu ##

    ## edit individuals content ##

        self.edit_individuals_event_1_menu = customtkinter.CTkFrame(self.root, width=850, height=800, )

        # self.edit_individuals_event_1_menu.pack(pady=30)
        # self.edit_individuals_frame_func()

##        ##------------------------------------------------------------------------------------------------------------

    ## display scoreboard navigation ##

        self.display_scoreboard_frame_navigation = customtkinter.CTkFrame(self.root, fg_color="#002542")

        self.display_scoreboard_frame_navigation.columnconfigure(0, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(1, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(2, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(3, weight=1, )
        self.display_scoreboard_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nDisplay scoreboard\n", font=self.the_font, height=0, command=self.switch_to_display_scoreboard_frame, fg_color="#25b2a1", hover_color="#25b2a1").grid(row=0, column=0, sticky=customtkinter.W + customtkinter.E)

        self.edit_teams_and_individuals_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nEdit teams and individuals\n", font=self.the_font, height=0, command=self.switch_to_edit_teams_and_individuals_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=1, sticky=customtkinter.W + customtkinter.E)

        self.start_menu_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nStart menu\n", font=self.the_font, height=0, command=self.switch_to_start_menu_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=2, sticky=customtkinter.W + customtkinter.E)

        self.event_menu_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nEdit events\n", font=self.the_font, height=0, command=self.switch_to_events_menu_frame, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=3, sticky=customtkinter.W + customtkinter.E)

        self.close_program_button = customtkinter.CTkButton(self.display_scoreboard_frame_navigation, text="\nClose program\n", font=self.the_font, height=0, command=self.close_the_program, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=4, sticky=customtkinter.W + customtkinter.E,)

##        ##------------------------------------------------------------------------------------------------------------

    ## display scoreboard content ##

        self.display_scoreboard_content_frame = customtkinter.CTkFrame(self.root, height=400, width=400)

        self.display_scoreboard_content_frame.columnconfigure(0, weight=0, )
        self.display_scoreboard_content_frame.columnconfigure(1, weight=0, )

        self.edit_individuals_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Display individual scoreboards", font=self.the_font, height=600, width=400, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=0, padx=100, pady=50)

        self.edit_teams_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Display team scoreboards", font=self.the_font, height=600, width=400, hover_color="#25b2a1", fg_color="#002542").grid(row=0, column=1, padx=100, pady=50)

##        ##------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

my_gui()
