
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

    def event_1_to_5_buttons_frame(self,  variable_1, variable_2, variable_3, variable_4, variable_5, command_1, command_2, command_3, command_4, command_5):

        self.events_1_to_5_main_frame = customtkinter.CTkFrame(self.root, width=850, height=800, )

        self.event_1_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_1, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_1).grid(row=0, column=0, pady=10, padx=10)
        self.event_2_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_2, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_2).grid(row=0, column=1, pady=10, padx=10)
        self.event_3_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_3, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_3).grid(row=0, column=2, pady=10, padx=10)
        self.event_4_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_4, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_4).grid(row=0, column=3, pady=10, padx=10)
        self.event_5_button = customtkinter.CTkButton(self.events_1_to_5_main_frame, textvariable=variable_5, font=self.the_font_small, fg_color="#002542", hover_color="#25b2a1", height=300, width=225, command=command_5).grid(row=0, column=4, pady=10, padx=10)

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

        self.student_num_lable = customtkinter.CTkLabel(self.edit_teams_main_frame, font=("roboto", 14), text="enter student numbers:").grid(column=1, row=1, pady=10, padx=10,)

        self.individual_text_box_1 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 1", font=("roboto", 14), width=150, height=35, textvariable=variable_1, ).grid(column=1, row=2, pady=10, padx=10)
        self.individual_text_box_2 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 2", font=("roboto", 14), width=150, height=35, textvariable=variable_2, ).grid(column=1, row=3, pady=10, padx=10)
        self.individual_text_box_3 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 3", font=("roboto", 14), width=150, height=35, textvariable=variable_3, ).grid(column=1, row=4, pady=10, padx=10)
        self.individual_text_box_4 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 4", font=("roboto", 14), width=150, height=35, textvariable=variable_4, ).grid(column=1, row=5, pady=10, padx=10)
        self.individual_text_box_5 = customtkinter.CTkEntry(self.edit_teams_main_frame, placeholder_text="enter individual 5", font=("roboto", 14), width=150, height=35, textvariable=variable_5, ).grid(column=1, row=6, pady=10, padx=10)

        return self.edit_teams_main_frame

    ## event 1 ##
    def edit_teams_content_frame_func(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_1, self.individual_2_team_1_event_1, self.individual_3_team_1_event_1, self.individual_4_team_1_event_1, self.individual_5_team_1_event_1, self.team_1_event_1, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_1, self.individual_2_team_3_event_1, self.individual_3_team_3_event_1, self.individual_4_team_3_event_1, self.individual_5_team_3_event_1, self.team_2_event_1, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_1, self.individual_2_team_2_event_1, self.individual_3_team_2_event_1, self.individual_4_team_2_event_1, self.individual_5_team_2_event_1, self.team_3_event_1, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_1, self.individual_2_team_4_event_1, self.individual_3_team_4_event_1, self.individual_4_team_4_event_1, self.individual_5_team_4_event_1, self.team_4_event_1, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_1_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    def edit_team_content_frame_for_event_2(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_2, self.individual_2_team_1_event_2, self.individual_3_team_1_event_2, self.individual_4_team_1_event_2, self.individual_5_team_1_event_2, self.team_1_event_2, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_2, self.individual_2_team_3_event_2, self.individual_3_team_3_event_2, self.individual_4_team_3_event_2, self.individual_5_team_3_event_2, self.team_2_event_2, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_2, self.individual_2_team_2_event_2, self.individual_3_team_2_event_2, self.individual_4_team_2_event_2, self.individual_5_team_2_event_2, self.team_3_event_2, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_2, self.individual_2_team_4_event_2, self.individual_3_team_4_event_2, self.individual_4_team_4_event_2, self.individual_5_team_4_event_2, self.team_4_event_2, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_2_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    def edit_team_content_frame_for_event_3(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_3, self.individual_2_team_1_event_3, self.individual_3_team_1_event_3, self.individual_4_team_1_event_3, self.individual_5_team_1_event_3, self.team_1_event_3, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_3, self.individual_2_team_3_event_3, self.individual_3_team_3_event_3, self.individual_4_team_3_event_3, self.individual_5_team_3_event_3, self.team_2_event_3, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_3, self.individual_2_team_2_event_3, self.individual_3_team_2_event_3, self.individual_4_team_2_event_3, self.individual_5_team_2_event_3, self.team_3_event_3, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_3, self.individual_2_team_4_event_3, self.individual_3_team_4_event_3, self.individual_4_team_4_event_3, self.individual_5_team_4_event_3, self.team_4_event_3, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_3_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    def edit_team_content_frame_for_event_4(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_4, self.individual_2_team_1_event_4, self.individual_3_team_1_event_4, self.individual_4_team_1_event_4, self.individual_5_team_1_event_4, self.team_1_event_4, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_4, self.individual_2_team_3_event_4, self.individual_3_team_3_event_4, self.individual_4_team_3_event_4, self.individual_5_team_3_event_4, self.team_2_event_4, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_4, self.individual_2_team_2_event_4, self.individual_3_team_2_event_4, self.individual_4_team_2_event_4, self.individual_5_team_2_event_4, self.team_3_event_4, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_4, self.individual_2_team_4_event_4, self.individual_3_team_4_event_4, self.individual_4_team_4_event_4, self.individual_5_team_4_event_4, self.team_4_event_4, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_4_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    def edit_team_content_frame_for_event_5(self):

        self.edit_teams_content_frame("1st place", self.individual_1_team_1_event_5, self.individual_2_team_1_event_5, self.individual_3_team_1_event_5, self.individual_4_team_1_event_5, self.individual_5_team_1_event_5, self.team_1_event_5, ).place(x=50, y=25)
        self.edit_teams_content_frame("3rd place", self.individual_1_team_3_event_5, self.individual_2_team_3_event_5, self.individual_3_team_3_event_5, self.individual_4_team_3_event_5, self.individual_5_team_3_event_5, self.team_2_event_5, ).place(x=50, y=415)
        self.edit_teams_content_frame("2nd place", self.individual_1_team_2_event_5, self.individual_2_team_2_event_5, self.individual_3_team_2_event_5, self.individual_4_team_2_event_5, self.individual_5_team_2_event_5, self.team_3_event_5, ).place(x=500, y=25)
        self.edit_teams_content_frame("4th place", self.individual_1_team_4_event_5, self.individual_2_team_4_event_5, self.individual_3_team_4_event_5, self.individual_4_team_4_event_5, self.individual_5_team_4_event_5, self.team_4_event_5, ).place(x=500, y=415)
        self.save_and_back_button = customtkinter.CTkButton(self.editing_teams_frame, command=self.data_validashion_for_event_5_teams_all_func, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=750, y=800)

    ## editing individuals frame #
    def edit_individuals_frame(self, place_variable_1, place_variable_2, place_variable_3, place_variable_4, place_variable_5, place_variable_6, place_variable_7, place_variable_8, place_variable_9, place_variable_10, text_var_1, text_var_2, text_var_3, text_var_4, text_var_5, text_var_6, text_var_7, text_var_8, text_var_9, text_var_10, ):

        self.edit_individuals_event_1_1_menu = customtkinter.CTkFrame(self.edit_individuals_event_1_menu)

        self.individual_entry_1 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_1, ).grid(column=1, row=0, padx=10, pady=10, )
        self.first_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_1, font=self.the_font_small, ).grid(column=0, row=0, padx=10, pady=10, )

        self.individual_entry_2 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_2, ).grid(column=1, row=1, padx=10, pady=10, )
        self.second_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_2, font=self.the_font_small, ).grid(column=0, row=1, padx=10, pady=10, )

        self.individual_entry_3 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_3, ).grid(column=1, row=2, padx=10, pady=10, )
        self.third_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_3, font=self.the_font_small, ).grid(column=0, row=2, padx=10, pady=10, )

        self.individual_entry_4 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_4, ).grid(column=1, row=3, padx=10, pady=10, )
        self.forth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_4, font=self.the_font_small, ).grid(column=0, row=3, padx=10, pady=10, )

        self.individual_entry_5 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_5, ).grid(column=1, row=4, padx=10, pady=10, )
        self.fifth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_5, font=self.the_font_small, ).grid(column=0, row=4, padx=10, pady=10, )

        self.individual_entry_6 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_6, ).grid(column=1, row=5, padx=10, pady=10, )
        self.sixth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_6, font=self.the_font_small, ).grid(column=0, row=5, padx=10, pady=10, )

        self.individual_entry_7 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_7, ).grid(column=1, row=6, padx=10, pady=10, )
        self.seventh_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_7, font=self.the_font_small, ).grid(column=0, row=6, padx=10, pady=10, )

        self.individual_entry_8 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_8).grid(column=1, row=7, padx=10, pady=10, )
        self.eighth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_8, font=self.the_font_small, ).grid(column=0, row=7, padx=10, pady=10, )

        self.individual_entry_9 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_9).grid(column=1, row=8, padx=10, pady=10, )
        self.ninth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_9, font=self.the_font_small, ).grid(column=0, row=8, padx=10, pady=10, )

        self.individual_entry_10 = customtkinter.CTkEntry(self.edit_individuals_event_1_1_menu, textvariable=text_var_10, ).grid(column=1, row=9, padx=10, pady=10, )
        self.tenth_place_label = customtkinter.CTkLabel(self.edit_individuals_event_1_1_menu, text=place_variable_10, font=self.the_font_small, ).grid(column=0, row=9, padx=10, pady=10, )

        return self.edit_individuals_event_1_1_menu

    def edit_individuals_frame_func(self):

        self.edit_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_1, self.individual_2_event_1, self.individual_3_event_1, self.individual_4_event_1, self.individual_5_event_1, self.individual_6_event_1, self.individual_7_event_1, self.individual_8_event_1, self.individual_9_event_1, self.individual_10_event_1, ).place(x=100, y=50)
        self.edit_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_1, self.individual_12_event_1, self.individual_13_event_1, self.individual_14_event_1, self.individual_15_event_1, self.individual_16_event_1, self.individual_17_event_1, self.individual_18_event_1, self.individual_19_event_1, self.individual_20_event_1, ).place(x=400, y=50)
        self.save_and_back_button = customtkinter.CTkButton(self.edit_individuals_event_1_menu, command=self.data_validashon_for_event_1_all_individuals, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=500, y=600)


    def edit_individuals_frame_event_2(self):

        self.edit_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_2, self.individual_2_event_2, self.individual_3_event_2, self.individual_4_event_2, self.individual_5_event_2, self.individual_6_event_2, self.individual_7_event_2, self.individual_8_event_2, self.individual_9_event_2, self.individual_10_event_2, ).place(x=100, y=50)
        self.edit_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_2, self.individual_12_event_2, self.individual_13_event_2, self.individual_14_event_2, self.individual_15_event_2, self.individual_16_event_2, self.individual_17_event_2, self.individual_18_event_2, self.individual_19_event_2, self.individual_20_event_2, ).place(x=400, y=50)
        self.save_and_back_button = customtkinter.CTkButton(self.edit_individuals_event_1_menu, command=self.data_validashon_for_event_2_all_individuals, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=500, y=600)

    def edit_individuals_frame_event_3(self):

        self.edit_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_3, self.individual_2_event_3, self.individual_3_event_3, self.individual_4_event_3, self.individual_5_event_3, self.individual_6_event_3, self.individual_7_event_3, self.individual_8_event_3, self.individual_9_event_3, self.individual_10_event_3, ).place(x=100, y=50)
        self.edit_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_3, self.individual_12_event_3, self.individual_13_event_3, self.individual_14_event_3, self.individual_15_event_3, self.individual_16_event_3, self.individual_17_event_3, self.individual_18_event_3, self.individual_19_event_3, self.individual_20_event_3, ).place(x=400, y=50)
        self.save_and_back_button = customtkinter.CTkButton(self.edit_individuals_event_1_menu, command=self.data_validashon_for_event_3_all_individuals, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=500, y=600)

    def edit_individuals_frame_event_4(self):

        self.edit_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_2, self.individual_2_event_4, self.individual_3_event_4, self.individual_4_event_4, self.individual_5_event_4, self.individual_6_event_4, self.individual_7_event_4, self.individual_8_event_4, self.individual_9_event_4, self.individual_10_event_4 ).place(x=100, y=50)
        self.edit_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_4, self.individual_12_event_4, self.individual_13_event_4, self.individual_14_event_4, self.individual_15_event_4, self.individual_16_event_4, self.individual_17_event_4, self.individual_18_event_4, self.individual_19_event_4, self.individual_20_event_4, ).place(x=400, y=50)
        self.save_and_back_button = customtkinter.CTkButton(self.edit_individuals_event_1_menu, command=self.data_validashon_for_event_4_all_individuals, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=500, y=600)

    def edit_individuals_frame_event_5(self):

        self.edit_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_5, self.individual_2_event_5, self.individual_3_event_5, self.individual_4_event_5, self.individual_5_event_5, self.individual_6_event_5, self.individual_7_event_5, self.individual_8_event_5, self.individual_9_event_5, self.individual_10_event_5, ).place(x=100, y=50)
        self.edit_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_5, self.individual_12_event_5, self.individual_13_event_5, self.individual_14_event_5, self.individual_15_event_5, self.individual_16_event_5, self.individual_17_event_5, self.individual_18_event_5, self.individual_19_event_5, self.individual_20_event_5, ).place(x=400, y=50)
        self.save_and_back_button = customtkinter.CTkButton(self.edit_individuals_event_1_menu, command=self.data_validashon_for_event_5_all_individuals, font=self.the_font, hover_color="#25b2a1", fg_color="#002542", text="Save changes and go back").place(x=500, y=600)

