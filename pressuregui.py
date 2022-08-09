import pandas
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import numpy as np
import tkinter as tk
import os
from datetime import datetime

# This class represents a results window
class Results(tk.Toplevel):
    def __init__(self, root, times, pressures):
        # Initializes a results window
        super().__init__(root)
        self.title('Results')
        
        # Analyzes the data
        max_pressure = max(pressures).round(3)
        # The np.where function returns all the indices for which the pressure equals its maximum value
        # Therefore the -1th index specifies that max_pressure_time is the latest time at which pressure is maximum
        max_pressure_time = times[np.where(pressures == max(pressures))][-1]
        time_to_drop = (times[-1] - max_pressure_time).round(3)

        # Produces a matplotlib figure and populates it with time-pressure data
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        figure = Figure(figsize=(screen_width // 125, screen_height // 125), dpi=100)
        axes = figure.add_subplot(1, 1, 1)
        axes.set_xlabel('Time (seconds)')
        axes.set_ylabel('Pressure (psi)')
        axes.scatter(times, pressures, label='Raw Data')
        axes.scatter(max_pressure_time, max_pressure, label='Overall Maximum Pressure', s=50)
        axes.legend()

        # Embeds the matplotlib figure in the results window with a toolbar
        canvas_tkagg = FigureCanvasTkAgg(figure, master=self)
        canvas_tkagg.get_tk_widget().pack()
        NavigationToolbar2Tk(canvas_tkagg, self)

        # Prints quantities of interest to the results window
        processed_data = tk.Frame(self)
        processed_data.pack()
        overall_max = tk.Label(processed_data, text=f'Overall maximum pressure: {max_pressure} psi')
        overall_max.pack()
        time_to_drop = tk.Label(processed_data, text=f'Time to drop from maximum to final value: {time_to_drop} s')
        time_to_drop.pack()

# This class represents the overall application
class Application(tk.Tk):
    def __init__(self):
        # The following initializes the Data File Upload window and places it at the center of the screen
        super().__init__()
        self.title('Data File Upload')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        root_width = screen_width // 3
        root_height = screen_height // 3
        root_x = screen_width // 2 - root_width // 2
        root_y = screen_height // 2 - root_height // 2
        self.geometry(f'{root_width}x{root_height}+{root_x}+{root_y}')

        # Initializes the button widget, which calls the on_click function upon being clicked
        upload_button = tk.Button(self, text='Upload File', command=self.on_click)
        upload_button.place(anchor='c', relx=0.5, rely=0.5)

        # Initializes the error message
        self.error_message = tk.Label(self, text='File Format Error') 

    # Handles button clicks
    def on_click(self):
        path = tk.filedialog.askopenfilename(filetypes=(('Excel Files', '*.xlsx'), ('CSV Files', '*.csv')))
        extension = os.path.splitext(path)[-1]
        try:
            if extension == '.xlsx': # For Excel Files
                data = pandas.read_excel(path, header=10)
                times = np.array([i.timestamp() for i in data.Time])
            elif extension == '.csv': # For CSV files
                data = pandas.read_csv(path, header=9)
                times = np.array([datetime.strptime(i, r'%Y-%m-%d %H:%M:%S.%f %p').timestamp() for i in data.Time])   
            times = times - times[0] # Makes time start at zero
            pressures = np.array(data.Value)
            self.error_message.pack_forget()
            Results(self, times, pressures)
        except:
            self.error_message.pack()

# Start the program
if __name__ == '__main__':
    app = Application()
    app.mainloop()