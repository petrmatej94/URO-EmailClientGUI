from tkinter import font
from tkinter import *

mainBg = "#F6F8FC"
my_font = "Helvetica 10"
primary_bg = "#1A1F30"


def open_new_message(my_class, root, imagesArray):
    window = Toplevel(root)
    window.geometry("600x400")
    window.minsize(width=600, height=400)
    window.title('Compose new Email')
    window.config(bg="#1A1F30")

    # Header of Email
    main_frame = Frame(window, relief=GROOVE, border=0, bg=mainBg)
    main_frame.pack(fill=X, expand=0, side=TOP, padx=7, pady=7, ipadx=0, ipady=5)
    main_frame.grid_columnconfigure(1, weight=1)

    email_from = Label(main_frame, text="From", bg=mainBg)
    email_to = Label(main_frame, text="Email to", bg=mainBg)
    subject = Label(main_frame, text="Subject", bg=mainBg)

    email_from.grid(row=0, column=0, sticky=W)
    email_to.grid(row=1, column=0, sticky=W)
    subject.grid(row=2, column=0, sticky=W)

    from_text = StringVar()
    from_text.set("Petr.matej@vsb.cz")
    from_field = Entry(main_frame, textvariable=from_text, bg="#FAFAFA", state="disabled")
    email_to_field = Entry(main_frame, highlightcolor="black", highlightthickness=1)
    subject_field = Entry(main_frame, highlightcolor="black", highlightthickness=1)

    padx = 20
    ipadx = 0
    pady = 3
    ipady = 3
    from_field.grid(row=0, column=1, padx=padx, ipadx=ipadx, pady=pady, ipady=ipady, sticky="WE")
    email_to_field.grid(row=1, column=1, padx=padx, ipadx=ipadx, pady=pady, ipady=ipady, sticky="WE")
    subject_field.grid(row=2, column=1, padx=padx, ipadx=ipadx, pady=pady, ipady=ipady, sticky="WE")

    # Toolbar
    inactive_bg = "#3E75FF"
    active_bg = '#3e55ff'

    toolbar_bg = primary_bg
    toolbar_frame = Frame(window, relief=GROOVE, border=0, bg=mainBg)
    toolbar_frame.pack(fill=X, expand=0, side=TOP, padx=7, pady=(0,7), ipadx=0, ipady=0)

    for img in imagesArray:
        butt = HoverButton(toolbar_frame, image=img, activebackground=inactive_bg, background=mainBg)
        butt.pack(anchor="e", side=LEFT, padx=0, ipady=2, ipadx=5)
        butt.config(fg="white", borderwidth=0)

    # Message Entry
    message_bg = "white"
    message_frame = Frame(window, relief=GROOVE, border=0, bg=toolbar_bg)
    message_frame.pack(fill=BOTH, expand=1, side=TOP, padx=0, pady=(0, 0), ipadx=10, ipady=10)

    entry = Text(message_frame, height=5)
    entry.pack(fill=BOTH, expand=1)
    entry.insert(END, "Write your message here...")


    # Buttons
    buttons_bg = primary_bg
    buttons_frame = Frame(window, border=0, bg=buttons_bg)
    buttons_frame.pack(fill=X, expand=0, side=TOP, padx=2, pady=(0, 0), ipadx=0, ipady=5)

    padx = 3
    inactive_bg = "#3E75FF"
    active_bg = '#3e55ff'

    send_button = Button(buttons_frame, text="Send")
    save_button = Button(buttons_frame, text="Save to Drafts")
    throw_button = Button(buttons_frame, text="Throw away", command=window.destroy)
    attachment_button = Button(buttons_frame, text="Add Attachment...")
    buttons = [send_button, save_button, throw_button]

    for button in buttons:
        button.pack(anchor="e", side=RIGHT, padx=padx, ipady=2, ipadx=5)
        button.config(fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0, activeforeground="white")

    attachment_button.pack(anchor="w", side=LEFT, padx=padx, ipady=2, ipadx=5)
    attachment_button.config(fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0, activeforeground="white")


class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
