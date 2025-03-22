import subprocess

# Path to the SPICE file
spice_file_path = '/home/anilk/SKYWATER130_GMID/PMOS/DC_PFET1v8.spice'

# Define the command for simulating the DC_NFET1v8.spice file
command = ['ngspice', '-i', 'DC_PFET1v8.spice']

# Run the SPICE simulation
try:
    subprocess.run(command, check=True)
    print("NGSpice simulation completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error running ngspice: {e}")
except FileNotFoundError:
    print("ngspice command not found. Ensure it's installed and in the system PATH.")

# Paths to the header file and data file
header_file_path = "/home/anilk/SKYWATER130_GMID/PMOS/pmos_data/gmid_pmos_header.txt"
data_file_path = "/home/anilk/SKYWATER130_GMID/PMOS/pmos_data/gmid_pmos_output.txt"

# Define the header for adding the header to the simulated data file
header = "vg gm vg idbyw vg gmbyid vg gmbygds vg ft vg cgg vg gds vg Voverdrive"

# Step 1: Write the header and append the data
with open(header_file_path, 'w') as header_file:
    # Write the header
    header_file.write(header + '\n')

    # Open the data file and append its content to the header file
    with open(data_file_path, 'r') as data_file:
        for line in data_file:
            header_file.write(line)

print(f"Header and data merged into {header_file_path}")

# Step 2: Remove odd-numbered columns (except the first column) from the file
output_file_path = "/home/anilk/SKYWATER130_GMID/PMOS/pmos_data/gmid_pmos_header_unformatted.txt"

with open(header_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        # Split the line into columns
        columns = line.strip().split()

        # Keep only the first column and even-numbered columns (1-indexed)
        filtered_columns = [columns[i] for i in range(len(columns)) if i == 0 or i % 2 == 1]

        # Write the filtered line to the output file
        outfile.write(" ".join(filtered_columns) + '\n')

print(f"Filtered data saved to {output_file_path}")
