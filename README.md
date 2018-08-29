# Script for the Python course (GU)

This script is intended to help analyze data from Thermal Shift Assays (more info on wiki https://en.wikipedia.org/wiki/Thermal_shift_assay). Mainly, it finds a melting temperature (a temperature at which protein unfolds). 
The script normalizes the fluorescence data and finds the value which is closest to 0.5. 

To run script you need to have these python packages:
     pandas
     matplotlib

Script file is called Main_Project.py     

The dataset, which is analyzed is called 'test.csv'

Simply launch the script (Main_Project.py) and it should find the csv file, which is located in the local folder.

Firstly, it will normalize and plot your data. A plot will be shown, after closing it, you will have to select The First and Second temperature. These temperatures define the data range you want to analyse. Range should include yor main flourescence transition (for test.csv, you can select 30 and 70 respectively). It may show a warning, but you can safely ignore it.

Next, it will plot and normalize your data again (with range you chose) and put black line at 0.5 value.
You can close it and script will export your melting temperatures to Results.csv file and creat a bar plot.

Update 1. 

You can click with mouse cursor on data and get information about X and Y values and which dataset it belongs. 
