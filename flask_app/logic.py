"""
Author: Shaina Krumme
Description: Input Coordinate Calculator logic
"""

import numpy as np # Scientific computing
import matplotlib.pyplot as plt # Plot generation
from unit_tests import Testdatatype # Unit testing
import os.path # Pathnames
import glob # Pathname pattern expansion
from datetime import datetime # Dates and times


def calculate_coordinates(im_dim:tuple, corner_points:list):
    """
    Description:
        Calculate evenly spaced (x, y) coordinate pairs 
        given the dimensions and corner points of an image.

    Parameters:
        im_dim:         tuple of (width, height)
        corner_points:  list of 4 tuples or 4 (x, y) coordinate pairs.
    
    Return:
        out:            3D output array
        x_values:       1D array of x values
        y_values:       1D array of y values
    """  
    # Unit Testing
    unit_test = Testdatatype()
    unit_test.test_shape(corner_points)
    unit_test.test_unique_corner_points(corner_points)
    
    out = np.zeros((im_dim[0],im_dim[1],2)) # 3D output array

    # Max corner values
    x_max = max([i[0] for i in corner_points])
    y_max = max([i[1] for i in corner_points])
    
    # Min corner values
    x_min = min([i[0] for i in corner_points])
    y_min = min([i[1] for i in corner_points])
    
    # x values
    x_values = np.linspace(x_min, x_max, im_dim[0]) # 1D array of x values
    x_values = np.round(x_values, 2) # Round array to 2 decimals
    
    # y values
    y_values = np.linspace(y_min, y_max, im_dim[1]) # 1D array of y values
    y_values = np.sort(y_values)[::-1] # Sort array
    y_values = np.round(y_values, 2) # Round array to 2 decimals
    
    # Populate 3D output array
    for i in range(len(x_values)):
        for j in range(len(y_values)):
            out[i, j, :] = [x_values[i], y_values[j]]
            
    out = np.transpose(out, (1, 0, 2)) # Transpose array
    out = np.round(out, 2) # Round array to 2 decimals
    
    return out, x_values, y_values # Return arrays


def clean_plot_folder():
    """
    Description:    Remove any existing plots from the folder where plots are saved.
    Parameters:     None 
    Return:         None
    """  
    for filename in glob.glob("./static/plot*"):
        os.remove(filename) 


def create_plot(im_dim, out, x_values, y_values):
    """
    Description: Create plot.
    Parameters:
        im_dim:     tuple of (width, height)
        out:        3D output array
        x_values:   1D array of x values
        y_values:   1D array of y values
    Return:      URL for plot
    """ 
    # Populate scatter plot
    for i in range(im_dim[1]):
        for j in range(im_dim[0]):
            plt.scatter(out[i, j, 0], out[i, j, 1], c = 'b')
            
    plt.xticks(x_values) # Set x-axis tick locations
    plt.yticks(y_values) # Set y-axis tick locations
    
    plt.grid() # Configure grid lines
    
    plt.title("Evenly Spaced Pixels") # Set a title
    
    plt.xlabel('x') # Set x-axis label
    plt.ylabel('y') # Set y-axis label
    
    # Date and Time
    date_time = datetime.now()
    
    # Date
    date = date_time.date()
    month = date.month
    day = date.day
    year = date.year
    date_str = str(month) + "m" + str(day) + "d" + str(year) + "y"
    
    # Time
    time = date_time.time()
    hour = time.hour
    minute = time.minute
    second = time.second
    time_str = str(hour) + "h" + str(minute) + "m" + str(second) + "s"

    path = "./static/plot_" + date_str + "_" + time_str + ".png"   
    
    plt.savefig(path) # Save the figure
    
    plt.close() # Close the figure
    
    url = path[1:]  # URL for plot
    return url      # Return URL for plot