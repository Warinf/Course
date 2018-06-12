# Script for the Python course (GU)

This script is intended to help analyze data from Thermal Shift Assays (more info on wiki https://en.wikipedia.org/wiki/Thermal_shift_assay). Mainly it finds a melting temperature (a temperature at which protein unfolds). 
The script normalizes the fluorescence data and finds the value which is closest to 0.5. 

To run script you need to have these python packages:
     pandas
     matplotlib
Script file is called Main_Project.py     
The dataset, which is analyzed is called 'test.csv'

Simply launch the script (Main_Project.py) and it should find the csv file which is located in the local folder.

It will normalize and plot your data. Close it and afterwards it will ask you to select The First and Second temperature. These temperatures define the data range you want to use. Range should include yor main flourescence transition (for test.csv, you can select 30 and 70 respectively).

Next, it will plot and normalize your data again (with range you chose) and put black line at 0.5 value.
You can close it and finnaly it will export your melting temperatures to Results.csv file and plot in bar.
