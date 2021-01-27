from flask import Flask, redirect, url_for, render_template
from board import Board
from board import Score

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html', board = Board(20, 20), score = Score())

if __name__ == '__main__':
    app.run(debug = True)
