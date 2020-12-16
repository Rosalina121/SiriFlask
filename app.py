# flask stuff
from flask import Flask, request, jsonify, json, make_response
from wishes import *
from werkzeug.utils import secure_filename
from json import dumps

# funcs with arguments
from functools import partial

# base64
import base64

# everything
from everything import *

# pillow
from PIL import Image

# windows notifications
from win10toast import ToastNotifier

# googling i guess
import webbrowser

UPLOAD_FOLDER = 'C:\\Users\\kapits\\PycharmProjects\\SiriFlask\\uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def isBase64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s
    except Exception:
        return False


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/google', methods=['POST', 'GET'])
def google():
    if request.method == 'POST':
        if 'query' in request.form:
            url = "https://www.google.com/search?q={}".format(request.form['query'])
            webbrowser.open_new_tab(url)
            return 'Googled!'


@app.route('/clipboard', methods=['POST', 'GET'])
def clipboard():
    if request.method == 'POST':
        toaster = ToastNotifier()
        if 'file' in request.form:
            clip_string = request.form['image']
            base64_img_bytes = clip_string.encode('utf-8')
            # name specified in a share sheet
            if 'name' in request.form:
                image_name = request.form['name']
            # from copy/paste, might thinkg about adding a filename
            else:
                image_name = "img.png"
                if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], image_name)):
                    expand = 1
                    while True:
                        expand += 1
                        new_file_name = image_name[:-4] + str(expand) + ".png"
                        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], new_file_name)):
                            continue
                        else:
                            image_name = new_file_name
                            break
            with open(os.path.join(app.config['UPLOAD_FOLDER'], image_name), 'wb') as file_to_save:
                decoded_data = base64.decodebytes(base64_img_bytes)
                file_to_save.write(decoded_data)
                toaster.show_toast("SiriFlask", "File saved to " + image_name)
        else:
            clip_string = request.form['clip']
            os.system('echo ' + clip_string + ' | clip')
            toaster.show_toast("SiriFlask", "Clipboard: " + clip_string)
        return 'Clipboard sent!'
    return 'Issue with POST maybe?'


@app.route('/files', methods=['POST', 'GET'])
def open_file():
    if request.method == 'POST':
        if 'open' in request.form:
            print(request.form['open'])
            path = '"' + request.form['open'] + '"'
            if os.path.isdir(request.form['open']):
                os.system('explorer.exe ' + path)
            else:
                os.system('explorer.exe /select,' + path)
            return 'Opening in Explorer.'
        elif 'run' in request.form:
            os.system('"' + request.form['run'].replace('\\', '\\\\') + '"')
            return 'Running the program.'
        else:
            file_name = request.form['name']
            print(file_name)
            results = get_filename(file_name)
            print(results)
            if results['count'] == 0:
                return 'No candidate found.'
            else:
                return jsonify(results)

    return 'POST error?'


@app.route('/wish/<int:wish_id>')
@app.route('/wish/<int:wish_id>/<int:value>')
def make_a_wish(wish_id, value=10):
    switch = {
        1: iTunes_open,
        2: play_pause,
        3: audio_headphones,
        4: audio_speakers,
        5: audio_midi,
        6: audio_microphone,
        7: audio_mute,
        8: partial(volume, value),
        9: next_song,
        10: partial(shutdown, value),
        11: abort_shutdown
    }
    func = switch.get(wish_id, err_opt)
    return func()
