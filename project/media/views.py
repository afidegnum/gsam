from . import media
import uuid
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, jsonify, json
from project import  app


from werkzeug.utils import secure_filename
import os


@media.route('/files')
def index():
    return render_template('ginn/media_index.html')


@media.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        extension = os.path.splitext(file.filename)[1]
        f_name = str(uuid.uuid4()) + extension
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        return json.dumps({'filename':f_name})