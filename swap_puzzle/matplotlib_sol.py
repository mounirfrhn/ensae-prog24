import matplotlib as plt
import numpy as np

def plot_list_of_lists(list_of_lists):
    """
    Takes a list of lists as input and plots it using matplotlib as a grid without color fill.
    Each cell is smaller compared to the previous plot.
    """
    # Convert the list of lists to a 2D NumPy array
    matrix = np.array(list_of_lists)

    nrows, ncols = matrix.shape
    fig, ax = plt.subplots(figsize=(ncols, nrows))  # Set figure size based on the number of rows and columns

    # Create a table to display the matrix
    table = plt.table(
        cellText=matrix,
        loc='center',
        cellLoc='center',
        bbox=[0, 0, 1, 1]  # Use full extent of the axes, making cells smaller if necessary
    )

    # Style the table
    table.auto_set_font_size(False)  # Prevent auto-setting of font-size
    table.set_fontsize(14)  # Small font size for table text
    table.scale(1, 1.5)  # Increase cell height a bit
    
    # Turn off the axis
    ax.axis('off')

    # Adjust layout to make room for the table:
    plt.tight_layout()

    # Show the plot
    plt.show()

# Example list of lists provided by the user
user_list_of_lists = [[5, 3, 6], [2, 1, 4]]

# Call the function with the user's list of lists
plot_list_of_lists(user_list_of_lists)
