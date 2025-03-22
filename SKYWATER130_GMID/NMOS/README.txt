###############################################################################Instructions for NMOS Device Characterization Using SkyWater130####################################################################################################

######Preliminary Steps############

1.	Navigate to the Directory
    Go to the following path:
    /home/anilk/SKYWATER130_GMID/NMOS/
    (Note: The path may differ in your workspace. For example, it could be: /your/workspace/path/SKYWATER130_GMID/NMOS/)

2.	Ensure .spice File Availability
    Check that a .spice file for NMOS device characterization is present. In this case, the file should be named DC_NFET1v8.spice

3.	Verify the Required Files and Folders
    Ensure that the directory /home/anilk/SKYWATER130_GMID/NMOS/ contains the following files and folders:
    •   DC_NFET1v8.sch
    •	DC_NFET1v8.spice
    •	README.txt
    •	gmid_nmos_skywater.py
    •	nmos_data/
    •	plots_sky_nmos_vd.py
    •	xschemrc
        If all files are available, you are good to proceed.

4.	Check the Python Script Configuration
    Open the file gmid_nmos_skywater.py and verify that the spice_file_path variable includes the correct path to the .spice file (e.g., yourspicefile.spice).

5.	Ensure ngspice Invocation
    Verify that the ngspice tool is invoked correctly in the file gmid_nmos_skywater.py with the following line:
    command = ['ngspice', '-i', 'DC_NFET1v8.spice']
    This Python script (gmid_nmos_skywater.py) runs the ngspice simulation using the DC_NFET1v8.spice file. The output is logged into gmid_nmos_output.txt and saved in the directory /home/anilk/SKYWATER130_GMID/NMOS/nmos_data/. Additionally, the script formats the data and writes it to gmid_nmos_header_unformatted.txt in the same folder.

####################################################################################################Running the Code#########################################################################################################################

######To generate NMOS data for various drain voltages, follow these steps:

1.	Run the Python Script for Simulation
    Execute the following command:
        python3 gmid_nmos_skywater.py
        This will simulate the NMOS device, and the results will be saved in the directory: /home/anilk/SKYWATER130_GMID/NMOS/nmos_data/

2.	Run the Plotting Script
        Execute the plotting script to visualize the results:
        python3 plots_sky_nmos_vd.py
            This script provides a user interface for selecting the x-axis, y-axis, and fixing the third parameter. For example, to plot vg versus gm at a specific vd (e.g., vd = 0.3), choose:
            o	x-axis = vg
            o	y-axis = gm
            o	Fixed parameter: vd = 0.3

3.	View the Plot. The selected plot will appear, and you can click on the graph with your mouse to view the data values.
