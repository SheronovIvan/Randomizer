from flask import Flask, render_template, request, session, redirect, url_for
import os
import random
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key_here"
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_text(text):
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    if len(lines) < 10:
        i = len(lines)
        random.shuffle(lines)
        return list(enumerate(lines[:i], start=1))
    random.shuffle(lines)
    # Возвращаем список кортежей (index, line)
    return list(enumerate(lines[:10], start=1))
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.pop('error', None)
        session.pop('result', None)
        
        if 'file' not in request.files:
            session['error'] = "Файл не выбран"
            return redirect(url_for('index'))
            
        file = request.files['file']
        if file.filename == '':
            session['error'] = "Файл не выбран"
            return redirect(url_for('index'))
            
        if file and allowed_file(file.filename):
            try:
                content = file.read().decode('utf-8')
                result = process_text(content)
                session['result'] = result
                return redirect(url_for('results'))
            except Exception as e:
                session['error'] = str(e)
                return redirect(url_for('index'))
                
        session['error'] = "Недопустимый формат файла"
        return redirect(url_for('index'))
    
    return render_template('index.html')

@app.route('/manual', methods=['GET', 'POST'])
def manual_input():
    if request.method == 'POST':
        session.pop('error', None)
        session.pop('result', None)
        
        text = request.form.get('text', '')
        if not text:
            session['error'] = "Введите текст"
            return redirect(url_for('manual_input'))
            
        try:
            result = process_text(text)
            session['result'] = result
            return redirect(url_for('results'))
        except Exception as e:
            session['error'] = str(e)
            return redirect(url_for('manual_input'))
    
    return render_template('manual.html')

@app.route('/results')
def results():
    if 'result' not in session:
        return redirect(url_for('index'))
    return render_template('results.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
# python -m waitress --listen=127.0.0.1:5000 app:app