##      ##--------------------------------------------------------------------------------------------------------------

## display scoreboard teams menu ##

    def display_scoreboard_teams_frame(self, team_name_var, variable_1, variable_2, variable_3, variable_4, variable_5, place_var, points_var, ):

        self.display_teams_frame = customtkinter.CTkFrame(self.display_scoreboard_for_teams, )

        self.display_teams_frame.columnconfigure(0, weight=1)
        self.display_teams_frame.columnconfigure(1, weight=1)
        self.display_teams_frame.rowconfigure(0, weight=1)
        self.display_teams_frame.rowconfigure(1, weight=1)
        self.display_teams_frame.rowconfigure(2, weight=1)
        self.display_teams_frame.rowconfigure(3, weight=1)
        self.display_teams_frame.rowconfigure(4, weight=1)
        self.display_teams_frame.rowconfigure(5, weight=1)
        self.display_teams_frame.rowconfigure(6, weight=1)

        self.place_label_for_teams = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_font, text=place_var, ).grid(column=0, row=0, padx=10, pady=10,)

        self.display_team_name_label = customtkinter.CTkLabel(self.display_teams_frame, text=team_name_var, font=self.the_font_small, width=150).grid(column=1, row=0, padx=10, pady=10, )

        self.score_lable = customtkinter.CTkLabel(self.display_teams_frame, text=points_var, font=self.the_smaller_font).grid(column=1, row=1, padx=10, pady=10, )

        self.individuals_lable = customtkinter.CTkLabel(self.display_teams_frame, text="individuals:", font=self.the_smaller_font).grid(column=2, row=1, padx=10, pady=10,)

        self.individual_text_box_1 = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_smaller_font, text=variable_1, ).grid(column=2, row=2, pady=10, padx=10)
        self.individual_text_box_2 = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_smaller_font, text=variable_2, ).grid(column=2, row=3, pady=10, padx=10)
        self.individual_text_box_3 = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_smaller_font, text=variable_3, ).grid(column=2, row=4, pady=10, padx=10)
        self.individual_text_box_4 = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_smaller_font, text=variable_4, ).grid(column=2, row=5, pady=10, padx=10)
        self.individual_text_box_5 = customtkinter.CTkLabel(self.display_teams_frame, font=self.the_smaller_font, text=variable_5, ).grid(column=2, row=6, pady=10, padx=10)

        return self.display_teams_frame

    def event_1_display_score_board_for_teams(self):

        self.display_scoreboard_teams_frame(self.team_1_event_1.get(), self.individual_1_team_1_event_1.get(), self.individual_2_team_1_event_1.get(), self.individual_3_team_1_event_1.get(), self.individual_4_team_1_event_1.get(), self.individual_5_team_1_event_1.get(), "1st place", "3 points").place(x=50, y=25)
        self.display_scoreboard_teams_frame(self.team_2_event_1.get(), self.individual_1_team_2_event_1.get(), self.individual_2_team_2_event_1.get(), self.individual_3_team_2_event_1.get(), self.individual_4_team_2_event_1.get(), self.individual_5_team_2_event_1.get(), "2nd place", "2 points").place(x=50, y=415)
        self.display_scoreboard_teams_frame(self.team_3_event_1.get(), self.individual_1_team_3_event_1.get(), self.individual_2_team_3_event_1.get(), self.individual_3_team_3_event_1.get(), self.individual_4_team_3_event_1.get(), self.individual_5_team_3_event_1.get(), "3rd place", "1 point").place(x=500, y=25)
        self.display_scoreboard_teams_frame(self.team_4_event_1.get(), self.individual_1_team_4_event_1.get(), self.individual_2_team_4_event_1.get(), self.individual_3_team_4_event_1.get(), self.individual_4_team_4_event_1.get(), self.individual_5_team_4_event_1.get(), "4th place", "0 points").place(x=500, y=415)

    def event_2_display_score_board_for_teams(self):

        self.display_scoreboard_teams_frame(self.team_1_event_2.get(), self.individual_1_team_1_event_2.get(), self.individual_2_team_1_event_2.get(), self.individual_3_team_1_event_2.get(), self.individual_4_team_1_event_2.get(), self.individual_5_team_1_event_2.get(), "1st place", "3 points").place(x=50, y=25)
        self.display_scoreboard_teams_frame(self.team_2_event_2.get(), self.individual_1_team_2_event_2.get(), self.individual_2_team_2_event_2.get(), self.individual_3_team_2_event_2.get(), self.individual_4_team_2_event_2.get(), self.individual_5_team_2_event_2.get(), "2nd place", "2 points").place(x=50, y=415)
        self.display_scoreboard_teams_frame(self.team_3_event_2.get(), self.individual_1_team_3_event_2.get(), self.individual_2_team_3_event_2.get(), self.individual_3_team_3_event_2.get(), self.individual_4_team_3_event_2.get(), self.individual_5_team_3_event_2.get(), "3rd place", "1 point").place(x=500, y=25)
        self.display_scoreboard_teams_frame(self.team_4_event_2.get(), self.individual_1_team_4_event_2.get(), self.individual_2_team_4_event_2.get(), self.individual_3_team_4_event_2.get(), self.individual_4_team_4_event_2.get(), self.individual_5_team_4_event_2.get(), "4th place", "0 points").place(x=500, y=415)

    def event_3_display_score_board_for_teams(self):

        self.display_scoreboard_teams_frame(self.team_1_event_3.get(), self.individual_1_team_1_event_3.get(), self.individual_2_team_1_event_3.get(), self.individual_3_team_1_event_3.get(), self.individual_4_team_1_event_3.get(), self.individual_5_team_1_event_3.get(), "1st place", "3 points").place(x=50, y=25)
        self.display_scoreboard_teams_frame(self.team_2_event_3.get(), self.individual_1_team_2_event_3.get(), self.individual_2_team_2_event_3.get(), self.individual_3_team_2_event_3.get(), self.individual_4_team_2_event_3.get(), self.individual_5_team_2_event_3.get(), "2nd place", "2 points").place(x=50, y=415)
        self.display_scoreboard_teams_frame(self.team_3_event_3.get(), self.individual_1_team_3_event_3.get(), self.individual_2_team_3_event_3.get(), self.individual_3_team_3_event_3.get(), self.individual_4_team_3_event_3.get(), self.individual_5_team_3_event_3.get(), "3rd place", "1 point").place(x=500, y=25)
        self.display_scoreboard_teams_frame(self.team_4_event_3.get(), self.individual_1_team_4_event_3.get(), self.individual_2_team_4_event_3.get(), self.individual_3_team_4_event_3.get(), self.individual_4_team_4_event_3.get(), self.individual_5_team_4_event_3.get(), "4th place", "0 points").place(x=500, y=415)

    def event_4_display_score_board_for_teams(self):

        self.display_scoreboard_teams_frame(self.team_1_event_4.get(), self.individual_1_team_1_event_4.get(), self.individual_2_team_1_event_4.get(), self.individual_3_team_1_event_4.get(), self.individual_4_team_1_event_4.get(), self.individual_5_team_1_event_4.get(), "1st place", "3 points").place(x=50, y=25)
        self.display_scoreboard_teams_frame(self.team_2_event_4.get(), self.individual_1_team_2_event_4.get(), self.individual_2_team_2_event_4.get(), self.individual_3_team_2_event_4.get(), self.individual_4_team_2_event_4.get(), self.individual_5_team_2_event_4.get(), "2nd place", "2 points").place(x=50, y=415)
        self.display_scoreboard_teams_frame(self.team_3_event_4.get(), self.individual_1_team_3_event_4.get(), self.individual_2_team_3_event_4.get(), self.individual_3_team_3_event_4.get(), self.individual_4_team_3_event_4.get(), self.individual_5_team_3_event_4.get(), "3rd place", "1 point").place(x=500, y=25)
        self.display_scoreboard_teams_frame(self.team_4_event_4.get(), self.individual_1_team_4_event_4.get(), self.individual_2_team_4_event_4.get(), self.individual_3_team_4_event_4.get(), self.individual_4_team_4_event_4.get(), self.individual_5_team_4_event_4.get(), "4th place", "0 points").place(x=500, y=415)

    def event_5_display_score_board_for_teams(self):

        self.display_scoreboard_teams_frame(self.team_1_event_5.get(), self.individual_1_team_1_event_5.get(), self.individual_2_team_1_event_5.get(), self.individual_3_team_1_event_5.get(), self.individual_4_team_1_event_5.get(), self.individual_5_team_1_event_5.get(), "1st place", "3 points").place(x=50, y=25)
        self.display_scoreboard_teams_frame(self.team_2_event_5.get(), self.individual_1_team_2_event_5.get(), self.individual_2_team_2_event_5.get(), self.individual_3_team_2_event_5.get(), self.individual_4_team_2_event_5.get(), self.individual_5_team_2_event_5.get(), "2nd place", "2 points").place(x=50, y=415)
        self.display_scoreboard_teams_frame(self.team_3_event_5.get(), self.individual_1_team_3_event_5.get(), self.individual_2_team_3_event_5.get(), self.individual_3_team_3_event_5.get(), self.individual_4_team_3_event_5.get(), self.individual_5_team_3_event_5.get(), "3rd place", "1 point").place(x=500, y=25)
        self.display_scoreboard_teams_frame(self.team_4_event_5.get(), self.individual_1_team_4_event_5.get(), self.individual_2_team_4_event_5.get(), self.individual_3_team_4_event_5.get(), self.individual_4_team_4_event_5.get(), self.individual_5_team_4_event_5.get(), "4th place", "0 points").place(x=500, y=415)

    def display_score_board_for_individuals_frame(self, place_variable_1, place_variable_2, place_variable_3, place_variable_4, place_variable_5, place_variable_6, place_variable_7, place_variable_8, place_variable_9, place_variable_10, individual_1, individual_2, individual_3, individual_4, individual_5, individual_6, individual_7, individual_8, individual_9, individual_10, score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, ):

        self.display_score_board_individuals_menu_1 = customtkinter.CTkFrame(self.display_score_board_individuals_menu_1_1, )

        self.place_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text="Rankings:", font=self.the_font_small, ).grid(column=0, row=0, padx=10, pady=10, )
        self.individual_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text="individuals:", font=self.the_font_small, ).grid(column=1, row=0, padx=10, pady=10, )
        self.place_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text="points:", font=self.the_font_small, ).grid(column=2, row=0, padx=10, pady=10, )

        self.first_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_1, font=self.the_font_small, ).grid(column=0, row=1, padx=10, pady=10, )
        self.second_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_2, font=self.the_font_small, ).grid(column=0, row=2, padx=10, pady=10, )
        self.third_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_3, font=self.the_font_small, ).grid(column=0, row=3, padx=10, pady=10, )
        self.forth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_4, font=self.the_font_small, ).grid(column=0, row=4, padx=10, pady=10, )
        self.fifth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_5, font=self.the_font_small, ).grid(column=0, row=5, padx=10, pady=10, )
        self.sixth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_6, font=self.the_font_small, ).grid(column=0, row=6, padx=10, pady=10, )
        self.seventh_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_7, font=self.the_font_small, ).grid(column=0, row=7, padx=10, pady=10, )
        self.eighth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_8, font=self.the_font_small, ).grid(column=0, row=8, padx=10, pady=10, )
        self.ninth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_9, font=self.the_font_small, ).grid(column=0, row=9, padx=10, pady=10, )
        self.tenth_place_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=place_variable_10, font=self.the_font_small, ).grid(column=0, row=10, padx=10, pady=10, )

        self.individual_1_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_1, font=self.the_font_small, ).grid(column=1, row=1, padx=10, pady=10, )
        self.individual_2_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_2, font=self.the_font_small, ).grid(column=1, row=2, padx=10, pady=10, )
        self.individual_3_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_3, font=self.the_font_small, ).grid(column=1, row=3, padx=10, pady=10, )
        self.individual_4_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_4, font=self.the_font_small, ).grid(column=1, row=4, padx=10, pady=10, )
        self.individual_5_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_5, font=self.the_font_small, ).grid(column=1, row=5, padx=10, pady=10, )
        self.individual_6_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_6, font=self.the_font_small, ).grid(column=1, row=6, padx=10, pady=10, )
        self.individual_7_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_7, font=self.the_font_small, ).grid(column=1, row=7, padx=10, pady=10, )
        self.individual_8_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_8, font=self.the_font_small, ).grid(column=1, row=8, padx=10, pady=10, )
        self.individual_9_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_9, font=self.the_font_small, ).grid(column=1, row=9, padx=10, pady=10, )
        self.individual_10_label = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=individual_10, font=self.the_font_small, ).grid(column=1, row=10, padx=10, pady=10, )

        self.score_1_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score1, font=self.the_font_small, ).grid(column=2, row=1, padx=10, pady=10, )
        self.score_2_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score2, font=self.the_font_small, ).grid(column=2, row=2, padx=10, pady=10, )
        self.score_3_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score3, font=self.the_font_small, ).grid(column=2, row=3, padx=10, pady=10, )
        self.score_4_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score4, font=self.the_font_small, ).grid(column=2, row=4, padx=10, pady=10, )
        self.score_5_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score5, font=self.the_font_small, ).grid(column=2, row=5, padx=10, pady=10, )
        self.score_6_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score6, font=self.the_font_small, ).grid(column=2, row=6, padx=10, pady=10, )
        self.score_7_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score7, font=self.the_font_small, ).grid(column=2, row=7, padx=10, pady=10, )
        self.score_8_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score8, font=self.the_font_small, ).grid(column=2, row=8, padx=10, pady=10, )
        self.score_9_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score9, font=self.the_font_small, ).grid(column=2, row=9, padx=10, pady=10, )
        self.score_10_lable = customtkinter.CTkLabel(self.display_score_board_individuals_menu_1, text=score10, font=self.the_font_small, ).grid(column=2, row=10, padx=10, pady=10, )

        return self.display_score_board_individuals_menu_1

    def event_1_score_board_for_individuals(self):

        self.display_score_board_for_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_1.get(), self.individual_2_event_1.get(), self.individual_3_event_1.get(), self.individual_4_event_1.get(), self.individual_5_event_1.get(), self.individual_6_event_1.get(), self.individual_7_event_1.get(), self.individual_8_event_1.get(), self.individual_9_event_1.get(), self.individual_10_event_1.get(), "5 points", "4 points", "3 points", "2 points", "1 point", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=25, y=40)
        self.display_score_board_for_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_1.get(), self.individual_12_event_1.get(), self.individual_13_event_1.get(), self.individual_14_event_1.get(), self.individual_15_event_1.get(), self.individual_16_event_1.get(), self.individual_17_event_1.get(), self.individual_18_event_1.get(), self.individual_19_event_1.get(), self.individual_20_event_1.get(), "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=375, y=40)

    def event_2_score_board_for_individuals(self):

        self.display_score_board_for_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_2.get(), self.individual_2_event_2.get(), self.individual_3_event_2.get(), self.individual_4_event_2.get(), self.individual_5_event_2.get(), self.individual_6_event_2.get(), self.individual_7_event_2.get(), self.individual_8_event_2.get(), self.individual_9_event_2.get(), self.individual_10_event_2.get(), "5 points", "4 points", "3 points", "2 points", "1 point", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=25, y=40)
        self.display_score_board_for_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_2.get(), self.individual_12_event_2.get(), self.individual_13_event_2.get(), self.individual_14_event_2.get(), self.individual_15_event_2.get(), self.individual_16_event_2.get(), self.individual_17_event_2.get(), self.individual_18_event_2.get(), self.individual_19_event_2.get(), self.individual_20_event_2.get(), "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=375, y=40)

    def event_3_score_board_for_individuals(self):

        self.display_score_board_for_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_3.get(), self.individual_2_event_3.get(), self.individual_3_event_3.get(), self.individual_4_event_3.get(), self.individual_5_event_3.get(), self.individual_6_event_3.get(), self.individual_7_event_3.get(), self.individual_8_event_3.get(), self.individual_9_event_3.get(), self.individual_10_event_3.get(), "5 points", "4 points", "3 points", "2 points", "1 point", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=25, y=40)
        self.display_score_board_for_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_3.get(), self.individual_12_event_3.get(), self.individual_13_event_3.get(), self.individual_14_event_3.get(), self.individual_15_event_3.get(), self.individual_16_event_3.get(), self.individual_17_event_3.get(), self.individual_18_event_3.get(), self.individual_19_event_3.get(), self.individual_20_event_3.get(), "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=375, y=40)

    def event_4_score_board_for_individuals(self):

        self.display_score_board_for_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_4.get(), self.individual_2_event_4.get(), self.individual_3_event_4.get(), self.individual_4_event_4.get(), self.individual_5_event_4.get(), self.individual_6_event_4.get(), self.individual_7_event_4.get(), self.individual_8_event_4.get(), self.individual_9_event_4.get(), self.individual_10_event_4.get(), "5 points", "4 points", "3 points", "2 points", "1 point", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=25, y=40)
        self.display_score_board_for_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_4.get(), self.individual_12_event_4.get(), self.individual_13_event_4.get(), self.individual_14_event_4.get(), self.individual_15_event_4.get(), self.individual_16_event_4.get(), self.individual_17_event_4.get(), self.individual_18_event_4.get(), self.individual_19_event_4.get(), self.individual_20_event_4.get(), "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=375, y=40)

    def event_5_score_board_for_individuals(self):

        self.display_score_board_for_individuals_frame("1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place", self.individual_1_event_5.get(), self.individual_2_event_5.get(), self.individual_3_event_5.get(), self.individual_4_event_5.get(), self.individual_5_event_5.get(), self.individual_6_event_5.get(), self.individual_7_event_5.get(), self.individual_8_event_5.get(), self.individual_9_event_5.get(), self.individual_10_event_5.get(), "5 points", "4 points", "3 points", "2 points", "1 point", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=25, y=40)
        self.display_score_board_for_individuals_frame("11th place", "12th place", "13th place", "14th place", "15th place", "16th place", "17th place", "18th place", "19th place", "20th place", self.individual_11_event_5.get(), self.individual_12_event_5.get(), self.individual_13_event_5.get(), self.individual_14_event_5.get(), self.individual_15_event_5.get(), self.individual_16_event_5.get(), self.individual_17_event_5.get(), self.individual_18_event_5.get(), self.individual_19_event_5.get(), self.individual_20_event_5.get(), "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points", "0 points").place(x=375, y=40)

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
        self.edit_individuals_event_1_menu.pack_forget()
        self.display_scoreboard_for_teams.pack_forget()

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
        self.edit_individuals_event_1_menu.pack_forget()
        self.display_scoreboard_for_teams.pack_forget()

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
        self.edit_individuals_event_1_menu.pack_forget()
        self.display_scoreboard_for_teams.pack_forget()

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
        self.edit_individuals_event_1_menu.pack_forget()

    def switch_to_edit_teams_menu(self):

        self.event_1_to_5_buttons_frame(self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable, self.switch_to_event_1_frame_teams_menu, self.switch_to_event_2_frame_teams_menu, self.switch_to_event_3_frame_teams_menu, self.switch_to_event_4_frame_teams_menu, self.switch_to_event_5_frame_teams_menu).pack(pady=250)

        self.edit_teams_and_individuals_content_frame.pack_forget()

    def switch_to_edit_individuals_menu(self):

        self.event_1_to_5_buttons_frame(self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable, self.switch_to_event_1_frame_individuals_menu, self.switch_to_event_2_frame_individuals_menu, self.switch_to_event_3_frame_individuals_menu, self.switch_to_event_4_frame_individuals_menu, self.switch_to_event_5_frame_individuals_menu).pack(pady=250)

        self.edit_teams_and_individuals_content_frame.pack_forget()

    def switch_to_teams_display_score_board_menu(self):

        self.event_1_to_5_buttons_frame(self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable, self.switch_to_event_1_display_scoreboard_for_teams, self.switch_to_event_2_display_scoreboard_for_teams, self.switch_to_event_2_display_scoreboard_for_teams, self.switch_to_event_2_display_scoreboard_for_teams, self.switch_to_event_2_display_scoreboard_for_teams).pack(pady=250)

        self.display_scoreboard_content_frame.pack_forget()

    def switch_to_individuals_display_score_board_menu(self):

        self.event_1_to_5_buttons_frame(self.event_1_variable, self.event_2_variable, self.event_3_variable, self.event_4_variable, self.event_5_variable, self.switch_to_event_1_display_scoreBoard_for_individuals, self.switch_to_event_2_display_scoreBoard_for_individuals, self.switch_to_event_3_display_scoreBoard_for_individuals, self.switch_to_event_4_display_scoreBoard_for_individuals, self.switch_to_event_5_display_scoreBoard_for_individuals).pack(pady=250)

        self.display_scoreboard_content_frame.pack_forget()

    def switch_to_event_1_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_teams_content_frame_func()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_2_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_team_content_frame_for_event_2()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_3_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_team_content_frame_for_event_3()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_4_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_team_content_frame_for_event_4()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_5_frame_teams_menu(self):

        self.editing_teams_frame.pack(pady=40)
        self.edit_team_content_frame_for_event_5()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_1_frame_individuals_menu(self):

        self.edit_individuals_event_1_menu.pack(pady=30)
        self.edit_individuals_frame_func()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_2_frame_individuals_menu(self):

        self.edit_individuals_event_1_menu.pack(pady=30)
        self.edit_individuals_frame_event_2()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_3_frame_individuals_menu(self):

        self.edit_individuals_event_1_menu.pack(pady=30)
        self.edit_individuals_frame_event_3()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_4_frame_individuals_menu(self):

        self.edit_individuals_event_1_menu.pack(pady=30)
        self.edit_individuals_frame_event_4()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_5_frame_individuals_menu(self):

        self.edit_individuals_event_1_menu.pack(pady=30)
        self.edit_individuals_frame_event_5()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_1_display_scoreboard_for_teams(self):

        self.display_scoreboard_for_teams.pack(pady=30)
        self.event_1_display_score_board_for_teams()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_2_display_scoreboard_for_teams(self):

        self.display_scoreboard_for_teams.pack(pady=30)
        self.event_2_display_score_board_for_teams()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_3_display_scoreboard_for_teams(self):

        self.display_scoreboard_for_teams.pack(pady=30)
        self.event_3_display_score_board_for_teams()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_4_display_scoreboard_for_teams(self):

        self.display_scoreboard_for_teams.pack(pady=30)
        self.event_4_display_score_board_for_teams()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_5_display_scoreboard_for_teams(self):

        self.display_scoreboard_for_teams.pack(pady=30)
        self.event_5_display_score_board_for_teams()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_1_display_scoreBoard_for_individuals(self):

        self.display_score_board_individuals_menu_1_1.pack(pady=30)
        self.event_1_score_board_for_individuals()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_2_display_scoreBoard_for_individuals(self):

        self.display_score_board_individuals_menu_1_1.pack(pady=30)
        self.event_2_score_board_for_individuals()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_3_display_scoreBoard_for_individuals(self):

        self.display_score_board_individuals_menu_1_1.pack(pady=30)
        self.event_3_score_board_for_individuals()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_4_display_scoreBoard_for_individuals(self):

        self.display_score_board_individuals_menu_1_1.pack(pady=30)
        self.event_4_score_board_for_individuals()

        self.events_1_to_5_main_frame.pack_forget()

    def switch_to_event_5_display_scoreBoard_for_individuals(self):

        self.display_score_board_individuals_menu_1_1.pack(pady=30)
        self.event_5_score_board_for_individuals()

        self.events_1_to_5_main_frame.pack_forget()

    def close_the_program(self):

        if self.msg.askyesno(title="Exit?", message="Are you sure you want to leave? Any unsaved changes wont be saved"):

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


    ## data validashion and data storage for event 1 ##
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

    ## data validashion and data storage for event 2 ##
    def data_validashion_for_event_2_team_1(self):

        self.check_team_name_input(self.team_1_event_2.get(), 44, )
        self.check_student_num_input(self.individual_1_team_1_event_2.get(), 24)
        self.check_student_num_input(self.individual_2_team_1_event_2.get(), 25)
        self.check_student_num_input(self.individual_3_team_1_event_2.get(), 26)
        self.check_student_num_input(self.individual_4_team_1_event_2.get(), 27)
        self.check_student_num_input(self.individual_5_team_1_event_2.get(), 28)

    def data_validashion_for_event_2_team_2(self):

        self.check_team_name_input(self.team_2_event_2.get(), 45, )
        self.check_student_num_input(self.individual_1_team_2_event_2.get(), 29)
        self.check_student_num_input(self.individual_2_team_2_event_2.get(), 30)
        self.check_student_num_input(self.individual_3_team_2_event_2.get(), 31)
        self.check_student_num_input(self.individual_4_team_2_event_2.get(), 32)
        self.check_student_num_input(self.individual_5_team_2_event_2.get(), 33)
    def data_validashion_for_event_2_team_3(self):

        self.check_team_name_input(self.team_3_event_2.get(), 46, )
        self.check_student_num_input(self.individual_1_team_3_event_2.get(), 34)
        self.check_student_num_input(self.individual_2_team_3_event_2.get(), 35)
        self.check_student_num_input(self.individual_3_team_3_event_2.get(), 36)
        self.check_student_num_input(self.individual_4_team_3_event_2.get(), 37)
        self.check_student_num_input(self.individual_5_team_3_event_2.get(), 38)

    def data_validashion_for_event_2_team_4(self):

        self.check_team_name_input(self.team_4_event_2.get(), 47, )
        self.check_student_num_input(self.individual_1_team_4_event_2.get(), 39)
        self.check_student_num_input(self.individual_2_team_4_event_2.get(), 40)
        self.check_student_num_input(self.individual_3_team_4_event_2.get(), 41)
        self.check_student_num_input(self.individual_4_team_4_event_2.get(), 42)
        self.check_student_num_input(self.individual_5_team_4_event_2.get(), 43)
    def data_validashion_for_event_2_teams_all_func(self):

        self.data_validashion_for_event_2_team_1()
        self.data_validashion_for_event_2_team_2()
        self.data_validashion_for_event_2_team_3()
        self.data_validashion_for_event_2_team_4()

    ## event 3 data validashion and data storage ##

    def data_validashion_for_event_3_team_1(self):

        self.check_team_name_input(self.team_1_event_3.get(), 68, )
        self.check_student_num_input(self.individual_1_team_1_event_3.get(), 48)
        self.check_student_num_input(self.individual_2_team_1_event_3.get(), 49)
        self.check_student_num_input(self.individual_3_team_1_event_3.get(), 50)
        self.check_student_num_input(self.individual_4_team_1_event_3.get(), 51)
        self.check_student_num_input(self.individual_5_team_1_event_3.get(), 52)

    def data_validashion_for_event_3_team_2(self):

        self.check_team_name_input(self.team_2_event_3.get(), 69, )
        self.check_student_num_input(self.individual_1_team_2_event_3.get(), 53)
        self.check_student_num_input(self.individual_2_team_2_event_3.get(), 54)
        self.check_student_num_input(self.individual_3_team_2_event_3.get(), 55)
        self.check_student_num_input(self.individual_4_team_2_event_3.get(), 56)
        self.check_student_num_input(self.individual_5_team_2_event_3.get(), 57)
    def data_validashion_for_event_3_team_3(self):

        self.check_team_name_input(self.team_3_event_3.get(), 70, )
        self.check_student_num_input(self.individual_1_team_3_event_3.get(), 58)
        self.check_student_num_input(self.individual_2_team_3_event_3.get(), 59)
        self.check_student_num_input(self.individual_3_team_3_event_3.get(), 60)
        self.check_student_num_input(self.individual_4_team_3_event_3.get(), 61)
        self.check_student_num_input(self.individual_5_team_3_event_3.get(), 62)

    def data_validashion_for_event_3_team_4(self):

        self.check_team_name_input(self.team_4_event_3.get(), 71, )
        self.check_student_num_input(self.individual_1_team_4_event_3.get(), 63)
        self.check_student_num_input(self.individual_2_team_4_event_3.get(), 64)
        self.check_student_num_input(self.individual_3_team_4_event_3.get(), 65)
        self.check_student_num_input(self.individual_4_team_4_event_3.get(), 66)
        self.check_student_num_input(self.individual_5_team_4_event_3.get(), 67)
    def data_validashion_for_event_3_teams_all_func(self):

        self.data_validashion_for_event_3_team_1()
        self.data_validashion_for_event_3_team_2()
        self.data_validashion_for_event_3_team_3()
        self.data_validashion_for_event_3_team_4()

    ## event 4 data validashion and data storage ##
    def data_validashion_for_event_4_team_1(self):

        self.check_team_name_input(self.team_1_event_4.get(), 92, )
        self.check_student_num_input(self.individual_1_team_1_event_4.get(), 72)
        self.check_student_num_input(self.individual_2_team_1_event_4.get(), 73)
        self.check_student_num_input(self.individual_3_team_1_event_4.get(), 74)
        self.check_student_num_input(self.individual_4_team_1_event_4.get(), 75)
        self.check_student_num_input(self.individual_5_team_1_event_4.get(), 76)

    def data_validashion_for_event_4_team_2(self):

        self.check_team_name_input(self.team_2_event_4.get(), 93, )
        self.check_student_num_input(self.individual_1_team_2_event_4.get(), 77)
        self.check_student_num_input(self.individual_2_team_2_event_4.get(), 78)
        self.check_student_num_input(self.individual_3_team_2_event_4.get(), 79)
        self.check_student_num_input(self.individual_4_team_2_event_4.get(), 80)
        self.check_student_num_input(self.individual_5_team_2_event_4.get(), 81)
    def data_validashion_for_event_4_team_3(self):

        self.check_team_name_input(self.team_3_event_4.get(), 94, )
        self.check_student_num_input(self.individual_1_team_3_event_4.get(), 82)
        self.check_student_num_input(self.individual_2_team_3_event_4.get(), 83)
        self.check_student_num_input(self.individual_3_team_3_event_4.get(), 84)
        self.check_student_num_input(self.individual_4_team_3_event_4.get(), 85)
        self.check_student_num_input(self.individual_5_team_3_event_4.get(), 86)

    def data_validashion_for_event_4_team_4(self):

        self.check_team_name_input(self.team_4_event_4.get(), 95, )
        self.check_student_num_input(self.individual_1_team_4_event_4.get(), 87)
        self.check_student_num_input(self.individual_2_team_4_event_4.get(), 88)
        self.check_student_num_input(self.individual_3_team_4_event_4.get(), 89)
        self.check_student_num_input(self.individual_4_team_4_event_4.get(), 90)
        self.check_student_num_input(self.individual_5_team_4_event_4.get(), 91)
    def data_validashion_for_event_4_teams_all_func(self):

        self.data_validashion_for_event_4_team_1()
        self.data_validashion_for_event_4_team_2()
        self.data_validashion_for_event_4_team_3()
        self.data_validashion_for_event_4_team_4()

    ## data validashion and data storage for event 5 ##
    def data_validashion_for_event_5_team_1(self):

        self.check_team_name_input(self.team_1_event_5.get(), 116, )
        self.check_student_num_input(self.individual_1_team_1_event_5.get(), 96)
        self.check_student_num_input(self.individual_2_team_1_event_5.get(), 97)
        self.check_student_num_input(self.individual_3_team_1_event_5.get(), 98)
        self.check_student_num_input(self.individual_4_team_1_event_5.get(), 99)
        self.check_student_num_input(self.individual_5_team_1_event_5.get(), 100)

    def data_validashion_for_event_5_team_2(self):

        self.check_team_name_input(self.team_2_event_5.get(), 117, )
        self.check_student_num_input(self.individual_1_team_2_event_5.get(), 101)
        self.check_student_num_input(self.individual_2_team_2_event_5.get(), 102)
        self.check_student_num_input(self.individual_3_team_2_event_5.get(), 103)
        self.check_student_num_input(self.individual_4_team_2_event_5.get(), 104)
        self.check_student_num_input(self.individual_5_team_2_event_5.get(), 105)
    def data_validashion_for_event_5_team_3(self):

        self.check_team_name_input(self.team_3_event_5.get(), 118, )
        self.check_student_num_input(self.individual_1_team_3_event_5.get(), 106)
        self.check_student_num_input(self.individual_2_team_3_event_5.get(), 107)
        self.check_student_num_input(self.individual_3_team_3_event_5.get(), 108)
        self.check_student_num_input(self.individual_4_team_3_event_5.get(), 109)
        self.check_student_num_input(self.individual_5_team_3_event_5.get(), 110)

    def data_validashion_for_event_5_team_4(self):

        self.check_team_name_input(self.team_4_event_5.get(), 119, )
        self.check_student_num_input(self.individual_1_team_4_event_5.get(), 111)
        self.check_student_num_input(self.individual_2_team_4_event_5.get(), 112)
        self.check_student_num_input(self.individual_3_team_4_event_5.get(), 113)
        self.check_student_num_input(self.individual_4_team_4_event_5.get(), 114)
        self.check_student_num_input(self.individual_5_team_4_event_5.get(), 115)
    def data_validashion_for_event_5_teams_all_func(self):

        self.data_validashion_for_event_5_team_1()
        self.data_validashion_for_event_5_team_2()
        self.data_validashion_for_event_5_team_3()
        self.data_validashion_for_event_5_team_4()

    ## data validashion and data validashion for individuals event 1 ##
    def data_validashon_for_event_1_all_individuals(self):

        self.check_student_num_input(self.individual_1_event_1.get(), 120)
        self.check_student_num_input(self.individual_2_event_1.get(), 121)
        self.check_student_num_input(self.individual_3_event_1.get(), 122)
        self.check_student_num_input(self.individual_4_event_1.get(), 123)
        self.check_student_num_input(self.individual_5_event_1.get(), 124)
        self.check_student_num_input(self.individual_6_event_1.get(), 125)
        self.check_student_num_input(self.individual_7_event_1.get(), 126)
        self.check_student_num_input(self.individual_8_event_1.get(), 127)
        self.check_student_num_input(self.individual_9_event_1.get(), 128)
        self.check_student_num_input(self.individual_10_event_1.get(), 129)
        self.check_student_num_input(self.individual_11_event_1.get(), 130)
        self.check_student_num_input(self.individual_12_event_1.get(), 131)
        self.check_student_num_input(self.individual_13_event_1.get(), 132)
        self.check_student_num_input(self.individual_14_event_1.get(), 133)
        self.check_student_num_input(self.individual_15_event_1.get(), 134)
        self.check_student_num_input(self.individual_16_event_1.get(), 135)
        self.check_student_num_input(self.individual_17_event_1.get(), 136)
        self.check_student_num_input(self.individual_18_event_1.get(), 137)
        self.check_student_num_input(self.individual_19_event_1.get(), 138)
        self.check_student_num_input(self.individual_20_event_1.get(), 139)

    ## data validashon and data storage for event 2 ##
    def data_validashon_for_event_2_all_individuals(self):

        self.check_student_num_input(self.individual_1_event_2.get(), 140)
        self.check_student_num_input(self.individual_2_event_2.get(), 141)
        self.check_student_num_input(self.individual_3_event_2.get(), 142)
        self.check_student_num_input(self.individual_4_event_2.get(), 143)
        self.check_student_num_input(self.individual_5_event_2.get(), 144)
        self.check_student_num_input(self.individual_6_event_2.get(), 145)
        self.check_student_num_input(self.individual_7_event_2.get(), 146)
        self.check_student_num_input(self.individual_8_event_2.get(), 147)
        self.check_student_num_input(self.individual_9_event_2.get(), 148)
        self.check_student_num_input(self.individual_10_event_2.get(), 149)
        self.check_student_num_input(self.individual_11_event_2.get(), 150)
        self.check_student_num_input(self.individual_12_event_2.get(), 151)
        self.check_student_num_input(self.individual_13_event_2.get(), 152)
        self.check_student_num_input(self.individual_14_event_2.get(), 153)
        self.check_student_num_input(self.individual_15_event_2.get(), 154)
        self.check_student_num_input(self.individual_16_event_2.get(), 155)
        self.check_student_num_input(self.individual_17_event_2.get(), 156)
        self.check_student_num_input(self.individual_18_event_2.get(), 157)
        self.check_student_num_input(self.individual_19_event_2.get(), 158)
        self.check_student_num_input(self.individual_20_event_2.get(), 159)

    ## data validashion and storage for event 3 ##
    def data_validashon_for_event_3_all_individuals(self):

        self.check_student_num_input(self.individual_1_event_3.get(), 160)
        self.check_student_num_input(self.individual_2_event_3.get(), 161)
        self.check_student_num_input(self.individual_3_event_3.get(), 162)
        self.check_student_num_input(self.individual_4_event_3.get(), 163)
        self.check_student_num_input(self.individual_5_event_3.get(), 164)
        self.check_student_num_input(self.individual_6_event_3.get(), 165)
        self.check_student_num_input(self.individual_7_event_3.get(), 166)
        self.check_student_num_input(self.individual_8_event_3.get(), 167)
        self.check_student_num_input(self.individual_9_event_3.get(), 168)
        self.check_student_num_input(self.individual_10_event_1.get(), 169)
        self.check_student_num_input(self.individual_11_event_3.get(), 170)
        self.check_student_num_input(self.individual_12_event_3.get(), 171)
        self.check_student_num_input(self.individual_13_event_3.get(), 172)
        self.check_student_num_input(self.individual_14_event_3.get(), 173)
        self.check_student_num_input(self.individual_15_event_3.get(), 174)
        self.check_student_num_input(self.individual_16_event_3.get(), 175)
        self.check_student_num_input(self.individual_17_event_3.get(), 176)
        self.check_student_num_input(self.individual_18_event_3.get(), 177)
        self.check_student_num_input(self.individual_19_event_3.get(), 178)
        self.check_student_num_input(self.individual_20_event_3.get(), 179)

    ## data validashion and storage for event 4 ##
    def data_validashon_for_event_4_all_individuals(self):

        self.check_student_num_input(self.individual_1_event_4.get(), 180)
        self.check_student_num_input(self.individual_2_event_4.get(), 181)
        self.check_student_num_input(self.individual_3_event_4.get(), 182)
        self.check_student_num_input(self.individual_4_event_4.get(), 183)
        self.check_student_num_input(self.individual_5_event_4.get(), 184)
        self.check_student_num_input(self.individual_6_event_4.get(), 185)
        self.check_student_num_input(self.individual_7_event_4.get(), 186)
        self.check_student_num_input(self.individual_8_event_4.get(), 187)
        self.check_student_num_input(self.individual_9_event_4.get(), 188)
        self.check_student_num_input(self.individual_10_event_4.get(), 189)
        self.check_student_num_input(self.individual_11_event_4.get(), 190)
        self.check_student_num_input(self.individual_12_event_4.get(), 191)
        self.check_student_num_input(self.individual_13_event_4.get(), 192)
        self.check_student_num_input(self.individual_14_event_4.get(), 193)
        self.check_student_num_input(self.individual_15_event_4.get(), 194)
        self.check_student_num_input(self.individual_16_event_4.get(), 195)
        self.check_student_num_input(self.individual_17_event_4.get(), 196)
        self.check_student_num_input(self.individual_18_event_4.get(), 197)
        self.check_student_num_input(self.individual_19_event_4.get(), 198)
        self.check_student_num_input(self.individual_20_event_4.get(), 199)

    ## data validashion and storage for event 5 ##

    def data_validashon_for_event_5_all_individuals(self):

        self.check_student_num_input(self.individual_1_event_5.get(), 200)
        self.check_student_num_input(self.individual_2_event_5.get(), 201)
        self.check_student_num_input(self.individual_3_event_5.get(), 202)
        self.check_student_num_input(self.individual_4_event_5.get(), 203)
        self.check_student_num_input(self.individual_5_event_5.get(), 204)
        self.check_student_num_input(self.individual_6_event_5.get(), 205)
        self.check_student_num_input(self.individual_7_event_5.get(), 206)
        self.check_student_num_input(self.individual_8_event_5.get(), 207)
        self.check_student_num_input(self.individual_9_event_5.get(), 208)
        self.check_student_num_input(self.individual_10_event_5.get(), 209)
        self.check_student_num_input(self.individual_11_event_5.get(), 210)
        self.check_student_num_input(self.individual_12_event_5.get(), 211)
        self.check_student_num_input(self.individual_13_event_5.get(), 212)
        self.check_student_num_input(self.individual_14_event_5.get(), 213)
        self.check_student_num_input(self.individual_15_event_5.get(), 214)
        self.check_student_num_input(self.individual_16_event_5.get(), 215)
        self.check_student_num_input(self.individual_17_event_5.get(), 216)
        self.check_student_num_input(self.individual_18_event_5.get(), 217)
        self.check_student_num_input(self.individual_19_event_5.get(), 218)
        self.check_student_num_input(self.individual_20_event_5.get(), 219)

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

        self.the_smaller_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")

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

        self.edit_individuals_button = customtkinter.CTkButton(self.edit_teams_and_individuals_content_frame, text="Edit individuals", font=self.the_font, height=600, width=400, fg_color="#002542", hover_color="#25b2a1", command=self.switch_to_edit_individuals_menu).grid(row=0, column=0, padx=100, pady=50)

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
            self.individual_1_team_4_event_5, self.individual_2_team_4_event_5, self.individual_3_team_4_event_5, self.individual_4_team_4_event_5, self.individual_5_team_4_event_5, = customtkinter.StringVar(value=data[111]), customtkinter.StringVar(value=data[112]), customtkinter.StringVar(value=data[113]), customtkinter.StringVar(value=data[114]), customtkinter.StringVar(value=data[115])

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

            ## event 3 ##

            self.individual_1_event_3, self.individual_2_event_3, self.individual_3_event_3, self.individual_4_event_3, self.individual_5_event_3 = customtkinter.StringVar(value=data[160]), customtkinter.StringVar(value=data[161]), customtkinter.StringVar(value=data[162]), customtkinter.StringVar(value=data[163]), customtkinter.StringVar(value=data[164])
            self.individual_6_event_3, self.individual_7_event_3, self.individual_8_event_3, self.individual_9_event_3, self.individual_10_event_3 = customtkinter.StringVar(value=data[165]), customtkinter.StringVar(value=data[166]), customtkinter.StringVar(value=data[167]), customtkinter.StringVar(value=data[168]), customtkinter.StringVar(value=data[169])
            self.individual_11_event_3, self.individual_12_event_3, self.individual_13_event_3, self.individual_14_event_3, self.individual_15_event_3 = customtkinter.StringVar(value=data[170]), customtkinter.StringVar(value=data[171]), customtkinter.StringVar(value=data[172]), customtkinter.StringVar(value=data[173]), customtkinter.StringVar(value=data[174])
            self.individual_16_event_3, self.individual_17_event_3, self.individual_18_event_3, self.individual_19_event_3, self.individual_20_event_3 = customtkinter.StringVar(value=data[175]), customtkinter.StringVar(value=data[176]), customtkinter.StringVar(value=data[177]), customtkinter.StringVar(value=data[178]), customtkinter.StringVar(value=data[179])

            ## event 4 ##

            self.individual_1_event_4, self.individual_2_event_4, self.individual_3_event_4, self.individual_4_event_4, self.individual_5_event_4 = customtkinter.StringVar(value=data[180]), customtkinter.StringVar(value=data[181]), customtkinter.StringVar(value=data[182]), customtkinter.StringVar(value=data[183]), customtkinter.StringVar(value=data[184])
            self.individual_6_event_4, self.individual_7_event_4, self.individual_8_event_4, self.individual_9_event_4, self.individual_10_event_4 = customtkinter.StringVar(value=data[185]), customtkinter.StringVar(value=data[186]), customtkinter.StringVar(value=data[187]), customtkinter.StringVar(value=data[188]), customtkinter.StringVar(value=data[189])
            self.individual_11_event_4, self.individual_12_event_4, self.individual_13_event_4, self.individual_14_event_4, self.individual_15_event_4 = customtkinter.StringVar(value=data[190]), customtkinter.StringVar(value=data[191]), customtkinter.StringVar(value=data[192]), customtkinter.StringVar(value=data[193]), customtkinter.StringVar(value=data[194])
            self.individual_16_event_4, self.individual_17_event_4, self.individual_18_event_4, self.individual_19_event_4, self.individual_20_event_4 = customtkinter.StringVar(value=data[195]), customtkinter.StringVar(value=data[196]), customtkinter.StringVar(value=data[197]), customtkinter.StringVar(value=data[198]), customtkinter.StringVar(value=data[199])

            ## event 5 ##

            self.individual_1_event_5, self.individual_2_event_5, self.individual_3_event_5, self.individual_4_event_5, self.individual_5_event_5 = customtkinter.StringVar(value=data[200]), customtkinter.StringVar(value=data[201]), customtkinter.StringVar(value=data[202]), customtkinter.StringVar(value=data[203]), customtkinter.StringVar(value=data[204])
            self.individual_6_event_5, self.individual_7_event_5, self.individual_8_event_5, self.individual_9_event_5, self.individual_10_event_5 = customtkinter.StringVar(value=data[205]), customtkinter.StringVar(value=data[206]), customtkinter.StringVar(value=data[207]), customtkinter.StringVar(value=data[208]), customtkinter.StringVar(value=data[209])
            self.individual_11_event_5, self.individual_12_event_5, self.individual_13_event_5, self.individual_14_event_5, self.individual_15_event_5 = customtkinter.StringVar(value=data[210]), customtkinter.StringVar(value=data[211]), customtkinter.StringVar(value=data[212]), customtkinter.StringVar(value=data[213]), customtkinter.StringVar(value=data[214])
            self.individual_16_event_5, self.individual_17_event_5, self.individual_18_event_5, self.individual_19_event_5, self.individual_20_event_5 = customtkinter.StringVar(value=data[215]), customtkinter.StringVar(value=data[216]), customtkinter.StringVar(value=data[217]), customtkinter.StringVar(value=data[218]), customtkinter.StringVar(value=data[219])

    ## edit individuals content ##

        self.edit_individuals_event_1_menu = customtkinter.CTkFrame(self.root, width=800, height=700, )

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

        self.edit_individuals_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Display individual scoreboards", font=self.the_font, height=600, width=400, hover_color="#25b2a1", fg_color="#002542", command=self.switch_to_individuals_display_score_board_menu).grid(row=0, column=0, padx=100, pady=50)

        self.edit_teams_button = customtkinter.CTkButton(self.display_scoreboard_content_frame, text="Display team scoreboards", font=self.the_font, height=600, width=400, hover_color="#25b2a1", fg_color="#002542", command=self.switch_to_teams_display_score_board_menu).grid(row=0, column=1, padx=100, pady=50)

    ## display scoreboard content frame ##

        self.display_scoreboard_for_teams = customtkinter.CTkFrame(self.root, width=900, height=800,)

    ## display individuals score board content ##

        self.display_score_board_individuals_menu_1_1 = customtkinter.CTkFrame(self.root, width=750, height=600)

##        ##------------------------------------------------------------------------------------------------------------

        self.root.mainloop()

my_gui()
