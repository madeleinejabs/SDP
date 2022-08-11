Usage Instructions:
This program takes as input a .xlsx or .csv file emitted by Omega's Pressure Transducer Application 2.3.1 for the PX409 pressure transducer. You can find the .exe to run the application within the "dist" folder of the "Sirtex Pressure Analysis" directory.

After the user uploads an appropriate file, the program displays a graph of the pressure versus time, the overall maximum pressure, and the time required to drop from the maximum pressure to the final pressure value.

If the user uploads a spreadsheet not produced by Pressure Transducer Application or if the spreadsheet has been edited by the user, then the application may display a "File Format Error."

Please note that the python file "Sirtex Pressure Analysis.py" can be modified and rebuilt, producing a new .exe application according to the instructions below.

Windows Re-Build Instructions:
Download the latest version of Python from python.org. Make sure to check the box next to "Add Python to PATH."
Launch Command Prompt.
Perform the following commands by typing them in Command Prompt and pressing enter after each one:
	pip install pyinstaller
	cd "<path of Sirtex Pressure Analysis folder>"
	pyinstaller --onefile -w "Sirtex Pressure Analysis.py"

At this point Command Prompt will show a wall of text describing the build process. After it has finished you will have a re-built .exe file within the "dist" directory, which should be located within the directory that 'Sirtex Pressure Analysis.py' is located.