from flask import Flask, request, jsonify, render_template
from password_generator import generate_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_result():
    min_length = int(request.form['min_length'])
    has_numbers = bool(request.form.get('has_numbers'))
    has_specials = bool(request.form.get('has_specials'))

    password = generate_password(min_length, has_numbers, has_specials)

    return render_template('result.html', password=password)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
