from flask import Flask, url_for, render_template, get_template_attribute, current_app

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug = True)
