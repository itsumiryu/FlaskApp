# Flask_App/scripts/db.py
# このスクリプトはmanage.pyで実行される

from flask_script import Command
from Flask_App import db# モデルインポート

class InitDB(Command):# スクリプト実行用のクラスとして定義される
    "create datebase"# クラス説明用コメント

    def run(self):# 実行される内容
        db.created_all()# モデル定義

# $ python
# >>> from flask_ blog import db
# >>> db. create_ all()
# スクリプト書いて実行してもよいが、インタラクティブモードから直接実行することもできる
