import pandas as pd
import matplotlib.pyplot as plt

# Ensure Arial Narrow is available; fallback if not
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.labelsize'] = 18  # Axis label font size
plt.rcParams['legend.fontsize'] = 18  # Legend font size
plt.rcParams['xtick.labelsize'] = 14  # X-axis tick font size
plt.rcParams['ytick.labelsize'] = 14  # Y-axis tick font size
plt.rcParams['xtick.direction'] = 'out'  # Tick direction outward
plt.rcParams['ytick.direction'] = 'out'

def add_vd_column_and_generate_file(input_file_path, output_file_path):
    """
    Reads data from the input file, adds a 'vd' column based on 'vg' values, and saves it to the output file.
    """
    # Read the data from the file, assuming it has headers
    df = pd.read_csv(input_file_path, sep=r'\s+', header=0)

    # Initialize vd to 0.1
    vd = 0.1
    vd_values = []  # List to hold the vd values for each row
    increment_next = False  # Flag to indicate when to increment vd

    for idx, row in df.iterrows():
        # Check if vg equals 2, and set the flag to increment vd for the next row
        if row['vg'] == 2 and not increment_next:
            increment_next = True  # Set the flag to increment in the next iteration
        elif increment_next:
            vd += 0.1  # Increment by 0.1 once the cluster for vg=2 ends
            increment_next = False  # Reset the flag after incrementing

        # Add the current vd value to the list
        vd_values.append(vd)

    # Add the new vd column to the DataFrame
    df['vd'] = vd_values

    # Write the modified DataFrame to a new file in scientific notation
    df.to_csv(output_file_path, sep='\t', index=False, header=True, float_format='%.6e')

    print(f"Data with 'vd' column has been saved to {output_file_path}.")

def plot_cluster_data_interactive(file_path):
    """
    Interactively plots data for user-specified columns (X and Y) from a specified cluster.
    Clicking on any point highlights its value.
    """
    # Read the data from the file
    df = pd.read_csv(file_path, sep=r'\s+', header=0)

    # Display available columns
    print("Available columns in the dataset:")
    print(", ".join(df.columns))

    # Prompt the user for input
    x_column = input("Enter the column name for the X-axis: ").strip()
    y_column = input("Enter the column name for the Y-axis: ").strip()
    cluster_column = input("Enter the column name to define the cluster: ").strip()
    cluster_value = float(input(f"Enter the value for the cluster in column '{cluster_column}': ").strip())

    # Validate column names
    if x_column not in df.columns or y_column not in df.columns or cluster_column not in df.columns:
        print("Error: One or more column names are invalid.")
        return

    # Filter the DataFrame for the specified cluster value
    cluster_data = df[df[cluster_column] == cluster_value]

    if cluster_data.empty:
        print(f"No data found for cluster '{cluster_value}' in column '{cluster_column}'.")
        return

    # Ensure the data is in a format that matplotlib can plot (convert to numpy arrays)
    x_data = cluster_data[x_column].values
    y_data = cluster_data[y_column].values

    # Plot the data
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_data, y_data, marker='o', linestyle='-', label=f"Cluster: {cluster_value}")

    # Customize plot labels, title, and grid
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    ax.set_title(f"{y_column} vs {x_column} for {cluster_column} = {cluster_value}")
    ax.grid(True)
    ax.legend()

    # Function to display the point clicked
    def on_click(event):
        if event.inaxes == ax:  # Check if the click is within the plot
            # Find the nearest data point
            distances = ((x_data - event.xdata) ** 2 + (y_data - event.ydata) ** 2) ** 0.5
            nearest_index = distances.argmin()
            nearest_x = x_data[nearest_index]
            nearest_y = y_data[nearest_index]

            # Highlight the clicked point
            ax.plot(nearest_x, nearest_y, marker='x', color='red', markersize=10, label='Selected Point')
            ax.annotate(f"({nearest_x:.3f}, {nearest_y:.3f})",
                        (nearest_x, nearest_y),
                        textcoords="offset points",
                        xytext=(10, 10),
                        ha='center',
                        fontsize=10,
                        color='red')

            # Redraw the plot to show the changes
            fig.canvas.draw()

    # Connect the click event to the on_click function
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Show the plot
    plt.show()

# Combined functionality
input_file_path = "/home/anilk/SKYWATER130_GMID/NMOS/nmos_data/gmid_nmos_header_unformatted.txt"
output_file_path = "/home/anilk/SKYWATER130_GMID/NMOS/nmos_data/gmid_characteristics_vd_cluster.txt"

# Step 1: Generate the new file with 'vd' column
add_vd_column_and_generate_file(input_file_path, output_file_path)

# Step 2: Plot data from the generated file
plot_cluster_data_interactive(output_file_path)
