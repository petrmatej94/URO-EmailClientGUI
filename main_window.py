from tkinter import font
from tkinter import *
import data, settings, new_message

menuBackground = "#1A1F30"
activeItemBg = '#151825'
my_font = "Helvetica 10"


def callback(f, *a):
    return lambda: f(*a)


class Client:
    def menu_action(self, action):
        if action != "composeEmailButton":
            for item in self.buttons:
                item.config(bg=menuBackground)

        header = self.mailHeader.cget("text")
        if action == "composeEmailButton":
            new_message.open_new_message(self, root)
        elif action == "InboxButton":
            self.InboxButton.config(bg=activeItemBg)
            self.update_emails(data.inbox)
            header = "Inbox"
        elif action == "DraftsButton":
            header = "Drafts"
            self.DraftsButton.config(bg=activeItemBg)
            self.update_emails(data.drafts)
        elif action == "SentButton":
            header = "Sent"
            self.SentButton.config(bg=activeItemBg)
            self.update_emails(data.sent)
        elif action == "SpamButton":
            header = "Spam"
            self.SpamButton.config(bg=activeItemBg)
            self.update_emails(data.spam)
        elif action == "TrashButton":
            header = "Trash"
            self.TrashButton.config(bg=activeItemBg)
            self.update_emails(data.trash)
        elif action == "Settings":
            settings.open_settings(root)

        # self.mailHeader.config(text=header)
        self.currentFolder = header

    def __init__(self, root):
        root.title('Email Client')
        root.geometry("800x700")
        root.minsize(width=1200, height=400)
        root.grid()

        # Main Window
        self.window = Frame(root)
        self.window.pack(fill=BOTH, expand=1)

        # Top Menu
        # self.topMenu = Frame(self.window, relief=GROOVE, borderwidth=2, bg="gray")
        # self.topMenu.pack(fill=X, side=TOP, ipady=20)

        self.topMenu = Menu(self.window)
        root.config(menu=self.topMenu)

        self.menuData = Menu(self.topMenu, tearoff=0)
        self.topMenu.add_cascade(label="File", menu=self.menuData)
        self.menuData.add_command(label="Compose Email")
        self.menuData.add_command(label="Export Emails")
        self.menuData.add_command(label="Settings", command=callback(self.menu_action, "Settings"))
        self.menuData.add_command(label="Exit")


        # Main Frame
        self.mainFrame = Frame(self.window, relief=GROOVE, bg="white")
        self.mainFrame.pack(fill=BOTH, expand=1, side=TOP)

        # Left Menu
        self.leftMenu = Frame(self.mainFrame, relief=GROOVE, bg="#1A1F30")
        self.leftMenu.pack(fill=Y, side=LEFT, ipadx=30)

        self.sendImage = PhotoImage(file="imagesSmall/mail.png")
        self.composeEmailButton = Button(self.leftMenu, text='  Compose Email', bg="#3E75FF", fg="white", cursor="hand2",
                                         image=self.sendImage, compound="left", activebackground='#3e55ff',
                                         activeforeground="white", borderwidth=0, font=my_font + " bold", anchor='c', command=callback(self.menu_action, "composeEmailButton"))
        self.composeEmailButton.pack(fill=X, side=TOP, ipadx=15, pady=30, ipady=10)

        # Left Menu items
        self.la=Label(self.leftMenu, text="MAILBOXES", bg=menuBackground, fg="white", anchor="w", font=my_font)
        self.la.pack(fill=X, padx=8, pady=1)

        items = ["    Inbox", "    Drafts", "    Sent", "    Spam", "    Trash",]
        folder = "imagesSmall/"
        images = ["inbox.png", "draft.png", "sent.png", "spam.png", "trash.png"]

        i = 0
        self.inboxImage = PhotoImage(file=folder+images[i])
        self.InboxButton = Button(self.leftMenu, text=items[i], bg=activeItemBg, fg="white", cursor="hand2",
                                         image=self.inboxImage, compound="left", activebackground=activeItemBg,
                                         activeforeground="white", borderwidth=0, font=my_font, anchor="w", command=callback(self.menu_action, "InboxButton"))
        self.InboxButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.draftImage = PhotoImage(file=folder+images[i])
        self.DraftsButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white", cursor="hand2",
                                         image=self.draftImage, compound="left", activebackground=activeItemBg,
                                         activeforeground="white", borderwidth=0, font=my_font, anchor="w", command=callback(self.menu_action, "DraftsButton"))
        self.DraftsButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.sentImage = PhotoImage(file=folder+images[i])
        self.SentButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.sentImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor="w", command=callback(self.menu_action, "SentButton"))
        self.SentButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.spamImage = PhotoImage(file=folder+images[i])
        self.SpamButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.spamImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor="w", command=callback(self.menu_action, "SpamButton"))
        self.SpamButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.trashImage = PhotoImage(file=folder+images[i])
        self.TrashButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.trashImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor="w", command=callback(self.menu_action, "TrashButton"))
        self.TrashButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.buttons = [self.InboxButton, self.DraftsButton, self.SentButton, self.SpamButton, self.TrashButton]

        # Emails List
        self.emailListBackground = "white"
        self.inactiveEmail = "#DAE1EC"
        self.fontFrom = font.Font(size=9, weight="normal")
        self.fontSubject = font.Font(size=11, weight="bold")
        self.fontDate = font.Font(size=8, weight="normal")
        self.fontMessage = font.Font(size=9, weight="normal")

        self.emailsList = Frame(self.mainFrame, bg="#f7f7f7")
        self.emailsList.pack(fill=BOTH, side=LEFT)

        # Emails List: Search Frame
        self.header = Frame(self.emailsList, relief=GROOVE, borderwidth=0, bg=self.emailListBackground, cursor="hand2")
        # self.header .pack(fill=X, side=TOP)

        self.mailHeader = Label(self.header, text="   Search for messages...", bg=self.emailListBackground, font=my_font, cursor="hand2")
        # self.mailHeader.pack(fill=X, ipady=10, anchor="w", side=LEFT)

        self.currentFolder = "Inbox"

        # Emails List: List of Emails
        self.canvas = Canvas(self.emailsList)
        self.canvas.pack(side=LEFT, fill=Y)

        scrollbar = Scrollbar(self.emailsList, command=self.canvas.yview)
        scrollbar.pack(side=LEFT, fill=Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind('<Configure>', self.on_configure)

        self.frame = Frame(self.canvas, bg=menuBackground)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.userImage = PhotoImage(file="imagesBig/user.png")
        self.update_emails(data.inbox)


        # Email Detail Window
        self.emailWindow = Frame(self.mainFrame, relief=GROOVE, bg="white")
        self.emailWindow.pack(fill=BOTH, expand=1, side=LEFT, pady=15, padx=30)

        self.detailLabel = Label(self.emailWindow, text="You don't have any selected emails", bg=self.emailListBackground, font=my_font, cursor="hand2")
        self.detailLabel.pack(fill=X, ipady=10, side=TOP)

        # new_message.open_new_message(root)


    def update_emails(self, emails):
        for item in self.frame.pack_slaves():
            item.destroy()

        for key, value in emails.items():
            email = Frame(self.frame, relief=GROOVE, bg=self.inactiveEmail)
            email.pack(fill=X, side=TOP, ipadx=90, ipady=5, pady=(0, 1), anchor="w")
            email.bind("<Button-1>", lambda event, id=key: self.select_email(id))

            photo = Label(email, image=self.userImage, bg=email.cget("bg"))
            photo.grid(row=0, column=0, padx=15, pady=(10, 1), rowspan=2)

            email_from = Label(email, text=value["from"], bg=email.cget("bg"), font=self.fontFrom)
            email_from.grid(row=0, column=1, padx=8, pady=(5,0), sticky="SW")

            subject = Label(email, text=value["subject"], bg=email.cget("bg"), font=self.fontSubject)
            subject.grid(row=1, column=1, padx=8, pady=1, sticky="W")

            text = value["message"]
            if len(text) >= 40: text = text[:40]+"..."

            message = Label(email, text=text, bg=email.cget("bg"), font=self.fontMessage)
            message.grid(row=2, column=1, padx=8, pady=1, sticky="W")

            date = Label(email, text=value["date"], bg=email.cget("bg"), font=self.fontDate)
            date.grid(row=3, column=1, padx=8, pady=1, sticky="W")

    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def select_email(self, id):
        self.detailLabel.destroy()
        cnt = 1
        for item in self.frame.pack_slaves():
            item.config(bg=self.inactiveEmail)
            for grid in item.grid_slaves():
                grid.config(bg=self.inactiveEmail)
                if cnt == id:
                    item.config(bg="white")
                    grid.config(bg="white")
            cnt += 1
        email_array = {}
        if self.currentFolder == "Inbox":
            email_array = data.inbox
        elif self.currentFolder == "Spam":
            email_array = data.spam
        elif self.currentFolder == "Trash":
            email_array = data.trash
        elif self.currentFolder == "Sent":
            email_array = data.sent
        elif self.currentFolder == "Drafts":
            email_array = data.drafts

        for key, value in email_array.items():
            if key == id:
                print("selected :", key, value)
                for item in self.emailWindow.grid_slaves():
                    item.destroy()

                # Grid with Email Details inside self.emailWindow
                email = self.emailWindow
                font_from = ("Arial", 8, "bold")
                font_date = ("Arial", 8, "")
                font_subject = ("Arial", 17, "bold")

                email.grid_columnconfigure(1, weight=1)

                photo = Label(email, image=self.userImage, bg=email.cget("bg"))
                photo.grid(row=0, column=0, padx=8, pady=1)

                email_from = Label(email, text="From: " + value["from"], bg=email.cget("bg"), font=font_from)
                email_from.grid(row=0, column=1, padx=8, pady=1, sticky="W")

                email_from = Label(email, text=value["date"], bg=email.cget("bg"), font=font_date)
                email_from.grid(row=1, column=1, padx=8, pady=0, sticky="W")

                subject = Label(email, text=value["subject"], bg=email.cget("bg"), font=font_subject)
                subject.grid(row=2, column=1, padx=8, pady=0, sticky="W")

                subject = Label(email, text=value["message"], bg=email.cget("bg"), justify=LEFT, anchor="nw", font=font_date, wraplength=self.emailWindow.winfo_width()-100)
                subject.grid(row=3, column=1, padx=8, pady=1, sticky="nw")
                subject.config(height=30)

                subject = Label(email, text="Attachments", bg=email.cget("bg"), font=font_from)
                subject.grid(row=4, column=1, padx=8, pady=1, sticky="W")

                subject = Label(email, text="Text Input Area", bg=email.cget("bg"), font=font_from)
                subject.grid(row=5, column=1, padx=8, pady=1, sticky="W")

                subject = Label(email, text="Buttons", bg=email.cget("bg"), font=font_from)
                subject.grid(row=6, column=1, padx=8, pady=1, sticky="W")



root = Tk()
app = Client(root)
root.mainloop()

