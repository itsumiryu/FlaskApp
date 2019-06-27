# Flask_App/views/views.py

from flask import request, redirect, url_for, render_template, flash, session
from Flask_App import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('ユーザ名が異なります')# ブラウザにメッセージを渡す
        elif request.form['password'] != app.config['PASSWORD']:
            flash('パスワードが異なります')
        else:
            session['logged_in'] = True
            flash('ログインしました')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)# 指定したキーの要素を削除し値を取得: pop()
    # 指定したキーが辞書に含まれていない場合は2番目に指定したNoneを返す
    flash('ログアウトしました')
    return redirect(url_for('show_entries'))
