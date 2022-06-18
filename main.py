import customtkinter as ct


# import tkinter.messagebox
# import sqlite3 as sql


class LabelEntry(ct.CTkFrame):
    def __init__(self, parent, text, width=240):
        super().__init__(parent)
        self.pack()
        self.configure(fg_color="#EBEBEC")
        lbl = ct.CTkLabel(self, text=text, width=14)
        lbl.pack(side=ct.LEFT, padx=5, pady=5)
        entry = ct.CTkEntry(self, placeholder_text="Enter " + text, width=width)
        entry.pack(side=ct.LEFT, padx=5)


class NewRecord(ct.CTkFrame):
    def __init__(self, parent, controller):
        ct.CTkFrame.__init__(self, parent)
        label1 = ct.CTkLabel(self, text="New Record", text_font=("Times", 24))
        label2 = ct.CTkLabel(
            self, text="NOTE: If you want a new record, previous one will be deleted,continue?",
            text_font=("Times", 14))

        bt2 = ct.CTkButton(self, text="YES", text_font=("Times", 16), bg="orange",
                           height=2, width=17, command=lambda: controller.show_frame())
        bt3 = ct.CTkButton(self, text="NO", text_font=("Times", 16), bg="red", height=2,
                           width=17, command=lambda: controller.show_frame())
        label1.pack()
        label2.pack()
        bt2.pack()
        bt3.pack()


class AddStudentPage(ct.CTkFrame):
    def __init__(self, parent, controller):
        ct.CTkFrame.__init__(self, parent)
        self.WIDTH = self.winfo_screenwidth()
        self.HEIGHT = self.winfo_screenheight()
        self.configure(fg_color="#EBEBEC")
        self.label_title = ct.CTkLabel(text="Welcome to Attendance Management System", text_font=("", -24))
        self.label_title.pack(padx=15, pady=15)
        login_frame = ct.CTkFrame(self, fg_color="#EBEBEC")
        login_frame.place(x=(self.WIDTH / 2) - 150, y=(self.HEIGHT / 2) - 200)
        LabelEntry(login_frame, "First Name")
        LabelEntry(login_frame, "Last Name")
        LabelEntry(login_frame, "Phone Number")
        LabelEntry(login_frame, "Standard")


class AttendanceManager(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Attendance Management System")
        self.attributes("-zoomed", True)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        container = ct.CTkFrame(self)
        container.pack(side="bottom", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = dict()
        for F in (AddStudentPage,):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AddStudentPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        self.destroy()


if __name__ == '__main__':
    app = AttendanceManager()
    app.mainloop()
