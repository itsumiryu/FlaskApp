# Flask_App/views.py

from Flask_App import app

@app.route('/')
def show_entries():
    return "Hello World!"
