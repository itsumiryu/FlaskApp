# Flask_App/views/entries.py

from flask import request, redirect, url_for, render_template, flash, session
from Flask_App import app

@app.route('/')# /にアクセスしたとき下のメソッド実行
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))# loginメソッド実行
    return render_template('entries/index.html')# ログイン成功
