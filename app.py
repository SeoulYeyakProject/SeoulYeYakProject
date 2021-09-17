from flask import Flask, request, render_template, redirect


app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')