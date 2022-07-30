import pandas
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sps
import tkinter as tk
import os
from datetime import datetime

# Window configuration
root = tk.Tk()
root.title('Data File Upload')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root_width = screen_width // 3
root_height = screen_height // 3
root_x = screen_width // 2 - root_width // 2
root_y = screen_height // 2 - root_height // 2
root.geometry(f'{root_width}x{root_height}+{root_x}+{root_y}')
    
    
def datetime_string_to_float(string):
    datetime_object = datetime.strptime(string, r'%Y-%m-%d %H:%M:%S.%f %p')
    return datetime_object.timestamp()

def upload_file():
    # Ask user which file they want to analyze
    path = tk.filedialog.askopenfilename(filetypes=(('Excel Files', '*.xlsx'), ('CSV Files', '*.csv')))
    extension = os.path.splitext(path)[-1]

    try:
        if extension == '.xlsx':
            data = pandas.read_excel(path, header=9)
        elif extension == '.csv':
            data = pandas.read_csv(path, header=9)
        time = np.array([datetime.strptime(string, r'%Y-%m-%d %H:%M:%S.%f %p').timestamp() for string in data.Time])
        time = time - time[0]
        pressure = np.array(data.Value)
        error_message.pack_forget()
    except:
        error_message.pack()


    if len(time) > 0 and len(pressure) > 0:
        # Analyze data
        peaks = sps.find_peaks(pressure, height=1)[0]
        peak_times = time[peaks]
        peak_pressures = pressure[peaks]

        troughs = sps.find_peaks(-pressure, height=(None, -1))[0]
        trough_times = time[troughs]
        trough_pressures = pressure[troughs]

        # Open new window
        window = tk.Toplevel(root)
        window.title('Results')
        window.state('zoomed')

        # Plot data and peaks
        figure = Figure(figsize=(screen_width // 125, screen_height // 125), dpi=100)
        canvas_tkagg = FigureCanvasTkAgg(figure, master=window)
        axes = figure.add_subplot(1, 1, 1)
        axes.set_xlabel('Time (seconds)')
        axes.set_ylabel('Pressure (psi)')
        axes.scatter(time, pressure, label='Raw Data')
        axes.scatter(peak_times, peak_pressures, marker='X', s=100, label='Peaks')
        axes.scatter(trough_times, trough_pressures, marker='P', s=100, label='Troughs')
        axes.legend()
        canvas_tkagg.get_tk_widget().place(anchor='n', relx=0.5)

# GUI widgets
upload_button = tk.Button(
    root,
    text='Upload File',
    command=upload_file
).place(anchor='c', relx=0.5, rely=0.5)

error_message = tk.Label(
    root,
    text="File Format Error"
)

# Main GUI Loop
root.mainloop()