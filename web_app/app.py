from flask import Flask, render_template, request, url_for
import cv2
import os
from Process import process

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "E:/yolo_v4/web_app/upload/"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    if not request.files.get('img'):
        return render_template('index.html')
    
    img = request.files.get('img')
    img.save(os.path.join(app.config["IMAGE_UPLOADS"], 'upload.jpg'))
    process()

    return render_template('result.html')


if __name__ == '__main__':
    app.run()