import webbrowser
import customtkinter
from PIL import Image, ImageTk
import datarequest

# Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        WIDTH = 800
        HEIGHT = 600

        # self.tk.eval('tk::PlaceWindow . center')
        self.lift()
        self.title("Speedrun Profile")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(False, False)

        speedrun = Image.open('speedrun.png').resize((20,20))
        speedrun = ImageTk.PhotoImage(speedrun)

        def searchUser():
            
            def callback(url):
                webbrowser.open_new_tab(userProfile.get('webLink'))
 
            
            # destroys widgets in mainFrame to refresh visuals
            if frameMain.winfo_children() is not None:
                for widget in frameMain.winfo_children():
                    widget.destroy()

            # Get user name and clear entry
            userName = self.entry.get()
            self.entry.delete(0, len(userName))
            self.focus()

            # Get user data
            userProfile = datarequest.getUserProfile(userName)
            personalBestsData = datarequest.getPersonalBests(
                userProfile.get('userId'))
            runCountData = datarequest.getRunCount(
                userProfile.get('userId'))

            profileFrame = customtkinter.CTkFrame(frameMain)
            profileFrame.grid(row=0, column=1)

            # Display user data
            self.userNameLabel = customtkinter.CTkLabel(profileFrame, text="{}".format(
                userProfile.get('userName')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.userNameLabel.grid(row=0, column=0, padx=10, pady=10)

            self.speedrunLink = customtkinter.CTkLabel(profileFrame, text='', image=speedrun, compound='right')
            self.speedrunLink.bind("<Button>", lambda e: callback(userProfile.get('webLink'))) # click to open link
            self.speedrunLink.grid(row=0, column=1, padx=10, pady=10)

            self.signUpDateLabel = customtkinter.CTkLabel(profileFrame, text="Member Since: {}".format(
                userProfile.get('userSignup')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.signUpDateLabel.grid(row=2, column=0, padx=10, pady=10)
            
            ###
            self.totalRunsLabel = customtkinter.CTkLabel(frameMain, text="Total Runs: {}".format(
                runCountData.get('totalRuns')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.totalRunsLabel.grid(row=3, column=0, padx=10, pady=10)

            self.verifiedRunsLabel = customtkinter.CTkLabel(frameMain, text=" Verified Runs: {}".format(
                runCountData.get('verifiedRuns')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.verifiedRunsLabel.grid(row=4, column=0, padx=10, pady=10)

            self.rejectedRunsLabel = customtkinter.CTkLabel(frameMain, text="Rejected Runs: {}".format(
                runCountData.get('rejectedRuns')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.rejectedRunsLabel.grid(row=5, column=0, padx=10, pady=10)

            ###
            self.personalBestsLabel = customtkinter.CTkLabel(frameMain, text="Personal Bests: {}".format(
                personalBestsData.get('personalBests')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.personalBestsLabel.grid(row=6, column=0, padx=10, pady=10)
            
            self.firstPlaceLabel = customtkinter.CTkLabel(frameMain, text="1st: {}".format(
                personalBestsData.get('firstPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.firstPlaceLabel.grid(row=7, column=0, padx=10, pady=10)

            self.secondPlaceLabel = customtkinter.CTkLabel(frameMain, text="2nd: {}".format(
                personalBestsData.get('secondPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.secondPlaceLabel.grid(row=8, column=0, padx=10, pady=10)

            self.thirdPlaceLabel = customtkinter.CTkLabel(frameMain, text="3rd: {}".format(
                personalBestsData.get('thirdPlace')), font=customtkinter.CTkFont(size=20, weight="bold"))
            self.thirdPlaceLabel.grid(row=9, column=0, padx=10, pady=10)

        # Configure size of top and main frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0, minsize=HEIGHT*.15)
        self.rowconfigure(1, weight=1, minsize=HEIGHT*.85)

        # Create top frame and configure grid size
        frameTop = customtkinter.CTkFrame(
            self, fg_color='#3B3F44', corner_radius=0)
        frameTop.grid(row=0, column=0, sticky='NSWE')
        # TODO: create grid within top frame to align components

        # Top frame
        self.entry = customtkinter.CTkEntry(
            frameTop, placeholder_text="Username", width=WIDTH*.20)
        self.entry.grid(row=0, column=1, padx=(
            20, 20), pady=(25, 25), sticky="n")
        self.search_button = customtkinter.CTkButton(
            frameTop, width=40, text='Search', command=searchUser)
        self.search_button.grid(row=0, column=2, padx=10, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(
            frameTop, text="Search", anchor="n")
        self.appearance_mode_label.grid(row=0, column=6, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            frameTop, values=["System", "Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=0, column=6, padx=10, pady=10)

        # Create main frame and configure grid size
        frameMain = customtkinter.CTkFrame(self, corner_radius=0)
        frameMain.grid(row=1, column=0, sticky='NSWE')


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def test():
        root = customtkinter.CTk()
        root.geometry()
        frame = customtkinter.CTkFrame(root)
        frame.pack(pady=20, padx=60)
        root.mainloop()

# App.test()

