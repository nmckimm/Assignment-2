from flask import render_template
from app import app

import importlib.util
spec = importlib.util.spec_from_file_location("main", "/home/neil/git/COM30670/Assignment2/systeminfo/systeminfo/main.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)


showinfo = foo.displayInfo()

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'You..' # Feel free to put your name here!
    returnDict['title'] = 'Damn'



    return render_template("index.html", **returnDict, showsyst=showinfo)

