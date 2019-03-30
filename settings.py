from tkinter import *
from tkinter import ttk

padx = 3
inactive_bg = "#3E75FF"
active_bg = '#3e55ff'

def open_settings(root, instance):
    window = Toplevel(root)
    window.grab_set()
    window.geometry("610x410")
    window.minsize(width=610, height=410)
    window.title('Settings')
    window.resizable(0, 0)

    nb = ttk.Notebook(window)
    basic_window = Frame(nb)
    server_window = Frame(nb)
    identity_window = Frame(nb)
    nb.add(server_window, text="Server")
    nb.add(basic_window, text="General")
    nb.add(identity_window, text="Identity")
    nb.pack(expand=1, fill=BOTH)
    create_buttons(window)

    # General settings
    localization = LabelFrame(basic_window, text="Localization", padx=5, pady=5)
    localization.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    i = 0
    Label(localization, text="Language:").grid(row=i, column=0, sticky="w")
    choices = ['English', 'German', 'Czech', 'Poland']
    instance.variable_language.set('English')
    ttk.Combobox(localization, values=choices, textvariable=instance.variable_language, state="readonly").grid(row=i, column=1, sticky="nsew", pady=(0,2), columnspan=10)
    i += 1

    Label(localization, text="Phone format:").grid(row=i, column=0, sticky="w")
    choices = ['+420 xxx xxx', '+44 xxxx xxx', '+123 xx xxx xxx', '987 xxx xxx']
    instance.variable_phone.set('+420 xxx xxx')
    ttk.Combobox(localization, values=choices, textvariable=instance.variable_phone, state="readonly").grid(row=i, column=1, sticky="nsew", pady=(0,2), columnspan=10)
    i += 1

    Label(localization, text="Timezone:").grid(row=i, column=0, sticky="w")
    choices = ["UTC+0", "UTC+1", "UTC+2", "UTC+3", "UTC+4", "UTC+5"]
    instance.variable_timezone.set('UTC+0')
    ttk.Combobox(localization, values=choices, textvariable=instance.variable_timezone, state="readonly").grid(row=i, column=1, sticky="nsew", pady=(0,2), columnspan=10)
    i += 1

    padx=5
    instance.variable_date = IntVar(value=0)
    Label(localization, text="Date format:").grid(row=i, column=0, sticky="w")
    # i += 1
    Radiobutton(localization, text="September 22, 2014", variable=None).grid(row=i, column=1, sticky="w", padx=padx)
    # i += 1
    Radiobutton(localization, text="2014-09-22", variable=instance.variable_date).grid(row=i, column=2, sticky="w", padx=padx)
    # i += 1
    Radiobutton(localization, text="09/22/2014", variable=instance.variable_date).grid(row=i, column=3, sticky="w", padx=padx)
    # i += 1
    Radiobutton(localization, text="22/09/2014", variable=instance.variable_date).grid(row=i, column=4, sticky="w", padx=padx)
    i += 1

    Label(localization, text="Number format:").grid(row=i, column=0, sticky="w")
    r111 = Radiobutton(localization, text="Decimal point", variable=instance.variable_number, value="point")
    r111.grid(row=i, column=1, padx=padx, sticky="w")
    r222 = Radiobutton(localization, text="Decimal comma", variable=instance.variable_number, value="comma")
    r222.grid(row=i, column=2, padx=padx, sticky="w")
    r111.select()
    i += 1

    group = LabelFrame(basic_window, text="Display settings", padx=5, pady=5)
    group.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    instance.category_variable = [IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1), IntVar(value=1)]
    i = 0
    Label(group, text="Categories:").grid(row=i, column=0, sticky="w")
    Checkbutton(group, text="Inbox", variable=instance.category_variable[0]).grid(row=i, column=1, sticky="w", padx=0)
    Checkbutton(group, text="Drafts", variable=instance.category_variable[1]).grid(row=i, column=2, sticky="w", padx=0)
    Checkbutton(group, text="Sent", variable=instance.category_variable[2]).grid(row=i, column=3, sticky="w",
                                                                                 padx=(0, 40))
    Checkbutton(group, text="Spam", variable=instance.category_variable[3]).grid(row=i, column=4, sticky="w",
                                                                                 padx=(0, 40))
    Checkbutton(group, text="Trash", variable=instance.category_variable[4]).grid(row=i, column=5, sticky="w",
                                                                                  padx=(0, 40))
    i += 1

    Label(group, text="Highlight messages:").grid(row=i, column=0, pady=(10, 0), sticky="w")
    r1 = Radiobutton(group, text="Activated", variable=instance.variable_messages, value="Yes")
    r1.grid(row=i, column=1, sticky="w", pady=(10, 0))
    r2 = Radiobutton(group, text="Deactivated", variable=instance.variable_messages, value="No")
    r2.grid(row=i, column=2, sticky="w", pady=(10, 0))
    r1.select()
    i += 1

    Label(group, text="Key shortcuts:").grid(row=i, column=0, sticky="w")
    r11 = Radiobutton(group, text="Activated", variable=instance.variable_keys, value="Yes")
    r11.grid(row=i, column=1, sticky="w")
    r22 = Radiobutton(group, text="Deactivated", variable=instance.variable_keys, value="No")
    r22.grid(row=i, column=2, sticky="w")
    r11.select()
    i += 1

    # Server settings
    conn_settings = LabelFrame(server_window, text="Connection settings", padx=5, pady=5)
    conn_settings.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    i = 0
    Label(conn_settings, text="Server Type:").grid(row=i, column=0, sticky="w")
    Label(conn_settings, text="POP Mail Server").grid(row=i, column=1, sticky="w")
    i += 1

    Label(conn_settings, text="Server Name:").grid(row=i, column=0, sticky="w")
    Entry(conn_settings).grid(row=i, column=1, sticky="w")
    Label(conn_settings, text="Port:").grid(row=i, column=2, sticky="w")
    Entry(conn_settings).grid(row=i, column=3, sticky="w")
    Label(conn_settings, text="Default:").grid(row=i, column=4, sticky="w")
    Label(conn_settings, text="110").grid(row=i, column=5, sticky="w")
    i += 1

    Label(conn_settings, text="User Name:").grid(row=i, column=0, sticky="w")
    Entry(conn_settings).grid(row=i, column=1, sticky="w")
    i += 1

    server_settings = LabelFrame(server_window, text="Server Settings", padx=5, pady=5)
    server_settings.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    Checkbutton(server_settings, text="Automatically download new messages at startup - messages will be saved locally").pack(side=TOP, anchor="w")
    Checkbutton(server_settings, text="Fetch headers only - only headers will be stored locally at your computer").pack(side=TOP, anchor="w")
    Checkbutton(server_settings, text="Leave messages on server - messages won't be downloaded to your computer locally").pack(side=TOP, anchor="w")
    Checkbutton(server_settings, text="Empty trash on exit - messages placed in trash will be deleted when you close client").pack(side=TOP, anchor="w")
    Checkbutton(server_settings, text="Use secure connection (SSL)").pack(side=TOP, anchor="w")
    Checkbutton(server_settings, text="Check for new messages at startup").pack(side=TOP, anchor="w")

    Button(server_settings, text="Advanced...", fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0, activeforeground="white").pack(side=RIGHT, anchor="w", padx=3, ipady=2, ipadx=5)

    for i in range(0, 6):
        conn_settings.grid_columnconfigure(i, weight=1)


    # Identity Window
    default_identity = LabelFrame(identity_window, text="Default Identity", padx=5, pady=5)
    default_identity.pack(fill=X, expand=0, padx=10, pady=10, side=TOP)

    default_identity.grid_columnconfigure(1, weight=1)

    i = 0
    Label(default_identity, text="Each account has an identity, which is the information that other people see when they read your messages.").grid(row=i, column=0, sticky="w", columnspan=2, pady=(0,10))
    i += 1

    pady=2
    Label(default_identity, text="Your Name: ").grid(row=i, column=0, sticky="w", pady=(0,pady))
    Entry(default_identity).grid(row=i, column=1, sticky="nsew", pady=(0,pady))
    i += 1

    Label(default_identity, text="Email Address: ").grid(row=i, column=0, sticky="w", pady=(0,pady))
    Entry(default_identity).grid(row=i, column=1, sticky="nsew", pady=(0,pady))
    i += 1

    Label(default_identity, text="Reply to Address: ").grid(row=i, column=0, sticky="w", pady=(0,pady))
    Entry(default_identity).grid(row=i, column=1, sticky="nsew", pady=(0,pady))
    i += 1

    Label(default_identity, text="Organization: ").grid(row=i, column=0, sticky="w", pady=(0,pady))
    Entry(default_identity).grid(row=i, column=1, sticky="nsew", pady=(0,pady))
    i += 1

    Label(default_identity, text="Signature Text: ").grid(row=i, column=0, sticky="w", pady=(5,pady))
    Checkbutton(default_identity, text="Use HTML (e.g. <b>bold</b>)").grid(row=i, column=1, sticky="w", pady=(5,pady))
    i += 1

    Text(default_identity, height=4, width=71).grid(row=i, column=0, sticky="w", columnspan=2, pady=(0,pady))
    i += 1

    Checkbutton(default_identity, text="Attach the signature from a file instead (text, HTML or image)").grid(row=i, column=0, sticky="w", columnspan=2, pady=(5,pady))
    i += 1

    Entry(default_identity).grid(row=i, column=0, sticky="nsew", columnspan=2, pady=(0,pady))
    i += 1

    Button(default_identity, text="Choose...", fg="white", bg=inactive_bg, activebackground=active_bg, borderwidth=0, activeforeground="white").grid(ipady=2, ipadx=4, row=i, column=0, sticky="e", columnspan=2, pady=(0,pady))
    i += 1


def create_buttons(master):
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

