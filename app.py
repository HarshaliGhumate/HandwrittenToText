from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
import converttolines
import answer
import SpellChecker
import nltk 
from nltk.tokenize import word_tokenize
app = Flask(__name__)
import removelines

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit(
        '.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        f = f'uploads/{filename}'
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        image = removelines.remove_l("static/uploads/" + filename)
        converttolines.convert_to_words(image)
        directory = "words"
        arr = [""] * len(os.listdir(directory))
        for filename in os.listdir(directory):
            arr[int(filename.split(".")[0]) - 1] = answer.answer("words/" +
                                                                 filename)
            arr[int(filename.split(".")[0]) - 1] = SpellChecker.correct_sentence(arr[int(filename.split(".")[0]) - 1])
        for i in arr:
             if(i == '" ' or i == "' " or i =="- " or i =="-" or i == "'" or i == '"' or i == "."):
                arr.remove(i)  
        print(arr)
        return render_template('display.html',
                               filename = f,
                               text=" ".join(arr))
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)


# @app.route('/')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/'+ filename),code=301)


if __name__ == "__main__":
    app.run()
