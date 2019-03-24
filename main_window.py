from tkinter import font
from tkinter import *
import data, settings, new_message
import os
from PIL import Image
from PIL import ImageTk

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
            new_message.open_new_message(self, root, self.toolbarImages)
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
            settings.open_settings(root, self)

        # self.mailHeader.config(text=header)
        self.currentFolder = header

    def __init__(self, root):
        root.title('Email Client')
        root.geometry("800x700")
        root.minsize(width=1200, height=720)
        root.grid()
        root.bind("<Configure>", self.on_resize)

        # Main Window
        self.window = Frame(root)
        self.window.pack(fill=BOTH, expand=1)
        self.message = None

        self.topMenu = Menu(self.window)
        root.config(menu=self.topMenu)

        self.menuFile = Menu(self.topMenu, tearoff=0)
        self.topMenu.add_cascade(label="File", menu=self.menuFile)
        self.menuFile.add_command(label="Compose Email")
        self.menuFile.add_command(label="Export Emails")
        self.menuFile.add_command(label="Settings", command=callback(self.menu_action, "Settings"))
        self.menuFile.add_command(label="Exit", command=root.destroy)

        self.menuEdit = Menu(self.topMenu, tearoff=0)
        self.topMenu.add_cascade(label="Edit", menu=self.menuEdit)
        self.menuEdit.add_command(label="Undo")
        self.menuEdit.add_command(label="Redo")
        self.menuEdit.add_command(label="Copy")
        self.menuEdit.add_command(label="Paste")

        self.menuTools = Menu(self.topMenu, tearoff=0)
        self.topMenu.add_cascade(label="Tools", menu=self.menuTools)
        self.menuTools.add_command(label="Console")
        self.menuTools.add_command(label="Drawings")
        self.menuTools.add_command(label="Addons")
        self.menuTools.add_command(label="Plugins")

        self.imagesNames = os.listdir("imagesSmall/toolbar")
        print(self.imagesNames)
        self.variable_messages = StringVar()
        self.variable_keys = StringVar()
        self.variable_categories = StringVar()
        self.variable_display = StringVar()
        self.variable_language = StringVar()
        self.variable_phone = StringVar()
        self.variable_number = StringVar()
        self.toolbarImages = []
        for image in self.imagesNames:
            self.toolbarImages.append(PhotoImage(file="imagesSmall/toolbar/" + image))

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

        anchor="w"
        i = 0
        self.inboxImage = PhotoImage(file=folder+images[i])
        self.InboxButton = Button(self.leftMenu, text=items[i], bg=activeItemBg, fg="white", cursor="hand2",
                                         image=self.inboxImage, compound="left", activebackground=activeItemBg,
                                         activeforeground="white", borderwidth=0, font=my_font, anchor=anchor, command=callback(self.menu_action, "InboxButton"))
        self.InboxButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.draftImage = PhotoImage(file=folder+images[i])
        self.DraftsButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white", cursor="hand2",
                                         image=self.draftImage, compound="left", activebackground=activeItemBg,
                                         activeforeground="white", borderwidth=0, font=my_font, anchor=anchor, command=callback(self.menu_action, "DraftsButton"))
        self.DraftsButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.sentImage = PhotoImage(file=folder+images[i])
        self.SentButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.sentImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor=anchor, command=callback(self.menu_action, "SentButton"))
        self.SentButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.spamImage = PhotoImage(file=folder+images[i])
        self.SpamButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.spamImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor=anchor, command=callback(self.menu_action, "SpamButton"))
        self.SpamButton.pack(fill=X, side=TOP, ipadx=15, pady=0, ipady=10)
        i += 1

        self.trashImage = PhotoImage(file=folder+images[i])
        self.TrashButton = Button(self.leftMenu, text=items[i], bg=menuBackground, fg="white",
                                         image=self.trashImage, compound="left", activebackground=activeItemBg, cursor="hand2",
                                         activeforeground="white", borderwidth=0, font=my_font, anchor=anchor, command=callback(self.menu_action, "TrashButton"))
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

        # settings.open_settings(root)

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
                font_subject = ("Georgia", 20, "bold")
                font_text = ("Arial", 10, "")

                email.grid_columnconfigure(1, weight=1)

                photo = Label(email, image=self.userImage, bg=email.cget("bg"))
                photo.grid(row=0, column=0, padx=8, pady=1)

                email_from = Label(email, text="From: " + value["from"], bg=email.cget("bg"), font=font_from)
                email_from.grid(row=0, column=1, padx=8, pady=1, sticky="W")

                email_from = Label(email, text=value["date"], bg=email.cget("bg"), font=font_date)
                email_from.grid(row=1, column=1, padx=8, pady=0, sticky="W")

                subject = Label(email, text=value["subject"], bg=email.cget("bg"), font=font_subject)
                subject.grid(row=2, column=1, padx=8, pady=(2,10), sticky="W")

                self.message = Label(email, text=value["message"], bg=email.cget("bg"), justify=LEFT, anchor="nw", font=font_text, wraplength=self.emailWindow.winfo_width()-100)
                self.message.grid(row=3, column=1, padx=8, pady=1, sticky="nsew")

                divideFrame = Frame(email, bg=self.inactiveEmail)
                divideFrame.grid(row=4, column=0, columnspan=3, padx=8, ipady=1, pady=20, sticky="nsew")


                # Attachments frame
                attachments_frame = Frame(email, relief=GROOVE, border=0, bg="white")
                attachments_frame.grid(row=5, column=1, sticky="nsew", pady=(0,20))

                image = Image.open("imagesBig/wild.png")
                image = image.resize((100, 60), Image.ANTIALIAS)

                self.img = ImageTk.PhotoImage(image)
                img1 = Label(attachments_frame, image=self.img, width=100, height=60)
                img1.pack(side=LEFT, padx=(0, 10))

                img1 = Label(attachments_frame, image=self.img, width=100, height=60)
                img1.pack(side=LEFT, padx=(0, 10))

                img1 = Label(attachments_frame, image=self.img, width=100, height=60)
                img1.pack(side=LEFT, padx=(0, 10))


                # Text Input in Email frame
                message_frame = Frame(email, relief=GROOVE, border=0, bg="black", borderwidth=5)
                message_frame.grid(row=6, column=1, sticky="nsew")

                entry = Text(message_frame, height=5)
                entry.pack(fill=X, expand=1)
                entry.insert(END, "Write your message here...")


                # Buttons in Email frame
                buttons_frame = Frame(master=email, bg="white")
                buttons_frame.grid(row=7, column=0, columnspan=3, padx=8, pady=1, sticky="nsew")

                send_button = Button(buttons_frame, text="Send")
                save_button = Button(buttons_frame, text="Save to Drafts")
                throw_button = Button(buttons_frame, text="Throw away")

                buttons = [send_button, save_button, throw_button]
                inactive_bg = "#3E75FF"
                active_bg = '#3e55ff'

                for button in buttons:
                    button.pack(anchor="e", side=RIGHT, padx=2, ipady=2, ipadx=5)
                    button.config(fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0,
                                  activeforeground="white")

    def on_resize(self, event):
        if self.message is not None:
            self.message.config(wraplength=self.emailWindow.winfo_width()-100)



root = Tk()
app = Client(root)
root.mainloop()



