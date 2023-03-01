
## importing tkinter ##

import tkinter as tk

class my_gui:

##    ##----------------------------------------------------------------------------------------------------------------

    ## functions ##

    def switch_to_events_menu_frame(self):

        self.event_menu_frame_navigation.pack(fill="x", )

        self.navigation_button_frame.pack_forget()

    def switch_to_start_menu_frame(self):

        self.navigation_button_frame.pack(fill="x", )

        self.event_menu_frame_navigation.pack_forget()

    def __init__(self):

        ## initialising the gui ##

        self.root = tk.Tk()

        self.root.title("scoring system")

        self.root.geometry("900x800")

##        ##------------------------------------------------------------------------------------------------------------

        ## frames ##


        # self.navigation_bar_frame = tk.Frame(self.root, bg="red")
        #
        # self.navigation_bar_frame.configure(self.navigation_bar_frame, height=300, )
        #
        # self.navigation_bar_frame.pack()

        self.navigation_button_frame = tk.Frame(self.root, )

        self.navigation_button_frame.columnconfigure(0, weight=1, )
        self.navigation_button_frame.columnconfigure(1, weight=1, )
        self.navigation_button_frame.columnconfigure(2, weight=1, )
        self.navigation_button_frame.columnconfigure(3, weight=1, )
        self.navigation_button_frame.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = tk.Button(self.navigation_button_frame, text="display scoreboard", font=("", 18), height=2, bg="blue").grid(row=0, column=0, sticky=tk.W + tk.E)

        self.edit_teams_and_individuals_button = tk.Button(self.navigation_button_frame, text="edit teams and individuals", font=("", 18), height=2, ).grid(row=0, column=1, sticky=tk.W + tk.E)

        self.start_menu_button = tk.Button(self.navigation_button_frame, text="start menu", font=("", 18), height=2, command=self.switch_to_start_menu_frame).grid(row=0, column=2, sticky=tk.W + tk.E)

        self.event_menu_button = tk.Button(self.navigation_button_frame, text= "edit events", font=("", 18), height=2, command=self.switch_to_events_menu_frame).grid(row=0, column=3, sticky=tk.W + tk.E)

        self.close_program_button = tk.Button(self.navigation_button_frame, text="close program", font=("", 18), height=2, ).grid(row=0, column=4, sticky=tk.W + tk.E)

        self.navigation_button_frame.pack(fill="x", )

##        ##------------------------------------------------------------------------------------------------------------

        ## events menu navigation ##

        self.event_menu_frame_navigation = tk.Frame(self.root, )

        self.event_menu_frame_navigation.columnconfigure(0, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(1, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(2, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(3, weight=1, )
        self.event_menu_frame_navigation.columnconfigure(4, weight=1, )

        self.display_scoreboard_button = tk.Button(self.event_menu_frame_navigation, text="display scoreboard", font=("", 18), height=2, ).grid(row=0, column=0, sticky=tk.W + tk.E)

        self.edit_teams_and_individuals_button = tk.Button(self.event_menu_frame_navigation, text="edit teams and individuals", font=("", 18), height=2, ).grid(row=0, column=1, sticky=tk.W + tk.E)

        self.start_menu_button = tk.Button(self.event_menu_frame_navigation, text="start menu", font=("", 18), height=2, command=self.switch_to_start_menu_frame).grid(row=0, column=2, sticky=tk.W + tk.E)

        self.event_menu_button = tk.Button(self.event_menu_frame_navigation, text="edit events", font=("", 18), height=2, command=self.switch_to_events_menu_frame).grid(row=0, column=3, sticky=tk.W + tk.E)

        self.back_button = tk.Button(self.event_menu_frame_navigation, text="back", font=("", 18), height=2, ).grid(row=0, column=4, sticky=tk.W + tk.E)

        self.root.mainloop()


my_gui()