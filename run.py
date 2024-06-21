from flask import Flask, render_template, url_for

app= Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.errorhandler(401)
def unauthorized(error):
    return render_template('401.html'), 401

if __name__ == '__main__':
    app.run(debug=True)