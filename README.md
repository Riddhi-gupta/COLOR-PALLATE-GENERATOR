# COLOR-PALLATE-GENERATOR
The user uploads an image file to the website, through a simple form. The Python program reads this file, converts it to a NumPy matrix, filters out unique colours, count the occurrences of these unique colors
# Key Features
User-Friendly Interface:

Web Form for Image Upload: Simple and intuitive interface for users to upload their images directly from their browser.
Real-Time Color Palette Generation: Instantly generates and displays the color palette after the image is uploaded.
# Color Analysis:

Unique Colors Extraction: Processes the uploaded image to identify all unique colors present.
RGB Code Display: Shows the RGB codes for each unique color found in the image.
Color Count: Displays the number of occurrences of each color, providing insight into the color distribution within the image.
# Responsive Design:
CSS Styling: Ensures the application looks good on both desktop and mobile devices.
Dynamic Content Display: Adjusts the layout to fit different screen sizes, making the palette easy to view on any device.
# Technical Implementation
Backend:
Python and Flask: The core backend of the application is built using Flask, a lightweight web framework for Python.
Pillow: A Python Imaging Library (PIL) fork used for image processing, including resizing and color extraction.
NumPy: Used for efficient numerical operations on the image data.
Werkzeug: A utility library used for secure file handling and upload management.
Frontend:

HTML: Provides the structure for the web pages.
CSS: Styles the web pages to make the user interface clean and visually appealing.
Bootstrap: Utilized for responsive design to ensure the application is usable on various devices.
How It Works
Image Upload:

The user accesses the web interface and uploads an image using the provided form.
The application securely handles the file upload and stores the image in a designated directory.
Color Extraction:

The uploaded image is processed to extract its color data. The image is resized to a manageable size to reduce processing time without significantly losing color detail.
The image pixels are converted into a list of RGB tuples, and a count of each unique color is maintained using the Counter class from Python’s collections module.
# Result Display:

The unique colors and their counts are sorted and displayed on the web page.
Each color is shown as a colored box with its corresponding RGB code and count.
# Installation and Setup

# Prerequisites:

Python 3.x
Flask
Pillow
NumPy
Installation:

Clone the repository: git clone <repository_url>
Navigate to the project directory: cd project-root
Install dependencies: pip install -r requirements.txt
# Running the Application:
Start the Flask server: color pallate gene.py

# Project Directory Structure
php
Copy code
project-root/
│
├── app.py                   # Main Flask application
├── templates/
│   └── index.html           # HTML template
└── static/
    ├── uploads/             # Directory for uploaded images
    └── styles.css           # CSS styles
# Usage
Launch the Application:
Run the Flask application using python app.py.

# Upload an Image:

Click the "Choose File" button to select an image from your device.
Click the "Upload" button to submit the image.
# View the Color Palette:

After the image is processed, view the generated color palette displayed on the page.
Each color box shows the RGB code and the count of how many times that color appears in the image.
# Conclusion
The Image Color Palette Generator web application is a practical tool for designers, artists, and developers who need to analyze and extract color palettes from images. By combining the power of Python, Flask, and web technologies, this project provides a straightforward and efficient solution for color extraction and analysis.
