
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

    def edit_teams_content_frame(self, label_text, variable_1, variable_2, variable_3, variable_4, variable_5, team_name):

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

        self.team_entry = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter team name", font=("roboto", 16), height=35, textvariable=team_name, ).grid(column=0, row=1, pady=10, padx=10, )

        self.individual_text_box_1 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 1", font=("roboto", 14), width=150, height=35, textvariable=variable_1, ).grid(column=1, row=2, pady=10, padx=10)
        self.individual_text_box_2 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 2", font=("roboto", 14), width=150, height=35, textvariable=variable_2, ).grid(column=1, row=3, pady=10, padx=10)
        self.individual_text_box_3 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 3", font=("roboto", 14), width=150, height=35, textvariable=variable_3, ).grid(column=1, row=4, pady=10, padx=10)
        self.individual_text_box_4 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 4", font=("roboto", 14), width=150, height=35, textvariable=variable_4, ).grid(column=1, row=5, pady=10, padx=10)
        self.individual_text_box_5 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 5", font=("roboto", 14), width=150, height=35, textvariable=variable_5, ).grid(column=1, row=6, pady=10, padx=10)

        return self.edit_teams_main_frame
    def edit_teams_content_frame_func(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_1, self.individual_2_team_1_event_1, self.individual_3_team_1_event_1, self.individual_4_team_1_event_1, self.individual_5_team_1_event_1, self.team_1_event_1, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_1, self.individual_2_team_3_event_1, self.individual_3_team_3_event_1, self.individual_4_team_3_event_1, self.individual_5_team_3_event_1, self.team_2_event_1, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_1, self.individual_2_team_2_event_1, self.individual_3_team_2_event_1, self.individual_4_team_2_event_1, self.individual_5_team_2_event_1, self.team_3_event_1, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_1, self.individual_2_team_4_event_1, self.individual_3_team_4_event_1, self.individual_4_team_4_event_1, self.individual_5_team_4_event_1, self.team_4_event_1, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_1_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

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

    ## data storage for teams ##

    def save_team_names(self, name, line_to_write_to, ):

        with open("event_info.txt") as f:

            lines = f.readlines()

            lines[line_to_write_to] = name + "\n"

            with open("event_info.txt", "w") as f:

                for line in lines:

                    f.write(line)

    ## data validashion for team names ##

    def check_team_name_input(self, input, line_num, ):

        self.name_input = input

        self.validashion_points = 0

        if self.name_input == "":

            self.msg.showinfo(title="Error", message=("Team names cant be blank, if there is no team just leave the teams as team 1, team 2, team 3 and team 4"))

        else:

            self.validashion_points = self.validashion_points + 1

        if len(self.name_input) > 13:

            self.msg.showinfo(title="Error", message=(self.name_input + ": cant be more then 13 charicters"))

        else:

            self.validashion_points = self.validashion_points + 1

        if self.validashion_points == 2:

            self.save_team_names(self.name_input, line_num)

    ## data saveing for individuals ##

    def data_storage_func(self, verable, line_to_write_to, ):

        with open("event_info.txt") as f:

            lines = f.readlines()

            lines[line_to_write_to] = verable + "\n"

            with open("event_info.txt", "w") as f:

                for line in lines:

                    f.write(line)

    ## data validation for individuals ##
    def check_student_num_input(self, input, line_num):

        self.invalid_charicters = (":", ";", "/", ",", ".", ">", "<", "?", "|", "@", "'", "#", "~", "-", "_", "=", "+", "}", "{", "[", "]", "(", ")", "¬", "`", "!", "£", "$", "%", "^", "&", "*", )

        self.charicters_counter = 0

        self.user_input = input

        print(self.user_input)

        self.validashion_chechks = 0

        if self.user_input == "":

            self.msg.showinfo(title="Error", message="cant leve indvidual feilds blank. input 000000 if no one is playing")

        else:

            self.validashion_chechks = + 1

        for char in self.invalid_charicters:

            if char in self.user_input:

                self.charicters_counter = + 1

        if self.charicters_counter > 0:

            self.msg.showinfo(title="Error", message=(self.user_input + ": cant have :, ;, /, , ., >, <, ?, |, @, ', # ~, -, _, =, +, }, {, [, ], (, ), ¬, `, !, £, $, %, ^, &, *, in the student number"))

        else:

            self.validashion_chechks = self.validashion_chechks + 1

        try:

            int(self.user_input); self.validashion_chechks = self.validashion_chechks + 1

        except ValueError:

            self.msg.showinfo(title="Error", message=(self.user_input + ": must be a student number, names and other words wont be accepted"))

        if len(self.user_input) > 6:

            self.msg.showinfo(title="Error", message=(self.user_input + ": cant have more the 6 numbers: "))

        else:

            self.validashion_chechks = self.validashion_chechks + 1

        if len(self.user_input) < 6:

            self.msg.showinfo(title="Error", message=(self.user_input + ": cant be less then 6 numbers"))

        else:

            self.validashion_chechks = self.validashion_chechks + 1

        if self.validashion_chechks == 5:

            self.data_storage_func(self.user_input, line_num)


    ## data validashion for event 1 ##
    def data_validashion_for_event_1_team_1(self):

        self.check_team_name_input(self.team_1_event_1.get(), 20, )
        self.check_student_num_input(self.individual_1_team_1_event_1.get(), 0)
        self.check_student_num_input(self.individual_2_team_1_event_1.get(), 1)
        self.check_student_num_input(self.individual_3_team_1_event_1.get(), 2)
        self.check_student_num_input(self.individual_4_team_1_event_1.get(), 3)
        self.check_student_num_input(self.individual_5_team_1_event_1.get(), 4)

    def data_validashion_for_event_1_team_2(self):

        self.check_team_name_input(self.team_2_event_1.get(), 21, )
        self.check_student_num_input(self.individual_1_team_2_event_1.get(), 5)
        self.check_student_num_input(self.individual_2_team_2_event_1.get(), 6)
        self.check_student_num_input(self.individual_3_team_2_event_1.get(), 7)
        self.check_student_num_input(self.individual_4_team_2_event_1.get(), 8)
        self.check_student_num_input(self.individual_5_team_2_event_1.get(), 9)
    def data_validashion_for_event_1_team_3(self):

        self.check_team_name_input(self.team_3_event_1.get(), 22, )
        self.check_student_num_input(self.individual_1_team_3_event_1.get(), 10)
        self.check_student_num_input(self.individual_2_team_3_event_1.get(), 11)
        self.check_student_num_input(self.individual_3_team_3_event_1.get(), 12)
        self.check_student_num_input(self.individual_4_team_3_event_1.get(), 13)
        self.check_student_num_input(self.individual_5_team_3_event_1.get(), 14)

    def data_validashion_for_event_1_team_4(self):

        self.check_team_name_input(self.team_4_event_1.get(), 23, )
        self.check_student_num_input(self.individual_1_team_4_event_1.get(), 15)
        self.check_student_num_input(self.individual_2_team_4_event_1.get(), 16)
        self.check_student_num_input(self.individual_3_team_4_event_1.get(), 17)
        self.check_student_num_input(self.individual_4_team_4_event_1.get(), 18)
        self.check_student_num_input(self.individual_5_team_4_event_1.get(), 19)
    def data_validashion_for_event_1_teams_all_func(self):

        self.data_validashion_for_event_1_team_1()
        self.data_validashion_for_event_1_team_2()
        self.data_validashion_for_event_1_team_3()
        self.data_validashion_for_event_1_team_4()

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

        self.combo_box_var = customtkinter.StringVar()

        with open("event_info.txt", "r") as f:

            data = f.read().splitlines()

                ## edit teams verables ##

            ## event 1 ##

            ## team 1 ##
            self.individual_1_team_1_event_1, self.individual_2_team_1_event_1, self.individual_3_team_1_event_1, self.individual_4_team_1_event_1, self.individual_5_team_1_event_1, = customtkinter.StringVar(value=data[0]), customtkinter.StringVar(value=data[1]), customtkinter.StringVar(value=data[2]), customtkinter.StringVar(value=data[3]), customtkinter.StringVar(value=data[4])

            ## team 2 ##
            self.individual_1_team_2_event_1, self.individual_2_team_2_event_1, self.individual_3_team_2_event_1, self.individual_4_team_2_event_1, self.individual_5_team_2_event_1, = customtkinter.StringVar(value=data[5]), customtkinter.StringVar(value=data[6]), customtkinter.StringVar(value=data[7]), customtkinter.StringVar(value=data[8]), customtkinter.StringVar(value=data[9])

            ## team 3 ##
            self.individual_1_team_3_event_1, self.individual_2_team_3_event_1, self.individual_3_team_3_event_1, self.individual_4_team_3_event_1, self.individual_5_team_3_event_1, = customtkinter.StringVar(value=data[10]), customtkinter.StringVar(value=data[11]), customtkinter.StringVar(value=data[12]), customtkinter.StringVar(value=data[13]), customtkinter.StringVar(value=data[14])

            ## team 4 ##
            self.individual_1_team_4_event_1, self.individual_2_team_4_event_1, self.individual_3_team_4_event_1, self.individual_4_team_4_event_1, self.individual_5_team_4_event_1, = customtkinter.StringVar(value=data[15]), customtkinter.StringVar(value=data[16]), customtkinter.StringVar(value=data[17]), customtkinter.StringVar(value=data[18]), customtkinter.StringVar(value=data[19])

            ## team names for event 1 ##
            self.team_1_event_1, self.team_2_event_1, self.team_3_event_1, self.team_4_event_1 = customtkinter.StringVar(value=data[20]), customtkinter.StringVar(value=data[21]), customtkinter.StringVar(value=data[22]), customtkinter.StringVar(value=data[23])

            ## event 2 ##

            ## team 1 ##
            self.individual_1_team_1_event_2, self.individual_2_team_1_event_2, self.individual_3_team_1_event_2, self.individual_4_team_1_event_2, self.individual_5_team_1_event_2, = customtkinter.StringVar(value=data[24]), customtkinter.StringVar(value=data[25]), customtkinter.StringVar(value=data[26]), customtkinter.StringVar(value=data[27]), customtkinter.StringVar(value=data[28])

            ## team 2 ##
            self.individual_1_team_2_event_2, self.individual_2_team_2_event_2, self.individual_3_team_2_event_2, self.individual_4_team_2_event_2, self.individual_5_team_2_event_2, = customtkinter.StringVar(value=data[29]), customtkinter.StringVar(value=data[30]), customtkinter.StringVar(value=data[31]), customtkinter.StringVar(value=data[32]), customtkinter.StringVar(value=data[33])

            ## team 3 ##
            self.individual_1_team_3_event_2, self.individual_2_team_3_event_2, self.individual_3_team_3_event_2, self.individual_4_team_3_event_2, self.individual_5_team_3_event_2, = customtkinter.StringVar(value=data[34]), customtkinter.StringVar(value=data[35]), customtkinter.StringVar(value=data[36]), customtkinter.StringVar(value=data[37]), customtkinter.StringVar(value=data[38])

            ## team 4 ##
            self.individual_1_team_4_event_2, self.individual_2_team_4_event_2, self.individual_3_team_4_event_2, self.individual_4_team_4_event_2, self.individual_5_team_4_event_2, = customtkinter.StringVar(value=data[39]), customtkinter.StringVar(value=data[40]), customtkinter.StringVar(value=data[41]), customtkinter.StringVar(value=data[42]), customtkinter.StringVar(value=data[43])

            ## team names for event 2 ##
            self.team_1_event_2, self.team_2_event_2, self.team_3_event_2, self.team_4_event_2 = customtkinter.StringVar(value=data[44]), customtkinter.StringVar(value=data[45]), customtkinter.StringVar(value=data[46]), customtkinter.StringVar(value=data[47])

            ## event 3 ##

            ## team 1 ##
            self.individual_1_team_1_event_3, self.individual_2_team_1_event_3, self.individual_3_team_1_event_3, self.individual_4_team_1_event_3, self.individual_5_team_1_event_3, = customtkinter.StringVar(value=data[48]), customtkinter.StringVar(value=data[49]), customtkinter.StringVar(value=data[50]), customtkinter.StringVar(value=data[51]), customtkinter.StringVar(value=data[52])

            ## team 2 ##
            self.individual_1_team_2_event_3, self.individual_2_team_2_event_3, self.individual_3_team_2_event_3, self.individual_4_team_2_event_3, self.individual_5_team_2_event_3, = customtkinter.StringVar(value=data[53]), customtkinter.StringVar(value=data[54]), customtkinter.StringVar(value=data[55]), customtkinter.StringVar(value=data[56]), customtkinter.StringVar(value=data[57])

            ## team 3 ##
            self.individual_1_team_3_event_3, self.individual_2_team_3_event_3, self.individual_3_team_3_event_3, self.individual_4_team_3_event_3, self.individual_5_team_3_event_3, = customtkinter.StringVar(value=data[58]), customtkinter.StringVar(value=data[59]), customtkinter.StringVar(value=data[60]), customtkinter.StringVar(value=data[61]), customtkinter.StringVar(value=data[62])

            ## team 4 ##
            self.individual_1_team_4_event_3, self.individual_2_team_4_event_3, self.individual_3_team_4_event_3, self.individual_4_team_4_event_3, self.individual_5_team_4_event_3, = customtkinter.StringVar(value=data[63]), customtkinter.StringVar(value=data[64]), customtkinter.StringVar(value=data[65]), customtkinter.StringVar(value=data[66]), customtkinter.StringVar(value=data[67])

            ## team names for event 3 ##
            self.team_1_event_3, self.team_2_event_3, self.team_3_event_3, self.team_4_event_3 = customtkinter.StringVar(value=data[68]), customtkinter.StringVar(value=data[69]), customtkinter.StringVar(value=data[70]), customtkinter.StringVar(value=data[71])

            ## event 4 ##

            ## team 1 ##
            self.individual_1_team_1_event_4, self.individual_2_team_1_event_4, self.individual_3_team_1_event_4, self.individual_4_team_1_event_4, self.individual_5_team_1_event_4, = customtkinter.StringVar(value=data[72]), customtkinter.StringVar(value=data[73]), customtkinter.StringVar(value=data[74]), customtkinter.StringVar(value=data[75]), customtkinter.StringVar(value=data[76])

            ## team 2 ##
            self.individual_1_team_2_event_4, self.individual_2_team_2_event_4, self.individual_3_team_2_event_4, self.individual_4_team_2_event_4, self.individual_5_team_2_event_4, = customtkinter.StringVar(value=data[77]), customtkinter.StringVar(value=data[78]), customtkinter.StringVar(value=data[79]), customtkinter.StringVar(value=data[80]), customtkinter.StringVar(value=data[81])

            ## team 3 ##
            self.individual_1_team_3_event_4, self.individual_2_team_3_event_4, self.individual_3_team_3_event_4, self.individual_4_team_3_event_4, self.individual_5_team_3_event_4, = customtkinter.StringVar(value=data[82]), customtkinter.StringVar(value=data[83]), customtkinter.StringVar(value=data[84]), customtkinter.StringVar(value=data[85]), customtkinter.StringVar(value=data[86])

            ## team 4 ##
            self.individual_1_team_4_event_4, self.individual_2_team_4_event_4, self.individual_3_team_4_event_4, self.individual_4_team_4_event_4, self.individual_5_team_4_event_4, = customtkinter.StringVar(value=data[87]), customtkinter.StringVar(value=data[88]), customtkinter.StringVar(value=data[89]), customtkinter.StringVar(value=data[90]), customtkinter.StringVar(value=data[91])

            ## team names for event 4 ##
            self.team_1_event_4, self.team_2_event_4, self.team_3_event_4, self.team_4_event_4 = customtkinter.StringVar(value=data[92]), customtkinter.StringVar(value=data[93]), customtkinter.StringVar(value=data[94]), customtkinter.StringVar(value=data[95])

            ## event 5 ##

            ## team 1 ##
            self.individual_1_team_1_event_5, self.individual_2_team_1_event_5, self.individual_3_team_1_event_5, self.individual_4_team_1_event_5, self.individual_5_team_1_event_5, = customtkinter.StringVar(value=data[96]), customtkinter.StringVar(value=data[97]), customtkinter.StringVar(value=data[98]), customtkinter.StringVar(value=data[99]), customtkinter.StringVar(value=data[100])

            ## team 2 ##
            self.individual_1_team_2_event_5, self.individual_2_team_2_event_5, self.individual_3_team_2_event_5, self.individual_4_team_2_event_5, self.individual_5_team_2_event_5, = customtkinter.StringVar(value=data[101]), customtkinter.StringVar(value=data[102]), customtkinter.StringVar(value=data[103]), customtkinter.StringVar(value=data[104]), customtkinter.StringVar(value=data[105])

            ## team 3 ##
            self.individual_1_team_3_event_5, self.individual_2_team_3_event_5, self.individual_3_team_3_event_5, self.individual_4_team_3_event_5, self.individual_5_team_3_event_5, = customtkinter.StringVar(value=data[106]), customtkinter.StringVar(value=data[107]), customtkinter.StringVar(value=data[108]), customtkinter.StringVar(value=data[109]), customtkinter.StringVar(value=data[110])

            ## team 4 ##
            self.individual_1_team_4_event_5, self.individual_2_team_4_event_5, self.individual_3_team_4_event_5, self.individual_4_team_4_event_5, self.individual_5_team_4_event_4, = customtkinter.StringVar(value=data[111]), customtkinter.StringVar(value=data[112]), customtkinter.StringVar(value=data[113]), customtkinter.StringVar(value=data[114]), customtkinter.StringVar(value=data[115])

            ## team names for event 5 ##
            self.team_1_event_5, self.team_2_event_5, self.team_3_event_5, self.team_4_event_5 = customtkinter.StringVar(value=data[116]), customtkinter.StringVar(value=data[117]), customtkinter.StringVar(value=data[118]), customtkinter.StringVar(value=data[119])

                ## individuals verables ##

            ## event 1 ##

            self.individual_1_event_1, self.individual_2_event_1, self.individual_3_event_1, self.individual_4_event_1, self.individual_5_event_1 = customtkinter.StringVar(value=data[120]), customtkinter.StringVar(value=data[121]), customtkinter.StringVar(value=data[122]), customtkinter.StringVar(value=data[123]), customtkinter.StringVar(value=data[124])
            self.individual_6_event_1, self.individual_7_event_1, self.individual_8_event_1, self.individual_9_event_1, self.individual_10_event_1 = customtkinter.StringVar(value=data[125]), customtkinter.StringVar(value=data[126]), customtkinter.StringVar(value=data[127]), customtkinter.StringVar(value=data[128]), customtkinter.StringVar(value=data[129])
            self.individual_11_event_1, self.individual_12_event_1, self.individual_13_event_1, self.individual_14_event_1, self.individual_15_event_1 = customtkinter.StringVar(value=data[130]), customtkinter.StringVar(value=data[131]), customtkinter.StringVar(value=data[132]), customtkinter.StringVar(value=data[133]), customtkinter.StringVar(value=data[134])
            self.individual_16_event_1, self.individual_17_event_1, self.individual_18_event_1, self.individual_19_event_1, self.individual_20_event_1 = customtkinter.StringVar(value=data[135]), customtkinter.StringVar(value=data[136]), customtkinter.StringVar(value=data[137]), customtkinter.StringVar(value=data[138]), customtkinter.StringVar(value=data[139])

            ## event 2 ##

            self.individual_1_event_2, self.individual_2_event_2, self.individual_3_event_2, self.individual_4_event_2, self.individual_5_event_2 = customtkinter.StringVar(value=data[140]), customtkinter.StringVar(value=data[141]), customtkinter.StringVar(value=data[142]), customtkinter.StringVar(value=data[143]), customtkinter.StringVar(value=data[144])
            self.individual_6_event_2, self.individual_7_event_2, self.individual_8_event_2, self.individual_9_event_2, self.individual_10_event_2 = customtkinter.StringVar(value=data[145]), customtkinter.StringVar(value=data[146]), customtkinter.StringVar(value=data[147]), customtkinter.StringVar(value=data[148]), customtkinter.StringVar(value=data[149])
            self.individual_11_event_2, self.individual_12_event_2, self.individual_13_event_2, self.individual_14_event_2, self.individual_15_event_2 = customtkinter.StringVar(value=data[150]), customtkinter.StringVar(value=data[151]), customtkinter.StringVar(value=data[152]), customtkinter.StringVar(value=data[153]), customtkinter.StringVar(value=data[154])
            self.individual_16_event_2, self.individual_17_event_2, self.individual_18_event_2, self.individual_19_event_2, self.individual_20_event_2 = customtkinter.StringVar(value=data[155]), customtkinter.StringVar(value=data[156]), customtkinter.StringVar(value=data[157]), customtkinter.StringVar(value=data[158]), customtkinter.StringVar(value=data[159])

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
