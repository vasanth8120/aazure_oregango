from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = '09'

@app.route('/')
def home():
    return "hfgj"

if __name__ == '__main__':
    app.run(debug=True)
