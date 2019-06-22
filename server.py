# server.py

from Flask_App import app
# __init__.pyのappインスタンスをインポート

if __name__ == '__main__':# 直接実行されたときに実行される処理
    app.run(debug=True)
