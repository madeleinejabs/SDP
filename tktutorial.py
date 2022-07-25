import tkinter as tk

# Window settings
root = tk.Tk() # root window
root.title("Banana interest survey") # Set title
root.geometry('650x480+300+399') # Set root window size
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
name_label = tk.Label(root, text="What is your name?")
name_input = tk.Entry(root)

# Eat question
eater_input = tk.Checkbutton(
    root,
    text="Check this box if you eat bananas"
)

# Number question
num_label = tk.Label(
    root,
    text="How many bananas do you eat per day?"
)
num_input = tk.Spinbox(root, from_=0, to=1000, increment=1)

# Color question
color_label = tk.Label(
    root,
    text="What is the best color for a banana?"
)
color_input = tk.Listbox(root, height=1)
color_choices = (
    "Any", "Green",  "Green-Yellow",
    "Yellow", "Brown Spotted", "Black"
)
for choice in color_choices:
    color_input.insert(tk.END, choice)

# Plantain question
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_input = tk.Radiobutton(plantain_frame, text="Yes")
plantain_no_input = tk.Radiobutton(plantain_frame, text="Eww, no!")

# Haiku question
banana_haiku_label = tk.Label(
    root,
    text="Write a haiku about bananas"
)
banana_haiku_input = tk.Text(root, height=3)

# Handle submission
submit_button = tk.Button(root, text="Submit Survey")
def on_submit():
    name = name_input.get()
    number = num_input.get()
    selected_index = color_input.curselection()
    if selected_index:
        color = color_input.get(selected_index)
    else:
        color = ""
    haiku = banana_haiku_input.get('1.0', tk.END)

    message = (
        f"Thanks for taking the survey, {name}.\n"
        f"Enjoy your {number} {color} bananas!"
    )
    output_line.configure(text=message)
    print(haiku)
submit_button.configure(command=on_submit)

output_line = tk.Label(root, text="", anchor="w", justify="left")

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