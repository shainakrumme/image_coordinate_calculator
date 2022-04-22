"""
Author: Shaina Krumme
Description: Flask Web Application
"""

from flask import Flask, request, render_template
from logic import calculate_coordinates, clean_plot_folder, create_plot


app = Flask(__name__) # Flask constructor


@app.route('/', methods=['GET', 'POST'])
def index():
    # If a form is submitted
    if request.method == "POST":
        
        # Image Dimensions
        height = int(request.form.get("im_dim_y"))  # Get height value
        width = int(request.form.get("im_dim_x"))   # Get width value
        
        im_dim = (width, height)                    # Image dimensions tuple
        print("Image Dimensions:", im_dim)          # Print image dimensions
        
        # Corner 1
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        
        # Corner 2
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))
        
        # Corner 3
        x3 = float(request.form.get("x3"))
        y3 = float(request.form.get("y3"))
        
        # Corner 4
        x4 = float(request.form.get("x4"))
        y4 = float(request.form.get("y4"))
        
        # Corner Points
        corner_points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        
        # Arrays
        out, x_values, y_values = calculate_coordinates(im_dim, corner_points)
        
        # Print output array
        print("Output Array:", out)

        # Remove any existing plots from the folder where plots are saved.
        clean_plot_folder()
        
        # Create plot
        url = create_plot(im_dim, out, x_values, y_values)
        
        return render_template('index.html', out = out, url = url, form_submitted = True)

    # If a form is not submitted
    else:
        return render_template('index.html')


@app.route('/instructions/')
def instructions():
    return render_template('instructions.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)