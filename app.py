from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__, 
    static_folder='static',
    template_folder='templates')

# Создаем необходимые директории, если их нет
os.makedirs('static/css', exist_ok=True)
os.makedirs('static/img', exist_ok=True)
os.makedirs('static/js', exist_ok=True)

@app.route('/')
def index():
    return render_template('1.html')

@app.route('/address-book')
def address_book():
    return render_template('address_book.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/service-isod')
def service_isod():
    return render_template('serviceIsod.html')

@app.route('/create-notice')
def create_notice():
    return render_template('create_notice.html')

@app.route('/legal-base')
def legal_base():
    return render_template('legal_base.html')

@app.route('/person-details')
def person_details():
    return render_template('person_details.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/sodi-system')
def sodi_system():
    return render_template('sodi_system.html')

@app.route('/img/<path:filename>')
def serve_image(filename):
    return send_from_directory('img', filename)

@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('js', filename)

if __name__ == '__main__':
    app.run(debug=True) 