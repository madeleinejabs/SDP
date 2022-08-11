import tkinter as tk

# Window settings
root = tk.Tk() # root window
root.title("Banana interest survey") # Set title
root.geometry('650x480+300+300') # Set root window size
root.resizable(False, False)
root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)
title = tk.Label(
    root, 
    text="Please take the survey",
    font="Arial 16 bold",
    bg="brown",
    fg="#FF0"
)

# Name question
name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What is your name?")
name_input = tk.Entry(root, textvariable=name_var)

# Eat question
eater_var = tk.BooleanVar()
eater_input = tk.Checkbutton(
    root,
    variable=eater_var,
    text="Check this box if you eat bananas"
)

# Number question
num_var = tk.IntVar(value=3)
num_label = tk.Label(
    root,
    text="How many bananas do you eat per day?"
)
num_input = tk.Spinbox(
    root, 
    textvariable=num_var,
    from_=0, 
    to=1000, 
    increment=1
)

# Color question
color_var = tk.StringVar(value='Any')
color_label = tk.Label(
    root,
    text="What is the best color for a banana?"
)
color_choices = (
    "Any", "Green",  "Green-Yellow",
    "Yellow", "Brown Spotted", "Black"
)
color_input = tk.OptionMenu(
    root, color_var, *color_choices
)

# Plantain question
plantain_var = tk.BooleanVar()
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_input = tk.Radiobutton(
    plantain_frame, 
    text="Yes",
    value=True,
    variable=plantain_var
)
plantain_no_input = tk.Radiobutton(
    plantain_frame, 
    text="Eww, no!",
    value=False,
    variable=plantain_var
)

# Haiku question
banana_haiku_label = tk.Label(
    root,
    text="Write a haiku about bananas"
)
banana_haiku_input = tk.Text(root, height=3)

output_var = tk.StringVar(value='')
output_line = tk.Label(
    root, 
    textvariable=output_var,
    anchor="w", 
    justify="left"
)

# Handle submission
submit_button = tk.Button(root, text="Submit Survey")
def on_submit():
    name = name_var.get()
    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000
    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()
    haiku = banana_haiku_input.get('1.0', tk.END)
    message = f'Thanks for taking the survey, {name}.\n'
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f'Enjoy your {number} {color} bananas!\n'
    if plantain_eater:
        message += 'Enjoy your plantains!'
    else:
        message += 'May you successfully avoid plantains!'
    if haiku.strip():
        message += f'\n\nYour Haiku:\n{haiku}'
    output_var.set(message)
submit_button.configure(command=on_submit)

# Place everything into the grid
title.grid(columnspan=2)
name_label.grid(row=1, column=0)
name_input.grid(row=1, column=1)
eater_input.grid(row=2, columnspan=2, sticky='we')
num_label.grid(row=3, sticky=tk.W)
num_input.grid(row=3, column=1, sticky=tk.W + tk.E)
color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_input.grid(row=5, columnspan=2, sticky=tk.W + tk.E, padx=25)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)
plantain_yes_input.pack(side="left", fill="x", ipadx=10, ipady=5)
plantain_no_input.pack(side="left", fill="x", ipadx=10, ipady=5)
banana_haiku_label.grid(row=8, sticky=tk.W)
banana_haiku_input.grid(row=9, columnspan=2, sticky="NSEW")
submit_button.grid(row=99)
output_line.grid(row=100, columnspan=2, sticky="NSEW")

root.mainloop()