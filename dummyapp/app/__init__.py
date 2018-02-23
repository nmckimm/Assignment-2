from flask import Flask
app = Flask(__name__)
from app import views
import importlib.util
spec = importlib.util.spec_from_file_location("main", "/home/neil/git/COM30670/Assignment2/systeminfo/systeminfo/main.py")
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
