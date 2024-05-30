from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
#to import file into the web application
from PIL import Image
#importing numpy library
import numpy as np
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
#add allowed extensions file for the image they are jpg, jpeg and png universally available extensions so that everyone can use this
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_colors(image_path):
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize to reduce processing time
    pixels = np.array(image)
    pixels = pixels.reshape(-1, pixels.shape[-1])
    count = Counter([tuple(pixel) for pixel in pixels])
    return count.most_common()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            colors = get_colors(filepath)
            return render_template('index.html', filename=filename, colors=colors)
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == '__main__':
    app.run(debug=True)
