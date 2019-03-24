from tkinter import font
from tkinter import *
from tkinter import ttk


def open_settings(root, instance):
    window = Toplevel(root)
    # window.grab_set()
    window.geometry("600x400")
    window.minsize(width=600, height=400)
    window.title('Settings')

    nb = ttk.Notebook(window)
    basic_window = Frame(nb)
    account_window = Frame(nb)
    filters_window = Frame(nb)
    appearance_window = Frame(nb)
    nb.add(basic_window, text="General")
    nb.add(account_window, text="Account")
    nb.add(filters_window, text="Filters")
    nb.add(appearance_window, text="Appearance")
    nb.pack(expand=1, fill=BOTH)

    group = LabelFrame(basic_window, text="General settings", padx=5, pady=5)
    group.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    i = 0
    Label(group, text="Categories:").grid(row=i, column=0)
    Checkbar(group, ['Inbox', 'Drafts', 'Sent', 'Spam', 'Trash']).grid(row=i, column=1)
    Label(group, text="Display:          ").grid(row=i, column=3)
    Checkbar(group, ['Header', 'Sender', 'Message', 'Date']).grid(row=i, column=4)
    i += 1

    Label(group, text="Highlight messages:").grid(row=i, column=0, pady=(10,0))
    r1 = Radiobutton(group, text="Activated", variable=instance.variable_messages, value="Yes")
    r1.grid(row=i, column=1, sticky="nsew", pady=(10,0))
    r2 = Radiobutton(group, text="Deactivated", variable=instance.variable_messages, value="No")
    r2.grid(row=i, column=2, sticky="nsew", pady=(10,0))
    r1.select()
    i += 1

    Label(group, text="Key shortcuts:").grid(row=i, column=0)
    r11 = Radiobutton(group, text="Activated", variable=instance.variable_keys, value="Yes")
    r11.grid(row=i, column=1)
    r22 = Radiobutton(group, text="Deactivated", variable=instance.variable_keys, value="No")
    r22.grid(row=i, column=2)
    r11.select()
    i += 1

    # p1
    localization = LabelFrame(basic_window, text="Localization", padx=5, pady=5)
    localization.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    i = 0
    Label(localization, text="Language:").grid(row=i, column=0)
    choices = ['English', 'German', 'Czech', 'Poland']
    instance.variable_language.set('English')
    ttk.Combobox(localization, values=choices).grid(row=i, column=1, sticky="nsew")
    i += 1

    Label(localization, text="Phone format:").grid(row=i, column=0, sticky="nsew")
    choices = ['+420', '+44', '+123', '987']
    instance.variable_phone.set('+420')
    ttk.Combobox(localization, values=choices).grid(row=i, column=1, sticky="nsew")
    i += 1

    Label(localization, text="Number format:").grid(row=i, column=0)
    r111 = Radiobutton(localization, text="Decimal point", variable=instance.variable_number, value="point")
    r111.grid(row=i, column=1)
    r222 = Radiobutton(localization, text="Decimal comma", variable=instance.variable_number, value="comma")
    r222.grid(row=i, column=2)
    r111.select()
    i += 1



    create_buttons(basic_window)
    create_buttons(account_window)
    create_buttons(filters_window)
    create_buttons(appearance_window)








    # p2
    la2 = Label(account_window, text="Druhe okno")
    la2.pack()


def create_buttons(master):
    padx = 3
    inactive_bg = "#3E75FF"
    active_bg = '#3e55ff'

    buttons_frame = Frame(master, border=0)
    buttons_frame.pack(fill=X, expand=0, side=TOP, padx=2, pady=(0, 0), ipadx=0, ipady=5)

    ok_button = Button(buttons_frame, text="OK")
    cancel_button = Button(buttons_frame, text="Cancel")
    apply_button = Button(buttons_frame, text="Apply")
    buttons = [ok_button, cancel_button, apply_button]

    for button in buttons:
        button.pack(anchor="e", side=RIGHT, padx=padx, ipady=2, ipadx=5)
        button.config(fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0, activeforeground="white")


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=TOP, anchor=W):
        Frame.__init__(self, parent)
        self.vars = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]
        i = 0
        for pick in picks:
            chk = Checkbutton(self, text=pick, variable=self.vars[i])
            chk.pack(side=side, anchor=anchor, expand=YES)
            chk.select()
            i+=1

