# manage.py
# db.pyをコンソール上で実行させるためのスクリプト

from flask_script import Manager
from Flask_App import app
from Flask_App.scripts.db import InitDB

if __name__ == "__main__":
    manager = Manager(app)
    manager.add_command('init_db', InitDB())# InitDBクラスを'init_db'という名前で実行
    manager.run()
